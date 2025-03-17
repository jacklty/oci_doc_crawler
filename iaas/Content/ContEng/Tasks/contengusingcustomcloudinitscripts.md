Updated 2025-01-15
# Using Custom Cloud-init Initialization Scripts to Set Up Managed Nodes
_Find out how to write custom cloud-init scripts to run on worker nodes in clusters you've created using Kubernetes Engine (OKE)._
Cloud-init is the industry standard method for cloud instance initialization, provisioning systems for private cloud infrastructure and bare-metal installations. It is supported across all major public cloud providers, including Oracle Cloud Infrastructure (see [User Data](https://docs.oracle.com/iaas/Content/Compute/References/images.htm#User)). Cloud-init runs scripts to initialize and configure instances. For more information about cloud-init, see the [cloud-init documentation](https://cloudinit.readthedocs.io/en/latest/).
Kubernetes Engine uses cloud-init to set up the compute instances hosting managed nodes. Kubernetes Engine installs a default start-up script on each instance hosting a managed node. When the instance boots up for the first time, cloud-init runs the default start-up script. The default start-up script contains the following logic provided by Kubernetes Engine:
Copy
```
#!/bin/bash
curl --fail -H "Authorization: Bearer Oracle" -L0 http://169.254.169.254/opc/v2/instance/metadata/oke_init_script | base64 --decode >/var/run/oke-init.sh
bash /var/run/oke-init.sh
```

You can customize the default start-up script by adding your own logic to the script, either before or after the default logic. Customizing the default start-up script enables you to, for example:
  * configure an SELinux policy on all worker node hosts for security and compliance purposes
  * unassign an instance's ephemeral public IP on start-up, and reassign the instance a reserved public IP instead
  * configure a corporate proxy
  * configure custom yum proxies
  * install mandated anti-virus software, and other security tools


If you do customize the default start-up script, do not modify the logic provided by Kubernetes Engine.
You can customize the default start-up script when creating a new cluster, creating new node pools, and modifying existing node pools:
  * using the Console (when creating a new cluster, use the 'Custom Create' workflow)
  * using the CLI
  * using the API


The customized start-up script runs when an instance hosting a worker node boots up for the first time. After customizing the default start-up script, it's a good idea to run the Node Doctor script to confirm that worker nodes on newly started instances are working as expected (see [Troubleshooting Node Issues for Kubernetes Clusters Using the Node Doctor Script](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtroubleshooting_topic-node_troubleshooting.htm#contengtroubleshooting_topic_node_troubleshooting "Find out how to use the Node Doctor script to help you resolve issues with compute instances hosting worker nodes in clusters you've created using Kubernetes Engine \(OKE\).")).
## Example Usecases for Custom Cloud-init Scripts 🔗 
### Example 1: Using a Custom Cloud-init Script to Configure SELinux (Security-Enhanced Linux) on Managed Nodes
You can use a custom cloud-init script to configure [SELinux](https://selinuxproject.org/page/Main_Page) on managed nodes. SELinux is a security enhancement to Linux that enables administrators to constrain which users and applications can access which resources based on rules in a policy. SELinux also adds finer granularity to access controls. 
SELinux can be in one of two states, either enabled or disabled. When it is enabled, SELinux can run in one of two modes, either enforcing or permissive. 
By default, SELinux is enabled and set to run in permissive mode on worker nodes. When running in permissive mode, SELinux does not enforce access rules and only performs logging.
If you want SELinux to enforce access rules, you can set it to run in enforcing mode. When running in enforcing mode, SELinux blocks actions that are contrary to the policy and logs a corresponding event in the audit log. 
To set SELinux to run in enforcing mode, use the following cloud-init script:
Copy
```
#!/bin/bash
curl --fail -H "Authorization: Bearer Oracle" -L0 http://169.254.169.254/opc/v2/instance/metadata/oke_init_script | base64 --decode >/var/run/oke-init.sh
bash /var/run/oke-init.sh
setenforce 1
sed -i 's/^SELINUX=.*/SELINUX=enforcing/' /etc/selinux/config 
```

To confirm the status and mode of SELinux that is running on a worker node, connect to the worker node and use the `getenforce` command. When the above cloud-init script has been run on worker nodes, the `getenforce` command returns `Enforcing`. 
### Example 2: Using a Custom Cloud-init Script to Set NodeLocal DNSCache on Managed Nodes
You can use a custom cloud-init script to configure [NodeLocal DNSCache](https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns/) on managed nodes. NodeLocal DNSCache improves Cluster DNS performance by running a DNS caching agent on worker nodes as a daemonset. 
If NodeLocal DNSCache is not enabled, pods in the ClusterFirst DNS mode reach out to a kube-dns serviceIP for DNS queries. Using iptables rules, this request is translated to a kube-dns/CoreDNS endpoint added by kube-proxy. For more information, see [DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/) in the Kubernetes documentation. 
If NodeLocal DNSCache is enabled, pods reach out to a DNS caching agent running on the same worker node, which enables them to bypass iptables DNAT rules and connection tracking. The local caching agent queries the kube-dns/CoreDNS service for cache misses of cluster hostnames (cluster.local suffix by default).
To configure NodeLocal DNSCache, use the following cloud-init script. Replace `CLUSTER DNS` with a local listen IP address that does not collide with anything in the cluster. There is a recommended link local range of 169.254.0.0/16 for IPv4 or from the Unique Local Address range of fd00::/8 for IPv6.
Copy
```
#!/bin/bash
curl --fail -H "Authorization: Bearer Oracle" -L0 http://169.254.169.254/opc/v2/instance/metadata/oke_init_script | base64 --decode >/var/run/oke-init.sh
bash /var/run/oke-init.sh --cluster-dns "[CLUSTER DNS]"
```

To confirm that NodeLocal DNSCache was successfully deployed, connect to a worker node and use the `sudo systemctl status -l kubelet` command. When the above cloud-init script has been run on worker nodes, the `sudo systemctl status -l kubelet` command returns `--cluster-dns` as one of the kubelet flags, set to a default local link address (for example, `169.254.20.10`).
After creating nodes using the above cloud-init script, deploy the DNS caching agent by following the steps in [Using NodeLocal DNSCache in Kubernetes clusters](https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns/#configuration) in the Kubernetes documentation. Once enabled, a node-local-dns pod runs in the kube-system namespace on each of the cluster nodes. The node-local-dns pod runs [CoreDNS](https://github.com/coredns/coredns) in cache mode, so all CoreDNS metrics exposed by the different plugins are available on a per-node basis.
To test DNS resolution, use one or more of the following commands (see [Debugging DNS Resolution](https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/) in the Kubernetes documentation). The commands should both work, and also output the IP address set by the `--cluster-dns` flag in the custom cloud-init script: 
Copy
```
kubectl apply -f https://k8s.io/examples/admin/dns/dnsutils.yaml
```

Copy
```
kubectl exec -it dnsutils – nslookup kubernetes.default
```

Copy
```
kubectl exec -it dnsutils – cat /etc/resolv.conf
```

You can disable NodeLocal DNSCache by removing the daemonset and deleting the nodelocaldns manifest. You should also revert any changes you made to the kubelet configuration.
### Example 3: Using a Custom Cloud-init Script to Set kubelet-extra-args on Managed Nodes
You can use a custom cloud-init script to configure a number of extra options on the [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/) (the primary node agent) on managed nodes. These extra options are sometimes referred to as `kubelet-extra-args`. One such `kubelet-extra-args` option is the option to configure debug level log verbosity.
To configure debug level log verbosity, use the following cloud-init script:
Copy
```
#!/bin/bash
curl --fail -H "Authorization: Bearer Oracle" -L0 http://169.254.169.254/opc/v2/instance/metadata/oke_init_script | base64 --decode >/var/run/oke-init.sh
bash /var/run/oke-init.sh --kubelet-extra-args "--v=4"
```

To confirm the setting of debug level log verbosity, connect to a worker node and use the `sudo systemctl status -l kubelet` command. When the above cloud-init script has been run on worker nodes, the `sudo systemctl status -l kubelet` command returns the verbosity level as 4. The kubelet logs also contain more detail. 
### Example 4: Using a Custom Cloud-init Script to Reserve Resources for Kubernetes and OS System Daemons 🔗 
You can use a custom cloud-init script to reserve CPU and memory resources for Kubernetes system daemons (such as `kubelet` and `container runtime`) and OS system daemons (such as `sshd` and `systemd`). To reserve resources for the Kubernetes and OS system daemons, include the `--kube-reserved` and `--system-reserved` kubelet flags respectively as `kubelet-extra-args` options in a custom cloud-init script.
To reserve resources for the Kubernetes and OS system daemons, use the following cloud-init script:
Copy
```
#!/bin/bash
curl --fail -H "Authorization: Bearer Oracle" -L0 http://169.254.169.254/opc/v2/instance/metadata/oke_init_script | base64 --decode >/var/run/oke-init.sh
bash /var/run/oke-init.sh --kubelet-extra-args "--kube-reserved=cpu=500m,memory=1Gi --system-reserved=cpu=100m,memory=100Mi"
```

For more information, and for recommended values for the `--kube-reserved` and `--system-reserved` kubelet flags, see [Best Practice: Reserve resources for Kubernetes and OS system daemons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengbestpractices_topic-Cluster-Management-best-practices.htm#contengbestpractices_topic-Cluster-Management-best-practices__ManagingOKEClusters-Reserveresourcesforkubernetesandossystemdaemons).
### Example 5: Using a Custom Cloud-init Script and oci-growfs to Increase the Size of the Boot Volume Partition 🔗 
You can use a custom cloud-init script to extend the partition for the boot volume of managed nodes. When you create and update clusters and node pools, you can specify a custom size for worker node boot volumes. The custom boot volume size you specify must be larger than the default boot volume size of the image you select. When you increase the size of the boot volume, to take advantage of the larger boot volume size, you also need to extend the partition for the boot volume .
Oracle Linux platform images include the `oci-utils` package. You can use the `oci-growfs[](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm#oci-growfs)` command from that package in a cloud-init script to extend the root partition and then grow the file system.
To extend the partition for the boot volume, use the following cloud-init script:
Copy
```
#!/bin/bash
curl --fail -H "Authorization: Bearer Oracle" -L0 http://169.254.169.254/opc/v2/instance/metadata/oke_init_script | base64 --decode >/var/run/oke-init.sh
bash /usr/libexec/oci-growfs -y
bash /var/run/oke-init.sh
```

For more information, see [Extending the Partition for a Boot Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/extendingbootpartition.htm).
## Creating a Custom Cloud-init Script 🔗 
To customize the default cloud-init start-up script that Kubernetes Engine provides:
  1. Create a new script file containing the default logic that Kubernetes Engine provides. You can do this in two ways:
     * By selecting the **Download Custom Cloud-Init Script Template** option (in the node pool **Advanced Options** section) when using the **Custom Create Cluster** , **Add Node Pool** , or **Edit Node Pool** dialog. The file you download contains the default logic.
     * By creating a new file from scratch with a filetype supported by cloud-init (such as .yaml) and adding the default logic that Kubernetes Engine provides. For example:
Copy
```
#!/bin/bash
curl --fail -H "Authorization: Bearer Oracle" -L0 http://169.254.169.254/opc/v2/instance/metadata/oke_init_script | base64 --decode >/var/run/oke-init.sh
bash /var/run/oke-init.sh
```

  2. Either before or after the default logic provided by Kubernetes Engine, add your own custom logic to the script file. Do not modify the default logic.
For example, to configure debug level log verbosity, you might add `--kubelet-extra-args "--v=4"`, so that the file looks like:
Copy
```
#!/bin/bash
curl --fail -H "Authorization: Bearer Oracle" -L0 http://169.254.169.254/opc/v2/instance/metadata/oke_init_script | base64 --decode >/var/run/oke-init.sh
bash /var/run/oke-init.sh --kubelet-extra-args "--v=4"
```

For other examples, see [Example Usecases for Custom Cloud-init Scripts](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingcustomcloudinitscripts.htm#contengusingcustomcloudinitscripts_topic_Examplecloudinitscriptusecases).
  3. Save the custom cloud-init script file you have created.
  4. Specify the custom cloud-init script file when you create a new cluster, add a new node pool, or modify an existing node pool:
     * [Using the Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingcustomcloudinitscripts.htm#contengusingcustomcloudinitscripts_topic_Using_the_Console)
     * [Using the CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingcustomcloudinitscripts.htm#contengusingcustomcloudinitscripts_topic_Using_the_CLI)
     * Using the API


## Using the Console 🔗 
To use the Console to provide a custom cloud-init script for instances hosting managed nodes in a new cluster, a new node pool, or an existing node pool:
  1. Create a valid cloud-init file, in one of the formats (for example, cloud-config) and filetypes (for example, a .yaml file) supported by cloud-init. See [Creating a Custom Cloud-init Script](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingcustomcloudinitscripts.htm#contengusingcustomcloudinitscripts_topic_Creatingthecloudinitscript).
  2. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
  3. Choose a **Compartment** you have permission to work in.
  4. Create a new cluster using the 'Custom Create' workflow, or add a new node pool to an existing cluster, or modify an existing node pool.
  5. In the node pool **Advanced Options** section of the **Custom Create Cluster** , **Add Node Pool** , or **Edit Node Pool** dialog (as appropriate), specify:
     * **Initialization Script:** (Optional) A script for cloud-init to run on each instance hosting worker nodes when the instance boots up for the first time. The script you specify must be written in one of the formats supported by cloud-init (for example, cloud-config), and must be a supported filetype (for example, .yaml). Specify the script as follows:
       * **Choose Cloud-Init Script** : Select a file containing the cloud-init script, or drag and drop the file into the box.
       * **Paste Cloud-Init Script** : Copy the contents of a cloud-init script, and paste it into the box.
If you have not previously written cloud-init scripts for initializing worker nodes in clusters created by Kubernetes Engine, you might find it helpful to click **Download Custom Cloud-Init Script Template**. The downloaded file contains the default logic provided by Kubernetes Engine. You can add your own custom logic either before or after the default logic, but do not modify the default logic. For examples, see [Example Usecases for Custom Cloud-init Scripts](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingcustomcloudinitscripts.htm#contengusingcustomcloudinitscripts_topic_Examplecloudinitscriptusecases).


## Using the CLI 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/). 
To use the CLI to provide a custom cloud-init script for instances hosting worker nodes in a new node pool, or in an existing node pool:
  1. Create a valid cloud-init file, in one of the formats (for example, cloud-config) and filetypes (for example, a .yaml file) supported by cloud-init. See [Creating a Custom Cloud-init Script](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingcustomcloudinitscripts.htm#contengusingcustomcloudinitscripts_topic_Creatingthecloudinitscript).
  2. Open a command prompt and enter one of the following commands to create a new node pool, or update an existing node pool, as appropriate:
     * `oci ce node-pool create`
     * `oci ce node-pool update`
  3. As well as the mandatory parameters required by the command you are using:
    1. Include the `--node-image-id` parameter, even if you do not want to specify a custom image.
    2. Include the `--node-metadata` optional parameter in the format:```
--node-metadata '{"user_data": "'$(cat <cloud-init-file> | base64)'"}'
```

where:
       * `<cloud-init-file>` is the name of the cloud-init file you created
       * `base64` specifies the file is to be base64-encoded
For example:
```
--node-metadata '{"user_data": "'$(cat my-custom-cloud-init.yaml | base64)'"}'
```



### Example
This example command creates a new node pool called `my-cloud-init-test-nodepool` for an existing cluster, with a single Kubernetes 1.18.10 node that has a VM 2.1 shape running Oracle Linux. When the instance hosting the worker node in the new node pool boots up for the first time, it will run a custom cloud-init script called `my-custom-cloud-init.yaml`:
```
oci ce node-pool create \
--cluster-id ocid1.cluster.oc1.iad.aaaa______m4w \
--name my-cloud-init-test-nodepool \
--node-image-id ocid1.image.oc1.iad.aaaa______zpq \
--compartment-id ocid1.tenancy.oc1..aaa______q4a \
--kubernetes-version v1.18.10 \
--node-shape VM.Standard2.1 \
--placement-configs "[  { \"availabilityDomain\": \"PKGK:US-ASHBURN-AD-1\", \"subnetId\": \"ocid1.subnet.oc1.iad.aaaa______kfa\"  }  ]" \
--size 1 \
--region us-ashburn-1 \
--node-metadata '{"user_data": "'$(cat my-custom-cloud-init.yaml | base64)'"}'
```

Was this article helpful?
YesNo


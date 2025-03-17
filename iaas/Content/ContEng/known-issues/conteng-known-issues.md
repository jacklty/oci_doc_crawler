Updated 2025-03-06
# Known Issues for Kubernetes Engine (OKE)
Known issues have been identified in Kubernetes Engine.
## Worker node properties out-of-sync with updated node pool properties 🔗  

Details
    
The properties of new worker nodes starting in a node pool do not reflect the latest changes to the node pool's properties. The likely cause is use of the deprecated quantityPerSubnet and subnetIds attributes when using the UpdateNodePoolDetails API operation to update node pool properties. 

Workaround
    
Do one of the following:
  * Start using the nodeConfigDetails attribute when using the UpdateNodePoolDetails API operation. First, scale the node pool to 0 using quantityPerSubnet. Then stop using the subnetIds and quantityPerSubnet attributes, and use the nodeConfigDetails attribute instead.
  * Contact Oracle Support to restart the back-end component responsible for synchronization (the tenant-agent component).


## Unable to launch Kubernetes Dashboard 🔗  

Details
    
When you launch the Kubernetes Dashboard, in some situations you might encounter "net/http: TLS handshake timeout" and "connection reset by peer" error messages in your web browser. This issue has only been observed in newly created clusters running Kubernetes version 1.11. For details about a related Kubernetes issue, see <https://github.com/kubernetes/dashboard/issues/3038>. 

Workaround
    
  1. In a terminal window, enter:
```
$ kubectl -n kube-system port-forward svc/kubernetes-dashboard 8443:443
```

  2. In your web browser, go to `https://localhost:8443`


## Unable to access in-cluster Helm 🔗  

Details
    
When you use a Kubeconfig token version 2.0.0 to access Helm/Tiller versions prior to version 2.11, you will receive one of the following errors: 
  * `Error: Unauthorized`
  * `Error: could not get Kubernetes client: exec plugin: invalid apiVersion "client.authentication.k8s.io/v1beta1"`



Workaround
    
Upgrade Helm/Tiller as follows:
  1. In a terminal window, download a Kubeconfig token version 1.0.0 by entering the following command:
Copy
```
$ oci ce cluster create-kubeconfig --token-version=1.0.0 --cluster-id=<cluster_ocid>
```

  2. Identify the region key to use to specify the Oracle Cloud Infrastructure Registry registry in the cluster's region (see [Availability by Region](https://docs.oracle.com/iaas/Content/Registry/Concepts/registryprerequisites.htm#regional-availability)). For example, if the cluster is in US East (Ashburn), `iad` is the region key to use to specify the registry in that region.
  3. Upgrade Tiller by entering the following command:
Copy
```
$ helm init --upgrade -i <region-key>.ocir.io/odx-oke/oke-public/tiller:v2.14.3
```

where `<region-key>` is the key that you identified in the previous step.
  4. In a browser, navigate to <https://helm.sh/docs/using_helm/#installing-the-helm-client> and follow the instructions to download and install the Helm client binary.
  5. Having upgraded Helm/Tiller, download a Kubeconfig token version 2.0.0 by entering the following command:
Copy
```
$ oci ce cluster create-kubeconfig --token-version=2.0.0 --cluster-id=<cluster_ocid>
```



## Some Kubernetes features (for example, the Metrics Server) cannot communicate with the kubelet via http/2 🔗  

Details
    
The Kubernetes Engine 1.8.0 release included a security improvement to improve cipher strength on the kubelet running on customer worker nodes. New worker nodes created between August 20, 2019 and September 16, 2019 include this configuration. The new set of ciphers does not allow connections to the kubelet via http/2. This restriction impacts the Metric Server, and also the Horizontal Pod Autoscaler which depends on the Metrics Server. 

Workaround
    
For each existing worker node in turn:
  1. Prevent new pods from starting and delete existing pods on the worker node by entering `kubectl drain <node_name>`. For more information:
     * about using kubectl, see [Accessing a Cluster Using Kubectl](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaccessingclusterkubectl.htm#Accessing_a_Cluster_Using_Kubectl "Find out how to use kubectl to access a Kubernetes cluster you've created using Kubernetes Engine \(OKE\).")
     * about the drain command, see [drain](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#drain) in the Kubernetes documentation
**Recommended:** Leverage pod disruption budgets as appropriate for your application to ensure that there's a sufficient number of replica pods running throughout the drain operation.
  2. Delete the worker node (for example, by terminating it in the Console).
  3. Wait for a replacement worker node to start.


The replacement worker nodes include include new settings to enable communication with the kubelet.
## Kubernetes pods fail to mount volumes due to timeouts 🔗  

Details
    
When a new pod starts on a worker node in a cluster, in some situations the pod fails to mount all volumes attached to the node due to timeouts and you see a message similar to the following:
```
Unable to mount volumes for pod "<pod_name>(<pod_uid>)": timeout expired waiting for volumes to attach or mount for pod "<namespace>"/"<pod_name>". list of unmounted volumes=[<failed_volume>]. list of unattached volumes=[<… list of volumes >]
```

One possible cause identified for this issue is if the pod spec includes an `fsGroup` field in the `securityContext` field. If the container is running on a worker node as a non-root user, setting the `fsGroup` field in the `securityContext` can cause timeouts due to the number of files to which Kubernetes must make ownership changes (see <https://github.com/kubernetes/kubernetes/issues/67014>). 
If the pod spec does not include an `fsgroup` field in the `securityContext`, the cause is unknown. 

Workaround
    
If the pod spec includes the `fsgroup` field in the `securityContext` and the container is running a non-root user, consider the following workarounds:
  * Remove the `fsgroup` field from the `securityContext`.
  * Use the `supplementalGroups` field in the `securityContext` (instead of `fsgroup`), and set `supplementalGroups` to the volume identifier.
  * Change the pod spec so that the container runs as root.


If the pod spec does not include the `fsgroup` field in the `securityContext`, or if the container is already running as root, you have to restart or replace the worker node. For example, by stopping and starting the instance, by rebooting the instance, or by terminating the instance so that a new instance is started. Follow the instructions in [Stopping, Starting, or Restarting an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/restartinginstance.htm) or [Terminating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/terminatinginstance.htm) as appropriate to use the Console or the API. Alternatively you can use CLI commands, such as the following example to terminate an instance:
```
$ INSTANCE_OCID=$(kubectl get node <name> -ojsonpath='{.spec.providerID}')
$ oci compute instance terminate --instance-id $INSTANCE_OCID
```

where `<name>` is the worker node name, derived from the Private IP Address property of the instance (for example, `10.0.10.5`).
## OS Management causes Kubernetes cluster node pools to fail 🔗  

Details
    
When using the OS Management service to manage operating system updates and patches on Oracle Cloud Infrastructure instances, there are some situations in which cluster node pools created by Kubernetes Engine fail to come online. 

Workaround
    
There are two possible workarounds:
  * **Workaround 1:** If you want to use OS Management to manage Oracle Cloud Infrastructure instances, enable Oracle Enterprise Linux in OS Management. See [Managing Software Sources](https://docs.oracle.com/iaas/os-management/osms/osms-software-sources.htm).
  * **Workaround 2:** If you don't want to use OS Management to manage Oracle Cloud Infrastructure instances, make sure there are no policies that allow OS Management to run. Specifically, remove the policy that grants a dynamic group of instances access to the OS Management service. See [Setting Up Policies for OS Management](https://docs.oracle.com/iaas/os-management/osms/osms-getstarted.htm#osms-setup-policies). 


## Volume mount issues in node pools with master nodes running Kubernetes version 1.19 (or later) and worker nodes running Kubernetes version 1.18 (or earlier) 🔗  

Details
    
If node pools have master nodes running Kubernetes version 1.19 (or later) and worker nodes running Kubernetes version 1.18 (or earlier), mounting block volumes attached to the cluster using the FlexVolume volume plugin might not work as expected. For example, you might see:
  * A `FailedMount` warning message in the events of a pod running on a worker node, even though the block volume has been attached successfully.
  * A `Volume not attached according to node status for volume` error message in the logs of the kubelet running on a worker node.



Workaround
    
  1. If there isn't already a node pool in the cluster with worker nodes running Kubernetes version 1.19 (or later), add such a node pool now. 
  2. Remove the affected worker node that is running Kubernetes version 1.18 (or earlier), as follows:
    1. Prevent new pods from starting and delete existing pods on the affected worker node by entering `kubectl drain <node_name>`. For more information:
       * about using kubectl, see [Accessing a Cluster Using Kubectl](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaccessingclusterkubectl.htm#Accessing_a_Cluster_Using_Kubectl "Find out how to use kubectl to access a Kubernetes cluster you've created using Kubernetes Engine \(OKE\).")
       * about the drain command, see [drain](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#drain) in the Kubernetes documentation
    2. Delete the affected worker node (for example, by terminating it in the Console).


## Issues resolving with DNS (nslookup, dig, or curl)  🔗  

Details
    
If the Bridge Netfilter kernel module is not enabled, traffic communication with `localhost` doesn't route correctly. For example: ```
/ # nslookup www.oracle.com
;; reply from unexpected source: 10.244.0.167#53, expected 10.96.5.5#53
;; reply from unexpected source: 10.244.0.167#53, expected 10.96.5.5#53
;; reply from unexpected source: 10.244.0.167#53, expected 10.96.5.5#53
;; connection timed out; no servers could be reached 
```

To verify this issue, open a terminal window on the instance and run the following command:
```
sudo /usr/sbin/lsmod | grep br_netfilter 
```

If no results are returned, then the Bridge Netfilter kernel module is not enabled. The Bridge Netfilter kernel module is required to masquerade VxLAN traffic for Kubernetes pods. 

Workaround
    
Enable the Bridge Netfilter kernel module. Open a terminal window on the instance and run the following commands: 
```
sudo modprobe br_netfilter 
sudo sh -c 'echo "br_netfilter" > /etc/modules-load.d/br_netfilter.conf'
```

## Source client IP is not preserved for traffic through a LoadBalancer Service using externalTrafficPolicy: Local 🔗  

Details
    
When using VCN-native pod networking, the source client IP address of inbound requests to a pod might not be preserved as expected. Instead, inbound requests received via a Kubernetes service of type LoadBalancer that has `externalTrafficPolicy: Local` set in the manifest file might be shown as originating from the worker node's IP address. 

Workaround
    
For inbound TCP requests received via a Kubernetes service of type LoadBalancer that has the `oci.oraclecloud.com/load-balancer-type: "lb"` annotation in the manifest file, obtain the source client IP address from the `X-Forwarded-For` or `X-Real-IP` header.
## Pod network connectivity issues on bare metal instances 🔗  

Details
    
When using VCN-native pod networking, pods might be unable to communicate over the network if you have specified a bare metal shape for worker nodes in one or more of the node pools in the cluster. 

Workaround
    
Specify a VM shape for worker nodes in every node pool in the cluster when using VCN-native pod networking.
## Incorrect maximum pods per node limit for flexible shapes 🔗  

Details
    
When using VCN-native pod networking, the maximum number of pods per worker node in a node pool might be limited to 31, regardless of the number of OCPUs you specify for the flexible shape you have selected for the node pool.  

Workaround
    
If you want more than 31 pods per worker node in a node pool, select a different shape for worker nodes in the node pool.
## Pod network connectivity issues on VCNs with added CIDR blocks 🔗  

Details
    
When using VCN-native pod networking, pods running on worker nodes connected to a pod subnet with a CIDR block outside the first CIDR block specified for the VCN might be unable to communicate with Kubernetes services. 

Workaround
    
Create pod subnets with CIDR blocks within the first CIDR block specified for the VCN.
## Node Doctor script displays FileNotFoundError: [Errno 2] exception 🔗  

Details
    
When using the Node Doctor script to troubleshoot node issues, the script might display an exception error message similar to the following:
```
FileNotFoundError: [Errno 2] No such file or directory: '/home/opc/vendor/pip…
```

The Node Doctor script will probably continue to run and, having displayed the message `Generating node doctor bundle`, produce troubleshooting output. 

Workaround
    
We are aware of the issue and working on a resolution. In the meantime, if the Node Doctor script displays the message `Generating node doctor bundle`, note that the troubleshooting output is still valid.
If you do not want the Node Doctor script to display the `FileNotFoundError: [Errno 2]...` exception error message, update the Node Doctor script by entering:
Copy
```
node-doctor.sh --update
```

For more information about the Node Doctor script and how to update it, see [Troubleshooting Node Issues for Kubernetes Clusters Using the Node Doctor Script](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtroubleshooting_topic-node_troubleshooting.htm#contengtroubleshooting_topic_node_troubleshooting "Find out how to use the Node Doctor script to help you resolve issues with compute instances hosting worker nodes in clusters you've created using Kubernetes Engine \(OKE\).").
## RESOLVED: DNS resolution sometimes fails in clusters using VCN-native pod networking 🔗  

Details
    
If a cluster uses VCN-native pod networking and has both a workload pod and the CoreDNS pod running on the same worker node, DNS resolution sometimes fails because traffic is incorrectly NATed. 

Resolution
    
On 2023-03-21, an update to the OCI VCN-Native Pod Networking CNI plugin was released that resolved this issue. Follow the instructions in [Updating the OCI VCN-Native Pod Networking CNI plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin__section_vcn_native_upgrade) to deploy the update.
## RESOLVED: Pods sometimes fail to start on a worker node running Oracle Linux 8, in clusters using VCN-native pod networking 🔗  

Details
    
If a cluster uses VCN-native pod networking and has worker nodes running Oracle Linux 8 (OL8), pods sometimes fail to start on one of the worker nodes. The issue has the following characteristics:
  * The worker node is running an OL8 image.
  * Host-network related pods run as expected on the worker node, but all other pods fail to start.
  * The crictl logs contain the message `Adding address to IPVLAN parent device` (indicating that an IP address is being attached to the worker node's secondary VNIC), followed by the error message `Error adding secondary VNIC IP`.
  * Running the Linux `ip address` command on the worker node shows that one (or more) secondary VNICs does not have an attached IP address.
  * All (or most) other worker nodes are operating as expected.


A likely cause identified for this issue is related to the NetworkManager, which manages network devices and connections. In some cases, the NetworkManager detaches the IP address attached to one or more of the worker node's secondary VNICs, causing the OCI VCN-Native Pod Networking CNI plugin to fail.  

Resolution
    
On 2023-03-21, an update to the OCI VCN-Native Pod Networking CNI plugin was released that resolved this issue. Follow the instructions in [Updating the OCI VCN-Native Pod Networking CNI plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin__section_vcn_native_upgrade) to deploy the update.
## Worker node status unexpectedly changes to NotReady when running Oracle Linux 8.7 or Oracle Linux 8.8 with Kubernetes version 1.24.1, 1.25.4, or 1.26.2 🔗  

Details
    
If you have specified Oracle Linux 8.7 or Oracle Linux 8.8 for a node pool (by selecting an Oracle Linux 8.7 or Oracle Linux 8.8 platform image, or an OKE worker node image built on top of Oracle Linux 8.7 or Oracle Linux 8.8), the status of the node pool's worker nodes might unexpectedly change to `NotReady`. The issue has the following characteristics:
  * The worker nodes are running Oracle Linux 8.7 or Oracle Linux 8.8.
  * The worker nodes are running Kubernetes version 1.24.1, 1.25.4, or 1.26.2. (Worker nodes running Kubernetes version 1.25.12, 1.26.7, and 1.27 are not affected.)
  * Short-lived pods are frequently deployed on the worker nodes.
  * Pods deployed on worker nodes in the node pool might also remain in the `ContainerCreating` status for longer than you expect. 



Workaround
    
We are aware of the issue and working on a resolution. 
In the meantime, if you encounter this issue, use whichever of the following workarounds best meets your requirements:
  * Specify an Oracle Linux 7 image for the node pool.
  * Specify an Oracle Linux 8.6 image (or an earlier Oracle Linux 8 image) for the node pool.
  * Specify a later version of Kubernetes for the node pool. (Worker nodes running Kubernetes version 1.25.12, 1.26.7, and 1.27 are not affected.)


To obtain the OCIDs of images that no longer appear in the Console:
  * **Platform images:** See [All Oracle Linux 7.x Images](https://docs.oracle.com/iaas/images/oraclelinux-7x/) and [All Oracle Linux 8.x Images](https://docs.oracle.com/iaas/images/oracle-linux-8x/)
  * **OKE worker node images:** See [All OKE Worker Node Oracle Linux 7.x Images](https://docs.oracle.com/iaas/images/oke-worker-node-oracle-linux-7x/) and [All OKE Worker Node Oracle Linux 8.x Images](https://docs.oracle.com/iaas/images/oke-worker-node-oracle-linux-8x/)


## Provisioning new worker nodes takes longer than expected in clusters using VCN-native pod networking 🔗  

Details
    
In clusters created before June 26, 2023 that use VCN-native pod networking, you might see a delay in the provisioning of new worker nodes.
When bootstrapping worker nodes with the OCI VCN-Native Pod Networking CNI plugin, Kubernetes Engine deploys a Kubernetes custom resource (the NativePodNetwork, or NPN, resource) on each compute instance. When a worker node has been successfully bootstrapped, Kubernetes Engine gives a status of SUCCESS to the NPN resource associated with the compute instance . 
In some cases, if a compute instance is terminated before Kubernetes Engine gives a status of SUCCESS to the associated NPN resource, the NPN resource remains in a BACKOFF or IN_PROGRESS status indefinitely. The existence of such 'stale' resources can delay the provisioning of new worker nodes. 

Resolution
    
The issue is fixed in clusters created after 2023-06-26. To resolve the issue in clusters created before 2023-06-26, take a one-time action to delete the stale resources by following the instructions in this section.
Before you start, make sure that your system meets the following prerequisites:
  * the OCI CLI is installed (see [Installing the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliinstall.htm))
  * the OCI CLI is configured (see [Configuring the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliconfigure.htm))
  * jq has been downloaded and installed (see <https://jqlang.github.io/jq/download/>)
  * an IAM policy exists that grants at least the INSTANCE_READ permission, such as `Allow group <group-name> to manage instance-family in <location>` (see [Create Required Policy for Groups](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm#policyforgroupsrequired))
  * the appropriate kubeconfig files are accessible to enable you to use kubectl to manage clusters that use the OCI VCN-Native Pod Networking CNI plugin (see [Accessing a Cluster Using Kubectl](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaccessingclusterkubectl.htm#Accessing_a_Cluster_Using_Kubectl "Find out how to use kubectl to access a Kubernetes cluster you've created using Kubernetes Engine \(OKE\)."))


Identify and delete the stale resources as follows:
  1. Validate that your system meets all the prerequisites:
    1. Save the following script in a file named `pre-req-check.sh`:
Copy
```
#!/bin/bash
echo Validating cluster access to get npn resources
ACTIVE_RESOURCES=($(kubectl get npn -o json | jq '[.items[] | select(.status.state == "SUCCESS")]' | jq -r '.[] | .metadata.name'))
if [[ -z "$ACTIVE_RESOURCES" ]] || [ ${#ACTIVE_RESOURCES[@]} == 0 ]
then
 echo No active NPN resources found. Make sure you have cluster access and this is an OCI VCN-Native CNI cluster. '\'nPlease check prerequisites and retry.
 exit
fi
 
cr_name=${ACTIVE_RESOURCES[0]}
echo Validating access to get compute instance
INSTANCE_ID=$(kubectl get npn $cr_name -o json | jq -r '. | .spec.id')
INSTANCE_STATE=$(oci compute instance get --instance-id $INSTANCE_ID | jq -r '. | .data."lifecycle-state"')
 
if [[ -z "$INSTANCE_STATE" ]]
then
 echo Unable to get instance details, please check prerequisites and retry.
else
 echo All prerequisites in place, please proceed to cleaning up stale resources.
fi
```

    2. Run the `pre-req-check.sh` script by entering:
Command
CopyTry It
```
sh pre-req-check.sh
```

  2. Identify NPN resources that are possible candidates for deletion because they do not have a status of SUCCESS:
    1. Output a list of NPN resources that do not have a status of SUCCESS to a text file named` potential_stale_resources.txt` by entering:
Command
CopyTry It
```
kubectl get npn -o json | jq '[.items[] | select(.status.state != "SUCCESS")]' | jq -r '.[] | .metadata.name' >> potential_stale_resources.txt
```

    2. Optionally view the list of candidate NPN resources in `potential_stale_resources.txt` by entering:
Command
CopyTry It
```
cat potential_stale_resources.txt
```

For example, `potential_stale_resources.txt` might contain:
```
anyhqljth4...trq
anyhqljth4...snq
anyhqljth4...qhq
```

  3. Identify the stale NPN resources to delete by determining which candidate NPN resources are associated with compute instances that are not available or have been terminated:
    1. Save the following script in a file named `get_stale_resources.sh`:
Copy
```
#!/bin/bash
resources=$1
echo Reading resources from $1
while read -r cr_name
do
 echo verifying NPN resource $cr_name
 INSTANCE_ID=$(kubectl get npn $cr_name -o json | jq -r '. | .spec.id')
 if [ -z $INSTANCE_ID ]
 then
  echo Unable to get npn resource details. Please check prerequisites and retry from step 2.
  exit
 fi
 echo Associated instance is $INSTANCE_ID
 INSTANCE_STATE=$(oci compute instance get --instance-id $INSTANCE_ID | jq -r '. | .data."lifecycle-state"')
 if [ -z $INSTANCE_STATE ]
 then
  # check for 404 for tombstoned instances
  STATUS=$(oci compute instance get --instance-id $INSTANCE_ID 2>&1 | tail -n +2 | jq .status)
  if [ $STATUS == 404 ]
  then
   echo 404 getting instance $INSTANCE_ID, Instance has been tombstoned. Adding resource $cr_name to stale_resources.txt '\'n
   echo $cr_name >> stale_resources.txt
  fi
 else
  echo Instance $INSTANCE_ID in $INSTANCE_STATE state
  if [ $INSTANCE_STATE == "TERMINATED" ]
  then
   echo Adding resource $cr_name to stale_resources.txt '\'n
   echo $cr_name >> stale_resources.txt
  else
   echo Instance $INSTANCE_ID not terminated. '\'nSkipping resource $cr_name '\'n
  fi
 fi
done < $1
```

    2. Run the `get_stale_resources.sh` script by entering:
Command
CopyTry It
```
sh get_stale_resources.sh potential_stale_resources.txt
```

The `get_stale_resources.sh` script identifies the stale NPN resources to delete, outputs processing messages to the screen, and writes the names of stale NPN resources to a file named `stale_resources.txt`. For example:
```
Reading resources from potential_stale_resources.txt
verifying NPN resource anyhqljth4...trq
Associated instance is ocid1.instance.oc1.phx.anyhqljth4...trq
Instance ocid1.instance.oc1.phx.anyhqljth4...trq in RUNNING state
Instance ocid1.instance.oc1.phx.anyhqljth4...trq not terminated.
Skipping resource anyhqljth4...trq
 
verifying NPN resource anyhqljth4...snq
Associated instance is ocid1.instance.oc1.phx.anyhqljth4...snq
Instance ocid1.instance.oc1.phx.anyhqljth4...snq in TERMINATED state
Adding resource anyhqljth4...snq to stale_resources
 
verifying NPN resource anyhqljth4...qhq
Associated instance is ocid1.instance.oc1.phx.anyhqljth4...qhq
ServiceError:
{
  "client_version": "Oracle-PythonSDK/2.104.2, Oracle-PythonCLI/3.29.0",
  "code": "NotAuthorizedOrNotFound",
  "logging_tips": "Please run the OCI CLI command using --debug flag to find more debug information.",
  "message": "instance ocid1.instance.oc1.phx.anyhqljth4...qhq not found",
  "opc-request-id": "CCB8D1925...38ECB8",
  "operation_name": "get_instance",
  "request_endpoint": "GET https://iaas.us-phoenix-1.oraclecloud.com/20160918/instances/ocid1.instance.oc1.phx.anyhqljth4...qhq",
  "status": 404,
  "target_service": "compute",
  "timestamp": "2023-06-27T20:24:28.992241+00:00",
  "troubleshooting_tips": "See [https://docs.oracle.com/iaas/Content/API/References/apierrors.htm] for more information about resolving this error. If you are unable to resolve this issue, run this CLI command with --debug option and contact Oracle support and provide them the full error message."
}
404 getting instance ocid1.instance.oc1.phx.anyhqljth4...qhq, Instance has been tombstoned
Adding resource anyhqljth4...qhq to stale_resources
```

    3. Optionally view the list of stale NPN resources in `stale_resources.txt` by entering:
Command
CopyTry It
```
cat stale_resources.txt
```

For example, `stale_resources.txt` might contain:
```
anyhqljth4...snq
anyhqljth4...qhq
```

  4. Delete the stale NPN resources listed in the `stale_resources.txt` file:
    1. Save the following script in a file named `delete_stale_resources.sh`:
Copy
```
#!/bin/bash
resources=$1
echo Reading resources from $1
while read -r cr_name
do
  echo Deleting $cr_name
  kubectl delete npn $cr_name
done < $1
```

    2. Run the `delete_stale_resources.sh` script by entering:
Command
CopyTry It
```
sh delete_stale_resources.sh stale_resources.txt
```

The `delete_stale_resources.sh` script deletes the stale NPN resources listed in the `stale_resources.txt` file and outputs processing messages to the screen. For example:
```
Reading resources from stale_resources.txt
Deleting anyhqljth4...snq
nativepodnetwork.oci.oraclecloud.com "anyhqljth4...snq" deleted
```

  5. As good housekeeping practice, delete the `stale_resources.txt` and `potential_stale_resources.txt` files you created previously.


## Virtual node Architecture shown as AMD64 when pods scheduled to run on Arm processors 🔗  

Details
    
When you specify an Arm shape for a virtual node, pods scheduled on the node run on Arm processors as intended. However, if you examine the virtual node using the `kubectl describe node` command or the Kubernetes API, the node's Architecture property indicates `AMD64`, even though pods scheduled on the node run on Arm processors.  

Workaround
    
We are aware of the issue and working on a resolution.
In the meantime, if you encounter this issue, ignore the value of the virtual node's Architecture property.
## OCI Load Balancers cannot be updated when delete protection is enabled 🔗  

Details
    
When Kubernetes Engine provisions an OCI load balancer for a Kubernetes service of type LoadBalancer, the load balancer does not have delete protection enabled.
If you subsequently use the Console, the CLI, or the API to enable delete protection for the load balancer, the cloud-controller-manager is not only prevented from deleting the load balancer, but is also unable to update any of the load balancer's properties.  

Workaround
    
We are aware of the issue and working on a resolution.
In the meantime, do not use the Console, the CLI, or the API to enable delete protection for a load balancer.
Note that using the Console, the CLI, or the API to modify OCI load balancers provisioned by Kubernetes Engine is not recommended (for more information, see [Defining Kubernetes Services of Type LoadBalancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancer.htm#Creating_Load_Balancers_to_Distribute_Traffic_Between_Cluster_Nodes "Find out how to create different types of load balancer to distribute traffic between the nodes of a cluster you've created using Kubernetes Engine \(OKE\).")).
## Clusters in OC2 and OC3 are not using the latest version of the OCI VCN-Native Pod Networking CNI plugin 🔗  

Details
    
New versions of the OCI VCN-Native Pod Networking CNI plugin are normally released in the OC1, OC2, and OC3 realms. 
However, on September 3, 2024, OCI VCN-Native Pod Networking CNI plugin version 2.2.0, containing security and performance enhancements, was released in the OC1 realm only.
On October 4, 2024, OCI VCN-Native Pod Networking CNI plugin version 2.2.2 was released in the OC1, OC2, and OC3 realms, containing further enhancements.
Therefore, between September 3, 2024 and October 4, 2024:
  * New clusters you created in the OC2 and OC3 realms used the earlier version of the OCI VCN-Native Pod Networking CNI plugin, namely version 2.1.0.
  * In the case of existing clusters in the OC2 and OC3 realms, even if you had specified that you wanted Oracle to deploy updates to the OCI VCN-Native Pod Networking CNI plugin on a cluster automatically, version 2.2.0 was not deployed on those clusters.


Regardless of whether you or Oracle is responsible for deploying updates to the OCI VCN-Native Pod Networking CNI plugin, the updates are only applied when worker nodes are next rebooted. 
As a result, you might have clusters in the OC2 and OC3 realms that are still running OCI VCN-Native Pod Networking CNI plugin version 2.1.0. 

Workaround
    
To benefit from the enhancements in OCI VCN-Native Pod Networking CNI plugin versions 2.2.0 and 2.2.2, we strongly recommend that you update any cluster in OC2 or OC3 to use version 2.2.2.
OCI VCN-Native Pod Networking CNI plugin version 2.2.0 will not be released in the OC2 and OC3 realms, even though you can select version 2.2.0 in the Console.
If you enable the OCI VCN-Native Pod Networking CNI plugin for an enhanced cluster in the OC2 or OC3 realm, and specify that you want to choose the version of the add-on to deploy, do not select version 2.2.0. Instead, select version 2.2.2 (or later). If you do select version 2.2.0 for an enhanced cluster in the OC2 and OC3 realms, be aware that worker nodes will not come up and the cluster will not function.
For more information, see [Using the OCI VCN-Native Pod Networking CNI plugin for pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin "Find out about the OCI VCN-Native Pod Networking CNI plugin for pod communication on worker nodes in clusters created using Kubernetes Engine \(OKE\).").
## Clusters exhibit unexpected delays when interacting with the Kubernetes API server (also known as kube-apiserver latency) 🔗  

Details
    
When you work with a Kubernetes cluster created by Kubernetes Engine, you might notice unexpected delays when the cluster interacts with the Kubernetes API server (such as slow responses to kubectl commands).
If you are using a client machine with an older version of the OCI CLI and/or Python installed, these intermittent spikes in kube-apiserver latency might be due to a known OCI CLI performance issue. This performance issue has been observed with Python version 3.6 specifically.
By default, the kubeconfig file that Kubernetes Engine creates for a cluster contains an OCI CLI command to generate a token (the [oci ce cluster generate-token](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/generate-token.html) command). The token is used to authenticate requests to the kube-apiserver. Currently, each kube-apiserver request triggers an invocation of the OCI CLI to run the command to generate the token. It is this OCI CLI invocation that might be impacted by the known OCI CLI performance issue.
To confirm that kube-apiserver latency is caused by the known OCI CLI performance issue, locate and view the kubeconfig file being used by the client. In the `users` section of the kubeconfig file, locate the user associated with the cluster in question. Assuming that no modifications have been made to the kubeconfig file to use a service account (see [Adding a Service Account Authentication Token to a Kubeconfig File](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaddingserviceaccttoken.htm#Adding_a_Service_Account_Authentication_Token_to_a_Kubeconfig_File "Find out how to add a service account authentication token to the kubeconfig file of a Kubernetes cluster you've created using Kubernetes Engine \(OKE\).")), the `user` section contains the OCI CLI token generation command in the following yaml format:
```
- name: <user-name>
 user:
  exec:
   apiVersion: client.authentication.k8s.io/v1beta1
   args:
   - ce
   - cluster
   - generate-token
   - --cluster-id
   - <your-cluster-ocid>
   - --region
   - <your-region>
   command: oci
   env: []
```

To confirm that kube-apiserver latency is caused by the known performance issue, use the following command to return the time that the OCI CLI takes to run the token generation command:
```
time oci ce cluster generate-token --cluster-id <your-cluster-ocid> --region <your-region>
```

If the time taken to run the command is close to the kube-apiserver latency that you have observed, you might be experiencing the known performance issue. 

Workaround
    
Make sure that you are using the latest stable version of the OCI CLI, along with a supported version of Python (see [Manual Installation](https://docs.oracle.com/iaas/Content/API/SDKDocs/climanualinst.htm#climanualinst_intro) in the OCI CLI documentation).
If you are using Python version 3.6, we recommend that you upgrade to a newer Python version.
If you cannot upgrade to a newer Python version, disable the importing of all services (the default behavior) and instead selectively import only those individual services and modules that are required. Selectively importing services is known to improve the performance of Python version 3.6. For more information, see [Enable Selective Service Imports for Python 3.6](https://docs.oracle.com/iaas/tools/python/latest/sdk_behaviors/enable_selective_service_imports.html).
Was this article helpful?
YesNo


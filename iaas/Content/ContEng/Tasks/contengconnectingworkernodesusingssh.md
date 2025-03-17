Updated 2024-08-14
# Connecting to Managed Nodes Using SSH
_Find out how to use SSH to connect to worker nodes in node pools in clusters you've created using Kubernetes Engine (OKE)._
If you provided a public SSH key when creating a managed node pool in a cluster, the public key is installed on all worker nodes in the node pool. On UNIX and UNIX-like platforms (including Solaris and Linux), you can then connect through SSH to the worker nodes using the ssh utility (an SSH client) to perform administrative tasks. Note you cannot connect to virtual nodes using SSH.
Note the following instructions assume the UNIX machine you use to connect to the worker node:
  * Has the ssh utility installed.
  * Has access to the SSH private key file paired with the SSH public key that was specified when the cluster was created.


How to connect to worker nodes using SSH depends on whether you specified public or private subnets for the worker nodes when defining the node pools in the cluster.
## Connecting to Managed Nodes in Public Subnets Using SSH 🔗 
Before you can connect to a managed node in a public subnet using SSH, you must define an ingress rule in the applicable network security group (recommended) or subnet security list to allow SSH access. The ingress rule must allow access to port 22 on worker nodes from source 0.0.0.0/0 and any source port, as follows:
Type | Source CIDR | IP Protocol | Source Port Range | Dest. Port Range | Type and Code | Allows: and Description:  
---|---|---|---|---|---|---  
Stateful | 0.0.0.0/0 | TCP | All | 22 | n/a |  **Allows:** TCP traffic for ports: 22 SSH Remote Login Protocol **Description:** Enables SSH access.  
To connect to a managed node in a public subnet through SSH from a UNIX machine using the ssh utility:
  1. Find out the IP address of the worker node to which you want to connect. You can do this in a number of ways:
     * Using kubectl. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster."). Then in a terminal window, enter `kubectl get nodes` to see the public IP addresses of worker nodes in node pools in the cluster.
     * Using the Console. In the Console, display the **Cluster List** page and then select the cluster to which the worker node belongs. On the **Node Pools** tab, click the name of the node pool to which the worker node belongs. On the **Nodes** tab, you see the public IP address of every worker node in the node pool.
     * Using the REST API. Use the [ListNodePools](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePoolSummary/ListNodePools) operation to see the public IP addresses of worker nodes in a node pool.
  2. In the terminal window, enter `ssh opc@<node_ip_address>` to connect to the worker node, where `<node_ip_address>` is the IP address of the worker node that you made a note of earlier. For example, you might enter `ssh opc@192.0.2.254`.
Note that if the SSH private key is not stored in the file or in the path that the ssh utility expects (for example, the ssh utility might expect the private key to be stored in ~/.ssh/id_rsa), you must explicitly specify the private key filename and location in one of two ways:
     * Use the `-i` option to specify the filename and location of the private key. For example, `ssh -i ~/.ssh/my_keys/my_host_key_filename opc@192.0.2.254`
     * Add the private key filename and location to an SSH configuration file, either the client configuration file (~/.ssh/config) if it exists, or the system-wide client configuration file (/etc/ssh/ssh_config). For example, you might add the following:
```
Host 192.0.2.254 IdentityFile ~/.ssh/my_keys/my_host_key_filename
```

For more about the ssh utility's configuration file, enter `man ssh_config`
Note also that permissions on the private key file must allow you read/write/execute access, but prevent other users from accessing the file. For example, to set appropriate permissions, you might enter `chmod 600 ~/.ssh/my_keys/my_host_key_filename`. If permissions are not set correctly and the private key file is accessible to other users, the ssh utility will simply ignore the private key file.


## Connecting to Managed Nodes in Private Subnets Using SSH 🔗 
Managed worker nodes in private subnets have private IP addresses only (they do not have public IP addresses). They can only be accessed by other resources inside the VCN.
You can use Cloud Shell Private Access to gain SSH access to worker nodes in private subnets (see [Cloud Shell Private Networking](https://docs.oracle.com/iaas/Content/API/Concepts/devcloudshellintro.htm#Cloud_Shell_Private_Access)).
Oracle recommends using the Oracle Cloud Infrastructure Bastion service to enable external SSH access to worker nodes in private subnets. For more information about bastions, see [Setting Up a Bastion for Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm#contengsettingupbastion "Find out how to set up a bastion to access clusters you've created using Kubernetes Engine \(OKE\).").
Was this article helpful?
YesNo


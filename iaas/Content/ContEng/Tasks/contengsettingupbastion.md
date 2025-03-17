Updated 2025-01-15
# Setting Up a Bastion for Cluster Access
_Find out how to set up a bastion to access clusters you've created using Kubernetes Engine (OKE)._
When performing operations on a cluster using kubectl, you must have access to the Kubernetes API endpoint. Similarly, when performing administrative tasks on worker nodes, you must have access to the worker nodes. However, access to the Kubernetes API endpoint and/or the worker nodes might be restricted due to security list rules, or because the Kubernetes API endpoint and/or the worker nodes are in a private subnet. In these situations, you can set up bastions in the Oracle Cloud Infrastructure Bastion service to provide secure access to the Kubernetes API endpoint and/or the worker nodes.
Setting up bastions and bastion sessions involves a number of different tasks. Depending on your organization, these tasks might be performed by the same person, or by different people, as follows:
  * A VCN administrator is responsible for creating the VCN, the subnets, and the security rules for a Kubernetes cluster and a bastion. IAM policies enable the VCN administrator to manage the VCN.
  * A cluster administrator is responsible for creating bastions to access Kubernetes API endpoints and worker nodes, and for creating bastion sessions for worker node access. IAM policies enable the cluster administrator to manage clusters and bastions.
  * A cluster user is responsible for creating bastion sessions to access Kubernetes API endpoints. IAM policies enable the cluster user to use clusters and bastions.


This diagram shows an example cluster configuration with a bastion providing secure access to a cluster's Kubernetes API endpoint and worker nodes.
[![This image shows an example cluster configuration with a Kubernetes API endpoint subnet, a worker node subnet, and load balancer subnets. Access to the subnets is controlled by the seclist-KubernetesAPIendpoint, seclist-workernodes, and seclist-loadbalancers security lists respectively. The Kubernetes API endpoint subnet is connected to the cluster control plane by a VNIC. A bastion in a bastion subnet provides SSH access to the cluster's Kubernetes API endpoint and worker nodes. Other features of this example configuration are described in the surrounding text.](https://docs.oracle.com/en-us/iaas/Content/ContEng/images/conteng-network-bastion-to-API-and-workers.png)](https://docs.oracle.com/en-us/iaas/Content/ContEng/images/conteng-network-bastion-to-API-and-workers.png)
## Required IAM Policies for Creating and Using Bastions to Access Clusters 🔗 
For information on the IAM policies required to create bastions and bastion sessions, see [Bastion Policies](https://docs.oracle.com/iaas/Content/Bastion/Reference/bastionpolicyreference.htm).
If desired, cluster administrators can also set up IAM policies to limit the resources that cluster users can access using a bastion. See [Setting up IAM policies to limit the use of bastions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm#contengsettingupbastion_topic_Using_IAM_policies_to_limit_bastion_access).
## Setting up a bastion to access the Kubernetes API endpoint 🔗 
For cluster users to access the private Kubernetes API endpoint of a cluster, VCN administrators, cluster administrators, and cluster users each have to perform a number of steps, as described in this section.
### VCN Administrator Steps 🔗 
As the VCN administrator, follow these steps to set up egress and ingress security rules to enable a bastion to access the Kubernetes API endpoint:
  1. Create a new private subnet to host the bastion, in the same VCN as the cluster to which you want to provide access.
Note that if you've already created a subnet to host a bastion to access worker nodes, you can reuse that subnet instead of creating a new subnet. See [Setting up a bastion to provide SSH access to managed nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm#contengsettingupbastion_topic_Access_worker_nodes).
  2. Add the following TCP/6443 egress security rule to the security list associated with the bastion subnet.
This egress security rule allows traffic from the bastion subnet to the cluster's Kubernetes API endpoint subnet.
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | Kubernetes API Endpoint CIDR (for example, 10.0.0.0/29) | TCP/6443 | Allow bastion to Kubernetes API endpoint communication.  
  3. If it's not already present, add the following TCP/6443 ingress security rule to a new or existing security list associated with the subnet hosting the Kubernetes API endpoint. 
This ingress security rule allows traffic into the Kubernetes API endpoint subnet from the bastion subnet.
State: | Source | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | Bastion subnet CIDR | TCP/6443 | Allow bastion to Kubernetes API endpoint communication.  
**Note**
Although it is not Oracle's preferred design, you can use the same subnet for both the bastion and the cluster's Kubernetes API endpoint. In this case, add the TCP/6443 egress security rule to the security list associated with the Kubernetes API endpoint subnet.


### Cluster Administrator Steps
As the cluster administrator, follow these steps to set up a bastion to access the Kubernetes API endpoint:
  1. Create a bastion, as follows:
    1. In the Console, open the navigation menu and click ****Identity & Security****.
    2. Click ****Bastion****.
    3. On the **Bastion** page, click **Create bastion**.
    4. In the **Create bastion** dialog, set the following properties:
       * **Bastion name:** A name for the bastion. Avoid entering confidential information. Only alphanumeric characters are supported.
       * **Target Virtual Cloud Network:** Specify the VCN of the Kubernetes cluster to which you want to provide access.
       * **Target Subnet:** The subnet to host the bastion, with the ingress and egress security rules you've set up.
       * **CIDR Block Allowlist:** One or more address ranges in CIDR notation that you want to allow to connect to sessions hosted by this bastion. For example, 0.0.0.0/0 to allow access from the internet, or a more limited address range. For example, 203.0.113.0/24. 
    5. (Optional) To change the maximum amount of time that any session on this bastion can remain active, click **Show Advanced Options** , and then enter a value for **Maximum Session Time-to-Live**.
    6. Click **Create Bastion**.
    7. When the bastion has been created, click the name of the bastion to see information about it, including its OCID.
For more information about creating a bastion, see [To create a bastion](https://docs.oracle.com/iaas/Content/Bastion/Tasks/managingbastions.htm#To_create_a_bastion).
  2. Provide cluster users with the OCID of the bastion.
  3. Ensure that suitable IAM policies are in place to authorize cluster users to use the bastion. See [Required IAM Policies for Creating and Using Bastions to Access Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm#contengsettingupbastion__section_ghr_1sm_yrb).
If desired, you can also set up IAM policies to limit the resources that cluster users can access using the bastion. See [Setting up IAM policies to limit the use of bastions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm#contengsettingupbastion_topic_Using_IAM_policies_to_limit_bastion_access).


### Cluster User Steps
As a cluster user, follow these steps to create a bastion session to access the Kubernetes API endpoint:
  1. If you haven't done so already, create the kubeconfig file for the cluster you want to access, by running:```
oci ce cluster create-kubeconfig \
 --cluster-id <cluster OCID> \
 --file $HOME/.kube/config \
 --region <region> \
 --token-version 2.0.0

```

  2. Edit the cluster's kubeconfig file and change the IP address specified for `server` to specify the IP address and port on which to listen for SSH traffic:
    1. Locate the line:```
server: https://x.x.x.x:6443
```

    2. Change the line to:```
server: https://127.0.0.1:6443
```

For example:
```
apiVersion: v1
clusters:
- cluster:
  certificate-authority-data:______
  server: https://127.0.0.1:6443
- name: cluster-xxxxxxx
…

```

  3. Create a bastion session using the Console or the CLI as follows:
[Using the Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm)
    1. On the **Bastion** page, click the name of the bastion created by the cluster administrator.
    2. On the **Sessions** page, click **Create session**.
    3. In the **Create session** dialog, set the following properties:
       * **Session type:** Select **SSH port forwarding session**.
       * **Session name:** A display name for the new session. Avoid entering confidential information.
       * **Connect to the target host by using:** Select **IP address**.
       * **IP address** : Specify the IP address part of the cluster's Kubernetes API private endpoint (shown on the **Cluster Details** page).
       * **Port:** Specify the port part of the cluster's Kubernetes API private endpoint (shown on the **Cluster Details** page). For example, 6443.
       * **SSH Key:** Specify the public key file of an existing SSH key pair that you want to use for the session, or generate a new SSH key pair and save the private key.
    4. (Optional) To change the maximum amount of time that the session can remain active, click **Show Advanced Options** , and then enter a value for **Maximum Session Time-to-Live**.
    5. Click **Create session**.
[Using the CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm)
```
oci bastion session create-port-forwarding \
 --bastion-id <bastion OCID> \
 --ssh-public-key-file <ssh public key> \
 --target-private-ip <API Private IP endpoint> \
 --target-port 6443

```

For more information about creating a bastion session, see [To create a session](https://docs.oracle.com/iaas/Content/Bastion/Tasks/managingsessions.htm#To_create_a_session).
  4. Obtain the command to create an SSH tunnel using the Console or the CLI as follows:
[Using the Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm)
On the **Sessions** page, select **Copy SSH Command** from the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) beside the session you have just created.
[Using the CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm)
```
oci bastion session get --session-id <session OCID> | jq '.data."ssh-metadata".command'
```

The SSH tunnel command you've obtained has the following format:
```
ssh -i <privateKey> -N -L <localPort>:<session-IP>:<session-port> -p 22 <session-ocid>
```

where:
     * `<session-IP>:<session-port>` is the IP address and port number of the Kubernetes API endpoint that you specified when creating the bastion session. For example, `10.0.0.6:6443`.
     * `<session-ocid>` is the OCID of the bastion session you created.
  5. Execute the command to create the SSH tunnel on a local workstation or in Cloud Shell, as follows:
    1. Edit the SSH tunnel command you've obtained as follows:
       * Replace `<privateKey>` with the path to the file containing the private key of the SSH key pair you specified for the session. For example, `/home/johndoe/.ssh/id_rsa`
       * Replace `<localPort>` with `6443`, or a free port on your system (either a local workstation if your network is peered with the cluster's VCN, or Cloud Shell)
       * Add `&` to the end of the command to make the command run in the background.
    2. Run the edited SSH tunnel command on a local workstation, or in the Cloud Shell window.
For example:
```
ssh -i /home/johndoe/.ssh/id_rsa -N -L 6443:10.0.0.6:6443 -p 22 ocid1.bastionsession_______oraclecloud.com &
```



You can now perform kubectl operations on the cluster until the SSH tunnel or bastion session times out.
## Setting up a bastion to provide SSH access to managed nodes 🔗 
For cluster users to have SSH access to managed nodes, VCN administrators, cluster administrators, and cluster users each have to perform a number of steps, as described in this section.
### VCN Administrator Steps
As the VCN administrator, follow these steps to set up egress and ingress security rules to enable a bastion to provide SSH access to managed nodes:
  1. Create a new subnet to host the bastion, in the same VCN as the cluster to which you want to provide access.
Note that if you've already created a subnet to host a bastion to access the Kubernetes API endpoint, you can reuse that subnet instead of creating a new subnet. See [Setting up a bastion to access the Kubernetes API endpoint](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm#contengsettingupbastion_topic_Access_Kubernetes_API_endpoint).
  2. Add the following TCP/22 egress security rule to the security list associated with the bastion subnet.
This egress security rule allows traffic from the bastion subnet to the worker nodes subnet.
State: | Destination | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | Worker Nodes CIDR (for example, 10.0.1.0/24) | TCP/22 | Allow bastion to worker nodes communication.  
  3. If it's not already present, add the following TCP/22 ingress security rule to a new or existing security list associated with the subnet hosting the worker nodes.
This ingress security rule allows traffic into the worker node subnet from the bastion subnet.
State: | Source | Protocol / Dest. Port | Description:  
---|---|---|---  
Stateful | Bastion subnet CIDR | TCP/22 | Allow bastion to worker nodes communication.  
**Note**
Although it is not Oracle's preferred design, you can use the same subnet for both the bastion and the worker nodes. In this case, add the TCP/22 egress security rule to the security list associated with the worker node subnet.


### Cluster Administrator Steps
As the cluster administrator, follow these steps to set up a bastion to provide SSH access to managed nodes:
  1. Enable the bastion agent on the worker node to which you want to connect through SSH as follows:
    1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. On the **Cluster List** page, click the name of the cluster containing the worker node to which you want to connect.
    3. Under **Resources** , click **Node Pools** and click the name of the node pool containing the worker node to which you want to connect.
    4. Under **Resources** , click **Nodes** and click the name of the worker node to which you want to connect.
    5. On the **Instance Details** page, display the **Oracle Cloud Agent** tab, and toggle the **Enabled** the **Bastion** plugin.
It can take up to 10 minutes for the change to take effect.
    6. Wait until the Bastion plugin **Status** is shown as **Running** before continuing to the next step.
  2. Create a bastion, as follows:
    1. Open the navigation menu and click ****Identity & Security****.
    2. Click ****Bastion****.
    3. On the **Bastion** page, click **Create bastion**.
    4. In the **Create bastion** dialog, set the following properties:
       * **Bastion name:** A name for the bastion. Avoid entering confidential information. Only alphanumeric characters are supported.
       * **Target Virtual Cloud Network:** Specify the VCN of the Kubernetes cluster to which you want to provide access.
       * **Target Subnet:** The subnet to host the bastion, with the ingress and egress security rules you've set up.
       * **CIDR Block Allowlist:** One or more address ranges in CIDR notation that you want to allow to connect to sessions hosted by this bastion. For example, 0.0.0.0/0 to allow access from the internet, or a more limited address range. For example, 203.0.113.0/24. 
    5. (Optional) To change the maximum amount of time that any session on this bastion can remain active, click **Show Advanced Options** , and then enter a value for **Maximum Session Time-to-Live**.
    6. Click **Create Bastion**.
    7. When the bastion has been created, click the name of the bastion to see information about it, including its OCID.
For more information about creating a bastion, see [To create a bastion](https://docs.oracle.com/iaas/Content/Bastion/Tasks/managingbastions.htm#To_create_a_bastion).
  3. Provide cluster users with the OCID of the bastion.
  4. Ensure that suitable IAM policies are in place to authorize cluster users to use the bastion. See [Required IAM Policies for Creating and Using Bastions to Access Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm#contengsettingupbastion__section_ghr_1sm_yrb).
If desired, you can also set up IAM policies to limit the resources that cluster users can access using the bastion. See [Setting up IAM policies to limit the use of bastions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm#contengsettingupbastion_topic_Using_IAM_policies_to_limit_bastion_access).


### Cluster User Steps
As a cluster user, follow these steps to create a bastion session to provide SSH access to managed nodes:
  1. Create a bastion session using the Console or the CLI as follows:
[Using the CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm)
    1. On the **Bastion** page, click the name of the bastion created by the cluster administrator.
    2. On the **Sessions** page, click **Create session**.
    3. In the **Create session** dialog, set the following properties:
       * **Session type:** Select **Managed SSH session**.
       * **Session name:** A display name for the new session. Avoid entering confidential information.
       * **Username:** Enter `opc`.
       * **Compute instance in <compartment name>:** Select the name of the worker node compute instance from the list of compute instances in the compartment. If needed, change the compartment to find the instance. Only active instances are listed.
       * **SSH Key:** Specify the public key file of an existing SSH key pair that you want to use for the session, or generate a new SSH key pair and save the private key.
    4. (Optional) To change the maximum amount of time that the session can remain active, click **Show Advanced Options** , and then enter a value for **Maximum Session Time-to-Live**.
Notice that you do not change the default value in the **Target compute instance port** field (the default port is already set to 22). Also, you do not specify IP addresses in the **Target compute instance IP address** field because you already selected the compute instances.
    5. Click **Create session**.
[Using the CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm)
```
oci bastion session create-managed-ssh \
 --bastion-id <bastion OCID> \
 --ssh-public-key-file <ssh public key> \
 --target-resource-id <worker node instance OCID> \
 --target-os-username <instance_username>
```

For more information about creating a bastion session, see [To create a session](https://docs.oracle.com/iaas/Content/Bastion/Tasks/managingsessions.htm#To_create_a_session).
  2. Obtain the command to create an SSH tunnel using the Console or the CLI as follows:
[Using the Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm)
On the **Sessions** page, select **Copy SSH Command** from the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) beside the session you have just created.
[Using the CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm)
```
oci bastion session get --session-id <session OCID> | jq '.data."ssh-metadata".command'
```

The SSH tunnel command you've obtained has the following format:
```
ssh -i <privateKey> -o ProxyCommand="ssh -i <privateKey> -W %h:%p -p 22 <session-ocid>" -p 22 opc@<node-private-ip>
```

where:
     * `<session-ocid>` is the OCID of the bastion session you created.
     * `<node-private-ip>` is the private IP address of the worker node that you specified when creating the bastion session. For example, `10.0.10.99`.
  3. Execute the command to create the SSH tunnel on a local workstation or in Cloud Shell, as follows:
    1. Edit the SSH tunnel command you've obtained as follows:
       * Replace `<privateKey>` with the path to the file containing the private key of the SSH key pair you specified for the session. For example, `/home/johndoe/.ssh/id_rsa`
       * Add `&` to the end of the command to made the command run in the background.
    2. Run the edited SSH tunnel command on a local workstation, or in the Cloud Shell window.
For example:
```
ssh -i /home/johndoe/.ssh/id_rsa -o ProxyCommand="ssh -i /home/johndoe/.ssh/id_rsa -W %h:%p -p 22 ocid1.bastionsession_______oraclecloud.com" -p 22 opc@10.0.10.99 &
```



You can now perform operations on the worker nodes until the SSH tunnel or bastion session times out.
## Setting up IAM policies to limit the use of bastions 🔗 
Cluster administrators can set up IAM policies to limit the resources that cluster users can access using a bastion. For example, a common requirement is to restrict cluster users to the use of a bastion to access just a cluster's Kubernetes API endpoint, rather than also being able to access worker nodes via SSH. 
The following example policy allows users in the group `cluster-users` to create, connect to, and terminate bastion sessions for Kubernetes API endpoints (in subnet 10.0.0.11/32, on port 6443) only, in the compartment `ABC`:
```
Allow group cluster-users to use bastion in compartment ABC 
Allow group cluster-users to manage bastion-session in compartment ABC where ALL {target.bastion.ocid='ocid1.bastion.xxx', target.bastion-session.type='port_forwarding', target.bastion-session.ip in ['10.0.0.11/32'], target.bastion-session.port='6443'}
Allow group cluster-users to read vcn in compartment ABC
Allow group cluster-users to read subnet in compartment ABC
```

The example assumes:
  * A bastion has already been created.
  * The networks and worker nodes are in the same compartment as the bastion.
  * The network access must be set to the minimum required.


Was this article helpful?
YesNo


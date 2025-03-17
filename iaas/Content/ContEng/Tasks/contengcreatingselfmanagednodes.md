Updated 2025-02-12
# Creating Self-Managed Nodes
_Find out how to create a new self-managed node and add it to an existing cluster._
You use the Compute service to create the compute instance on which to run a self-managed node. Having created the self-managed node, you then add it to an existing enhanced cluster.
If you want a self-managed node to use the flannel CNI plugin for pod networking, you can create the self-managed node using the Console, the CLI, and the API. If you want a self-managed node to use the OCI VCN-Native Pod Networking CNI plugin for pod networking, you can create the self-managed node using the CLI, and the API.
**Note** For information about creating self-managed nodes that run Ubuntu, see [Running Ubuntu on Worker Nodes Using Custom Images](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes "Find out how to include worker nodes that run the Ubuntu Linux distribution in clusters created with Kubernetes Engine \(OKE\), using custom images and cloud-init scripts.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingselfmanagednodes.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingselfmanagednodes.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingselfmanagednodes.htm)


  * To create a self-managed node using the Console:
    1. Create the cloud-init script containing the Kubernetes API private endpoint and base64-encoded CA certificate of the enhanced cluster to which you want to add the self- managed node. See [Creating Cloud-init Scripts for Self-managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcloudinitforselfmanagednodes.htm#contengcloudinitforselfmanagednodes "Find out how to create the cloud-init script for a self-managed node that you want to add to an enhanced cluster created with Kubernetes Engine.").
    2. Create a new compute instance to host the self-managed node:
      1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
      2. Follow the instructions in the [Compute service documentation](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm) to create a new compute instance. Note that appropriate policies must exist to allow the new compute instance to join the enhanced cluster. See [Creating a Dynamic Group and a Policy for Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdynamicgrouppolicyforselfmanagednodes.htm#contengprereqsforselfmanagednodes-accessreqs "Find out how to create a dynamic group and a policy to allow the compute instance hosting a self-managed node to join an enhanced cluster created with Kubernetes Engine.").
      3. In the **Image and Shape** section, click **Change image**. 
      4. Click **My images** , select the **Image OCID** option, and then enter the OCID of the OKE Oracle Linux 7 (OL7) or Oracle Linux 8 (OL8) image you want to use. See [Image Requirements](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengprereqsforselfmanagednodes.htm#contengprereqsforselfmanagednodes-imagereqs).
      5. Click **Show advanced options** , and on the **Management** tab, select the **Paste cloud-init script** option.
      6. Copy and paste the cloud-init script containing the Kubernetes API private endpoint and base64-encoded CA certificate into the **Cloud-init script** field. See [Creating Cloud-init Scripts for Self-managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcloudinitforselfmanagednodes.htm#contengcloudinitforselfmanagednodes "Find out how to create the cloud-init script for a self-managed node that you want to add to an enhanced cluster created with Kubernetes Engine.").
      7. Click **Create** to create the compute instance to host the self-managed node.
When the compute instance is created, it is added as a self-managed node to the cluster with the Kubernetes API endpoint that you specified . 
    3. Verify that the self-managed node has been added to the Kubernetes cluster and confirm the node's readiness status by entering:
Command
CopyTry It
```
kubectl get nodes
```

For example:
```
kubectl get nodes
NAME      STATUS  ROLES  AGE  VERSION
10.0.103.170  Ready  <none>  40m  v1.25.4
```

    4. Confirm that labels have been added to the node and set as expected by entering:
Command
CopyTry It
```
kubectl get node <node-name> -o json | jq '.metadata.labels'
```

For example
```
kubectl get node 10.0.103.170 -o json | jq '.metadata.labels'
{
...
"displayName": "oke-self-managed-node",
"oci.oraclecloud.com/node.info.byon": "true",
...
}
```

  * Use the [oci Compute instance launch](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html) command and required parameters to create a self-managed node:
Command
CopyTry It
```
oci compute instance launch --availability-domain <availability-domain> --compartment-id <compartment-ocid> --shape <shape> --subnet-id <subnet-ocid> [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**Tips:**
    * Specify the name of the file containing the cloud-init script (required to add the compute instance to the cluster as a self-managed node) using the [oci Compute instance launch](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html) command's `--user-data-file` parameter. See [Creating Cloud-init Scripts for Self-managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcloudinitforselfmanagednodes.htm#contengcloudinitforselfmanagednodes "Find out how to create the cloud-init script for a self-managed node that you want to add to an enhanced cluster created with Kubernetes Engine.").
    * Specify the image to use to create the self-managed node by setting the [oci Compute instance launch](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html) command's `--image-id` parameter. See [Image Requirements](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengprereqsforselfmanagednodes.htm#contengprereqsforselfmanagednodes-imagereqs).
    * If you want the self-managed node to use the OCI VCN-Native Pod Networking CNI plugin for pod networking, add the `--metadata` parameter to the `oci compute instance launch` command, as follows:
Copy
```
--metadata '{"oke-native-pod-networking": "true", "oke-max-pods": "<max-pods-per-node>", "pod-subnets": "<pod-subnet-ocid>", "pod-nsgids": "<nsg-ocid>"}'
```

where:
      * `"oke-native-pod-networking": "true"` specifies that you want the self-managed node to use the OCI VCN-Native Pod Networking CNI plugin for pod networking.
      * `"oke-max-pods": "<max-pods-per-node>"` specifies the maximum number of pods that you want to run on the self-managed node.
      * `"pod-subnets": "<pod-subnet-ocid>"` specifies the OCID of the pod subnet that supports communication between pods and direct access to individual pods using private pod IP addresses. The pod subnet must be a private subnet. 
      * `"pod-nsgids": "<nsg-ocid>"` optionally specifies the OCID of one or more network security groups (NSGs) containing security rules to route network traffic to pods. When specifying multiple NSGs, use a comma-delimited list in the format `"pod-nsgids": "<nsg-ocid-1>,<nsg-ocid-2>"`
For more information about the OCI VCN-Native Pod Networking CNI plugin, see [Using the OCI VCN-Native Pod Networking CNI plugin for pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin "Find out about the OCI VCN-Native Pod Networking CNI plugin for pod communication on worker nodes in clusters created using Kubernetes Engine \(OKE\).").
    * If you want the self-managed node to be a dual stack IPv4/IPv6 node (with both IPv4 and IPv6 addresses), add the `--metadata` parameter to the `oci compute instance launch` command, as follows:
Copy
```
--metadata '{"ip-families": "IPv4,IPv6"}'
```

**Examples:**
Example 1: Command to create a self-managed node that uses the flannel CNI plugin for pod networking.
Copy
```
oci compute instance launch \
  --profile oc1 \
  --compartment-id ocid1.compartment.oc1..aaaaaaa______neoq \
  --subnet-id ocid1.subnet.oc1.phx.aaaaaaa______hzia \
  --shape VM.Standard2.2 \
  --availability-domain zkJl:PHX-AD-1 \
  --image-id ocid1.image.oc1.phx.aaaaaaa______lcra \
  --display-name smn \
  --user-data-file my-cloud-init-file \
  --ssh-authorized-keys-file my-ssh-key-file
```

Example 2: Command to create a self-managed node that uses the OCI VCN-Native Pod Networking CNI plugin for pod networking.
Copy
```
oci compute instance launch \
  --profile oc1 \
  --compartment-id ocid1.compartment.oc1..aaaaaaa______neoq \
  --subnet-id ocid1.subnet.oc1.phx.aaaaaaa______hzia \
  --shape VM.Standard2.2 \
  --availability-domain zkJl:PHX-AD-1 \
  --image-id ocid1.image.oc1.phx.aaaaaaa______lcra \
  --display-name smn-npn \
  --user-data-file my-cloud-init-file \
  --ssh-authorized-keys-file my-ssh-key-file \
  --metadata '{"oke-native-pod-networking": "true", 
   "oke-max-pods": "21", 
   "pod-subnets": "ocid1.subnet.oc1.phx.aaaaaaa______4wka"},
   "pod-nsgids": "ocid1.networksecuritygroup.oc1.phx.aaaaaaa______qfca,ocid1.networksecuritygroup.oc1.phx.aaaaaaa______ohea"'
```

Example 3: Alternative command to create a self-managed node that uses the OCI VCN-Native Pod Networking CNI plugin for pod networking.
Copy
```
oci compute instance launch \
  --profile oc1 \
  --compartment-id ocid1.compartment.oc1..aaaaaaa______neoq \
  --subnet-id ocid1.subnet.oc1.phx.aaaaaaa______hzia \
  --shape VM.Standard2.2 \
  --availability-domain zkJl:PHX-AD-1 \
  --image-id ocid1.image.oc1.phx.aaaaaaa______lcra \
  --display-name smn-npn \
  --metadata '{"ssh_authorized_keys": "ssh-rsa AAAAB3NzaC1yc2EAAAA...",
   "oke-native-pod-networking": "true",
   "oke-max-pods": "21",
   "pod-subnets": "ocid1.subnet.oc1.phx.aaaaaaa______4wka,ocid1.subnet.oc1.phx.aaaaaaa______hzia",
   "pod-nsgids": "ocid1.networksecuritygroup.oc1.phx.aaaaaaa______qfca,ocid1.networksecuritygroup.oc1.phx.aaaaaaa______",
   "user_data": "IyEvdXNyL2Jpbi9lbnYgYmFzaA..."}'
```

  * Run the [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance) operation to create a self-managed node.
If you want the self-managed node to use the OCI VCN-Native Pod Networking CNI plugin for pod networking, use the **metadata** attribute to specify values for the following keys:
    * **oke-native-pod-networking:** Set to true to specify that you want the self-managed node to use the OCI VCN-Native Pod Networking CNI plugin for pod networking.
    * **oke-max-pods** : The maximum number of pods that you want to run on the self-managed node.
    * **pod-subnets** : The OCID of the pod subnet that supports communication between pods and direct access to individual pods using private pod IP addresses. The pod subnet must be a private subnet. 
    * **pod-nsgids:** (optional) The OCID of one or more network security groups (NSGs) containing security rules to route network traffic to pods. When specifying multiple NSGs, use a comma-delimited list in the format `"pod-nsgids": "<nsg-ocid-1>,<nsg-ocid-2>"`
For more information about the OCI VCN-Native Pod Networking CNI plugin, see [Using the OCI VCN-Native Pod Networking CNI plugin for pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin "Find out about the OCI VCN-Native Pod Networking CNI plugin for pod communication on worker nodes in clusters created using Kubernetes Engine \(OKE\).").


Was this article helpful?
YesNo


Updated 2025-02-05
# Running Ubuntu on Worker Nodes Using Custom Images
_Find out how to include worker nodes that run the Ubuntu Linux distribution in clusters created with Kubernetes Engine (OKE), using custom images and cloud-init scripts._
Ubuntu is a popular open-source Linux distribution that is commonly used to run GPU-intensive and AI/ML workloads. When you create clusters with Kubernetes Engine (OKE), you can use custom images and cloud-init scripts to create the following types of worker node to run Ubuntu:
  * managed nodes
  * self-managed nodes


Note that you cannot create virtual nodes to run Ubuntu using custom images and cloud-init scripts.
At a high level, the process for creating a worker node to run Ubuntu is:
  * [Step 1: Create a custom image based on an existing compute instance running the required Ubuntu release](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_createcustomimage). Oracle provides node packages for different Ubuntu releases, and each node package is compatible with certain Kubernetes versions. For more information, see [Availability and Compatibility](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_availabilitycompatibility).
  * [Step 2: Construct the URL from which to download an Ubuntu node package](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_constructubuntuurl). The URL from which to download the Ubuntu node package provided by Oracle depends on both the Ubuntu release and the Kubernetes version that you want to run on the worker node. There is a different download URL for each supported combination of Ubuntu release and Kubernetes version.
  * [Step 3: Create a cloud-init script to install the Ubuntu node package and bootstrap the worker node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_createcloudinitscript). The cloud-init script to create depends on whether the worker node on which you want to run Ubuntu is a managed node, or a self-managed node.
  * [Step 4: Add worker nodes running Ubuntu to a cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_addworkernodes). The way in which you add Ubuntu nodes to a cluster depends on whether you want to add the nodes as managed nodes or as self-managed nodes. For managed nodes, you define a managed node pool. For self-managed nodes, you add compute instances as worker nodes. 


## Availability and Compatibility 🔗 
This table lists the Ubuntu releases for which Oracle provides node packages, along with the Kubernetes versions that each node package is compatible with. The node packages that Oracle provides are designed to work on both x86 and ARM architectures. 
Ubuntu release | Package to use with Kubernetes 1.27 | Package to use with Kubernetes 1.28 | Package to use with Kubernetes 1.29 | Package to use with Kubernetes 1.30 | Package to use with Kubernetes 1.31  
---|---|---|---|---|---  
Jammy (Ubuntu 22.04) | `oci-oke-node-all-1.27.10` | `oci-oke-node-all-1.28.10` | `oci-oke-node-all-1.29.1` | `oci-oke-node-all-1.30.1` | `oci-oke-node-all-1.31.1`  
Noble (Ubuntu 24.04) | `oci-oke-node-all-1.27.10` | `oci-oke-node-all-1.28.10` | `oci-oke-node-all-1.29.1` | `oci-oke-node-all-1.30.1` | `oci-oke-node-all-1.31.1`  
## Step 1: Create a custom image based on an existing compute instance running the required Ubuntu release 🔗 
In this step, you use the Compute service to create a custom image from a compute instance that is already running the Ubuntu release you want on worker nodes in the Kubernetes cluster.
Note that you create the image as a 'custom' image, even though you do not modify the image.
  1. Decide which Ubuntu release and which Kubernetes version you want on worker nodes. 
Oracle provides node packages for different Ubuntu releases, and each node package is compatible with certain Kubernetes versions. For more information, see [Availability and Compatibility](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_availabilitycompatibility).
  2. Identify an existing compute instance that is running the Ubuntu release you require.
This is the compute instance that you will use as the basis of the custom image.
If a suitable compute instance does not already exist, follow the instructions in [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm) in the Compute service documentation to create a suitable compute instance now.
  3. Follow the instructions in [Managing Custom Images](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm#Using2) in the Compute service documentation, to create a custom image based on the existing compute instance that is running the Ubuntu release you require.
  4. Make a note of the OCID of the custom image you have created.


## Step 2: Construct the URL from which to download an Ubuntu node package 🔗 
In this step, you construct the URL from which to download the Ubuntu node package provided by Oracle.
The download URL depends on the Ubuntu release and Kubernetes version you want on worker nodes. The download URL includes the Object Storage location, as well as details of the particular Ubuntu release and Kubernetes version.
Bear in mind that the versions of Kubernetes running on control plane nodes and on worker nodes (including self-managed nodes) must be compatible, as described in the [Kubernetes version skew support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/) in the Kubernetes documentation. It is your responsibility to construct the download URL for a node package that contains a compatible Kubernetes version. Kubernetes Engine does not check that the Kubernetes version in the node package you specify is compatible with the Kubernetes version running on the cluster's control plane nodes.
Construct the download URL as follows:
  1. Open a new text file in your preferred text editor.
  2. Create the download URL as follows:
Copy
```
https://objectstorage.us-sanjose-1.oraclecloud.com/p/45eOeErEDZqPGiymXZwpeebCNb5lnwzkcQIhtVf6iOF44eet_efdePaF7T8agNYq/n/odx-oke/b/okn-repositories-private/o/prod/ _<ubuntu-release>_/_<kubernetes-version>_ stable main
```

where:
     * `_<ubuntu-release>_`is one of the following, according to the release of Ubuntu that you want to run on the worker node:
       * `ubuntu-jammy` (Ubuntu 22.04)
       * `ubuntu-noble` (Ubuntu 24.04)
     * `_<kubernetes-version>_`is one of the following, according to the minor version of Kubernetes that you want to run on the worker node:
       * `kubernetes-1.27`
       * `kubernetes-1.28`
       * `kubernetes-1.29`
       * `kubernetes-1.30`
       * `kubernetes-1.31`
For example, if you want to run Ubuntu 22.04 and Kubernetes version 1.29 on worker nodes, construct the following download URL for the appropriate node package:
```
https://objectstorage.us-sanjose-1.oraclecloud.com/p/45eOeErEDZqPGiymXZwpeebCNb5lnwzkcQIhtVf6iOF44eet_efdePaF7T8agNYq/n/odx-oke/b/okn-repositories-private/o/prod/ubuntu-noble/kubernetes-1.29 stable main
```

  3. (optional) Save the text file in a convenient location, as you need the download URL in the next step.


## Step 3: Create a cloud-init script to install the Ubuntu node package and bootstrap the worker node 🔗 
In this step, you create a cloud-init script to download and install the Ubuntu node package provided by Oracle, and to bootstrap the worker node.
Note that there is different logic to add to the cloud-init script, depending on whether you want to run Ubuntu on managed nodes, or on self-managed nodes.
### Creating a cloud-init script for managed nodes
To create a cloud-init script to run Ubuntu on managed nodes:
  1. Create a new cloud-init script file from scratch with a filetype supported by cloud-init (such as .yaml), and add the following logic to the script file:```
#cloud-config
apt:
 sources:
  oke-node: {source: 'deb [trusted=yes] _<download-url>_}
packages:                            
 - _<oci-package-name>_
runcmd:
 - oke bootstrap
```

where:
     * `_<download-url>_`is the URL from which to download the Ubuntu node package that you constructed in the previous step (see[Step 2: Construct the URL from which to download an Ubuntu node package](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_constructubuntuurl)). For example, `https://objectstorage.us-sanjose-1.oraclecloud.com/p/45eOeErEDZqPGiymXZwpeebCNb5lnwzkcQIhtVf6iOF44eet_efdePaF7T8agNYq/n/odx-oke/b/okn-repositories-private/o/prod/ubuntu-jammy/kubernetes-1.29 stable main`
     * _`<oci-package-name>`_is one of the following, according to the minor version of Kubernetes that you want to run on the managed node:
       * `oci-oke-node-all-1.27.10`
       * `oci-oke-node-all-1.28.10`
       * `oci-oke-node-all-1.29.1`
       * `oci-oke-node-all-1.30.1`
       * `oci-oke-node-all-1.31.1`
The Kubernetes minor version must match the Kubernetes minor version you specified when constructing the download URL (see [Step 2: Construct the URL from which to download an Ubuntu node package](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_constructubuntuurl)).
For example, if you want to run Ubuntu 22.04 (jammy) and Kubernetes version 1.29.1 on managed nodes, add the following logic to the script file:
```
#cloud-config
apt:
 sources:
  oke-node: {source: 'deb [trusted=yes] https://objectstorage.us-sanjose-1.oraclecloud.com/p/45eOeErEDZqPGiymXZwpeebCNb5lnwzkcQIhtVf6iOF44eet_efdePaF7T8agNYq/n/odx-oke/b/okn-repositories-private/o/prod/ubuntu-jammy/kubernetes-1.29 stable main}
packages:                            
 - oci-oke-node-all-1.29.1
runcmd:
 - oke bootstrap
```

  2. Save the cloud-init script file.


### Creating a cloud-init script for self-managed nodes
To create a cloud-init script to run Ubuntu on self-managed nodes:
  1. Follow the instructions in [Creating Cloud-init Scripts for Self-managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcloudinitforselfmanagednodes.htm#contengcloudinitforselfmanagednodes "Find out how to create the cloud-init script for a self-managed node that you want to add to an enhanced cluster created with Kubernetes Engine.") to obtain the Kubernetes API private endpoint of the enhanced cluster to which you want to add the self-managed node, using the Console or the CLI.
  2. Follow the instructions in [Creating Cloud-init Scripts for Self-managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcloudinitforselfmanagednodes.htm#contengcloudinitforselfmanagednodes "Find out how to create the cloud-init script for a self-managed node that you want to add to an enhanced cluster created with Kubernetes Engine.") to obtain the cluster's base64-encoded CA certificate from the cluster's kubeconfig file, using the Console or the CLI.
  3. Create a new cloud-init script file from scratch with a filetype supported by cloud-init (such as .yaml), and add the following logic to the script file:```
#cloud-config
apt:
 sources:
  oke-node: {source: 'deb [trusted=yes] _<download-url>_}
packages:
 - _<oci-package-name>_
write_files:
- path: /etc/oke/oke-apiserver
 permissions: '0644'
 content: _<cluster-endpoint>_
- encoding: b64
 path: /etc/kubernetes/ca.crt
 permissions: '0644'
 content: _<base64-encoded-certificate>_
runcmd:
 - oke bootstrap --ca _<base64-encoded-certificate>_ --apiserver-host _<cluster-endpoint>_
```

where:
     * `_<download-url>_`is the URL from which to download the Ubuntu node package that you constructed in the previous step (see[Step 2: Construct the URL from which to download an Ubuntu node package](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_constructubuntuurl)). For example, `https://objectstorage.us-sanjose-1.oraclecloud.com/p/45eOeErEDZqPGiymXZwpeebCNb5lnwzkcQIhtVf6iOF44eet_efdePaF7T8agNYq/n/odx-oke/b/okn-repositories-private/o/prod/ubuntu-jammy/kubernetes-1.29 stable main`
     * `_<oci-package-name>_`is one of the following, according to the minor version of Kubernetes that you want to run on the self-managed node:
       * `oci-oke-node-all-1.27.10`
       * `oci-oke-node-all-1.28.10`
       * `oci-oke-node-all-1.29.1`
       * `oci-oke-node-all-1.30.1`
       * `oci-oke-node-all-1.31.1`
The Kubernetes minor version must match the Kubernetes minor version you specified when constructing the download URL (see [Step 2: Construct the URL from which to download an Ubuntu node package](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_constructubuntuurl)).
     * `_<cluster-endpoint>_`is the IP address of the cluster's Kubernetes API endpoint that you obtained earlier.
     * `_<base64-encoded-certificate>_`is the cluster's base64-encoded CA certificate that you obtained earlier (starting with the characters`LS0t`).
For example, if you want to run Ubuntu 22.04 (Jammy) and Kubernetes version 1.29.1 on a self-managed node, add the following logic to the script file:
```
#cloud-config
apt:
 sources:
  oke-node: {source: 'deb [trusted=yes] https://objectstorage.us-sanjose-1.oraclecloud.com/p/45eOeErEDZqPGiymXZwpeebCNb5lnwzkcQIhtVf6iOF44eet_efdePaF7T8agNYq/n/odx-oke/b/okn-repositories-private/o/prod/ubuntu-jammy/kubernetes-1.29 stable main}
packages:
 - oci-oke-node-all-1.29.1
write_files:
- path: /etc/oke/oke-apiserver
 permissions: '0644'
 content: 10.114.0.5
- encoding: b64
 path: /etc/kubernetes/ca.crt
 permissions: '0644'
 content: LS0tLS1...LS0tCg==
runcmd:
 - oke bootstrap --ca LS0tLS1...LS0tCg== --apiserver-host 10.114.0.5
```

  4. Save the cloud-init script file.


## Step 4: Add worker nodes running Ubuntu to a cluster 🔗 
In this step, you use the cloud-init script you created earlier to add worker nodes running Ubuntu to a Kubernetes cluster.
Note that there are different instructions to follow, depending on whether you want to run Ubuntu on managed nodes, or on self-managed nodes. For managed nodes, you define a managed node pool. For self-managed nodes, you add compute instances as worker nodes. 
Note that you have to use the CLI to create managed nodes based on custom images. 
### Adding Ubuntu worker nodes as managed nodes
To add managed nodes running Ubuntu in an existing cluster
  1. Open a command prompt and use the [oci ce node-pool create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/create.html) to create a new node pool.
  2. As well as the mandatory parameters required by the command:
    1. Include the `--node-image-id` parameter, and specify the OCID of the custom image that you created in [Step 1: Create a custom image based on an existing compute instance running the required Ubuntu release](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_createcustomimage). 
    2. Include the `--node-metadata` parameter and specify the cloud-init script that you created for managed nodes in [Step 3: Create a cloud-init script to install the Ubuntu node package and bootstrap the worker node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_createcloudinitscript), in the appropriate format for your environment:
       * **Linux:** `--node-metadata '{"user_data": "'$(cat _<cloud-init-file>_ | base64 -w 0)'"}'`
       * **Mac:** `--node-metadata '{"user_data": "'$(cat _<cloud-init-file>_ | base64- b 0)'"}'`
where:
       * `_<cloud-init-file>_`is the name of the cloud-init file that you created
       * `base64` specifies the file is to be base64-encoded
For example, you might enter the following command on a Mac work station:
```
oci ce node-pool create \
--cluster-id ocid1.cluster.oc1.iad.aaaa______m4w \
--name my-ubuntu-nodepool \
--node-image-id ocid1.image.oc1.iad.aaaa______zpq \
--compartment-id ocid1.tenancy.oc1..aaa______q4a \
--kubernetes-version v1.29.1 \
--node-shape VM.Standard2.1 \
--placement-configs "[{\"availabilityDomain\":\"PKGK:US-ASHBURN-AD-1\", \"subnetId\":\"ocid1.subnet.oc1.iad.aaaa______kfa\"}]" \
--size 3 \
--region us-ashburn-1 \
--node-metadata '{"user_data": "'$(cat my-mgd-ubuntu-cloud-init.yaml | base64 -b 0)'"}'
```

The Kubernetes version must match the Kubernetes version you specified in the cloud-init script (see [Step 3: Create a cloud-init script to install the Ubuntu node package and bootstrap the worker node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_createcloudinitscript)).
Note that the Kubernetes version you specify using the `--kubernetes-version` parameter must correspond to the Kubernetes version you specified in the cloud-init script (see [Step 3: Create a cloud-init script to install the Ubuntu node package and bootstrap the worker node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_createcloudinitscript)).


### Adding Ubuntu worker nodes as self-managed nodes
Before you create a self-managed node, confirm that:
  * The cluster to which you want to add the self-managed node is configured appropriately for self-managed nodes. See [Cluster Requirements](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengprereqsforselfmanagednodes.htm#contengprereqsforselfmanagednodes-clusterreqs).
  * A dynamic group and an IAM policy already exist to allow the compute instance hosting the self-managed node to join an enhanced cluster created with Kubernetes Engine. See [Creating a Dynamic Group and a Policy for Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdynamicgrouppolicyforselfmanagednodes.htm#contengprereqsforselfmanagednodes-accessreqs "Find out how to create a dynamic group and a policy to allow the compute instance hosting a self-managed node to join an enhanced cluster created with Kubernetes Engine.").


**Using the Console**
  1. Create a new compute instance to host the self-managed node:
    1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Follow the instructions in the [Compute service documentation](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm) to create a new compute instance. Note that appropriate policies must exist to allow the new compute instance to join the enhanced cluster. See [Creating a Dynamic Group and a Policy for Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdynamicgrouppolicyforselfmanagednodes.htm#contengprereqsforselfmanagednodes-accessreqs "Find out how to create a dynamic group and a policy to allow the compute instance hosting a self-managed node to join an enhanced cluster created with Kubernetes Engine.").
    3. In the **Image and Shape** section, click **Change image**. 
    4. Click **My images** , select the **Image OCID** option, and then enter the OCID of the custom image that you created in [Step 1: Create a custom image based on an existing compute instance running the required Ubuntu release](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_createcustomimage).
    5. Click **Show advanced options** , and on the **Management** tab, select the **Paste cloud-init script** option.
    6. Copy and paste the cloud-init script you created for self-managed nodes in [Step 3: Create a cloud-init script to install the Ubuntu node package and bootstrap the worker node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_createcloudinitscript), into the **Cloud-init script** field.
    7. Click **Create** to create the compute instance to host the self-managed node.
When the compute instance is created, it is added as a self-managed node to the cluster with the Kubernetes API endpoint that you specified in the cloud-init script.
  2. (Optional) Verify that the self-managed node has been added to the Kubernetes cluster, and that labels have been added to the node and set as expected, by following the instructions in [Creating Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingselfmanagednodes.htm#contengcreatingselfmanagednodes "Find out how to create a new self-managed node and add it to an existing cluster.").


**Using the CLI**
  1. Open a command prompt and enter the `oci Compute instance launch[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html)` command and required parameters to create a self-managed node.
  2. As well as the mandatory parameters required by the command:
    1. Include the `--image-id` parameter, and specify the OCID of the custom image that you created in [Step 1: Create a custom image based on an existing compute instance running the required Ubuntu release](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_createcustomimage). 
    2. Include the `--user-data-file` parameter and specify the cloud-init script that you created for self-managed nodes in [Step 3: Create a cloud-init script to install the Ubuntu node package and bootstrap the worker node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes_createcloudinitscript) .
For example, you might enter the following command:
```
oci compute instance launch \
--availability-domain zkJl:PHX-AD-1 \
--compartment-id ocid1.compartment.oc1..aaaaaaa______neoq \
--shape VM.Standard2.2 \
--subnet-id ocid1.subnet.oc1.phx.aaaaaaa______hzia \
--user-data-file my-selfmgd-ubuntu-cloud-init.yaml \
--image-id ocid1.image.oc1.phx.aaaaaaa______slcr
```

When the compute instance is created, it is added as a self-managed node to the cluster with the Kubernetes API endpoint that you specified in the cloud-init script. 


Was this article helpful?
YesNo


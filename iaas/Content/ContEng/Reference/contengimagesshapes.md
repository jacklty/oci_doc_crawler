Updated 2025-01-15
# Supported Images (Including Custom Images) and Shapes for Worker Nodes
_Find out about the images and shapes you can specify for worker nodes in clusters created by Kubernetes Engine (OKE)._
You can configure the worker nodes in a cluster by specifying:
  * The operating system image to use for worker nodes (managed nodes and self-managed nodes only). The image is a template of a virtual hard drive that determines the operating system and other software for the worker node. 
  * The shape to use for worker nodes (managed nodes, self-managed nodes, and virtual nodes). The shape is the number of CPUs and the amount of memory to allocate to each newly created instance to be used as a worker node. 


This topic includes information about the Oracle Linux images and the shapes provided by Oracle Cloud Infrastructure that are supported by Kubernetes Engine. Note that some of the shapes might not be available in your particular tenancy. 
**Note** For information about creating managed nodes and self-managed nodes that run Ubuntu, see [Running Ubuntu on Worker Nodes Using Custom Images](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes "Find out how to include worker nodes that run the Ubuntu Linux distribution in clusters created with Kubernetes Engine \(OKE\), using custom images and cloud-init scripts.").
## Supported Images for Managed Nodes 🔗 
Kubernetes Engine supports the provisioning of worker nodes (managed nodes only) using some, but not all, of the latest Oracle Linux images provided by Oracle Cloud Infrastructure.
You can use these Oracle Linux images when provisioning managed nodes:
  * [OKE Images](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengimagesshapes.htm#images__oke-images)
  * [Platform Images](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengimagesshapes.htm#images__platform-images)
  * [Custom Images](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengimagesshapes.htm#images__custom-images)


To see the images supported by Kubernetes Engine:
  * When using the Console to create a cluster in the 'Custom Create' workflow, view the list of supported platform images and OKE images in the **Browse all images** window. 
  * When using the CLI, view the supported platform, OKE, and custom images (in the `data: sources:` section of the response) by entering:
Command
CopyTry It
```
oci ce node-pool-options get --node-pool-option-id all
```



Note the following when using Oracle Linux 8 images:
  * Oracle Linux 8 supports [Federal Information Processing Standards (FIPS)](https://www.nist.gov/standardsgov/compliance-faqs-federal-information-processing-standards-fips), a set of standards and guidelines for federal computer systems. When using Oracle Linux 8 images, you can enable FIPS mode. For more information, see [Configuring a System in FIPS Mode](https://docs.oracle.com/en/operating-systems/oracle-linux/8/security/fips-sec.html#configure-fips) in the [Oracle Linux 8](https://docs.oracle.com/en/operating-systems/oracle-linux/8/index.html) documentation.
  * You can select Oracle Linux 8 images to provision managed nodes in node pools running Kubernetes 1.20.x and later.
  * Docker is not included in Oracle Linux 8 images. Instead, in node pools running Kubernetes 1.20.x and later, Kubernetes Engine installs and uses the CRI-O container runtime and the crictl CLI (for more information, see [Notes about Kubernetes Engine Support for Kubernetes Version 1.20](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutk8sversions.htm#previouslysupportedk8sversions__notes-1-20)).


**Note** For information about creating managed nodes that run Ubuntu, see [Running Ubuntu on Worker Nodes Using Custom Images](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes "Find out how to include worker nodes that run the Ubuntu Linux distribution in clusters created with Kubernetes Engine \(OKE\), using custom images and cloud-init scripts.").
### OKE Images 🔗 
OKE images are provided by Oracle and built on top of platform images. OKE images are optimized for use as managed node base images, with all the necessary configurations and required software. You can select OKE images as the base images for managed nodes when creating and updating clusters and node pools. Using an OKE image minimizes the time it takes to provision managed nodes at runtime when compared to platform images and custom images. The use of OKE images reduces managed node provisioning time by more than half when compared to platform images. 
To see the OKE images currently supported by Kubernetes Engine:
  * When using the Console to create a cluster in the 'Custom Create' workflow, choose **OKE images** as the**Image source** in the **Browse all images** window, and view the list of supported OKE images. 
  * When using the CLI, view the supported images (in the `data: sources:` section of the response) by entering:
Command
CopyTry It
```
oci ce node-pool-options get --node-pool-option-id all
```



OKE image names have the following format (and have `OKE` in the image name as shown):
```
<platform-image-name>-OKE-<kubernetes-version>-<OKE-build-number>
```

For example, `Oracle-Linux-8.9-2024.01.26-0-OKE-1.29.1-679`
Note that OKE image names include the version number of the Kubernetes version they contain. If you specify a Kubernetes version when creating and updating node pools, the OKE image you select must have the same version number as the node pool.
### Platform Images 🔗 
Platform images are provided by Oracle and only contain an Oracle Linux operating system. When the compute instance hosting a managed node boots up for the first time, Kubernetes Engine downloads, installs, and configures required software. 
To see the platform images currently supported by Kubernetes Engine:
  * When using the Console to create a cluster in the 'Custom Create' workflow, choose **Platform images** as the**Image source** in the **Browse all images** window, and view the list of supported platform images. 
  * When using the CLI, view the supported images (in the `data: sources:` section of the response) by entering:
Command
CopyTry It
```
oci ce node-pool-options get --node-pool-option-id all
```

Platform image names might or might not include a CPU architecture reference, and do not include `OKE`. For example:
    * `Oracle-Linux-8.5-Gen2-GPU-2022.04.05-0`
    * `Oracle-Linux-7.9-2022.04.04-0`


### Custom Images 🔗 
Custom images are provided by you, and can be based on both supported platform images and OKE images. Custom images contain Oracle Linux operating systems, along with other customizations, configuration, and software that were present when you created the image.
When specifying the image that Kubernetes Engine uses to provision managed nodes in a node pool, you can specify your own custom image rather than one of the explicitly supported Oracle Linux images returned by the `oci ce node-pool-options get --node-pool-option-id all` command. Managed nodes provisioned from a custom image include the customizations, configuration, and software in the image. Note that Kubernetes Engine only supports custom images that are based on one of the Oracle Linux images returned by the `oci ce node-pool-options get` command.
To provision managed nodes from a custom image, you must use the CLI or API and specify the custom image's OCID when creating the node pool. For example, by running the `oci ce node-pool create` command and using the `--node-image-id` parameter to specify a custom image's OCID, as follows:
Copy
```
oci ce node-pool create \
--cluster-id ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd \
--name my-custom-linux-image \
--node-image-id ocid1.image.oc1.iad.aaaaaaaa6______nha \
--compartment-id ocid1.compartment.oc1..aaaaaaaay______t6q \
--kubernetes-version v1.15.7 \
--node-shape VM.Standard2.1 \
--placement-configs "[{\"availability-domain\":\"IqDk:US-ASHBURN-AD-2\", \"capacityReservationId\":\"ocid1.capacityreservation.oc1.iad.anuwcljt2ah______yeq\", \"subnet-id\":\"ocid1.subnet.oc1.iad.aaaaaaaa2xpk______zva\", \"faultDomains\":[\"FAULT-DOMAIN-3\", \"FAULT-DOMAIN-1\"]}, {\"availability-domain\":\"IqDk:US-ASHBURN-AD-1\", \"subnet-id\":\"ocid1.subnet.oc1.iad.aaaaaaaauhls______bpq\", \"faultDomains\": [\"FAULT-DOMAIN-1\", \"FAULT-DOMAIN-2\"]}]" \
--size 1 \
--region=us-ashburn-1
```

Note the following additional considerations when using custom images:
  * Kubernetes Engine installs Kubernetes on top of a custom image, and Kubernetes or the installation software might change certain kernel configurations.
  * Custom images must have access to a yum repository (public or internal).
  * For the best support, ensure you create a custom image from the most up-to-date base image.
  * When using OKE images as the base for custom images, note that OKE images are built for a specific Kubernetes version and CPU architecture. To see details (including the OCIDs) of OKE worker node images to use as the base for custom images, see [Image Release Notes](https://docs.oracle.com/iaas/images/).
  * If you specify the OCID of a custom image in a different tenancy to the cluster, you have to set up appropriate cross-tenancy IAM policies. For more information, see [Accessing Custom Images in other Tenancies When Creating or Updating Managed Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaccessingokeresourcesacrosstenancies.htm#contengcrosstenancyimagepolicies).


For more information about custom images and Oracle Cloud Infrastructure, see [Managing Custom Images](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingcustomimages.htm). 
## Supported Shapes for Managed Nodes and Virtual Nodes 🔗 
Kubernetes Engine supports the provisioning of worker nodes (both managed nodes and virtual nodes) using many, but not all, of the shapes provided by Oracle Cloud Infrastructure. More specifically:
  * **Managed Nodes:**
    * **Supported for managed nodes:** Flexible shapes, except flexible shapes to create burstable instances (for example, VM.Standard.E3.Flex); Bare Metal shapes, including standard shapes and GPU shapes; HPC shapes, except in RDMA networks; VM shapes, including standard shapes and GPU shapes; Dense I/O shapes.
For the list of supported GPU shapes, see [GPU shapes supported by Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengrunninggpunodes.htm#contengrunninggpunodes_topic-supportedgpushapes).
    * **Not Supported:** Dedicated VM host shapes; Micro VM shapes; HPC shapes on Bare Metal instances in RDMA networks; flexible shapes to create burstable instances (for example, VM.Standard.E3.Flex).
  * **Virtual Nodes:**
    * **Supported for virtual nodes:** Pod.Standard.A1.Flex, Pod.Standard.E3.Flex, Pod.Standard.E4.Flex.
    * **Not Supported:** All other shapes.


Note that you might be unable to select some shapes in your particular tenancy due to service limits and compartment quotas, even though those shapes are supported by Kubernetes Engine.
To see the shapes that are supported by Kubernetes Engine and available in your tenancy:
  * When using the Console to create a cluster in the 'Custom Create' workflow, view the list of supported shapes in the **Browse all shapes** window. 
  * When using the CLI, view the supported shapes (in the `data: shapes:` section of the response) by entering:
Command
CopyTry It
```
oci ce node-pool-options get --node-pool-option-id all
```



You might be able to use the Compute service's Console pages (or the Compute service's CLI or API) to subsequently change the shape of a worker node after it has been created. However, bear in mind that Kubernetes Engine only supports those shapes shown in the **Browse all shapes** window or returned by the `oci ce node-pool-options get --node-pool-option-id all` command.
For more information about all the shapes provided by Oracle Cloud Infrastructure, see [Compute Shapes](https://docs.oracle.com/iaas/Content/Compute/References/computeshapes.htm).
## Supported Images and Shapes for Self-Managed Nodes 🔗 
Kubernetes Engine supports the provisioning of self-managed nodes using some, but not all, of the Oracle Linux images and shapes provided by Oracle Cloud Infrastructure. More specifically:
  * **Images supported for self-managed nodes:** The image you select for the compute instance hosting a self-managed node must be one of the OKE Oracle Linux 7 (OL7) or Oracle Linux 8 (OL8) images, and the image must have a Release Date of March 28, 2023 or later. See [Image Requirements](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengprereqsforselfmanagednodes.htm#contengprereqsforselfmanagednodes-imagereqs).
  * **Shapes supported for self-managed nodes:** The shape you can select for the compute instance hosting a self-managed node is determined by the OKE Oracle Linux 7 (OL7) or Oracle Linux 8 (OL8) image you select for the compute instance. Note that you might be unable to select some shapes in your particular tenancy due to service limits and compartment quotas, even though those shapes are supported by the OKE image.
To see the supported shapes available in your tenancy for a given OKE image, follow the instructions in [Creating Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingselfmanagednodes.htm#contengcreatingselfmanagednodes "Find out how to create a new self-managed node and add it to an existing cluster.") to use the Console to create a new compute instance to host the self-managed node. Having selected one of the OKE Oracle Linux 7 (OL7) or Oracle Linux 8 (OL8) images, click **Change shape** and view the list of supported shapes in the **Browse all shapes** window. 


**Note** For information about creating self-managed nodes that run Ubuntu, see [Running Ubuntu on Worker Nodes Using Custom Images](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes "Find out how to include worker nodes that run the Ubuntu Linux distribution in clusters created with Kubernetes Engine \(OKE\), using custom images and cloud-init scripts.").
Was this article helpful?
YesNo


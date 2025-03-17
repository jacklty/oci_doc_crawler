Updated 2025-01-22
# Enabling In-Transit Encryption Between an Instance and Boot Volumes or Block Volumes
After you create a virtual machine (VM) instance, you can enable or disable in-transit encryption between the instance and its paravirtualized boot volume and block volume attachments.
All boot volume and block volume data at rest is always encrypted by the Oracle Cloud Infrastructure Block Volume service using the Advanced Encryption Standard (AES) algorithm with 256-bit encryption. For more information, see [Block Volume Encryption](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm#BlockVolumeEncryption).
**Important** See this known issue: [In-transit encryption for a boot volume attachment can be edited when unsupported by the image](https://docs.oracle.com/en-us/iaas/Content/Compute/known-issues.htm#in-transit-encryption-for-boot-volume-attachment-can-be-edited-when-unsupported-by-image).
For permissions, see [Required IAM Policy for Working with Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#permissions).
## Supported Shapes and Images 🔗 
You can enable or disable in-transit encryption for existing instances that use these VM shapes:
  * VM.Standard1 series
  * VM.Standard.B1 series
  * VM.Standard2 series
  * VM.Standard3 series
  * VM.Standard.E2 series
  * VM.Standard.E3.Flex
  * VM.Standard.E4.Flex
  * VM.Standard.E5.Flex
  * VM.Standard.A1.Flex
  * VM.DenseIO1 series
  * VM.DenseIO2 series
  * VM.GPU3 series
  * VM.GPU.A10 series
  * VM.Optimized3.Flex


These shapes cannot be edited:
  * VM.Standard.E2.1.Micro
  * VM.DenseIO.E4.Flex
  * VM.GPU2 series
  * VM instances that run on dedicated virtual machine hosts


The following bare metal shapes support in-transit encryption by default for block volumes and boot volumes. This setting is not configurable and applies to all volume attachments to the instance.
  * BM.Standard.E3.128
  * BM.Standard.E4.128
  * BM.DenseIO.E4.128


**Note**
In-transit encryption is not enabled for these shapes in the following scenarios:
  * Boot volumes for instances launched June 8, 2021 or earlier.
  * Volumes attached to the instance June 8, 2021 or earlier


To enable in-transit encryption for the volumes in these scenarios, you need to detach the volume from the instance and then reattach it. 
In-transit encryption is not supported on all other bare metal shapes.
In-transit encryption for boot volumes and block volumes is available for [platform images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm#OracleProvided_Images). It is not supported in most cases for instances launched from custom images imported for "bring your own image" (BYOI) scenarios. To confirm support for certain Linux-based custom images, [contact support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
## Using the Console 🔗 
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Select **More Actions** , and then select **Edit**.
  4. Click **Show advanced options**.
  5. On the **Launch options** tab, select the **Use in-transit encryption** check box.
  6. Click **Save changes**.
If the instance is running, it is rebooted. Confirm when prompted.


## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use this API operation to enable or disable in-transit encryption between an instance and its paravirtualized boot volume attachments:
  * [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance)


Was this article helpful?
YesNo


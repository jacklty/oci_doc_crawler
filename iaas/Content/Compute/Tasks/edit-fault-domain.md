Updated 2025-02-12
# Editing the Fault Domain for an Instance
You can change the fault domain where a virtual machine (VM) instance is placed.
A fault domain is a grouping of hardware and infrastructure that is distinct from other fault domains in the same availability domain. By properly leveraging fault domains you can increase the availability of applications running on Oracle Cloud Infrastructure. For more information and best practices, see [Fault Domains](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bestpracticescompute.htm#Fault).
For permissions, see [Required IAM Policy for Working with Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#permissions).
## Supported Shapes 🔗 
You can change the fault domain for instances that use these shapes:
  * VM.Standard1 series
  * VM.Standard.B1 series
  * VM.Standard2 series
  * VM.Standard3.Flex
  * VM.Standard.E2 series
  * VM.Standard.E3.Flex
  * VM.Standard.E4.Flex
  * VM.Standard.E5.Flex
  * VM.GPU3 series
  * VM.GPU.A10 series
  * VM.Optimized3.Flex


These shapes cannot be edited:
  * VM.Standard.E2.1.Micro
  * VM.GPU2 series
  * VM.DenseIO1 series
  * VM.DenseIO2 series
  * VM.DenseIO.E4.Flex
  * VM instances that run on dedicated virtual machine hosts
  * Bare metal shapes


## Using the Console 🔗 
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Select **More Actions** , and then select **Edit**.
  4. Click **Edit fault domain**. Then, select a new fault domain.
  5. Click **Save changes**.
If the instance is running, it is rebooted. Confirm when prompted.


## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use this API operation to change the fault domain for an instance:
  * [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance)


Was this article helpful?
YesNo


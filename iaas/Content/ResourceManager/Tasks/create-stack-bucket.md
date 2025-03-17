Updated 2025-01-07
# Creating a Stack from a Bucket
Create a stack in Resource Manager from a Terraform configuration stored in an Object Storage bucket.
Limit the bucket to files that are intended for use with Terraform. Ensure that the Terraform configuration is valid. See [Terraform Configurations for Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#top "Review requirements and recommendations for Terraform configurations used with Resource Manager. Use Terraform and Resource Manager to install, configure, and manage resources using the infrastructure-as-code model.") and [Authoring Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/authoring-configurations.htm#top "Write a Terraform configuration to describe infrastructure using the HashiCorp Configuration Language format \(HCL\).").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-bucket.htm)


  *     1. On the **Stacks** list page, select **Create stack**. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/list-stacks.htm).
    2. On the **Create stack** page, under **Choose the origin of the Terraform configuration** , select **My configuration**.
    3. Under **Stack configuration** , select **Object Storage bucket** and then select the bucket that you want.
Limit the bucket to files that are intended for use with Terraform.
    4. (Optional) To use [custom providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-custom-providers.htm#top "Update a stack to fetch custom providers from Object Storage buckets."), select **Use custom providers** and then select the bucket that contains the custom provider.
    5. (Optional) Edit the default stack name and enter a stack description. Avoid entering confidential information.
    6. Select the compartment that you want to store the stack in.
    7. For **Terraform version** , select the version used by the Terraform configuration.
    8. To add a defined tag, select the namespace and key, then enter a value.
    9. To add a free-form tag, enter a key and value.
    10. Select **Next**.
    11. In the **Configure variables** panel, review the variables listed from the Terraform configuration and change as needed.
**Important** Don't add your private key or other confidential information to configuration variables. 
    12. Select **Next**.
    13. In the **Review** panel, verify the stack configuration.
    14. (Optional) To automatically provision resources on creation of the stack, select **Run apply**.
    15. Select **Create**.
The stack is created and its details page opens.
If you selected **Run apply** , then Resource Manager runs the apply action on the new stack.
  * Use the `oci resource-manager stack create-from-object-storage[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/create-from-object-storage.html)` command and required parameters to create a stack from a bucket.
Copy
```
oci resource-manager stack create-from-object-storage --compartment-id <compartment_OCID> --config-source-bucket-name <bucket_name> --config-source-namespace <bucket_namespace> --config-source-region <bucket_region>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [CreateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/CreateStack) operation to create a stack from a bucket.
For an example of the `configSource` part of the request, see [CreateObjectStorageConfigSourceDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateObjectStorageConfigSourceDetails).
[Example request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-bucket.htm)
```
POST /20180917/stacks
Host: resourcemanager.us-phoenix-1.oraclecloud.com
<authorization and other headers>
{
 "compartmentId": "ocid1.compartment.oc1..<unique_ID>",
 "displayName": "My Bucket Terraform Configuration",
 "configSource": {
  "configSourceType": "OBJECT_STORAGE_CONFIG_SOURCE",
  "region": "us-phoenix-1",
  "namespace": "<bucket_namespace>",
  "bucketName": "<bucket_name>"
 }
}
```



Was this article helpful?
YesNo


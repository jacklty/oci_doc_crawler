Updated 2025-01-07
# Creating a Stack from a Zip File
Create a stack in Resource Manager from a local Terraform configuration stored in a zip file.
Ensure that your Terraform configuration is valid. See [Terraform Configurations for Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#top "Review requirements and recommendations for Terraform configurations used with Resource Manager. Use Terraform and Resource Manager to install, configure, and manage resources using the infrastructure-as-code model.") and [Authoring Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/authoring-configurations.htm#top "Write a Terraform configuration to describe infrastructure using the HashiCorp Configuration Language format \(HCL\).").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-local.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-local.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-local.htm)


  *     1. On the **Stacks** list page, select **Create stack**. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/list-stacks.htm).
    2. On the **Create stack** page, under **Choose the origin of the Terraform configuration** , select **My configuration**.
    3. Select **.Zip file** and add the revised [Terraform configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#top "Review requirements and recommendations for Terraform configurations used with Resource Manager. Use Terraform and Resource Manager to install, configure, and manage resources using the infrastructure-as-code model.").
You can either drag the file onto the dialog's control or select **Browse** and navigate to the location of the file or folder.
The page is populated with information contained in the Terraform configuration.
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
  * **Note** On Windows, be sure the zip file and variables.json files are in the same directory from which you're running the CLI. The CLI currently has a limitation on Windows that prevents correct handling of the files if either one is in a subdirectory.
Use the `oci resource-manager stack create[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/create.html)` command and required parameters to create a stack from a local zip file.
Command
CopyTry It
```
oci resource-manager stack create [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
[Example Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-local.htm)
Command
CopyTry It
```
oci resource-manager stack create --compartment-id ocid1.tenancy.oc1..uniqueid --config-source vcn.zip --variables file://variables.json --display-name "My Example Stack" --description "My Tutorial to Create a VCN" --working-directory ""
```

[Example Response](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-local.htm)
```
{
 "data": {
  config-source": 
  {
   "working-directory": null,
   "config-source-type": "ZIP_UPLOAD"
  },
  "defined-tags": {},
  "description": "My Tutorial to Create a VCN",
  "display-name": "My Example Stack",
  "freeform-tags": {},
  "id": "ocid1.ormstack.oc1..uniqueid",
  "lifecycle-state": "ACTIVE",
  "time-created": "2019-04-03T18:26:56.299000+00:00",
  "variables": 
  {
   "compartment_ocid": "ocid1.compartment.oc1..uniqueid", 
   "region": "us-phoenix-1"
  }
 }
}
```

  * Use the [CreateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/CreateStack) operation to create a stack from a local zip file.
For an example of the `configSource` part of the request, see [CreateZipUploadConfigSourceDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateZipUploadConfigSourceDetails).
[Example request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-local.htm)
```
POST /20180917/stacks
Host: resourcemanager.us-phoenix-1.oraclecloud.com
<authorization and other headers>
{
 "compartmentId": "ocid1.compartment.oc1..<unique_ID>",
 "terraformVersion": "0.12.x",
 "displayName": "My Zip Configuration",
 "configSource": {
  "configSourceType": "ZIP_UPLOAD",
  "zipFileBase64Encoded": "<zip_file_content_encoded_in_base64_format>",
  "workingDirectory": "<file_path_to_directory>"
 },
}
```



Was this article helpful?
YesNo


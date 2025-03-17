Updated 2024-10-08
# Using Custom Providers with a Stack
Update a stack to fetch custom providers from Object Storage buckets.
  * Limit the bucket to files that are intended for use with Terraform.
  * If the stack was created before custom providers were available, then first [update the stack to use Terraform Registry](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-reg.htm#top "Update an older stack to fetch providers from Terraform Registry."). This update enables the stack to use custom providers.


## Before You Begin 🔗 
Follow these steps to add a custom provider to a bucket. 
  1. Set up the bucket for the custom provider. See [Putting Data into Object Storage](https://docs.oracle.com/iaas/Content/GSG/Tasks/addingbuckets.htm).
     * To store amd/x86 binaries, create a directory under the root of the bucket with the following name:
` linux_amd64`
     * To store Arm binaries, create a directory under the root of the bucket with the following name:
`linux_arm64`
  2. Confirm that the name of each custom provider binary file aligns with the following convention:
`terraform-provider-<TYPE>_v<MAJOR.MINOR.PATCH>`
With optional suffix (example: `x5` or `x4`):
`terraform-provider-<TYPE>_v<MAJOR.MINOR.PATCH>_<OPTIONAL-SUFFIX>`
  3. Upload the custom provider binary files to the bucket. See [Putting Data into Object Storage](https://docs.oracle.com/iaas/Content/GSG/Tasks/addingbuckets.htm).
Limit the bucket to files that are intended for use with Terraform.


  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-custom-providers.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-custom-providers.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-custom-providers.htm)


  *     1. On the **Stacks** list page, find the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. From the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the stack, select **Edit**.
    3. On the **Edit stack** page, select **Use custom providers**.
    4. Select the bucket that contains the custom providers.
Limit the bucket to files that are intended for use with Terraform.
    5. Select **Next** twice.
    6. Select **Save changes**.
  * Use the `oci resource-manager stack update[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/update.html)` command and required parameters to use custom providers with stacks.
Copy
```
oci resource-manager stack update --custom-terraform-provider <json_input> [...]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [UpdateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/UpdateStack) operation to update the custom providers used by a stack.
For an example of the `CustomTerraformProvider` part of the request, see [CustomTerraformProvider](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CustomTerraformProvider).


Was this article helpful?
YesNo


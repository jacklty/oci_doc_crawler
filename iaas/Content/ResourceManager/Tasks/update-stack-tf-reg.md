Updated 2024-10-08
# Using Terraform Registry with an Older Stack
Update an older stack to fetch providers from Terraform Registry.
**Caution**
  * To prevent incompatible provider versions, update the configuration to specify version constraints, listing versions that exist in the configured provider source (Terraform Provider or custom providers).
  * To prevent job failures from unavailable provider versions, ensure that versions listed in the version constraints of the configuration exist in the configured provider source (Terraform Provider or custom providers), or remove version constraints entirely (results in retrieval of the latest versions).


Stacks that were created before [Terraform Registry](https://registry.terraform.io/browse/providers) sourcing was available continue to fetch providers from Resource Manager until updated. When updated, stacks fetch providers from Terraform Registry and [custom providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-custom-providers.htm#top "Update a stack to fetch custom providers from Object Storage buckets.") are available. 
**Tip**
To determine the source of providers for your stack, [review the logs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs.htm#top "View console logs for a job in Resource Manager.") for a recent job. The following phrase indicates that the stack is fetching providers from Terraform Registry: 
```
Getting providers from hashicorp registry and/or custom terraform providers
```

  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-reg.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-reg.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-reg.htm)


  *     1. On the **Stacks** list page, select the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. Select **More actions** and then select **Use Terraform registry**.
  * Use the `oci resource-manager stack update[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/update.html)` command and required parameters to update older stacks to fetch providers from [Terraform Registry](https://registry.terraform.io/browse/providers).
Copy
```
oci resource-manager stack update --is-third-party-provider-experience-enabled true [...]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [UpdateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/UpdateStack) operation to update the stack to fetch providers from [Terraform Registry](https://registry.terraform.io/browse/providers).
When defining details for [UpdateStackDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/UpdateStackDetails), set `isThirdPartyProviderExperienceEnabled` to `true`.


Was this article helpful?
YesNo


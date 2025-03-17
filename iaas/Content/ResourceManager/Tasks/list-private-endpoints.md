Updated 2025-01-23
# Listing Private Endpoints
List private endpoints in Resource Manager.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-private-endpoints.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-private-endpoints.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-private-endpoints.htm)


  *     1. Open the **navigation menu** and select **Developer Services**. Under **Resource Manager** , select **Private Endpoints**.
    2. To view the resources in a different compartment, use the **Compartment** filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see [Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
    3. (Optional) To filter the list by tag:
      1. Next to **Tag filters** , select **add**.
      2. In the **Add a tag filter** dialog, enter the following:
         * **Tag namespace:** Select the tag namespace.
         * **Tag key:** Select the key.
         * **Tag value:** Select from the following:
           * **Match any value** - returns all resources tagged with the selected namespace and key, regardless of the tag value.
           * **Specify matching values** - returns resources with the tag value you enter in the text box. Enter a single value in the text box. To specify multiple values for the same namespace and key, select **+** to display another text box. Enter one value per text box.
      3. Select **Apply filter**.
  * Use the `oci resource-manager private-endpoint list[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/private-endpoint/list.html)` command to list private endpoints.
Command
CopyTry It
```
oci resource-manager private-endpoint list --compartment-id <compartment_ocid>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [ListPrivateEndpoints](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/PrivateEndpointSummary/ListPrivateEndpoints) operation to list private endpoints.


Was this article helpful?
YesNo


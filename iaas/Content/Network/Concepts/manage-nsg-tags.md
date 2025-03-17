Updated 2025-01-15
# Managing Tags for an NSG
Manage tags for a network security group (NSG).
For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/manage-nsg-tags.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/manage-nsg-tags.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/manage-nsg-tags.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the VCN you're interested in.
    3. Under **Resources** , click **Network Security Groups**.
    4. Click the **Tags** tab to view or edit the existing tags. Or click **Add tags** to add new ones.
  * Use the [network nsg create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/create.html) command and required parameters to add tags when you create an NSG:
Command
CopyTry It
```
oci network nsg create --compartment-id ocid --vcn-id ocid [--defined-tags | --freeform-tags] tags ... [OPTIONS]
```

Use the [network nsg update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/update.html) command and required parameters to add tags to the specified NSG:
Command
CopyTry It
```
oci network nsg update --nsg-id ocid [--defined-tags | --freeform-tags] tags ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateNetworkSecurityGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/CreateNetworkSecurityGroup) operation to add tags when you create an NSG, and use the definedTags attribute.
Run the [UpdateNetworkSecurityGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/UpdateNetworkSecurityGroup) operation to add tags when you update an NSG, and use the definedTags or freeformTags attributes.


Was this article helpful?
YesNo


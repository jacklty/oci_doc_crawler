Updated 2025-01-15
# Tagging a Subnet
Add tags to a subnet.
Using tags enables you to define keys and values and associate them with resources. You can apply tags to your subnets to help you organize them according to your business needs. Apply tags at the time you create a subnet, or update the subnet with tags later. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). 
**Note** If you are not sure whether to apply tags, ask your administrator for guidance.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/manage_tags_subnet.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/manage_tags_subnet.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/manage_tags_subnet.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN that contains the subnet.
    3. Click the name of the subnet you're interested in. 
    4. Click the **Tags** tab to view or edit the existing tags. Or click **Apply tag(s)** to add new ones.
  * Use the [network subnet create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/create.html) command and parameters shown to add tags when you create a subnet:
Command
CopyTry It
```
oci network subnet create --compartment-id compartment_id [. . .] [--defined-tags | --freeform-tags] tags [OPTIONS]
```

Use the [network subnet update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/update.html) command and parameters shown to add tags to an existing subnet:
Command
CopyTry It
```
oci network subnet update --subnet-id ocid [. . .] [--defined-tags | --freeform-tags] tags [OPTIONS] 
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/CreateSubnet) operation to add tags when you create a subnet, and use the definedTags attribute.
Run the [UpdateSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/UpdateSubnet) operation to add tags when you update a subnet, and use the definedTags or freeformTags attributes.


Was this article helpful?
YesNo


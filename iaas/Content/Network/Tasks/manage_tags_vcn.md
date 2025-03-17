Updated 2025-01-15
#  Tagging a VCN
Add metadata to virtual cloud networks (VCNs) in the form of **tags**. Tags enable you to define keys and values and associate them with resources.
You can apply tags to your VCNs to help you organize them according to your business needs. Apply tags when you [create a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_vcn.htm#top "Create a VCN that instances, load balancers, and other resources can use to connect to each other and the internet. After you create a VCN, you must then manually create subnets, gateways, routing rules, and security settings before the VCN can connect to the internet or your on-premises network."), or update the VCN with tags later. If you're not sure whether to apply tags, ask your administrator for guidance. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/manage_tags_vcn.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/manage_tags_vcn.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/manage_tags_vcn.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN that you want to tag. You might need to change the compartment to find the VCN that you want.
    3. Click the **Tags** tab to view or edit the existing tags. Or click **Add tags** to add new ones.
  * Use the [network vcn create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/create.html) command and parameters shown to add tags when you create a VCN:
Command
CopyTry It
```
oci network vcn create --compartment-id compartment_id [. . .] [--defined-tags | --freeform-tags] tags [OPTIONS]
```

Use the [network vcn update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/update.html) command and parameters shown to add tags to an existing VCN:
Command
CopyTry It
```
oci network vcn update --vcn-id ocid [. . .] [--defined-tags | --freeform-tags] tags [OPTIONS] 
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/CreateVcn) operation to add tags when you create a VCN, and use the definedTags attribute.
Run the [UpdateVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/UpdateVcn) operation to add tags when you update a VCN, and use the definedTags or freeformTags attributes.


Was this article helpful?
YesNo


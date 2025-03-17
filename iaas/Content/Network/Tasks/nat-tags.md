Updated 2025-01-17
# Tagging a NAT Gateway
Add metadata to a NAT gateway, so you can define keys and values and associate them with resources.
You can apply tags to a NAT gateway to help you organize resources according to business needs. Apply tags at the time you create a NAT gateway, or update the NAT gateway with tags later. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). 
**Note** If you're not sure whether to apply tags, ask an administrator for guidance.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-tags.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-tags.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-tags.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the name of the VCN you're interested in.
    3. Under **Resources** , select **NAT Gateway**. 
    4. Select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the NAT gateway, and then select **View Tags**. From there you can view the existing tags, edit them, and apply new ones.
  * Use the [network nat-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nat-gateway/update.htm) command and required parameters to manage tags for the specified NAT gateway:
Command
CopyTry It
```
oci network nat-gateway update --nat-gateway-id natg-ocid [--defined-tags | --freeform-tags] tags ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateNatGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NatGateway/UpdateNatGateway) operation to add tags to a NAT gateway.


Was this article helpful?
YesNo


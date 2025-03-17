Updated 2025-01-17
# Tagging an LPG
Add metadata to a local peering gateway (LPG), which lets you define keys and values and associate them with resources.
You can apply tags to NSGs to help you organize them according to business needs. Apply tags at the time you create an NSG, or update the security list with tags later. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). 
**Note** If you're not sure whether to apply tags, ask an administrator for guidance.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/tags-lpg.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/tags-lpg.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/tags-lpg.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the VCN you're interested in.
    3. Under **Resources** , select **Local Peering Gateways**.
    4. Select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the local peering gateway, and then select **View Tags**. From there you can view the existing tags, edit them, and apply new ones.
  * Use the [network local-peering-gateway create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/local-peering-gateway/create.html) command and required parameters to create an LPG that uses tags::
Command
CopyTry It
```
oci network local-peering-gateway create --compartment-id ocid --vcn-id ocid ... [--defined-tags | --freeform-tags] tags [OPTIONS]
```

Use the [network local-peering-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/local-peering-gateway/update.html) command and required parameters to add tags to an LPG:
Command
CopyTry It
```
oci network local-peering-gateway update --local-peering-gateway-id lpg-ocid ... [--defined-tags | --freeform-tags] tags [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListVcns](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/ListVcns) operation to <task-being-performed>.


Was this article helpful?
YesNo


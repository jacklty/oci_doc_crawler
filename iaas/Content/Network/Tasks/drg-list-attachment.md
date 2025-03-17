Updated 2025-01-15
# Listing DRG Attachments
Find a list of DRG attachments for a specified Dynamic Routing Gateway (DRG) and compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list-attachment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list-attachment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list-attachment.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG whose attachments you want to list.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Click the name of the DRG.
    4. Under **Resources** , click one of the following options to see a list of attachments sorted by type: 
       * **VCN attachments**
       * **Virtual circuit attachments**
       * **IPSec tunnel attachments**
       * **Remote peering connection attachments**
       * **Cross-tenancy attachments**
  * Use the [network drg-attachment list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-attachment/list.html) command and parameters to find a list of DRG attachments for a specified DRG and compartment:
Command
CopyTry It
```
oci network drg-attachment list --compartment-id compartment-ocid --drg-id drg-ocid ... [OPTIONS]
```

You can also filter the results by attached network, attachment type, DRG route table or VCN route table.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListDrgAttachments](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgAttachment/ListDrgAttachments) operation to find a list of DRG attachments.


Was this article helpful?
YesNo


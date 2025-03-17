Updated 2025-01-15
# Getting a DRG Attachment's Details
Get the configuration details for a Dynamic Routing Gateway (DRG) attachment in Oracle Cloud Infrastructure. 
For details about DRGs, see [Working with DRGs and DRG Attachments](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__drg_attach).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-attachment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-attachment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-attachment.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG with the attachment you want to delete.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Click the name of the DRG.
    4. Under **Resources** , click one of the following options corresponding to the attachment type: 
       * VCN attachments 
       * Virtual circuit attachments 
       * IPSec tunnel attachments
       * Remote peering connection attachments 
       * Cross-tenancy attachments
       * Loopback attachments
    5. Click the name of the attachment you're interested in. 
If the attachment is in another compartment, select that compartment under **List scope**. 
  * Use the [network drg-attachment get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-attachment/get.html) command and required parameters to get details for a DRG attachment:
Command
CopyTry It
```
oci network drg-attachment get --drg-attachment-id attachment-ocid [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetDrgAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgAttachment/GetDrgAttachment) operation to get details for a DRG attachment.


Was this article helpful?
YesNo


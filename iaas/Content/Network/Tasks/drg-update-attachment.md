Updated 2025-01-15
# Updating a DRG Attachment
Update the configuration details of a Dynamic Routing Gateway (DRG) attachment in Oracle Cloud Infrastructure. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-update-attachment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-update-attachment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-update-attachment.htm)


  * You can use the Console to update the display name of an attachment and advanced options including DRG route table, VCN route table, and VCN route type.
    1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG with the attachment you want to update.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Click the name of the DRG.
    4. Under **Resources** , click the type of attachment that you want to update: 
       * VCN attachments 
       * Virtual circuit attachments 
       * IPSec tunnel attachments
       * Remote peering connection attachments 
       * Cross-tenancy attachments
       * Loopback attachments
If the attachment is in another compartment, select that compartment under **List scope**.
    5. Click the name of the attachment. 
    6. Click **Edit**. 
    7. (Optional) Change the display name of the attachment. 
    8. (Optional) Click **Show Advanced options** and change the DRG route table, the VCN route table, or the VCN route type associated with the attachment. 
    9. Click **Save changes**. 
  * Use the [network drg-attachment update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-attachment/update.html) command and required parameters to update a DRG attachment's configuration details:
Command
CopyTry It
```
oci network drg-attachment update --drg-attachment-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateDrgAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgAttachment/UpdateDrgAttachment) operation to update a DRG attachment's configuration details.


Was this article helpful?
YesNo


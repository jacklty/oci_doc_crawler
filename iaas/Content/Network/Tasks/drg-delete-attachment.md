Updated 2025-01-15
# Deleting a DRG Attachment
Detach a Dynamic Routing Gateway (DRG) from a resource in Oracle Cloud Infrastructure.
You detach a DRG from a Virtual Cloud Network (VCN) by deleting the `DrgAttachment` resource. This doesn't require deleting the VCN. 
When you delete a virtual circuit, IPSec tunnel, or remote peering connection (RPC) resource, the corresponding attachment to the DRG is automatically deleted. These resources can't be detached from a DRG without deleting the resource itself.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete-attachment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete-attachment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete-attachment.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG with the attachment you want to delete.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Click the name of the DRG.
    4. Under **Resources** , click **VCN attachments**.
    5. Click the name of the attachment you want to delete.
If the attachment that you want to delete is in another compartment, select that compartment under **List scope**.
    6. Click the name of the attachment.\
    7. Click **Delete**.
    8. To confirm that you want to delete the attachment, click **Delete**.
  * Use the [network drg-attachment delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-attachment/delete.html) command and required parameters to delete a DRG attachment:
Command
CopyTry It
```
oci network drg-attachment delete --drg-attachment-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteDrgAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgAttachment/DeleteDrgAttachment) operation to delete a DRG attachment.


Was this article helpful?
YesNo


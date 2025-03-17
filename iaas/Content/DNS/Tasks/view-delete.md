Updated 2025-03-10
# Deleting a Private View
Delete a private domain name service (DNS) view and its associated private zones.
See [Private DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm#private-dns "Create and manage private domain name system \(DNS\) zones.") and [Private Views](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/views.htm#top "Use private views to logically group a set of private domain name service \(DNS\) zones. A zone can only belong to a single view.") for a feature overview and more information.
For general service information, see the [DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
**Caution** Deletion removes any associated private zones.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-delete.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Private views**.
    2. Under **List scope** , select the compartment that contains the private view to delete. 
    3. Find the view in the list, select its Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Delete**.
    4. In the **Delete DNS private view** dialog box, review the private view and the zones to be deleted.
    5. Enter `DELETE` to confirm the deletion.
    6. Select **Delete all**.
  * Use the [view delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/view/delete.html) command and required parameters to delete a view and its associated zones:
Command
CopyTry It
```
oci dns view delete --view-id view_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteView](https://docs.oracle.com/iaas/api/#/en/dns/latest/View/DeleteView) operation to delete a view and its associated zones.


Was this article helpful?
YesNo


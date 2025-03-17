Updated 2025-03-10
# Editing a Private View
Update the name or tags for a private domain name service (DNS) view.
See [Private DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm#private-dns "Create and manage private domain name system \(DNS\) zones.") and [Private Views](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/views.htm#top "Use private views to logically group a set of private domain name service \(DNS\) zones. A zone can only belong to a single view.") for a feature overview and more information.
For general service information, see the [DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-edit.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-edit.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-edit.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Private views**.
    2. Under **List scope** , select the compartment that contains the private view. 
    3. Select the name of the view to open its details page.
    4. Select **Edit**.
    5. Update the name of the view, and then select **Save change**.
    6. On the view details page, edit, add, or delete tags as follows:
       * To edit or remove a tag, select the **Tags** tab, select the edit icon next to a tag, and change its value or remove it.
       * to add one or more tags, select **Add tags** and enter the tag namespace (for a defined tag), key, and value.
  * Use the [view update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/view/update.html) command and required parameters to edit details about a private view.
Command
CopyTry It
```
oci dns view update --view-id view_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateView](https://docs.oracle.com/iaas/api/#/en/dns/latest/View/UpdateView) operation to edit details for a private view.


Was this article helpful?
YesNo


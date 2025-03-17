Updated 2025-03-10
# Getting a Private View's Details
Get details for a private domain name service (DNS) view.
See [Private DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm#private-dns "Create and manage private domain name system \(DNS\) zones.") and [Private Views](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/views.htm#top "Use private views to logically group a set of private domain name service \(DNS\) zones. A zone can only belong to a single view.") for a feature overview and more information.
For general service information, see the [DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-get.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Private views**.
    2. Under **List scope** , select the compartment that contains the private view. 
    3. Select the name of the view to open its details page.
The details page contains information about the view, both general information and links to its resources. Some items in the page are read-only. See [Editing a Private View](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-edit.htm#top "Update the name or tags for a private domain name service \(DNS\) view.").
  * Use the [view get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/view/get.html) command and required parameters to get details about a private view.
Command
CopyTry It
```
oci dns view get --view-id view_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetView](https://docs.oracle.com/iaas/api/#/en/dns/latest/View/GetView) operation to see details about a specified private view.


Was this article helpful?
YesNo


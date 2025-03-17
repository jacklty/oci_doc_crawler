Updated 2025-03-10
# Creating a Private View
You can create a private view with a new private domain name service (DNS) zone.
**Note** Private views can be viewed only in the region in which they're created.
See [Private DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm#private-dns "Create and manage private domain name system \(DNS\) zones.") and [Private Views](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/views.htm#top "Use private views to logically group a set of private domain name service \(DNS\) zones. A zone can only belong to a single view.") for a feature overview and more information.
For general service information, see the [DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-create.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-create.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-create.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Private views**.
    2. Select **Create private view**.
    3. In the **Create private view** panel, enter the following values:
       * **Name:** Enter a descriptive name for the private view. Avoid entering confidential information.
       * **Create in Compartment:** Select the compartment to create the private view in, if it's different than the one you selected before.
       * Select **Show Advanced Options:** to apply tags to the view. 
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. 
    4. Select **Create**.
  * Use the [view create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/view/create.html) command and required parameters to create a view:
Command
CopyTry It
```
oci dns view create --compartment-id compartment_id ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateView](https://docs.oracle.com/iaas/api/#/en/dns/latest/View/CreateView) operation to create a private view.


Was this article helpful?
YesNo


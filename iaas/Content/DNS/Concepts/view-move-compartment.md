Updated 2025-03-10
# Moving a Private View Between Compartments
Move a private domain name service (DNS) view from one compartment to another. 
See [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm) for information about compartments and access control.
See [Private DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm#private-dns "Create and manage private domain name system \(DNS\) zones.") and [Private Views](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/views.htm#top "Use private views to logically group a set of private domain name service \(DNS\) zones. A zone can only belong to a single view.") for a feature overview and more information about private views.
For general service information, see the [DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/view-move-compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/view-move-compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/view-move-compartment.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Private views**.
    2. Under **List scope** , select the compartment that contains the view.
    3. Find the view in the list, select its Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and select **Move resource**.
    4. Select a destination compartment from the list.
    5. Select **Move resource**.
  * Use the [view change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/view/change-compartment.html) command and required parameters to move a view to a different compartment:
Command
CopyTry It
```
oci dns view change-compartment --view-id view_OCID --compartment-id compartment_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeViewCompartment](https://docs.oracle.com/iaas/api/#/en/dns/latest/View/ChangeViewCompartment) operation to move a view from one compartment to another.


Was this article helpful?
YesNo


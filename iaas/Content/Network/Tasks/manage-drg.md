Updated 2024-10-16
# DRG Management
Learn how to mange a Dynamic Routing Gateway (DRG) in Oracle Cloud Infrastructure.
In general, to use a DRG, you must complete these minimal steps:
  1. Create the DRG.
  2. Attach the DRG to one or more VCNs. You can also attach a DRG to an on-premises network using FastConnect virtual circuits and Site-to-Site VPN IPSec tunnels. 
  3. Route subnet traffic to the DRG by updating the route table associated with each subnet that must send traffic to the DRG.


The following tasks are available for a DRG: 
  * [Creating a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create.htm#drg-create "Create a Dynamic Routing Gateway \(DRG\) in Oracle Cloud Infrastructure.")
  * [Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm#drg-list "List the dynamic routing gateways \(DRGs\) in a compartment.")
  * [Getting a DRG's Details](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get.htm#drg-get "View the settings for a particular Dynamic Routing Gateway \(DRG\).")
  * [Getting a List of DRG Attachments](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-all-drg-attachments.htm#drg-get_all_drg_attachments "Get a list of DRG attachments that belong to a particular dynamic routing gateway \(DRG\).")
  * [Finding the DRG Upgrade Status](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-upgrade-status.htm#drg-get_upgrade_status "Find the Dynamic Routing Gateway \(DRG\) upgrade status.")
  * [Getting the DRG Redundancy Status](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-redundancy-status.htm#drg-get-redundancy-status "Get the redundancy status for a specified Dynamic Routing Gateway \(DRG\).")
  * [Updating the Name of a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-update.htm#drg-update "Rename a Dynamic Routing Gateway \(DRG\) in Oracle Cloud Infrastructure.")
  * [Upgrading a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-upgrade.htm#drg-upgrade "Upgrade a Dynamic Routing Gateway \(DRG\) in Oracle Cloud Infrastructure.")
  * [Moving a DRG to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-change-compartment.htm#drg-change_compartment "Move a Dynamic Routing Gateway \(DRG\) from one compartment to another.")
  * [Deleting a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete.htm#drg-delete "Delete a Dynamic Routing Gateway \(DRG\) in Oracle Cloud Infrastructure.")


The following tasks are available for DRG attachments: 
  * [Attaching a DRG to a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-attachment.htm#drg-create_attachment "Create a VCN attachment on a Dynamic Routing Gateway \(DRG\) in Oracle Cloud Infrastructure.")
  * [Getting a DRG Attachment's Details](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-attachment.htm#drg-get_attachment "Get the configuration details for a Dynamic Routing Gateway \(DRG\) attachment in Oracle Cloud Infrastructure.")
  * [Listing DRG Attachments](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list-attachment.htm#drg-list_attachment "Find a list of DRG attachments for a specified Dynamic Routing Gateway \(DRG\) and compartment.")
  * [Updating a DRG Attachment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-update-attachment.htm#drg-update_attachment "Update the configuration details of a Dynamic Routing Gateway \(DRG\) attachment in Oracle Cloud Infrastructure.")
  * [Deleting a DRG Attachment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete-attachment.htm#drg-delete_attachment "Detach a Dynamic Routing Gateway \(DRG\) from a resource in Oracle Cloud Infrastructure.")


## Limitations
Some functions might appear to be possible based on the structure of the resource interaction model, but the following functions aren't allowed: 
  1. Explicit creation or deletion of RPC, IPSec tunnel, or virtual circuit attachments
  2. Static routes in DRG route tables with next-hop of IPSec tunnel or virtual circuit attachments
  3. Use of non-default export route distributions
  4. Dynamic route export to VCN attachments
  5. Propagating a route through more than 3 DRG route tables
  6. Routes propagating via RPC through more than 4 DRGs 


Was this article helpful?
YesNo


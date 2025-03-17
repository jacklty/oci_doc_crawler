Updated 2025-03-10
# Private Views
Use private views to logically group a set of private domain name service (DNS) zones. A zone can only belong to a single view.
When you create a VCN, the VCN-dedicated resolver has a protected default view. You can add zones to the default view within restrictions on zone names to avoid collisions with protected zones. You can create and attach a view to a resolver in addition to the default view, so that their zones are resolvable in the VCN. If a resolver is deleted, and its default view contains unprotected zones, then the default view is converted to an unprotected view instead of being deleted. 
The same zone name can be used in many views, but zone names within a view must be unique. Views aren't used with public zones. 
See [Private DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm#private-dns "Create and manage private domain name system \(DNS\) zones.") for a feature overview and more information.
## Private View Tasks 🔗 
You can perform the following tasks with views:
  * [Creating a Private View](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-create.htm#top "You can create a private view with a new private domain name service \(DNS\) zone.")
  * [Creating a Private DNS Zone in a Private View](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-add-zone.htm#top "Create a private domain name service \(DNS\) zone in a private view to manage records and hostname resolution for applications running within and between virtual cloud networks \(VCNs\), and on-premises or other private networks.")
  * [Listing Views](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-list.htm#top "List all private domain name service \(DNS\) views in a compartment.")
  * [Getting a Private View's Details](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-get.htm#top "Get details for a private domain name service \(DNS\) view.")
  * [Editing a Private View](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-edit.htm#top "Update the name or tags for a private domain name service \(DNS\) view.")
  * [Moving a Private View Between Compartments](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/view-move-compartment.htm#top "Move a private domain name service \(DNS\) view from one compartment to another.")
  * [Deleting a Private View](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-delete.htm#top "Delete a private domain name service \(DNS\) view and its associated private zones.")


Was this article helpful?
YesNo


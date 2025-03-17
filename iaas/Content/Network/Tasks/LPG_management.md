Updated 2024-08-21
# Local Peering Gateway Management
Describes how to create and manage local peering gateways (LPGs) that can be used to provide traffic flow to and from resources in other virtual cloud networks (VCNs).
For the purposes of management access control, you must specify the compartment where you want the VCN to reside. Consult an administrator in your organization if you're not sure which compartment to use. For information about compartments and access control, see [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm).
The following management actions are available for LPGs:
  * [Creating a Local Peering Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-lpg.htm#create-lpg "Create a local peering gateway \(LPG\) that instances, load balancers, and other resources can use to connect to resources in other virtual cloud networks \(VCNs\) in the same Oracle Cloud Infrastructure \(OCI\) region.")
  * [Listing the LPGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-lpg.htm#list-lpg "List the local peering gateways \(LPGs\) in a virtual cloud network \(VCN\).")
  * [Getting Details for an LPG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-lpg.htm#get-lpg "Get configuration details for a specific LPG in a virtual cloud network \(VCN\).")
  * [Updating the Name of an LPG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-lpg.htm#update-lpg "Change the name of a local peering gateway \(LPG\) in a virtual cloud network \(VCN\).")
  * [Connecting to Another LPG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/connect-lpg.htm#lpg-connection "Connect a local peering gateway \(LPG\) to another one in a different virtual cloud network \(VCN\) in the same region.")
  * [Configuring VCN Route Tables to Use an LPG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/give-lpg-rt.htm#give-lpg-rt "Update a Virtual Cloud Network \(VCN\) route table to include a new rule that directs traffic destined for the other VCN's CIDR to flow through the local peering gateway \(LPG\).")
  * [Associating a Route Table with an Existing LPG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/lpg-add-route-table.htm#add_route_table "To use transit routing, you must associate a route table to an LPG after you create the LPG.")
  * [Configuring Security Rules to Use an LPG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/give-lpg-sl.htm#give-lpg-sl "Update a security list in a Virtual Cloud Network \(VCN\) to include a new rule that allows traffic destined for the other VCN's CIDR to flow through a local peering gateway \(LPG\).")
  * [Tagging an LPG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/tags-lpg.htm#tags-lpg "Add metadata to a local peering gateway \(LPG\), which lets you define keys and values and associate them with resources.")
  * [Moving a local peering gateway to a different compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-lpg.htm#move-lpg "You can move a local peering gateway \(LPG\) from one compartment to another. When you move a local peering gateway to a new compartment, IAM policies for the new compartment apply immediately.")
  * [Deleting an LPG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-lpg.htm#delete-lpg "Delete a local peering gateway \(LPG\) from a Virtual Cloud Network \(VCN\) in Networking.")


Was this article helpful?
YesNo


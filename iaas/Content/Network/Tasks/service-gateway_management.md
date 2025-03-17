Updated 2024-08-21
# Service Gateway Management
Describes how to create and manage service gateways that can be used to provide access to services hosted in the Oracle Services Network.
For the purposes of management access control, you must specify the compartment where you want the service gateway to reside. Consult an administrator in your organization if you're not sure which compartment to use. For information about compartments and access control, see [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm).
The following basic management actions are available for service gateways:
  * [Creating a Service Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-sgw.htm#create-sgw "Create a service gateway in a Virtual Cloud Network \(VCN\) to allow access to the Oracle Services Network \(OSN\).")
  * [Listing Service Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-sgw.htm#list-sgw "List the service gateways \(SGWs\) available in a given compartment.")
  * [Getting Details for a Service Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-sgw.htm#get-sgw "View the settings for a particular service gateway \(SGW\).")
  * [Updating a Service Gateway's Route Table Association](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-sgw.htm#update-sgw "You can update a service gateway in a Virtual Cloud Network \(VCN\) to associate it with a route table or change the existing route table association.")
  * [Controlling Traffic for a Service Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/sgw-traffic.htm#sgw-traffic "You can block or allow traffic for a service gateway in a virtual cloud network \(VCN\).")
  * [Adding a Service CIDR Label to a Service Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-sgw.htm#attach-sgw "Add a specified service CIDR label to the service gateway.")
  * [Removing or Changing a Service Gateway's Service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/detatch-sgw.htm#detatch-sgw "Remove or change a specified service CIDR label from the specified service gateway.")
  * [Tagging a Service Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/tags-sgw.htm#tags-sgw "Add tags to a service gateway.")
  * [Moving a Service Gateway to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-sgw.htm#move-sgw "Move a service gateway into a different compartment within the same tenancy.")
  * [Deleting a Service Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-sgw.htm#delete-sgw "Delete a service gateway in a Virtual Cloud Network \(VCN\) to remove access to the Oracle Services Network \(OSN\).")


## When You Switch to a Different Service CIDR Label 🔗 
To avoid disrupting your Object Storage connections while switching between the **OCI <region> Object Storage** service CIDR label and **All <region> Services in Oracle Services Network**, use the following process:
  1. Update the service gateway: See [Removing or Changing a Service Gateway's Service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/detatch-sgw.htm#detatch-sgw "Remove or change a specified service CIDR label from the specified service gateway."). You can't enable both labels for the service gateway.
  2. [Update relevant route rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm#update-rules-routetable "Add, edit, or delete rules for a Virtual Cloud Network \(VCN\) route table."): For each rule that uses the service gateway as the target, switch the rule's destination service from the existing service CIDR label to the one you want to switch to. 
  3. Update relevant security rules: Change any security rules that specify the existing service CIDR label to instead use the one you want to switch to. The rules can be in [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) or [security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists).


If you instead delete your existing service gateway and create a new one, your Object Storage connections will be disrupted. Remember that before you can delete a service gateway, you must delete any route rules that specify that gateway as a target.
Was this article helpful?
YesNo


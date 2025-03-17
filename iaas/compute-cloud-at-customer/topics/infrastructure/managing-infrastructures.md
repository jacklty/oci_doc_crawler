Updated 2023-09-26
# Managing Compute Cloud@Customer Infrastructures
Compute Cloud@Customer infrastructures are the resources in Oracle Cloud Infrastructure that communicate with the corresponding hardware and software in the customer's data center.
You must create an infrastructure before connecting the hardware and software.
See [Creating a Compute Cloud@Customer Infrastructure in OCI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/create-infrastructure.htm#create-infrastructure "Create a Compute Cloud@Customer infrastructure in Oracle Cloud Infrastructure \(OCI\) to communicate with the corresponding infrastructure in the data center.") and [Connecting a Compute Cloud@Customer Infrastructure to OCI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/connecting.htm#connecting "The Compute Cloud@Customer infrastructure in the data center needs to be connected to Oracle Cloud Infrastructure \(OCI\) before it can be used. This task involves a bootstrap process during which a secure connection is established.").
You can change the name and upgrade schedule associated with an infrastructure later. See [Editing a Compute Cloud@Customer Infrastructure in OCI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/edit-infrastructure.htm#edit-infrastructure "Edit the display name, description, or tags of a Compute Cloud@Customer infrastructure, or associate a new upgrade schedule with the infrastructure.").
If you need to change the compartment where infrastructures are stored, you can do this. See [Moving a Compute Cloud@Customer Infrastructure Between Compartments](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/move-infrastructure.htm#move-infrastructure "Move an existing Compute Cloud@Customer infrastructure to a different compartment within the same tenancy.").
Don't try to delete an infrastructure if it has been used to connect to the Compute Cloud@Customer infrastructure in the data center.
**Important**
Infrastructures depend on continuous connection to Oracle Cloud Infrastructure. When Oracle Cloud Infrastructure isn't accessible, IAM configuration changes aren't synchronized on Compute Cloud@Customer and the required monitoring and maintenance tasks aren't performed.
Was this article helpful?
YesNo


Updated 2023-10-19
# Task 1: Create a Compartment
On Compute Cloud@Customer, compartments help you organize and control access to your resources. A compartment is a collection of resources (such as cloud networks, compute instances, and block volumes) that can be accessed only by those groups that have been given permission by an administrator in your organization.
In this tutorial, you use one compartment for all resources. However, when you're ready to create a production environment, you can separate resources into different compartments. For example, you might place all instances in one compartment and all networking resources in another compartment.
If you want to use an existing compartment rather than create a new compartment, you can do so. Skip this task and use your compartment for the tasks that follow.
For more information about compartments, [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm).
**Note**
On Compute Cloud@Customer, IAM resources such as compartments are managed in Oracle Cloud Infrastructure (OCI), and synchronized to Compute Cloud@Customer.
  1. Sign in to the Oracle Cloud Console in OCI using your federated identity credentials.
For more information, see [Sign In to the Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm#Signing_In_to_the_Console).
  2. In the Oracle Cloud Console navigation menu, click **Identity & Security**. Under **Identity** , click **Compartments**.
  3. On the Compartments page, click **Create Compartment**.
  4. Enter the following information:
     * **Name:** Enter Sandbox.
Avoid entering confidential information.
     * **Description:** (Required) Enter a description for the compartment.
     * **Create in Compartment:** Select the compartment in which to create this new compartment.
  5. Click **Create Compartment**.
The new compartment is displayed in the list.
It might take 10 minutes for the new compartment to show up on the Compute Cloud@Customer infrastructure.


**Note**
The remaining tutorial tasks use the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") instead of the Oracle Cloud Console, except for [10-4: Delete the Compartment](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/10-clean-up-resources.htm#delete-the-compartment "You must remove all resources from a compartment before you can delete it, otherwise, the delete action fails and the compartment returns to an active state.").
**Perform the next task:**
[Task 2: Create a Virtual Cloud Network (VCN)](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/create-a-virtual-cloud-network-vcn.htm#create-a-virtual-cloud-network-vcn)
Was this article helpful?
YesNo


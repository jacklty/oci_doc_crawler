Updated 2024-10-07
# Task 10: (Optional) Clean Up Resources
After you've finished with the resources you created for this tutorial, you can delete and release the resources you no longer plan to use.
Perform the following tasks in the order listed:
[10-1: Detach and Delete the Block Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/10-clean-up-resources.htm)
After you detach a block volume, you can delete it as long as the volume isn't attached to any other instances.
**Caution**
You can't undo a termination. Any data on a volume is permanently deleted when the volume is deleted.
  1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
  2. Select the **Sandbox** compartment.
  3. Click the name of your instance.
  4. In the **Resources** panel, click **Attached Block Volumes**.
  5. Find your volume, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Detach**. Confirm the detachment.
You might need to refresh the web page to see that the block volume is no longer attached.
  6. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Block Volumes**.
  7. Select the **Sandbox** compartment.
  8. Find your volume, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), and then click **Terminate**. Confirm the termination.


**Perform the next task:**
[10-2: Terminate the Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/10-clean-up-resources.htm#terminate-the-instance "You can permanently terminate \(delete\) instances that you no longer need. Any attached VNICs and boot volumes are automatically detached when the instance terminates. Eventually, the instance's public and private IP addresses are released and become available for other instances.")
[10-2: Terminate the Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/10-clean-up-resources.htm)
You can permanently terminate (delete) instances that you no longer need. Any attached VNICs and boot volumes are automatically detached when the instance terminates. Eventually, the instance's public and private IP addresses are released and become available for other instances.
  1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
  2. Select the **Sandbox** compartment.
  3. Find the instance you created, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Terminate**.
  4. In the **Confirm Instances termination** dialog box, move the "**Permanently delete the attached boot volume**" selector to the right, and click **Confirm**.
Moving the selector to the right results in the boot volume being permanently deleted, which is appropriate for this tutorial.
In production, you can leave the selector in the left position to preserve the boot volume for use with another instance. This is convenient when you want to reuse a configured OS or data on the boot volume.


**Perform the next task:**
[10-3: Delete the Subnet, Internet Gateway, and VCN](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/10-clean-up-resources.htm#delete-the-subnet-internet-gateway-and-vcn "You can delete networking resources as long as the resource doesn't have any dependencies.")
[10-3: Delete the Subnet, Internet Gateway, and VCN](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/10-clean-up-resources.htm)
You can delete networking resources as long as the resource doesn't have any dependencies.
  * **Subnets** : Must be empty (for example, no instance VNICs or route rules).
  * **VCNs** : Must be empty and have no related resources or attached gateways (for example, no internet gateway, dynamic routing gateway, and so on).


  1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
  2. Select the **Sandbox** compartment.
  3. Click the name of your VCN.
  4. Under **Resources** , click **Route Tables**.
  5. Click the name of the route table.
  6. For the route rule you created, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), click **Delete** , and confirm the deletion.
The route rule is deleted.
  7. In the breadcrumb path at the top of the page, click the name of your VCN.
The VCN details page is displayed.
  8. Under **Resources** , click **Internet Gateways**.
  9. For the internet gateway that you created, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Delete** , and confirm the deletion.
The internet gateway is deleted.
  10. Under **Resources** , click **Subnets**.
  11. For the subnet you created, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Delete** , and confirm the deletion.
The subnet is deleted.
  12. At the top of the **VCN details** page, click **Terminate** and confirm the termination.
The VCN is deleted.


**Perform the next task:**
[10-4: Delete the Compartment](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/10-clean-up-resources.htm#delete-the-compartment "You must remove all resources from a compartment before you can delete it, otherwise, the delete action fails and the compartment returns to an active state.")
[10-4: Delete the Compartment](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/10-clean-up-resources.htm)
You must remove all resources from a compartment before you can delete it, otherwise, the delete action fails and the compartment returns to an active state.
**Note**
On Compute Cloud@Customer, IAM resources such as compartments are managed in Oracle Cloud Infrastructure (OCI), and synchronized to Compute Cloud@Customer.
  1. Sign in to the Oracle Cloud Console in OCI using your federated identity credentials.
For more information, see [Sign In to the Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm#Signing_In_to_the_Console).
  2. In the Oracle Cloud Console navigation menu, click **Identity & Security**, then under **Identity** , click **Compartments**.
  3. For the Sandbox compartment, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), and then click **Delete**.
  4. Confirm the deletion.


This concludes the tutorial.
Was this article helpful?
YesNo


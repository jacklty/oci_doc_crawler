Updated 2025-01-23
# Creating a Stack from a Resource Creation Page
Populate a resource creation page in another OCI service in the Console and then use the **Save as stack** button to create a stack in Resource Manager.
For example, create a stack from the **Create compute instance** page. Use the new stack to install, configure, and manage your compute **instance** through the "infrastructure-as-code" model.
**Note** Some resources don't yet have the **Save as stack** button.
  1. Open the resource creation page that you want to use for a new stack.
For example, open the **Create compute instance** page:
     * Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
     * Select **Create instance**.
**Note** If creating a stack from the resource creation page for a compute instance, then ensure that you review requirements for instances. See [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).
  2. Populate configuration fields to specify stack details.
For example, select the image you want to use in a stack for creating instances.
  3. Select **Save as stack**.
Depending on resource type, one of the following opens:
     * **Save as stack** panel (for Kubernetes clusters and other resources)
     * **Create stack** page (for compute instances and VCNs)
  4. (Optional) Edit the default stack name and enter a stack description. Avoid entering confidential information.
  5. Select the compartment that you want to store the stack in.
  6. To add a defined tag, select the namespace and key, then enter a value.
  7. To add a free-form tag, enter a key and value.
  8. Save the stack: Perform one of the following actions:
     * **Save as stack** panel: Select **Save**.
     * **Create stack** dialog box: Select **Next** twice and then select **Create**.
The result depends on the panel or page. For **Save as stack** , the **Open stack** link appears. For **Create stack** , the **Stack details** page opens.
  9. To view a stack created from the **Save as stack** panel, perform one of the following actions:
     * Select **Open stack**.
     * On the **Stacks** list page, select the new stack. The newest stack is at the top of the list. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").


Was this article helpful?
YesNo


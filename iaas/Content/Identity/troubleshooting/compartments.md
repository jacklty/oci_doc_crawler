Updated 2025-01-13
# Compartments
Learn how to troubleshoot common compartments issues.
## Compartment Fails to Delete 🔗 
If the compartment fails to delete, verify that you have removed all the resources.
  1. For most resources, you can use the tenancy explorer to help you locate them. See [Resources Supported by the Tenancy Explorer](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/compartmentexplorer.htm#Resource) for the list of supported resources.
**To view resources in a compartment**
Open the **navigation menu** and select **Governance & Administration**. Under **Tenancy Management** , select **Tenancy Explorer**. The tenancy explorer opens with a view of the root compartment. Select the compartment you want to explore from the compartment picker on the left side of the Console. After you select a compartment, the resources that you have permission to view are displayed. The **Name** and **Description** of the compartment you are viewing are displayed at the top of the page.
  2. Verify that there are no policies in the compartment (polices are not included in Search results).
**To find policies in a compartment**
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Policies**.
    2. From the compartments list on the left, select the compartment you want to delete.
Policies attached to the compartment are displayed.
  3. If you can't locate any resources in the compartment, check with your Administrator; you might not have permission to view all resources.


Was this article helpful?
YesNo


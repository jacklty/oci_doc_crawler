Updated 2025-02-11
# Attaching a Governance Rule to a Tenancy
Attach an existing governance rule to one or more tenancies.
For more information about governance rules, see [Adding Governance to Tenancies](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm#add_governance "Use governance rules to configure and attach controls to tenancies in your organization. When a governance rule is attached to a tenancy, a corresponding resource is created and then locked in the target tenancy.").
  1. Open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Governance Rules**.
  2. On the **Governance Rules** list page, select the governance rule that you want to attach to a tenancy. 
The **Tenancies** section of the details page lists the following information for every tenancy in the organization:
     * **Tenancy** : The tenancy name.
     * **Rule status** : The rule status, whether **Not attached** or **Attached**.
     * **Organization governance** : Indicates whether the tenancy has joined or not joined organization governance. Only tenancies that have joined organization governance can be attached to rules.
  3. Select one or more tenancies and the select **Attach tenancies**.
A confirmation is displayed to confirm that you want to attach the rule to the tenancy. 
  4. Select **Attach rule**. 
The governance rule detail page reloads and a new work request is started. After the work request completes, the rule is attached to the tenancy, and the **Rule Status** changes to **Attached**.


The governance rule now enforces its restrictions on the child tenancies. You can also view the associated governance rules by accessing the **Tenancies** page in **Organization Management**. On the **Tenancies** page, select the tenancy name to open the tenancy details page.
Under **Governance rules** , you can view the list of governance rules attached to the tenancy (to include their name and rule type). Select the governance rule name to go to the associated governance rule details page.
Meanwhile, the child tenancy that has attached governance rules can also view the rules on the **Governance rules** page, but can't interact with the rule, and can only view basic information about it, because the parent tenancy controls the rule configuration.
Was this article helpful?
YesNo


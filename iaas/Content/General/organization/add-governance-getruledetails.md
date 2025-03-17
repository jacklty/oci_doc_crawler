Updated 2025-02-11
# Getting a Governance Rule's Details
Get information about a governance rule in an organization.
  1. Open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Governance Rules**.
  2. On the **Governance Rules** list page, select the rule that you want to view details for.
On the details page, the **Rule details** tab shows the following information. Under **General information** :
     * **OCID** : OCID of the governance rule.
     * **Created** : Created time in UTC format.
     * **Targeted tenancies** : The number of targeted tenancies.
     * **Attachment method** : Attached to specific tenancies or the entire organization.
Under **Rule configuration** , some information changes depending on whether the rule is for allowed regions, quota policies, or tags:
     * **Rule type**
     * (Allowed region rule only) **Allowed regions** : Lists the allowed regions in the rule.
     * (Quota policy rule only) **Statement** : Select the **View details** link to see the statements in the **Quota policy statements** panel.
     * (Tags rule only) **Tag namespace** : Lists the namespace. To view information about the namespace, select **View details**.
     * (Tags rule only) **Tag defaults** : Lists the number of tag defaults. To see the tag defaults, select **View details**.
The **Tenancies** section of the governance rule details page lists the following information for every tenancy:
     * **Tenancy** : The tenancy name.
     * **Rule status** : The rule status, whether **Not attached** or **Attached**.
     * **Organization governance** : Indicates whether the tenancy has **Joined** or **Not joined** organization governance. Only tenancies that have joined organization governance can be attached to rules. 
For information about attaching a governance rule to a tenancy, see [Attaching a Governance Rule to a Tenancy](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-attachruletenancy.htm#add_governance_attachruletenancy "Attach an existing governance rule to one or more tenancies.").


Was this article helpful?
YesNo


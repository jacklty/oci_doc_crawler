Updated 2025-01-14
# Moving a Resource Between Compartments
Most resources can be moved after they're created.
There are a few resources that you can't move from one compartment to another. Also, you can't move certain resources from a security zone to a compartment that's not in the same security zone, because it might be less secure. For details about restrictions for resources in security zones, see [Restrict Resource Movement](https://docs.oracle.com/iaas/security-zone/using/security-zone-policies.htm).
Some resources have attached resource dependencies and some don't. Not all attached dependencies behave the same way when the parent resource moves.
For some resources, the attached dependencies move with the parent resource to the new compartment. The parent resource moves immediately, but in some cases attached dependencies move asynchronously and aren't visible in the new compartment until the move is complete.
For other resources, the attached resource dependencies don't move to the new compartment. You can move these attached resources independently.
After you move the resource to the new compartment, the policies that govern the new compartment apply immediately and affect access to the resource. Depending on the structure of your compartment organization, metering, billing, and alarms can also be affected.
See the service documentation for individual resources to familiarize yourself with the behavior of each resource and its attachments.
  1. Open the navigation menu and select the type of resource you want to work with. For example, to view Compute resources: Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**..
  2. In the **List Scope** section, select a compartment. Resources in the selected compartment are displayed. 
  3. Find the resource in the list, select the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and follow the prompts to move the resource to a new compartment. See the resource documentation for specific steps. 


Was this article helpful?
YesNo


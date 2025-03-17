Updated 2025-01-14
# Managing Oracle Identity Cloud Service Roles for Users
This topic describes managing user roles for users created in Oracle Identity Cloud Service. 
## About User Roles in Oracle Identity Cloud Service 🔗 
You can assign roles to a user to allow access to those Oracle Cloud services that have predefined roles defined in Oracle Identity Cloud Service. You can also grant access just to service instances. 
Services managed through Identity Cloud Service can have two types of predefined roles: 
  * Service access roles - grant access to use the service.
  * Instance access roles - grant access to specific instances of a service. These can only be granted after the instances are created


For information about more complex role management including assigning other administrative privileges, see [Managing Oracle Identity Cloud Service Users](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/manage-oracle-identity-cloud-service-users1.html).
## Available Roles for Each Service 🔗 
Service-specific roles vary from one Oracle Cloud service to another, but they typically include at least one administrator role. See [About Service Administrator Roles](https://docs.oracle.com/en/cloud/get-started/subscriptions-cloud/csgsg/service-administrator-roles.html) for more information about administrator roles. See your service-specific documentation for a description of the predefined roles for that service.
## Required Permissions to Manage Roles 🔗 
Before you can manage roles using the Oracle Cloud Infrastructure Console, you must be allowed to access the Identity Provider Details page. To access this page, you must belong to a group that is allowed to inspect identity providers. To give this permission to non-administrators, you'll need to write policies like the following:
Copy
```
allow group GroupA to {USAGE_BUDGET_READ} in tenancy
allow group GroupA to {USAGE_BUDGET_INSPECT} in tenancy
allow group GroupA to {USAGE_BUDGET_MANAGE} in tenancy
allow group GroupA to {TENANCY_INSPECT} in tenancy
```

where you replace GroupA with the name of the group you want to grant the permission to.
To manage the service roles for another user, you must be assigned the appropriate role in Oracle Identity Cloud Service. See [Understanding Administrator Roles](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/understand-administrator-roles.html).
## Managing Roles User Roles in the Console 🔗 
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. A list of the users in your tenancy is displayed. 
By default, users belonging to all identity providers are displayed. To view only users that belong to your Identity Cloud Service federation, clear the checkboxes for any other identity providers.
  2. Select the name of the user you want to edit. 
  3. On the user details page, select **Manage Roles**. The **Manage Roles** page displays the list of services for which you have Administrator access. The service and instance roles that this user has already been granted are also displayed.
Note that you won't see services that you don't have Administrator access for. 
  4. Find the service you want to edit this user's access to, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Manage service access** or **Manage instance access** , as appropriate. The list of roles for the selected service is displayed.
  5. Edit the user's access as follows:
     * Select each role you want to give to the user. 
     * Select the **x** next to each role you want remove from the user. Note that you can't remove a role that has been granted through a group. These roles are read only.
**Note** If a user is assigned the Cloud Account Administrator role, then you can't remove the individual entitlement roles for the user. 
  6. Select **Apply Role Settings** or **Update Instance Settings** , as appropriate.
  7. If you are granting roles to a user, in the confirmation dialog, select **Send Email to User** to send an email to the user to notify them of this change. 
  8. Your email client launches with a default email message you can send to the user. You can send the email as shown, or make modifications before sending.
  9. Return to the Console and select **Close**.


## Managing Instance Roles in the Console 🔗 
Some services allow you to grant access to instances of the service. After you (or someone in your organization) creates an instance, use this procedure to manage individual user access to the instance.
**Managing User Access to an Instance**
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. 
A list of the users in your tenancy is displayed. 
By default, users belonging to all identity providers are displayed. To view only users that belong to your Identity Cloud Service federation, clear the checkboxes for any other identity providers.
  2. Select the name of the user you want to edit. 
  3. On the user details page, select **Manage Roles**. The **Manage Roles** page displays the list of services for which you have Administrator access. The service and instance roles that this user has already been granted are also displayed.
Note that you won't see services that you don't have Administrator access for. 
  4. Find the service with instances that you want to edit this user's access to, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Manage instance access**. The list of instances for the selected service is displayed.
  5. On the **Manage Access to Instances** page, find the name of the instance you want to edit this user's access to. 
To grant access to this instance:
In the **Instance Role** column, select the role you want to grant to the user. You can select multiple roles from the list.
To remove access to this instance:
In the **Instance Role** column, select the **x** next to the role you want to remove from the user. 
  6. When you are finished editing roles, select **Update Instance Settings**.
  7. On the **Manage Roles** page, select **Apply Role Settings**.
  8. If you are granting roles to a user, in the confirmation dialog, select **Send Email to User** to send an email to the user to notify them of this change. 
  9. Your email client launches with a default email message you can send to the user. You can send the email as shown, or make modifications before sending.
  10. Return to the Console and select **Close**.


Was this article helpful?
YesNo


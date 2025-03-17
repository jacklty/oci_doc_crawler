Updated 2025-01-14
# Managing Oracle Identity Cloud Service Roles for Groups
This topic describes managing roles for groups created in Oracle Identity Cloud Service.
## About Group Roles in Oracle Identity Cloud Service 🔗 
You can assign roles to groups to allow access to those Oracle Cloud services that have predefined roles defined in Oracle Identity Cloud Service. You can also grant access just to service instances. 
Services managed through Identity Cloud Service can have two types of predefined roles: 
  * Service access roles - grant access to use the service.
  * Instance access roles - grant access to specific instances of a service. These can only be granted after the instances are created.


For information about more complex role management, see [Manage Oracle Identity Cloud Service Groups](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/manage-oracle-identity-cloud-service-groups1.html).
## Available Roles for Each Service 🔗 
Service-specific roles vary from one Oracle Cloud service to another, but they typically include at least one administrator role. See [About Service Administrator Roles](https://docs.oracle.com/en/cloud/get-started/subscriptions-cloud/csgsg/service-administrator-roles.html) for more information about administrator roles. See your service-specific documentation for a description of the predefined roles for that service.
## Required Permissions to Manage Roles 🔗 
Before you can manage roles using the Oracle Cloud Infrastructure Console, you must be allowed to access the Identity Provider Details page. To access this page, you must belong to a group that is allowed to inspect identity providers. If you are a Cloud Administrator or if you belong to the OCI_Administrators group, this permission is included. To give this permission to non-administrators, you'll need to write policies like the following:
Copy
```
allow group GroupA to {USAGE_BUDGET_READ} in tenancy
allow group GroupA to {USAGE_BUDGET_INSPECT} in tenancy
allow group GroupA to {USAGE_BUDGET_MANAGE} in tenancy
allow group GroupA to {TENANCY_INSPECT} in tenancy
```

where you replace GroupA with the name of the group you want to grant the permission to.
To manage service roles, you must be assigned the Administrator role for that service. 
## Managing Group Roles in the Console 🔗 
[To add roles to a group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managinggrouprolesidcs.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**.
  2. Click your Oracle Identity Cloud Service federation. For most tenancies, the federation is named **OracleIdentityCloudService**. The identity provider details page is displayed. 
  3. Select **Groups**.
The list of groups is displayed.
  4. Select the name of the group you want to add roles to. 
  5. On the group details page, select **Manage Roles**. The **Manage Roles** page displays the list of services for which you have Administrator access. The service and instance roles that this group has already been granted are also displayed.
Note that you won't see services that you don't have Administrator access for. 
  6. Find the service you want to edit this group's access to, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Manage service access**. The list of roles for the selected service is displayed.
  7. Select each role that you want to assign to the group.
  8. Select **Save Role Selections**.
  9. To add more service roles to this group, repeat steps 6 - 8.
  10. Select **Apply Role Settings**.
  11. In the confirmation dialog, select **Send Email to Group** to send an email to each member of the group to notify them of this change. 
Your email client launches with a default email message to the affected users with information about the access changes. You can send the email as written, or make modifications before sending.
  12. Return to the Console and select **Close**. 


[To revoke roles from a group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managinggrouprolesidcs.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**.
  2. Click your Oracle Identity Cloud Service federation. For most tenancies, the federation is named **OracleIdentityCloudService**. The identity provider details page is displayed. 
  3. Select **Groups**.
The list of groups is displayed.
  4. Select the name of the group you want to remove roles from. 
  5. On the group details page, select **Manage Roles**. The **Manage Roles** page displays the list of services for which you have Administrator access. The service and instance roles that this group has already been granted are also displayed.
Note that you won't see services that you don't have Administrator access for. 
  6. Find the service you want to edit this group's access to, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Manage service access** or **Manage instance access** , as appropriate. The list of roles for the selected service is displayed.
  7. Clear the checkbox for each role you want remove from the group.
  8. Select **Save Role Selections** or **Update Instance Settings** , as appropriate.. 
  9. To revoke more service or instance roles from this group, repeat steps 6 - 8.
  10. Select **Apply Role Settings**.
  11. A confirmation dialog displays the services that you modified access to in this session. Select **Close**. 


## Managing Instance Roles in the Console 🔗 
Some services allow you to grant access to instances of the service. After you (or someone in your organization) creates an instance, use this procedure to manage group access to the instance.
**Managing Group Access to an Instance**
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**.
  2. Click your Oracle Identity Cloud Service federation. For most tenancies, the federation is named **OracleIdentityCloudService**. The identity provider details page is displayed. 
  3. Select **Groups**.
The list of groups is displayed.
  4. On the group details page, select **Manage Roles**. The **Manage Roles** page displays the list of services for which you have Administrator access. The service and instance roles that this group has already been granted are also displayed.
Note that you won't see services that you don't have Administrator access for. 
  5. Find the service with instances that you want to edit this group's access to, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Manage instance access**. The list of instances for the selected service is displayed.
  6. On the **Manage Access to Instances** page, find the name of the instance you want to edit this group's access to. 
     * To grant access to this instance: In the **Instance Role** column, select the role you want to grant to the group. You can select multiple roles from the list.
     * To remove access to this instance: In the **Instance Role** column, select the **x** next to the role you want to remove from the group. 
  7. When you are finished editing roles for this service, select **Update Instance Settings**.
  8. To edit more instance roles for this group, repeat steps 6 - 7.
  9. On the **Manage Roles** page, select **Apply Role Settings**.
  10. If you added roles, in the confirmation dialog, select **Send Email to Group** to send an email to each member of the group to notify them of this change. Your email client launches with a default email message to the affected users with information about the access changes. You can send the email as written, or make modifications before sending. Return to the Console and select **Close**.
If you revoked roles, a confirmation dialog displays the services that you modified access to in this session. Select **Close**. 


Was this article helpful?
YesNo


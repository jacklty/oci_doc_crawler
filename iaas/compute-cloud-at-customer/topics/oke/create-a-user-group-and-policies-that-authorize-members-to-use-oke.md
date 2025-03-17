Updated 2024-12-16
# Create a User Group and Policies for OKE Users
In your OCI tenancy that's associated with Compute Cloud@Customer, create a user group and policies that authorize users to use OKE.
This procedure assumes the following conditions: 
  * Your intended OKE administrators already have OCI user accounts.
  * You tenancy is configured with Identity Domains. If you're not sure which type of identity service you're using, see [Determining the Tenancy Type](https://docs.oracle.com/iaas/Content/Security/Reference/determining_the_tenancy_type.htm). If your tenancy isn't using Identity Domains, create a group and policies as described in [Managing Groups (without Identity Domains)](https://docs.oracle.com/iaas/Content/Identity/Tasks/managinggroups.htm#Managing_Groups).


For more information about managing groups with Identity Domains, see [Managing Groups (with Identity Domains)](https://docs.oracle.com/iaas/Content/Identity/groups/managinggroups.htm#Managing_Groups).
For more information about policies, see these resources:
  * [How Policies Work (with Identity Domains)](https://docs.oracle.com/iaas/Content/Identity/policieshow/how-policies-work.htm)
  * [How Policies Work (without Identity Domains)](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm)


  1. Sign in to your OCI tenancy. In the Oracle Cloud Console, open the navigation menu, click **Identity & Security**. Under **Identity** , click **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Click **Groups**.
  3. Click **Create group**.
  4. Enter the following information:
     * **Name** : Enter a unique name for the group. Avoid entering confidential information.
     * **Description** : Enter a description.
  5. To allow users to request access to this group, select **User can request access**.
  6. To add users to the group, select the checkbox for each user who will manage OKE resources.
**Tip**
To search for a user, click the text box, enter all or part of the beginning of the username, first name, or last name of the user, and then press **Enter**.
  7. Click **Create**.
  8. Click your browser's back button to return to the Domains page.
  9. Under **Identity** , click **Policies**.
  10. Click **Create Policy**.
  11. Enter a policy name and description.
  12. Create the policies that authorize group members to use OKE.
Include the `manage cluster-family` authorization in the policy. The following shows example policies for the OKE user group. Depending on your organization, for example if you have a separate team that manages network resources, some of the following `manage` authorizations could be `read` or `use` authorizations. Or, you might need to add authorizations. You might need to create more than one user group to authorize OKE work in different compartments.
Copy
```
allow group <group-name> to read all-resources in tenancy
allow group <group-name> to manage cluster-family in compartment <compartment-name>
allow group <group-name> to manage instance-family in compartment <compartment-name>
allow group <group-name> to manage virtual-network-family in compartment <compartment-name>
allow group <group-name> to manage volume-family in compartment <compartment-name>
        
```

  13. Click **Create**.


**What's Next:**
Create a Dynamic Group and policies. Use one of the following procedures:
  * [Create a Dynamic Group and Policies (Using the Oracle Cloud Console)](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/create-a-dynamic-group.htm#create-a-dynamic-group "In your OCI tenancy that's associated with Compute Cloud@Customer, create a dynamic group and policies to authorize member instances to manage OKE resources.")
  * [Create a Dynamic Group and Policies (Using the Oracle Cloud Console)](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/create-a-dynamic-group.htm#create-a-dynamic-group "In your OCI tenancy that's associated with Compute Cloud@Customer, create a dynamic group and policies to authorize member instances to manage OKE resources.")


Was this article helpful?
YesNo


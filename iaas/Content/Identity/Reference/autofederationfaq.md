Updated 2025-01-14
# Find Out More About Oracle Identity Cloud Service Federated Users
When you sign up for Oracle Cloud Infrastructure, your account is automatically federated with Oracle Identity Cloud Service as your identity provider. This topic answers some frequently asked questions about the federation.
[What resources are created in Oracle Identity Cloud Service?](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/autofederationfaq.htm)
### The following resources are created in Identity Cloud Service:
  * **Applications:**
    * _OCI-V2- <tenancy_name>_
This SAML application that creates the federation with Oracle Cloud Infrastructure.
    * COMPUTEBAREMETAL application
A supporting application for the federation. 
**Important** Do not delete these applications.
  * **Group:**
OCI_Administrators group
This group is mapped to the Administrators group in Oracle Cloud Infrastructure. Members of this group have full administrator privileges in Oracle Cloud Infrastructure. 
  * **User:**
A default administrator user (e.g., user@example.com) who is a member of the OCI_Administrators group.


[What resources are created in Oracle Cloud Infrastructure?](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/autofederationfaq.htm)
### The following resources are created in Oracle Cloud Infrastructure:
  * **Identity Provider:** OracleIdentityCloudService
  * **Group Mappings:** The federation is created with one group mapping: 
OCI_Administrators group (from Oracle Identity Cloud Service) is mapped to the Administrators group (In Oracle Cloud Infrastructure).
  * **Users:**
    * The default administrator user created in Oracle Identity Cloud Service is provisioned in Oracle Cloud Infrastructure. This user can have the Oracle Cloud Infrastructure credentials, but not a Console password. 
    * A default administrator local-user with the same user name (user@example.com) is also created in Oracle Cloud Infrastructure's IAM service. Customers who choose **not** to use the Oracle Identity Cloud Service federation can use this user to administer Oracle Cloud Infrastructure. 


**Important** The default administrator created in Oracle Identity Cloud Service and the local default administrator created in Oracle Cloud Infrastructure exist independently in their respective identity systems. Ensure that you manage passwords for them separately. 
[Why is my account federated with Oracle Identity Cloud Service?](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/autofederationfaq.htm)
Oracle Identity Cloud Service is the identity provider for multiple Oracle services. Federating Oracle Cloud Infrastructure with Oracle Identity Cloud Service allows you to have a seamless connection between services, without having to create a separate username and password for each one.
[How do I know if I am signed in through Oracle Identity Cloud Service?](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/autofederationfaq.htm)
Select the **Profile** menu to display your username. Users signed in through an identity provider will see their username prefaced with their identity provider name, for example:
oracleidentitycloudservice/user@example.com
[How do I add a user to Oracle Identity Cloud Service (a federated user)?](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/autofederationfaq.htm)
See [Managing Oracle Identity Cloud Service Users and Groups in the Oracle Cloud Infrastructure Console](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#Managing_Oracle_Identity_Cloud_Service_Users_and_Groups_in_the_Oracle_Cloud_Infrastructure_Console).
[Can I add a user just for Oracle Cloud Infrastructure?](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/autofederationfaq.htm)
Yes. If you don't want to manage the user in Oracle Identity Cloud Service, you can add a user directly to the Oracle Cloud Infrastructure IAM service. See [Adding Users](https://docs.oracle.com/iaas/Content/GSG/Tasks/addingusers.htm). Using this procedure, you can create users who can sign in directly to the Oracle Cloud Infrastructure Console. Users created with this procedure do not have access to any other Oracle services.
[How do I manage groups?](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/autofederationfaq.htm)
In short, managing groups requires actions in both Oracle Identity Cloud Service and Oracle Cloud Infrastructure. Groups you create in Oracle Identity Cloud Service have no privileges in Oracle Cloud Infrastructure until you map them to a group in Oracle Cloud Infrastructure. You define the policies that permit access to Oracle Cloud Infrastructure resources in the IAM service in Oracle Cloud Infrastructure. For more information, see [Managing Oracle Identity Cloud Service Users and Groups in the Oracle Cloud Infrastructure Console](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#Managing_Oracle_Identity_Cloud_Service_Users_and_Groups_in_the_Oracle_Cloud_Infrastructure_Console).
[How do I find the client ID and client secret?](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/autofederationfaq.htm)
To edit mappings of your user groups in Oracle Identity Cloud Service to user groups in Oracle Cloud Infrastructure, you'll need to supply the client ID and client secret. The client ID and client secret are stored in Oracle Identity Cloud Service. To get this information:
  1. Sign in to the Oracle Identity Cloud Service console.
  2. In the Identity Cloud Service console, click **Applications**. The list of trusted applications is displayed.
  3. Click COMPUTEBAREMETAL. 
  4. Click **Configuration**.
  5. Expand **General Information**. The client ID is displayed. Click **Show Secret** to display the client secret.
[![Screenshot shows the client secret key in the Oracle Identity Cloud Service console](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_fed_secret.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_fed_secret.png)


[If I delete the federation, can I later recreate it?](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/autofederationfaq.htm)
Yes. To recreate the federation with Oracle Identity Cloud Service, follow the instructions in the topic [Federating with Oracle Identity Cloud Service](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm#top).
Was this article helpful?
YesNo


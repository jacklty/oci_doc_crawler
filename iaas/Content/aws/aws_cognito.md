Updated 2023-10-06
# Amazon Web Services Cognito
This document describes how to configure OCI IAM with identity domains to integrate with Amazon Web Services (AWS) Cognito.
## Before You Begin 🔗 
Read about the AWS Cognito application as well as learn what information you need before getting started.
### About AWS Cognito 🔗 
Amazon Cognito lets you add user sign-up, sign-in, and access control to your web and mobile apps quickly and easily. Amazon Cognito scales to millions of users and supports sign-in with social identity providers, such as Apple, Facebook, Google, and Amazon, and enterprise identity providers via SAML 2.0 and OpenID Connect.
In Cognito, we can create multiple userpools and each userpool can hold users, groups and manage different sign-ins. An integration with AWS Cognito is directly with a single userpool. Customer can have multiple userpools under a single Cognito account.
### What Do You Need? 🔗 
To create an AWS account, you need:
  * A **paid** Oracle Cloud Infrastructure (OCI) account, or an OCI trial account. See [Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm#Oracle_Cloud_Infrastructure_Free_Tier).
  * OCI administrator sign-in credentials
  * AWS IAM administrator sign-in credentials
  * AWS Cognito UserPool Access


To create an application in OCI identity, you need:
  * Identity domain administrator or security administrator role for the OCI IAM identity domain. See [Understanding Administrator Roles](https://docs.oracle.com/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles).
  * The following AWS cognito configuration information:
    * AccessKeyId
    * SecretAccessKey
    * External ID
    * Role ARN
    * Account Region
    * Cognito User Pool Id
    * (Optional) List of Group Names from which one wants to synchronize users


## Supported Operations 🔗 
Operation| Supported| Comments  
---|---|---  
Test Connectivity| yes| Tests the connectivity and configuration provided.  
Authoritative Sync (Full)| yes| Sync users , groups and user-group memberships from AWS Cognito and creates them in OCI Identity Domain.  
Incremental Authoritative Sync| no| AWS Cognito doesn't support for incremental or delta changes of users , groups , user-group memberships.  
## Creating an AWS Account 🔗 
  1. Sign in to the AWS Management Console with your administrator privileges.
  2. Go to **Services** , **Security & Identity** and select **IAM**.


### Create a Policy for Accessing Cognito APIs 🔗 
**Note** :- Please have the cognito pool ARN value before creating the policy
  1. Click **Policies** and then **Create policy**.
  2. Provide the following values:
     * **Service** : Cognito User Pools
     * **Actions** : Select the following APIs:
       * ListUsers
       * ListGroups
       * AdminListGroupsForUser
       * ListUsersInGroup
       * AdminGetUser
       * GetGroup
     * **Resources** : Add user pool ARN.
       1. Click the ARN link.
       2. Click list ARNs manually.
       3. Provide the user pool ARN value and click **Add**.
       4. Click **Next**.
  3. Provide tags, if required.
  4. Provide a policy name, for example, "cognitoAPIAccessPolicy".
  5. Click **Create Policy**.


### Create a Role 🔗 
  1. Click **Roles** and then **Create role**.
  2. In **Select trusted entity** :
    1. Click **AWS account**.
    2. In options, select the **externalID** checkbox.
    3. Provide the **externalID** value. This value can be any entry which can be unique for your reference only. For example, "cognito-integration".
    4. Click **Next**.
  3. Add Permissions.
    1. Select the previously created policy **cognitoAPIAccessPolicy**.
    2. Click **Next**.
  4. On the Details tab:
    1. Provide the role name, for example, "cognitoApiAccessRole".
    2. Click **Save**.


**Result:** The role is created.
### Create a Policy With AssumeRole 🔗 
**Note** :- Please have the ARN value of the role created in previous step
  1. Click **Policies** and then **Create policy**.
  2. Provide the following values:
    1. **Service** : STS
    2. **Actions** : AssumeRole
    3. **Resources** : Add role ARN.
      1. Click the ARN link.
      2. Click list ARNs manually.
      3. Provide the role ARN value created in previous step and click **Add**.
      4. Click **Next**.
  3. Provide tags, if required.
  4. Provide a policy name, for example, "assumeRolePolicy".
  5. Click **Create policy**.


### Create a User 🔗 
  1. Click **Users** and then **Create user**.
  2. Enter a username, for example, "serviceAccountUser".
    1. Select the **Access key - Programmatic access** checkbox.
    2. Click **Next**.
  3. Set the permissions:
    1. Select **attach existing policy**.
    2. Select the assume role policy created earlier. say **assumeRolePolicy**
    3. Click **Next** and then review.
    4. Click **Create user**. **Result** : The user is created.
  4. Copy the values for **accessKeyId** and **secretAccessKey** for the user. These values would be used for configuring the cognito application in OCI identity domain.


## Creating an Application in OCI Identity 🔗 
### Create an AWS Cognito Application 🔗 
  1. Access the OCI Console with your identity domain administrator credentials.
  2. Open the navigation menu and click **Identity & Security**. Under **Identity** , click **Domains**. Select the identity domain you want to work in and click **Applications**.
  3. Click **Add application**.
  4. In the **Add application** window, click **Application Catalog** , and then **Launch app catalog**.
  5. Locate and select **AWS Cognito**.
  6. Provide the application name and click **Next**.
  7. Click **Enable Provisioning** and confirm.
  8. Provide all the following configuration details: **Note** :- Sample values provided for reference only.
Configuration| Description| Sample Value  
---|---|---  
**AWS Cognito Region**|  Provide the AWS Cognito region value| us-east-1  
**Cognito User Pool Id**|  Provide the AWS Cognito User Pool id value| us-east-1_9876543210  
**List of Groups**|  Provide the list of groups for syncing users belonging to those groups. If no groups are provided, Application would brings all groups, users and user-group memberships. **Note** :- Please provide every group name in a new line| idp-adminidp-support  
**Access Key ID**|  Access key id value of the service user| None  
**Secret Access Key**|  Secret Access Key of the service user| None  
**External ID**|  External Id value provided as part of the role creation| cognito-integration  
**Role ARN**|  Role ARN value| arn:aws:iam::1234567890:role/cognitoApiAccessRole  
  9. Select the **Authoritative sync** checkbox.
  10. Turn on Enable synchronization.
  11. Click **Finish** and then **Save**.
  12. Click **Test Connectivity** to test the connection.
  13. Click **Activate** to activate the application.


### Import Synchronized Users 🔗 
If the test connection passed and the application is activated, then import all users, groups, and user-group memberships from AWS Cognito to OCI Identity.
  1. Click **Import** under **Resources**.
  2. Click **Import** to start the job.


**Result** : All synchronized users display in the Console.
## Troubleshooting 🔗 
There are no troubleshooting topics at this time.
### Known Issues 🔗 
There are no known issues topics at this time.
### Other Issues 🔗 
For other issues, open a support ticket. See [Open a Support Ticket](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport_topic-Open_a_support_service_request.htm).
Was this article helpful?
YesNo


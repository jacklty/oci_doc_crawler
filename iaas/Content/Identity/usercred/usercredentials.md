Updated 2024-12-18
# Working with User Credentials
You can manage several types of credentials with Oracle Cloud Infrastructure Identity and Access Management (IAM):
  * Console password: For signing in to the Console, the user interface for interacting with Oracle Cloud Infrastructure. Use a username and Console password, to sign in to your cloud account/tenancy and identity domain. Note that federated users can't have Console passwords because they sign in through their identity provider. See [Federating with Identity Providers](https://docs.oracle.com/en-us/iaas/Content/Identity/federating/federating_section.htm "Learn about and use identity federation."). If you need help signing in, see [Signing In for the First Time](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm).
  * API signing key (in PEM format): For sending API requests, which require authentication.
  * Auth token: An Oracle-generated token that you can use to authenticate with third-party APIs. For example, use an auth token to authenticate with a Swift client when using Recovery Manager (RMAN) to back up an Oracle Database System (DB System) database to Object Storage.
  * Customer Secret Keys: For using the Amazon S3 Compatibility API with Object Storage. See [Amazon S3 Compatibility API](https://docs.oracle.com/iaas/Content/Object/Tasks/s3compatibleapi.htm).
  * OAuth 2.0 Client Credentials: For interacting with the APIs of those services that use OAuth 2.0 authorization. See [OAuth 2.0 Client Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/usercred/OAuth_20_Credentials.htm#OAuth_20_Credentials "Use OAuth 2.0 client credential to interact programmatically with services that use the OAuth 2.0 authorization protocol.").
  * SMTP Credentials: For using the [Email Delivery service](https://docs.oracle.com/iaas/Content/Email/Concepts/overview.htm).
  * IAM Database Passwords: Users can create and manage their database password in their IAM user profile and use that password to authenticate to databases in their tenancy. See [Working with IAM Database User Names and Passwords](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#managingcredentials_topic_working_with_iam_db_passwords). 
  * IAM Database User Names: For users to create and manage their own user names for databases, and to create alternate user names as needed. See [Working with IAM Database User Names and Passwords](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#managingcredentials_topic_working_with_iam_db_passwords).


**Important** API signing keys are different from the SSH keys you use to access a compute instance (see[Security Credentials](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/credentials.htm#Security_Credentials)). For more information about API signing keys, see [Required Keys and OCIDs](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm). For more information about instance SSH keys, see [Managing Key Pairs](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingkeypairs.htm).
Was this article helpful?
YesNo


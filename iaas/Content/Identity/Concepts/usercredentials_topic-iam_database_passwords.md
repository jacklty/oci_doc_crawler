Updated 2024-12-18
# IAM Database Passwords
Manage your IAM database passwords overview.
## Overview 🔗 
An IAM database password is a different password than an Console password. Setting an IAM database password allows an authorized IAM user to sign in to one or more Autonomous Databases in their tenancy.
Centralizing user account management in IAM improves security and greatly minimizes database administrators having to manage users who are joining, moving within, and leaving an organization (also known as user lifecycle management). Users can set a database password in IAM and use that password to authenticate when logging in to appropriately configured Oracle databases in their tenancy.
## Easy to use 🔗 
Database end users can continue to use existing supported database clients and tools to access the database. However, instead of using their local database username and password, they use their IAM username and IAM database password. You can access database passwords that you manage through your OCI profile only after you successfully authenticate to OCI. This means administrators can create an extra layer of protection before users can access or manage their database password. They can enforce multifactor authentication on their Console password using, for example, FIDO authenticator, or push notifications through authenticator apps. 
## Supported Functions 🔗 
IAM database passwords support associating a database password directly with an IAM user. After you set a database password in IAM, you can use it to sign in to your IAM database in your tenancy, if you have been authorized to access the IAM database. You must be mapped to a global database schema to be authorized to access the database. See [Authenticating and Authorizing IAM Users for Oracle DBaaS Databases](https://docs.oracle.com/en/database/oracle/oracle-database/23/dbseg/authenticating-and-authorizing-iam-users-oracle-dbaas-databases.html#GUID-466A8800-5AF1-4202-BAFF-5AE727D242E8) in the Oracle Database Security Guide for more information about mapping global database users to IAM users and groups. 
## Password Security 🔗 
IAM administrators can impose extra security access layers by enabling multifactor authorization before a user can access a database password in IAM. See [Authenticating and Authorizing IAM Users for Oracle DBaaS Databases](https://docs.oracle.com/en/database/oracle/oracle-database/23/dbseg/authenticating-and-authorizing-iam-users-oracle-dbaas-databases.html#GUID-466A8800-5AF1-4202-BAFF-5AE727D242E8) in the Oracle Database Security Guide for more information about how IAM users authenticate and authorize to OCI databases. 
Was this article helpful?
YesNo


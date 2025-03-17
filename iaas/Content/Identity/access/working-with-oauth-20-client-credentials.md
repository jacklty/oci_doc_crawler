Updated 2025-01-08
# Working With OAuth 2.0 Client Credentials
OAuth 2.0 client credentials are required to interact programmatically with those services that use the OAuth 2.0 authorization protocol. 
**Note** OAuth 2.0 Client Credentials aren't available in the United Kingdom Government Cloud (OC4). 
The credentials enable you to obtain a secure token to access those service REST API endpoints. The allowed actions and endpoints granted by the token depend on the scopes (permissions) that you select when you generate the credentials. The services that use the OAuth 2.0 protocol are:
  * Oracle Analytics Cloud
  * Oracle Integration


An OAuth 2.0 access token is valid for 3600 seconds (1 hour). 
To create the credentials, you need to know the service resource and scope. Typically, you can select these from a drop-down list. However, if the information isn't available in the list, you can manually enter the resource and scope. The scope defines the allowed permissions for the token, so ensure to set the scope at the minimum required access level.
A user can create the credentials for themselves or an Administrator can create the credentials for another user. The lists of available resources and scopes display only those resources and permission levels that the user has been granted access to.
## OAuth 2.0 Client Credential Limits 🔗 
See [IAM Identity Domain Object Limits](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#iam-object-limits) to see how many OAuth 2.0 client credentials each user in your identity domain type can have.
Each OAuth 2.0 client credential can have up to 10 scopes.
Was this article helpful?
YesNo


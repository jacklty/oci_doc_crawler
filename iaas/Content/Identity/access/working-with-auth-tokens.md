Updated 2024-10-03
# Working with Auth Tokens
Auth tokens are Oracle-generated token strings that you can use to authenticate with third-party APIs that don't support Oracle Cloud Infrastructure's signature-based authentication.
**Note** "Auth tokens" were previously named "Swift passwords". Any Swift passwords you had created are now listed in the Console as auth tokens. You can continue to use the existing passwords.
Each user created in the IAM service automatically can create, update, and delete their own auth tokens in the Console or the API. An administrator doesn't need to create a policy to give a user those abilities. Administrators (or anyone with permission to the tenancy) also can manage auth tokens for other users.
Note that you can't change your auth token to a string of your own choice. The token is always an Oracle-generated string.
Auth tokens don't expire. Each user can have up to two auth tokens at a time. To get an auth token in the Console, see [Creating an Auth Token](https://docs.oracle.com/en-us/iaas/Content/Identity/access/to_create_an_auth_token.htm#create-swift-password "Use the Console to create an auth token."). 
Was this article helpful?
YesNo


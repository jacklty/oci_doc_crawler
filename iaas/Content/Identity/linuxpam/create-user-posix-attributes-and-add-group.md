Updated 2023-05-31
# Creating a User with POSIX Attributes and Add to Group
Create a user with POSIX attributes and add the user to the group previously created.
  1. Create a `user.json` file with the following request body: 
**`user.json` **
```
{
"password": "Securepasswd@1",
"userName": "userPosix",
"Name.givenName": "user",
"Name.familyName": "Posix",
"userType": "Employee",
"emails": [
{
"value": "user.posix@example.com",
"type": "work",
"primary": true
},
{
"value": "posix@example.com",
"type": "home"
}
],
"addresses": [
{
"type": "work",
"primary": true,
"streetAddress": "401 Island Parkway",
"locality": "Redwood Shores",
"region": "California",
"postalCode": "94065",
"country": "US",
"formatted": "userPosix"
}
],
"urn:ietf:params:scim:schemas:oracle:idcs:extension:posix:User": {
"homeDirectory": "/home/userPosix",
"loginShell": "/bin/bash",
"gecos": "userPosix 24855",
"uidNumber": 12001,
"gidNumber": 11010
},
"meta": {
"resourceType": "User"
},
"schemas": [
"urn:ietf:params:scim:schemas:core:2.0:User",
"urn:ietf:params:scim:schemas:oracle:idcs:extension:posix:User"
]
}
```

where:
     * `userName` is set to the username of the user that you want to create
     * `homeDirectory` is set to the location of the user's home directory
     * `loginShell` is set to the default shell
     * `gecos` is set to general information about the user, for example the user's username and phone number
     * `uidNumber` **must** be set to a unique user id (uid) number in Linux. Use the `getent passwd` command on Linux to see existing users and their uid's
     * `gidNumber` **must** be set to the group id (gid) number created previously
  2. Run the following curl command to create the user and add it to the group:
**`user.json` **
```
curl -k -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <token-string>" "https://identity-cloud-service-instance-url/admin/v1/Users" -d '@user.json'
```

where:
     * `token-string` is the OAuth access token that you obtained
     * `identity-cloud-service-instance-url` is your IAM Instance URL
**Note** You can't create a user with POSIX attributes using the Console.
After the user is created, the user will be sent a notification email to activate their account and set a new password. The user must activate their account before testing authentication in Linux.


Was this article helpful?
YesNo


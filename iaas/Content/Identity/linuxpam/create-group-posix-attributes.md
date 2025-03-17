Updated 2023-05-31
# Creating a Group with POSIX Attributes
Create a group with POSIX attributes.
  1. Create a `group.json` file with the following request body:
**`group.json` **
```
{ "schemas":
[ "urn:ietf:params:scim:schemas:core:2.0:Group",
"urn:ietf:params:scim:schemas:oracle:idcs:extension:group:Group",
"urn:ietf:params:scim:schemas:oracle:idcs:extension:posix:Group" ],
"displayName": "posix group",
"urn:ietf:params:scim:schemas:oracle:idcs:extension:group:Group": {
"description": "", "creationMechanism": "idcsui" },
"urn:ietf:params:scim:schemas:oracle:idcs:extension:posix:Group": {
"gidNumber": 11010 },
"members": [] }
```

where:
     * `displayName` is set to the name of the group that you wish to create
     * `gidNumber` must be set to a unique group id (gid) number. Use the `getent group` command on Linux to see the existing group gid's. 
  2. Run the following curl command to create the group:
```
curl -k -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <token-string>" "https://identity-cloud-service-instance-url/admin/v1/Groups" -d '@group.json'
```

where:
     * `token-string` is the OAuth access token that you obtained
     * `identity-cloud-service-instance-url` is your IAM Instance URL
**Note** You can't create a group with POSIX attributes using the Console.


Was this article helpful?
YesNo


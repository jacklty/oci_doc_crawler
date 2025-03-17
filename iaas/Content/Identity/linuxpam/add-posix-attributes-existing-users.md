Updated 2023-05-31
# Adding POSIX Attributes to Existing Users
Add POSIX attributes to existing users.
**Note** In order to add POSIX attributes to an existing user, that user must first be part of a group, and that group must have POSIX attributes.
  1. Create a `user_update.json` file with the following request body:
**`user_update.json` **
```
{
 "schemas": [
  "urn:ietf:params:scim:api:messages:2.0:PatchOp"
 ],
 "Operations": [
  {
   "op": "add",
   "path": "urn:ietf:params:scim:schemas:oracle:idcs:extension:posix:User:homeDirectory",
   "value": "/home/msmith"
  },
  {
   "op": "add",
   "path": "urn:ietf:params:scim:schemas:oracle:idcs:extension:posix:User:gecos",
   "value": "msmith 25895"
  },
  {
   "op": "add",
   "path": "urn:ietf:params:scim:schemas:oracle:idcs:extension:posix:User:uidNumber",
   "value": 12002
  },
  {
   "op": "add",
   "path": "urn:ietf:params:scim:schemas:oracle:idcs:extension:posix:User:gidNumber",
   "value": 11020
  },
  {
   "op": "add",
   "path": "urn:ietf:params:scim:schemas:oracle:idcs:extension:posix:User:loginShell",
   "value": "/bin/bash"
  }
 ]
}
```

where:
     * `homeDirectory` is set to the location of the user's home directory
     * `gecos` is set to general information about the user, for example the user's username and phone number
     * `uidNumber` **must** be set to a unique user id (uid) number in Linux. Use the `getent         passwd` command on Linux to see existing users and their uid's
     * `gidNumber` **must** be set to the group id (gid) number updated previously
     * `loginShell` is set to the default shell
  2. Run the following curl command to retrieve the user id's:
```
curl -k -X GET -H "Content-Type: application/json" -H "Authorization: Bearer <token-string>" "https://identity-cloud-service-instance-url/admin/v1/Users"
```

where:
     * `token-string` is the OAuth access token that you obtained
     * `identity-cloud-service-instance-url` is your IAM Instance URL
In the response, note the `id` of the user you want to update with POSIX attributes. For example, in the response below, the msmith user `id` is `e5438fce80374d539b8638c289036ecd`:
```
....
{
 "idcsCreatedBy": {
    "type": "User",
    "display": "admin example",
    "value": "f142a5ce639643c2befe8deb0ca5bcec",
    "$ref": "https://identity-cloud-service-instance-url/admin/v1/Users/f142a5chjky3c2befe8deb0ca5bcec"
   },
   "id": "e5438fce80374d539b8638c289036ecd",
   "meta": {
    "created": "2019-06-10T13:24:38.184Z",
    "lastModified": "2019-06-10T13:28:50.096Z",
    "resourceType": "User",
    "location": "https://identity-cloud-service-instance-url/admin/v1/Users/e5438fce80374d539b8638c289036ecd"
   },
   "active": true,
   "displayName": "Mark Smith",
...
```

  3. Run the following curl command to update the user:
```
curl -k -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer <token-string>" "https://identity-cloud-service-instance-url/admin/v1/Users/<id>" -d '@user_update.json'
```

where:
     * `token-string` is the OAuth access token that you obtained
     * `identity-cloud-service-instance-url` is your IAM Instance URL
     * `id` is the id for the user that you want to update with POSIX attributes
**Note** You can't update a user with POSIX attributes using the Console.


Was this article helpful?
YesNo


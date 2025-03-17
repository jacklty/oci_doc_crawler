Updated 2023-05-31
# Adding POSIX Attributes to Existing Groups
Add POSIX attributes to existing groups.
  1. Create a `group_update.json` file with the following request body:
**`group_update.json` **
```
{
 "schemas": [
  "urn:ietf:params:scim:api:messages:2.0:PatchOp"
 ],
 "Operations": [
  {
   "op": "add",
   "path": "urn:ietf:params:scim:schemas:oracle:idcs:extension:posix:Group:gidNumber",
   "value": 11020
  }
 ]
}
```

where:
     * `gidNumber` **must** be set to a **unique** group id (gid) number. Use the `getent         group` command on Linux to see the existing group gid's. 
  2. Run the following curl command to retrieve the group id's:
```
curl -k -X GET -H "Content-Type: application/json" -H "Authorization: Bearer <token-string>" "https://identity-cloud-service-instance-url/admin/v1/Groups"
```

where:
     * `token-string` is the OAuth access token that you obtained
     * `identity-cloud-service-instance-url` is your IAM Instance URL
In the response, note the `id` of the group you want to update with POSIX attributes. For example, in the response below, the Marketing group `id` is `8c1f45fee6354e20aa9e57079082d6a2`:
```
.....
	{
   "displayName": "Marketing",
   "idcsLastModifiedBy": {
    "type": "User",
    "value": "f142a5ce639643c2befe8deb0ca5bcec",
    "display": "admin example",
    "$ref": "https://identity-cloud-service-instance-url/admin/v1/Users/f142a5chjky3c2befe8deb0ca5bcec"
   },
   "idcsCreatedBy": {
    "type": "User",
    "display": "admin example",
    "value": "f142a5ce639643c2befe8deb0ca5bcec",
    "$ref": "https://identity-cloud-service-instance-url/admin/v1/Users/f142a5chjky3c2befe8deb0ca5bcec"
   },
   "id": "8c1f45fee6354e20aa9e57079082d6a2",
   "meta": {
    "created": "2019-06-10T13:23:59.451Z",
    "lastModified": "2019-06-10T13:23:59.451Z",
    "resourceType": "Group",
    "location": "https://identity-cloud-service-instance-url/admin/v1/Groups/8c1f45fee6354e20aa9e57079082d6a2"
   },
   "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Group"
   ]
  },
  .....
```

  3. Run the following curl command to update the group:
```
curl -k -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer <token-string>" "https://identity-cloud-service-instance-url/admin/v1/Groups/<id>" -d '@group_update.json'
```

where:
     * `token-string` is the OAuth access token that you obtained
     * `identity-cloud-service-instance-url` is your IAM Instance URL
     * `id` is the id for the group that you want to update with POSIX attributes
**Note** You can't update a group with POSIX attributes using the Console.


Was this article helpful?
YesNo


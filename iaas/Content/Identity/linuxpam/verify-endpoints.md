Updated 2023-05-31
# Verifying Endpoints
Verify that you can view users and groups and their POSIX attributes.
  1. Obtain a POSIX access token by running the following curl command:
```
curl -k -X POST -u "client-id:client-secret" -d "grant_type=client_credentials&scope=urn:opc:idm:__myscopes__" "https://identity-cloud-service-instance-url/oauth2/v1/token"
```

where:
     * `client-id` is the client ID for the POSIX confidential application
     * `client-secret` is the client secret for the POSIX confidential application
     * `identity-cloud-service-instance-url` is your IAM Instance URL
  2. Run the following curl command to view users with POSIX attributes:
```
curl -k -X GET -H "Authorization: Bearer <token-string>" "https://identity-cloud-service-instance-url/admin/v1/Users"
```

where:
     * `token-string` is the OAuth POSIX access token that you obtained
     * `identity-cloud-service-instance-url` is your IAM Instance URL
An example response is as follows:
**`GET HOST/admin/v1/Users` **
```
{
 "schemas": [
  "urn:ietf:params:scim:api:messages:2.0:ListResponse"
 ],
 "totalResults": 3,
 "Resources": [
  {
   "id": "af79f523f0f8416fb4407ed80a3bdbcb",
   "userName": "userPosix",
   "urn:ietf:params:scim:schemas:oracle:idcs:extension:posix:User": {
    "homeDirectory": "/home/userPosix",
    "loginShell": "/bin/bash",
    "gidNumber": 12001,
    "gecos": "userPosix 24855",
    "uidNumber": 11010
   }
  },
  {
   "id": "e5438fce80374d539b8638c289036ecd",
   "userName": "msmith",
   "urn:ietf:params:scim:schemas:oracle:idcs:extension:posix:User": {
    "homeDirectory": "/home/msmith",
    "loginShell": "/bin/bash",
    "gidNumber": 11020,
    "gecos": "msmith 25895",
    "uidNumber": 12002
   }
  },
  {
   "id": "f142a5ce639643c2befe8deb0ca5bcec",
   "userName": "admin@example.com"
  }
 ],
 "startIndex": 1,
 "itemsPerPage": 50
}
```

  3. Run the following curl command to view groups with POSIX attributes:
```
curl -k -X GET -H "Authorization: Bearer <token-string>" "https://identity-cloud-service-instance-url/admin/v1/Groups"
```

where:
     * `token-string` is the OAuth POSIX access token that you obtained
     * `identity-cloud-service-instance-url` is your IAM URL
An example response is as follows:
**`GET HOST/admin/v1/Groups` **
```

{
 "schemas": [
  "urn:ietf:params:scim:api:messages:2.0:ListResponse"
 ],
 "totalResults": 3,
 "Resources": [
  {
   "displayName": "posix group",
   "id": "afb20ea78e84421aaba7009adf212ecf",
   "urn:ietf:params:scim:schemas:oracle:idcs:extension:posix:Group": {
    "gidNumber": 11010
   },
   "members": [
    {
     "value": "af79f523f0f8416fb4407ed80a3bdbcb",
     "type": "User",
     "display": "user Posix",
     "name": "userPosix",
     "$ref": "https://identity-cloud-service-instance-url/admin/v1/Users/af79f523f0f8416fb4407ed80a3bdbcb"
    }
   ]
  },
  {
   "displayName": "Marketing",
   "id": "8c1f45fee6354e20aa9e57079082d6a2",
   "urn:ietf:params:scim:schemas:oracle:idcs:extension:posix:Group": {
    "gidNumber": 11020
   },
   "members": [
    {
     "value": "e5438fce80374d539b8638c289036ecd",
     "type": "User",
     "display": "Mark Smith",
     "name": "msmith",
     "$ref": "https://identity-cloud-service-instance-url/admin/v1/Users/e5438fce80374d539b8638c289036ecd"
    }
   ]
  },
  {
   "displayName": "All Tenant Users",
   "id": "AllUsersId"
  }
 ],
 "startIndex": 1,
 "itemsPerPage": 50
}
```



Was this article helpful?
YesNo


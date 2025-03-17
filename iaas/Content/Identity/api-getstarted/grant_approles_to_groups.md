Updated 2024-04-02
# Granting AppRoles to Groups
Use the following example to create a request that grants application roles to an a group.
```
{
 "app": {
  "value": "<app_id>"
 },
 "entitlement": {
  "attributeName": "appRoles",
  "attributeValue": "<appRoles_id>"
 },
 "grantMechanism": "ADMINISTRATOR_TO_GROUP",
 "grantee": {
  "value": "<grantee_id>",
  "type": "Group"
 },
 "schemas": [
  "urn:ietf:params:scim:schemas:oracle:idcs:Grant"
 ]
}
```

Was this article helpful?
YesNo


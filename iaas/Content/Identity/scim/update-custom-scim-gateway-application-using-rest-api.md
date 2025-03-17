Updated 2025-01-14
# Using REST APIs to Update the Custom SCIM Gateway Application
Use REST APIs to update the `port`, and `sslEnabled` parameters of the custom SCIM gateway application.
  1. To acquire an access token, use a client credential application in an identity domain. If a client credential application hasn't been created in your environment, then add one.
  2. Use the access token as an authorization bearer to run a `GET` request to the following endpoint: `https://domainURL.identity.oraclecloud.com/admin/v1/Apps?filter=displayName co "SCIM Gateway Application"`
The JSON response contains an ID value for this application.
  3. Use the ID value and the access token from the previous steps to run a `PATCH` request to the following endpoint: `https://domainURL.identity.oraclecloud.com/admin/v1/Apps/"ID"`
Replace the ID value with the ID value of your application, set the **Content-type** header to `application/json`, and provide the following content for the body: ```
{
 "schemas": [
  "urn:ietf:params:scim:api:messages:2.0:PatchOp"
 ],
 "Operations": [
   {
   "op": "replace",
   "path": "urn:ietf:params:scim:schemas:oracle:idcs:extension:managedapp:App:bundleConfigurationProperties[name eq \"sslEnabled"].value",
   "value": [ "false"]
  },
   {
   "op": "replace",
   "path": "urn:ietf:params:scim:schemas:oracle:idcs:extension:managedapp:App:bundleConfigurationProperties[name eq \"port\"].value",
   "value": [ "6355"]
  }
 ]
}
```

  4. In the Console, expand the **Navigation Drawer** , select **Applications** , and then select **SCIM Gateway Application**.
  5. In the **Provisioning** pane, select **Test Connectivity** to verify that a connection can be established between IAM and your custom SCIM gateway application.
  6. Select **Finish** , and then select **Activate** to activate the application.


Was this article helpful?
YesNo


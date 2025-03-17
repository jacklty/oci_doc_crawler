Updated 2023-04-25
# Radius Proxy Known Issues
Known issues for working with radius proxy in IAM.
## Changes in the RADIUS Proxy Configuration 🔗 
If any RADIUS Proxy configuration is changed in IAM, restart RADIUS Agent and RADIUS Proxy by completing the following steps so that the new configuration is reflected.
  1. `<radius_proxy_installer_location>/oracle_radius_proxy/radius_agent/scripts/src/radius_agent.py restart`.
  2. Verify if the configuration is updated in: `<radius_proxy_installer_location>/radius_proxy/conf/radius_proxy.conf` or `<radius_proxy_installer_location>/radius_proxy/conf/radius_clients.conf`.
  3. `/sbin/service idcs_radiusd restart`.


## Change an IP Address from CIDR Format 🔗 
You can't add an IP address in CIDR format using the IAM user interface. If the IP address of the Oracle Database is in CIDR format, use the following request from the Postman collection. Go to **RADIUS Proxy** , **RADIUS App** , **Modify** , and then **Update RADIUS App (IP Address in CIDR format)**.
Copy
```
PATCH: {{HOST}}/admin/v1/Apps/{{appid}}
{
 "schemas": [
 "urn:ietf:params:scim:api:messages:2.0:PatchOp"
 ],
 "Operations": [{
 "op": "replace",
 "path": "urn:ietf:params:scim:schemas:oracle:idcs:extension:radiusApp:App:clientIP",
 "value": "10.34.0.0/16"
 }]
}

```

The Postman collection is contained in a single Postman collection file and organized into folders within the collection. Folders are organized based on use cases, use scenarios, and so on, and include variations of API use. Download the collection and environment files from [GitHub](https://docs.oracle.com/en/cloud/paas/identity-cloud/rest-api/api-radius-proxy-radius-proxy-definition.html) and import them into Postman.
Was this article helpful?
YesNo


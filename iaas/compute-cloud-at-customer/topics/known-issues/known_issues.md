Updated 2024-10-11
# Compute Cloud@Customer Known Issues
These known issues have been identified in Compute Cloud@Customer.
  * [After an API key is created or changed, the initial CLI command might fail](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/known-issues/known_issues.htm#api-key-fails)
  * [The oci ccc get infrastructure and oci ccc infrastructure update CLI commands return null for the provisioning_pin value](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/known-issues/known_issues.htm#ccc-get-update-return-null-pin)
  * [When using the ccc infrastructure list CLI command with the --compartment-id-in-subtree true option, no results are returned](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/known-issues/known_issues.htm#ccc-infrastructure-list-no-results)
  * [Output from oci iam user get doesn't list user capabilities](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/known-issues/known_issues.htm#output-from-oci-iam-user-get-differs)


## After an API key is created or changed, the initial CLI command might fail 🔗  

Details
    
When an API key is added or changed for a user, the first CLI command with the new or changed key might fail. 

Workaround
    Wait a few minutes for the new key to synchronize on the Compute Cloud@Customer infrastructure, then retry the CLI command.
## The oci ccc get infrastructure and oci ccc infrastructure update CLI commands return null for the provisioning_pin value 🔗  

Details
    
When you create an infrastructure, a PIN is generated and displayed in the output. 
However, if you use the `oci ccc get infrastructure` command right after creating or updating the infrastructure, the PIN might not be returned.
This happens because the PIN isn't available to the `get` command for up to 5 minutes after creation.
Example output:
```
{
 "compartment_id": "ocid1.compartment.oc1..uniqueID",
. . .
 },
 "display_name": "C3ResourcePrincipal_infra",
 "freeform_tags": {},
 "id": "ocid1.cccinfrastructure.uniqueID",
 "lifecycle_details": null,
 "lifecycle_state": "ACTIVE",
 "provisioning_fingerprint": null,
 "provisioning_pin": null,
 "rack_inventory": {
  "capacity_storage_tray_count": null,
  "compute_node_count": null,
  "management_node_count": null,
  "performance_storage_tray_count": null,
  "serial_number": null
. . .
}
```


Workaround
    
Obtain the PIN from the `create` command, or wait 5 minutes to retrieve the PIN using the `get` command.
For more information, see the [ccc infrastructure](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ccc/infrastructure.html) CLI Reference page.
## When using the ccc infrastructure list CLI command with the --compartment-id-in-subtree true option, no results are returned 🔗  

Details
    
You get an empty list even though there are items in the subtree.
Example:
```
oci ccc infrastructure list --profile user1 --compartment-id-in-subtree true -c ocid1.tenancy.oc1..uniqueID
{
 "data": {
  "items": []
 }
}
```


Workaround
    
Instead of using the `--compartment-id-in-subtree` option, query each compartment directly using the `-compartment` option.
Example:
```
oci ccc infrastructure list --profile user1 -compartment ocid1.tenancy.oc1..uniqueID
{
 "data": {
  "items": [ list of compartment details ]
 }
}
```

For more information, see the [ccc infrastructure](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ccc/infrastructure.html) CLI Reference page.
## Output from `oci iam user get` doesn't list user capabilities 🔗  

Details
    
The output from `oci iam user get` differs between Oracle Cloud Infrastructure (OCI) and Compute Cloud@Customer. The Compute Cloud@Customer output shows `null` for `capabilites` and omits the list of capabilities, as shown in the following table.
OCI Output | Compute Cloud@Customer Output  
---|---  
```
oci iam user get --user-id ocid1.user.oc1..uniqueID
{
"data": {
"capabilities": {
"can-use-api-keys": true,
"can-use-auth-tokens": true,
"can-use-console-password": true,
"can-use-customer-secret-keys": true,
"can-use-o-auth2-client-credentials": true,
"can-use-smtp-credentials": true
},
"compartment-id":
"ocid1.tenancy.oc1..uniqueID",
"defined-tags": {
"Oracle-Recommended-Tags": {
"ResourceType": "group",
"UtilExempt": "minrequired"
}
},
"description": "user-1",
"email": null,
"email-verified": false,
"external-identifier": null,
"freeform-tags": {},
"id":
"ocid1.user.oc1..uniqueID"
,
"identity-provider-id": null,
"inactive-status": null,
"is-mfa-activated": false,
"last-successful-login-time": "2024-02-08T10:25:44.036000+00:00",
"lifecycle-state": "ACTIVE",
"name": "user-1",
"previous-successful-login-time": null,
"time-created": "2024-02-08T09:12:35.256000+00:00"
},
"etag": "60f0527b3bbd0f40f137d4149d131fbf77eb44ab"
}
```
|  ```
oci iam user get --user-id
ocid1.user.oc1..uniqueID
{
"data": {
"capabilities": null,
"compartment-id":
"ocid1.tenancy.oc1..uniqueID",
"defined-tags": {
"Oracle-Recommended-Tags": {
"ResourceType": "group",
"UtilExempt": "minrequired"
}
},
"description": "user-1",
"email": null,
"email-verified": null,
"external-identifier": null,
"freeform-tags": {},
"id":
"ocid1.user.oc1..uniqueID"
,
"identity-provider-id": null,
"inactive-status": null,
"is-mfa-activated": null,
"last-successful-login-time": null,
"lifecycle-state": "ACTIVE",
"name": "user-1",
"previous-successful-login-time": null,
"time-created": "2023-02-08T09:12:35.256000+00:00"
},
"etag": "bee44237-6d70-4691-b7f9-a98fbb332b12"

```


Workaround
    To see the list of capabilities, run the `oci iam user get` command in your OCI tenancy.  
Was this article helpful?
YesNo


Updated 2024-02-13
# Identity Cloud Service instances to IAM Known Issues
Known issues for the migration of Identity Cloud Service instances to OCI IAM.
## Unexpected Attribute Values After Conversion 🔗 
After Identity Cloud Service instances have been converted to identity domains in OCI IAM, you might find some attributes for some objects in the default identity domain have an unexpected result. You won't see anything different in the console, but if you are using scripts and APIs these changes might affect the results.
The attributes affected are:
  * `meta.lastModified`
  * `meta.version` (etag)
  * `idcsLastModifiedBy`


The changes apply to the following objects when they have been updated within approximately 3 weeks before the instances were converted:
  * Users
  * Groups
  * Applications
  * Some credentials (MFA TOTP)
  * User password `createdOn`


Here are details of the attribute changes.
When resource is first created as part of migration:
  * `meta.lastModified`, `meta.created` is set to the original date time when the resource is created in IAM.
  * `meta.version` (etag) is the original etag set when resource was created in IAM.
  * `idcsLastModifiedBy`, `idcsCreatedBy` is set to the original principal that created the resource in IAM.


If the resource is updated before migration completes:
  * `meta.lastModified` is set to the date time when the resource is updated in Identity Cloud Service.
  * `meta.version` (etag) is set based on the date time when resource is updated in Identity Cloud Service.
  * `idcsLastModifiedBy` is set to the Identity Service Principal who updated the resource in Identity Cloud Service.


You don't need to do anything. These attributes are set correctly the next time the object is modified.
## User in One Stripe Can See Audit Data For Other Stripes 🔗 
In Identity Cloud Service instances, a user in one stripe who is authorized to see AuditEvents can only see them from that stripe. Migration to OCI IAM creates a domain resource for each stripe in the default compartment of the corresponding OCI tenancy, and because authorization to see AuditEvents is based on compartments, the user can see AuditEvents from every stripe in the same compartment.
You can preserve the behaviour that a user in one stripe can only see AuditEvents in that stripe by creating a compartment for each stripe, then moving the domain resource that represents the stripe into its own compartment.
The [OCI tenancy administrator](https://docs.oracle.com/en-us/iaas/Content/Identity/conversion/security.htm#oci_admin_group) has the appropriate visibility and rights to see all the identity domain resources to do this.
  * Moving a domain resource into a compartment moves all users in that domain into that new compartment and implicitly gives them access to resources in that compartment.
  * Moving a domain resource into a compartment also makes all auditable events that domain emits into OCI Audit V2 specific to that compartment.
  * Only a user with access to that compartment can see the auditable events emitted by a domain in that compartment.


Was this article helpful?
YesNo


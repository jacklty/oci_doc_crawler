Updated 2025-01-14
# Details for the Certificates Service
Learn the details about permissions for the Certificates service so you can write policies to control access to its resources.
This topic covers Certificates service details about resource-types you can grant permissions to, special variables you can use when adding conditions to a policy, the hierarchy of permissions and API operations covered by each verb for each resource-type, and the permissions for each API operation.
## Individual Resource-Types 🔗 
Individual resource-types let you write policy statements scoped to a specific resource-type and no others.
`leaf-certificates`
`leaf-certificate-versions`
`leaf-certificate-bundles`
`certificate-authorities`
`certificate-authority-versions`
`certificate-authority-bundles`
`certificate-authority-delegates`
`cabundles`
`certificate-associations`
`certificate-authority-associations`
`cabundle-associations`
## Aggregate Resource-Types 🔗 
Aggregate resource-types let you write policy statements with a scope that extends beyond an individual resource-type to all resource-types covered by the aggregate resource-type.
`leaf-certificate-family`
`certificate-authority-family`
A policy that uses `<verb> leaf-certificate-family` is equivalent to writing one with a separate `<verb> <individual         resource-type>` statement for each of the following individual certificate resource-types: `leaf-certificates`, `leaf-certificate-versions`, `leaf-certificate-bundles`, `cabundles`, `certificate-associations`, and `cabundle-associations`.
A policy that uses `<verb> certificate-authority-family` is equivalent to writing one with a separate `<verb> <individual         resource-type>` statement for each of the following individual certificate authority (CA) and certificate resource-types: `certificate-authorities`, `certificate-authority-versions`, `certificate-authority-bundles`, `certificate-authority-delegates`, `leaf-certificates`, `leaf-certificate-versions`, `leaf-certificate-bundles`, `cabundles`, `certificate-associations`, `certificate-authority-associations`, and `cabundle-associations`.
See the table in [Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/keypolicyreference.htm#Details) for details of the API operations covered by each verb, for each individual resource-type included in `leaf-certificate-family` and `certificate-authority-family`.
## Supported Variables 🔗 
Certificates supports all the general variables, plus the ones listed here. For more information about general variables supported by Oracle Cloud Infrastructure services, see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General).
Operations for This Resource-Type... | Can Use These Variables... | Variable Type | Comments  
---|---|---|---  
certificate-authorities | `target.certificate-authority.id` | Entity (OCID) | Use this variable to control access to a certificate authority (CA) based on the OCID of the CA. (You cannot use this variable when creating a CA, as the CA does not exist to have an OCID yet.)  
`target.certificate-authority.name` | String | Use this variable to limit access to a specific CA name.  
`target.certificate-authority.subject` | String | Use this variable to control access to a CA based on the CA subject.  
`target.certificate-authority.type` | String | Use this variable to limit access to CAs of a certain type. CA types include `ROOT_CA` and `SUBORDINATE_CA`.  
`target.issuer-certificate-authority.id` | String | Use this variable to limit access to CAs based on the OCID of the issuer CA.  
certificate-authority-versions | `target.certificate-authority.id` | Entity (OCID) | Use this variable to control access to a CA version based on the OCID of its CA.  
`target.certificate-authority.name` | String | Use this variable to control access to a CA version based on the name of the CA.  
certificate-authority-bundles | `target.certificate-authority.id` | Entity (OCID) | Use this variable to control access to the bundle of a CA based on the OCID of the bundle's CA.  
`target.certificate-authority.name` | String | Use this variable to control access to the bundle of a CA by the name of the bundle's CA.  
certificate-authority-associations | `target.association.id` | Entity (OCID) | Use this variable to control access to a CA association based on the OCID of the association. (You cannot use this variable when creating a CA association, as the association does not exist to have an OCID yet.)  
`target.association.name` | String | Use this variable to control access to a CA association based on the name of the association.  
`target.association.resourceid` | Entity (OCID) | Use this variable to control access to a CA association based on the OCID of the resource configured in the association.  
`target.leaf-certificate.id` | Entity (OCID) | Use this variable to control access to a CA association based on the OCID of the certificate configured in the association.  
`target.leaf-certificate.name` | String | Use this variable to control access to a CA association based on the name of the certificate configured in the association.  
certificate-authority-delegates | `target.certificate-authority.id` | Entity (OCID) | Use this variable to control access to a CA delegate based on the OCID of the CA.  
`target.certificate-authority.name` | String | Use this variable to control access to a CA delegate based on the name of the CA.  
`target.issuer-certificate-authority.id` | String | Use this variable to control access to a CA delegate based on the OCID of the issuer CA.  
`target.resource.type` | String | Use this variable to control access to CA delegates based on the type of resource the delegate is, whether the resource is a `leaf-certificate`, `certificate-authority`, or `cabundle`.  
leaf-certificates | `target.leaf-certificate.allow-wildcard` | String | Use this variable to control access to a certificate based on whether the certificate common name or subject alternate name includes a wildcard.  
`target.leaf-certificate.alt-subject` | List | Use this variable to control access to a certificate based on the certificate subject alternate name.  
`target.leaf-certificate.alt-subject-size` | String | Use this variable to control access to a certificate based on the number of certificate subject alternate names.  
`target.leaf-certificate.id` | Entity (OCID) | Use this variable to control access to a certificate based on the certificate OCID. (You cannot use this variable when creating a certificate, as the certificate does not exist to have an OCID yet.)  
`target.leaf-certificate.name` | String | Use this variable to control access to a certificate based on the certificate name.  
`target.issuer-certificate-authority.id` | String | Use this variable to control access to a certificate based on the OCID of the issuer CA.  
`target.leaf-certificate.profile-type` | String | Use this variable to control access to certificates based on the certificate profile type. Certificate profile types include `TLS_SERVER_OR_CLIENT`, `TLS_SERVER`, `TLS_CLIENT`, and `TLS_CODE_SIGN`.  
`target.leaf-certificate.subject` | String | Use this variable to control access to certificates based on the certificate subject.  
`target.leaf-certificate.type` | String | Use this variable to control access to certificates based on the manner in which the certificate was created. Certificate configuration types include `MANAGED_EXTERNALLY_ISSUED_BY_INTERNAL_CA`, `ISSUED_BY_INTERNAL_CA`, or `IMPORTED`.  
leaf-certificate-versions | `target.leaf-certificate.id` | Entity (OCID) | Use this variable to control access to certificate versions based on the OCID of the certificate. Use this variable to control whether block volumes or buckets can be created without a Vault master encryption key.  
`target.leaf-certificate.name` | String | Use this variable to control access to certificate versions based on the name of the certificate.  
leaf-certificate-bundles | `target.leaf-certificate.id` | Entity (OCID) | Use this variable to control access to certificate bundles based on the OCID of the certificate.  
`target.leaf-certificate.name` | String | Use this variable to control access to certificate bundles based on the name of the certificate.  
`target.leaf-certificate.bundle-type` | String | Use this variable to control access to a certificate bundle based on the certificate bundle type. Certificate bundle types include `CERTIFICATE_CONTENT_PUBLIC_ONLY` and `CERTIFICATE_CONTENT_WITH_PRIVATE_KEY`.  
certificate-associations | `target.association.id` | Entity (OCID) | Use this variable to control access to certificate associations based on the OCID of the association. (You cannot use this variable when creating a certificate association, as the association does not exist to have an OCID yet.)  
`target.association.name` | String | Use this variable to control access to certificate bundles based on the name of the certificate bundle association.  
`target.association.resourceid` | Entity (OCID) | Use this variable to control access to certificate bundles based on the OCID of the resource targeted in the certificate bundle association.  
`target.leaf-certificate.id` | Entity (OCID) | Use this variable to control access to certificate associations based on the OCID of the certificate.  
`target.leaf-certificate.name` | String | Use this variable to control access to certificate associations based on the name of the certificate.  
cabundles | `target.cabundle.id` | Entity (OCID) | Use this variable to control access to CA bundles based on the OCID of the CA bundle. (You cannot use this variable when creating a CA bundle, as the CA bundle does not exist to have an OCID yet.)  
`target.cabundle.name` | String | Use this variable to control access to CA bundles based on the name of the CA bundle.  
cabundle-associations | `target.association.id` | Entity (OCID) | Use this variable to control access to a CA bundle association based on the OCID of the bundle association.  
`target.association.name` | String | Use this variable to control access to a CA bundle association based on the name of the bundle association (You cannot use this variable when creating a CA bundle association, as the association does not exist to have an OCID yet.).  
`target.association.resourceid` | Entity (OCID) | Use this variable to control access to a CA bundle association based on the OCID of the resource configured in the association.  
`target.cabundle.id` | Entity (OCID) | Use this variable to control access to a CA bundle association based on the OCID of the bundle.  
`target.cabundle.name` | String | Use this variable to control access to a CA bundle association based on the name of the bundle.  
## Details for Verb + Resource-Type Combinations 🔗 
Understand the incremental access granted by each verb for each resource-type so you can write policies that grant only the access required and nothing more.
The following tables show the [permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.
For example, the `use` verb for the `cabundles` resource-type includes the same permissions and API operations as the `read` verb, plus the CABUNDLE_UPDATE permission and the `UpdateCaBundle` API operation. The `manage` verb allows even more permissions and API operations when compared to the `use` verb.
[leaf-certificates](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/certificatespolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  CERTIFICATE_INSPECT | `ListCertificates` |  none  
read |  INSPECT + CERTIFICATE_READ |  INSPECT + `GetCertificate` |  none  
use |  READ + CERTIFICATE_UPDATE | no extra |  `RevokeCertificateVersion` (also needs `manage                   leaf-certificate-versions` and `use                   certificate-authority-delegates`, as well as permission to `update buckets` on the bucket associated with the certificate version and `use certificate-authorities` permissions for the issuer CA) `CancelCertificateVersionDeletion` (also needs permission to `delete leaf-certificate-versions`) `ScheduleCertificateVersionDeletion` (also needs permission to `delete leaf-certificate-versions`) `UpdateCertificate` (also needs `use                   certificate-authority-delegates` permissions, except with imported certificates, as well as permission to `update                   buckets` on the bucket associated with the certificate version, permission to `use` the issuer certificate authority, and permission to `use keys`)  
manage |  USE + CERTIFICATE_CREATE CERTIFICATE_DELETE CERTIFICATE_MOVE |  USE + `CancelCertificateDeletion` `ScheduleCertificateDeletion` `ChangeCertificateCompartment` |  `CreateCertificate` (also needs `use                   certificate-authority-delegates` permissions, except when importing a certificate, as well as permission to `update buckets` on the bucket associated with the certificate version, permission to `use keys`, and `use certificate-authorities` permissions for the issuer CA, except when importing a certificate)  
[leaf-certificate-versions](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/certificatespolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  CERTIFICATE_VERSION_INSPECT | `ListCertificateVersions` |  none  
read |  INSPECT + CERTIFICATE_VERSION_READ |  INSPECT + `GetCertificateVersion` |  none  
use |  READ + no extra |  none |  none  
manage |  USE + CERTIFICATE_VERSION_REVOKE CERTIFICATE_VERSION_DELETE |  none |  `RevokeCertificateVersion` (also needs `use                   leaf-certificates` and `use                   certificate-authority-delegates`) `CancelCertificateVersionDeletion` (also needs `use leaf-certificates`) `ScheduleCertificateVersionDeletion` (also needs `use leaf-certificates`)  
[certificate-authorities](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/certificatespolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  CERTIFICATE_AUTHORITY_INSPECT | `ListCertificateAuthorities` |  none  
read |  INSPECT + CERTIFICATE_AUTHORITY_READ |  INSPECT + `GetCertificateAuthority` |  none  
use |  READ + CERTIFICATE_AUTHORITY_UPDATE |  no extra |  `UpdateCertificateAuthority` (also needs `use                   certificate-authority-delegates`)  
manage |  USE + CERTIFICATE_AUTHORITY_CREATE CERTIFICATE_AUTHORITY_DELETE CERTIFICATE_AUTHORITY_MOVE |  USE + `CancelCertificateAuthorityDeletion` `ScheduleCertificateAuthorityDeletion` `ChangeCertificateAuthorityCompartment` |  `CreateCertificateAuthority` (also needs `use                   certificate-authority-delegates`)  
[certificate-authority-versions](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/certificatespolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  CERTIFICATE_AUTHORITY_VERSION_INSPECT | `ListCertificateAuthorityVersions` |  none  
read |  INSPECT + CERTIFICATE_AUTHORITY_VERSION_READ |  INSPECT + `GetCertificateAuthorityVersion` |  none  
use |  READ + no extra |  none |  none  
manage |  USE + CERTIFICATE_AUTHORITY_VERSION_DELETE CERTIFICATE_AUTHORITY_VERSION_REVOKE |  none |  `CancelCertificateAuthorityVersionDeletion` (also needs `use certificate-authorities`) `ScheduleCertificateAuthorityVersionDeletion` (also needs `use certificate-authorities`) `RevokeCertificateAuthorityVersion` (also needs `use certificate-authorities`)  
[leaf-certificate-bundles](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/certificatespolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  CERTIFICATE_BUNDLE_INSPECT | `ListCertificateBundleVersions` |  none  
read |  INSPECT + CERTIFICATE_BUNDLE_READ |  INSPECT + `GetCertificateBundle` **Note:** The permission required for this operation depends on the query parameter `certificateBundleType`. If `certificateBundleType` is set to `CERTIFICATE_CONTENT_PUBLIC_ONLY`, then any users with the permission CERTIFICATE_BUNDLE_READ will be able to perform this operation. If `certificateBundleType` is set to CERTIFICATE_CONTENT_WITH_PRIVATE_KEY, then you need a policy statement for the group that includes the variable `target.leaf-certificate.bundle-type` set to CERTIFICATE_CONTENT_WITH_PRIVATE_KEY. |  none  
use |  READ + no extra |  none |  none  
manage |  USE+ no extra |  none |  `CancelCertificateAuthorityVersionDeletion` (also needs `use certificate-authorities`) `ScheduleCertificateAuthorityVersionDeletion` (also needs `use certificate-authorities`) `RevokeCertificateAuthorityVersion` (also needs `use certificate-authorities`)  
[certificate-authority-bundles](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/certificatespolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  CERTIFICATE_AUTHORITY_BUNDLE_INSPECT | `ListCertificateAuthorityBundleVersions` |  none  
read |  INSPECT + CERTIFICATE_AUTHORITY_BUNDLE_READ |  INSPECT + `GetCertificateAuthorityBundle` |  none  
use |  READ + no extra | none |  none  
manage |  USE + no extra |  none |  none  
[cabundles](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/certificatespolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  CABUNDLE_INSPECT | `ListCaBundles` |  none  
read |  INSPECT + CABUNDLE_READ |  INSPECT + `GetCaBundle` |  none  
use |  READ + CABUNDLE_UPDATE | READ+`UpdateCaBundle` |  none  
manage |  USE + CABUNDLE_CREATE CABUNDLE_DELETE CABUNDLE_MOVE |  USE + `CreateCaBundle` `DeleteCaBundle` `ChangeCaBundleCompartment` |  none  
[certificate-authority-delegates](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/certificatespolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  none |  none |  none  
read |  no extra |  none |  none  
use |  READ + CERTIFICATE_AUTHORITY_APPLY | none |  UpdateCertificateAuthority (also needs `use                   certificate-authorities`)  
manage |  USE + no extra |  none |  none  
[certificate-associations](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/certificatespolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  CERTIFICATE_ASSOCIATION_INSPECT | `ListAssociations` |  none  
read |  INSPECT + CERTIFICATE_ASSOCIATION_READ |  INSPECT + `GetAssociation` |  none  
use |  READ + no extra |  none |  none  
manage |  USE + CERTIFICATE_ASSOCIATION_CREATE CERTIFICATE_ASSOCIATION_DELETE |  USE + `CreateAssociation` `DeleteAssociation` |  none  
[certificate-authority-associations](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/certificatespolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  CERTIFICATE_AUTHORITY_ASSOCIATION_INSPECT | `ListAssociations` |  none  
read |  INSPECT + CERTIFICATE_AUTHORITY_ASSOCIATION_READ |  INSPECT + `GetAssociation` |  none  
use |  READ + no extra | none |  none  
manage |  USE + CERTIFICATE_AUTHORITY_ASSOCIATION_CREATE CERTIFICATE_AUTHORITY_ASSOCIATION_DELETE |  USE + `CreateAssociation` `DeleteAssociation` |  none  
[cabundle-associations](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/certificatespolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  CABUNDLE_ASSOCIATION_INSPECT | `ListAssociations` |  none  
read |  INSPECT + CABUNDLE_ASSOCIATION_READ |  INSPECT + `GetAssociation` |  none  
use |  READ + no extra |  none |  none  
manage |  USE + CABUNDLE_ASSOCIATION_CREATE CABUNDLE_ASSOCIATION_DELETE |  USE + `CreateAssociation` `DeleteAssociation` |  none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).
API Operation | Permissions Required to Use the Operation  
---|---  
`ListCertificateAuthorities` | CERTIFICATE_AUTHORITY_INSPECT  
`GetCertificateAuthority` | CERTIFICATE_AUTHORITY_READ  
`CreateCertificateAuthority` | CERTIFICATE_AUTHORITY_CREATE and CERTIFICATE_AUTHORITY_APPLY  
`UpdateCertificateAuthority` | CERTIFICATE_AUTHORITY_UPDATE and CERTIFICATE_AUTHORITY_APPLY  
`ChangeCertificateAuthorityCompartment` | CERTIFICATE_AUTHORITY_MOVE  
`ScheduleCertificateAuthorityDeletion` | CERTIFICATE_AUTHORITY_DELETE  
`CancelCertificateAuthorityDeletion` | CERTIFICATE_AUTHORITY_DELETE  
`ListCertificateAuthorityVersions` | CERTIFICATE_AUTHORITY_VERSION_INSPECT  
`GetCertificateAuthorityVersion` | CERTIFICATE_AUTHORITY_VERSION_READ  
`RevokeCertificateAuthorityVersion` | CERTIFICATE_AUTHORITY_VERSION_REVOKE, CERTIFICATE_AUTHORITY_UPDATE, and CERTIFICATE_AUTHORITY_APPLY  
`ScheduleCertificateAuthorityVersionDeletion` | CERTIFICATE_AUTHORITY_VERSION_DELETE and CERTIFICATE_AUTHORITY_UPDATE  
`CancelCertificateAuthorityVersionDeletion` | CERTIFICATE_AUTHORITY_VERSION_DELETE and CERTIFICATE_AUTHORITY_UPDATE  
`ListCertificateAuthorityBundleVersions` | CERTIFICATE_AUTHORITY_BUNDLE_INSPECT  
`GetCertificateAuthorityBundle` | CERTIFICATE_AUTHORITY_BUNDLE_READ  
`ListCertificates` | CERTIFICATE_INSPECT  
`GetCertificate` | CERTIFICATE_READ  
`CreateCertificate` | CERTIFICATE_CREATE and CERTIFICATE_AUTHORITY_APPLY  
`UpdateCertificate` | CERTIFICATE_UPDATE and CERTIFICATE_AUTHORITY_APPLY  
`ChangeCertificateCompartment` | CERTIFICATE_MOVE  
`ScheduleCertificateDeletion` | CERTIFICATE_DELETE  
`CancelCertificateDeletion` | CERTIFICATE_DELETE  
`ListCertificateVersions` | CERTIFICATE_VERSION_INSPECT  
`GetCertificateVersion` | CERTIFICATE_VERSION_READ  
`RevokeCertificateVersion` | CERTIFICATE_VERSION_REVOKE, CERTIFICATE_UPDATE, and CERTIFICATE_AUTHORITY_APPLY  
`ScheduleCertificateVersionDeletion` | CERTIFICATE_VERSION_DELETE and CERTIFICATE_UPDATE  
`CancelCertificateVersionDeletion` | CERTIFICATE_VERSION_DELETE and CERTIFICATE_UPDATE  
`ListCertificateBundleVersions` | CERTIFICATE_BUNDLE_INSPECT  
`GetCertificateBundle` | CERTIFICATE_BUNDLE_READFor details, see [leaf-certificate-bundles](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/certificatespolicyreference.htm#leaf_certificate_bundles).  
`ListCaBundles` | CABUNDLE_INSPECT  
`GetCaBundle` | CABUNDLE_READ  
`CreateCaBundle` | CABUNDLE_CREATE  
`UpdateCaBundle` | CABUNDLE_UPDATE  
`ChangeCaBundleCompartment` | CABUNDLE_MOVE  
`DeleteCaBundle` | CABUNDLE_DELETE  
`ListAssociations` | CERTIFICATE_AUTHORITY_ASSOCIATION_INSPECT (for certificate-authorities), CERTIFICATE_ASSOCIATION_INSPECT (for leaf-certificates), or CABUNDLE_ASSOCIATION_INSPECT (for cabundles)  
`GetAssociation` | CERTIFICATE_AUTHORITY_ASSOCIATION_READ (for certificate-authorities), CERTIFICATE_ASSOCIATION_READ (for leaf-certificates), or CABUNDLE_ASSOCIATION_READ (for cabundles)  
`DeleteAssociation` | CERTIFICATE_AUTHORITY_ASSOCIATION_DELETE (for certificate-authorities), CERTIFICATE_ASSOCIATION_DELETE (for leaf-certificates), or CABUNDLE_ASSOCIATION_DELETE (for cabundles)  
Was this article helpful?
YesNo


Updated 2025-02-20
# Details for the Vault Service
This topic covers details for writing policies to control access to the Vault service.
## Individual Resource-Types 🔗 
`vaults`
`keys`
`key-delegate`
`secrets`
`secret-versions`
`secret-bundles`
## Supported Variables 🔗 
Vault supports all the general variables, plus the ones listed here. For more information about general variables supported by Oracle Cloud Infrastructure services, see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General).
Variable | Variable Type | Comments  
---|---|---  
`request.includePlainTextKey` | String | Use this variable to control whether to return the plaintext key, in addition to the encrypted key, in response to a request to generate a data encryption key.  
`request.kms-key.id` | String | Use this variable to control whether block volumes or buckets can be created without a Vault master encryption key.  
`target.boot-volume.kms-key.id` | String | Use this variable to control whether Compute instances can be launched with boot volumes that were created without a Vault master encryption key.  
`target.key.id` | Entity (OCID) | Use this variable to control access to specific keys by OCID.  
`target.vault.id` | Entity (OCID) | Use this variable to control access to specific vaults by OCID.  
`target.secret.name` | String | Use this variable to control access to specific secrets, secret versions, and secret bundles by name.  
`target.secret.id` | Entity (OCID) | Use this variable to control access to specific secrets, secret versions, and secret bundles by OCID.  
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
For example, the `use` verb for the `keys` resource-type includes the same permissions and API operations as the `read` verb, plus the KEY_ENCRYPT and KEY_DECRYPT permissions and a number of API operations (`Encrypt`, `Decrypt`, and `GenerateDataEncryptionKey`). The `manage` verb allows even more permissions and API operations when compared to the `use` verb.
[vaults](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/keypolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | VAULT_INSPECT | `ListVaults` | none  
read | INSPECT + VAULT_READ | INSPECT + `GetVault` | none  
use | READ + VAULT_CREATE_KEY VAULT_IMPORT_KEY VAULT_CREATE_SECRET | no extra | `CreateKey` (also needs `manage keys`) `ImportKey` (also needs `manage keys`) `CreateSecret` (also needs `manage secrets`)  
manage | USE + VAULT_CREATE VAULT_UPDATE VAULT_DELETE VAULT_MOVE VAULT_BACKUP VAULT_RESTORE VAULT_REPLICATE | USE + `CreateVault` `UpdateVault` `ScheduleVaultDeletion` `CancelVaultDeletion` `ChangeVaultCompartment` `BackupVault` `RestoreVaultFromFile` `RestoreVaultFromObjectStore` `CreateVaultReplica` `DeleteVaultReplica` | none  
[keys](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/keypolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | KEY_INSPECT | `ListKeys` `ListKeyVersions` | none  
read | INSPECT + KEY_READ | INSPECT + `GetKey` `GetKeyVersion` | none  
use | READ + KEY_ENCRYPT KEY_DECRYPT KEY_EXPORT KEY_SIGN KEY_VERIFY | READ + `Encrypt` `Decrypt` `ExportKey` `Sign` `Verify` | none  
manage | USE + KEY_CREATE KEY_UPDATE KEY_ROTATE KEY_DELETE KEY_MOVE KEY_IMPORT KEY_BACKUP KEY_RESTORE | USE + `CreateKey` `UpdateKey` `CreateKeyVersion` `CancelKeyDeletion` `ChangeKeyCompartment` `ImportKeyVersion` `BackupKey` `RestoreKeyFromFile` `RestoreKeyFromObjectStore` | `CreateKey` (also needs `use vaults`) `ImportKey` (also needs `use vaults`)  
[key-delegate](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/keypolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
use | KEY_ASSOCIATE KEY_DISASSOCIATE | `Encrypt` `GenerateDataEncryptionKey` `Decrypt` | none  
[hsm-cluster](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/keypolicyreference.htm)
Verbs | Permissions | API Fully Covered | API Partially Covered  
---|---|---|---  
Inspect |  HSM_CLUSTER_INSPECT |  ListHsmClusters ListHsmPartitions |  None  
read |  HSM_CLUSTER_READ |  GetHsmCluster GetHsmPartition |  None  
use |  HSM_CLUSTER_UPDATE |  GetPreCoUserCredentials DownloadCertificateSigningRequest UpdateHsmCluster UploadPartitionCertificates |  None  
manage |  HSM_CLUSTER_DELETE HSM_CLUSTER_CREATE HSM_CLUSTER_MOVE |  CreateHsmCluster ChangeHsmClusterCompartment ScheduleHsmClusterDeletion CancelHsmClusterDeletion |  None  
[secrets](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/keypolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | SECRET_INSPECT | `ListSecrets` | none  
read | INSPECT + SECRET_READ | INSPECT + `GetSecret` | none  
use | READ + SECRET_UPDATE | READ + `UpdateSecret` | READ + `ChangeSecretCompartment` (also needs `manage secrets)` `ScheduleSecretVersionDeletion` (also needs `manage secret-versions`) `CancelSecretVersionDeletion` (also needs `manage secret-versions`)  
manage | USE + SECRET_CREATE SECRET_DELETE SECRET_MOVE | USE + `ScheduleSecretDeletion` `CancelSecretDeletion` | USE + `CreateSecret` (also needs `use vaults`) `ChangeSecretCompartment` (also needs `use secrets`)  
[secret-versions](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/keypolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | SECRET_VERSION_INSPECT | `ListSecretVersions` | none  
read | INSPECT + SECRET_VERSION_READ | INSPECT + `GetKeyVersion` | none  
manage | READ + SECRET_VERSION_DELETE | no extra | `ScheduleSecretVersionDeletion` (also needs `use secrets`) `CancelSecretVersionDeletion` (also needs `use secrets`)  
[secret-bundles](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/keypolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | SECRET_BUNDLE_INSPECT | `ListSecretBundles` | none  
read | INSPECT + SECRET_BUNDLE_READ | INSPECT + `GetSecretBundle` | none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).
API Operation | Permissions Required to Use the Operation  
---|---  
`ListVaults` | VAULT_INSPECT  
`GetVault` | VAULT_READ  
`CreateVault` | VAULT_CREATE  
`UpdateVault` | VAULT_UPDATE  
`ScheduleVaultDeletion` | VAULT_DELETE  
`CancelVaultDeletion` | VAULT_DELETE  
`ChangeVaultCompartment` | VAULT_MOVE  
`BackupVault` | VAULT_BACKUP  
`RestoreVaultFromFile` | VAULT_RESTORE  
`RestoreVaultFromObjectStore` | VAULT_RESTORE  
`ListVaultReplicas` | VAULT_INSPECT  
`CreateVaultReplica` | VAULT_REPLICATE  
`DeleteVaultReplica` | VAULT_REPLICATE  
`ListKeys` | KEY_INSPECT  
`ListKeyVersions` | KEY_INSPECT  
`GetKey` | KEY_READ  
`CreateKey` | KEY_CREATE and VAULT_CREATE_KEY  
`EnableKey` | KEY_UPDATE  
`DisableKey` | KEY_UPDATE  
`UpdateKey` | KEY_UPDATE  
`ScheduleKeyDeletion` | KEY_DELETE  
`CancelKeyDeletion` | KEY_DELETE  
`ChangeKeyCompartment` | KEY_MOVE  
`BackupKey` | KEY_BACKUP  
`RestoreKeyFromFile` | KEY_RESTORE  
`RestoreKeyFromObjectStore` | KEY_RESTORE  
`GetKeyVersion` | KEY_READ  
`CreateKeyVersion` | KEY_ROTATE  
`ImportKey` | KEY_IMPORT and VAULT_IMPORT_KEY  
`ImportKeyVersion` | KEY_IMPORT  
`ExportKey` | KEY_EXPORT  
`GenerateDataEncryptionKey` | KEY_ENCRYPT  
`Encrypt` | KEY_ENCRYPT  
`Decrypt` | KEY_DECRYPT  
`Sign` | KEY_SIGN  
`Verify` | KEY_VERIFY  
`CreateSecret` | KEY_ENCRYPT, KEY_DECRYPT, SECRET_CREATE , and VAULT_CREATE_SECRET  
`UpdateSecret` | SECRET_UPDATE  
`ListSecrets` | SECRET_INSPECT  
`GetSecret` | SECRET_READ  
`ScheduleSecretDeletion` | SECRET_DELETE  
`ChangeSecretCompartment` | SECRET_MOVE and SECRET_UPDATE  
`ListSecretVersions` | SECRET_VERSION_INSPECT  
`GetSecretVersion` | SECRET_VERSION_READ  
`ScheduleSecretVersionDeletion` | SECRET_VERSION_DELETE and SECRET_UPDATE  
`CancelSecretVersionDeletion` | SECRET_VERSION_DELETE and SECRET_UPDATE  
`ListSecretBundles` | SECRET_BUNDLE_INSPECT  
`GetSecretBundle` | SECRET_BUNDLE_READ  
`GetSecretBundleByName` | SECRET_BUNDLE_READ  
Was this article helpful?
YesNo


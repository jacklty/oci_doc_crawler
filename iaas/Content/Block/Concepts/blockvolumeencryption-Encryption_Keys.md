Updated 2024-03-22
# Block Volume Encryption Keys
Block Volume encrypts resources such as block volumes, boot volumes, and volume backups by using the Advanced Encryption Standard (AES) algorithm with 256-bit encryption.
You can use an Oracle-provided encryption key or a customer-managed key using the Vault service.
Block Volume uses envelope encryption to encrypt the data. With envelop encryption, data is encrypted using a unique generated data encryption key (DEK) and then the data encryption key is encrypted using the customer-managed key. The data encryption key is unique for each volume.
## Oracle Managed Keys 🔗 
This is the default encryption scheme and uses keys managed internally by Oracle. No action is needed to use these keys. If you don't specify a customer-managed key, your Block Volume resources are encrypted using Oracle-managed keys. The service rotates the keys periodically.
## Customer-Managed Keys 🔗 
You can use customer-managed keys, which are your own keys stored with the [Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm) service. You can import external keys to the Vault service or use the service to generate new keys. Using customer-managed keys to encrypt data incurs no additional cost or performance impact. For more information, see [Managing Vault Encryption Keys for Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#managingblockencryptionkeys "Customer-managed keys are keys that are managed and made available using the Oracle Cloud Infrastructure Vault.").
Was this article helpful?
YesNo


Updated 2025-01-10
# Object Storage Integration
Integrate Object Storage Service with various Hadoop components on Big Data Service clusters.
## Object Storage API Key Parameters 🔗 
Object Storage API key parameters are used to secure an API by requiring the client to pass a specific token.
**Note** You can use either a combination of API key and passphrase or use IAM credentials to configure Object Storage in Big Data Service.
API Key Parameter | Description  
---|---  
fingerprint | A unique fingerprint associated with the API key created for any specific user on a specific tenancy.  
passphrase | The passphrase associated with the API key (chosen when preparing the key).  
pem_file_path | The location of the API key on the cluster.  
tenant_id | The OCID of the tenant where the API key is.  
user_id | The OCID of the user associated with the API key.  
key_alias | The alias of the API key (chose when preparing the key).  
Was this article helpful?
YesNo


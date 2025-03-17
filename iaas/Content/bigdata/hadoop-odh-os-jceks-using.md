Updated 2023-05-31
# Using JCEKS Files
Use JCEKS files instead of plaintext passphrase for better security. 
Pass the JCEKS file path in the passphrase argument while exporting `HADOOP_OPTS` by running one of the following examples.
**Example 1** :
Copy
```
export HADOOP_OPTS="-DBDS_OSS_CLIENT_AUTH_FINGERPRINT=<api_key_fingerprint>
   -DBDS_OSS_CLIENT_AUTH_PEMFILEPATH=<api_key_pem_file_path_location>
   -DBDS_OSS_CLIENT_AUTH_TENANTID=<api_key_tenant_id>
   -DBDS_OSS_CLIENT_AUTH_USERID=<api_key_user_id> -DBDS_OSS_CLIENT_REGION=<api_key_region>
   -DBDS_OSS_CLIENT_AUTH_PASSPHRASE=<jceks_file_provider>"
```

**Example 2** :
Copy
```
export HADOOP_OPTS="-DOCI_SECRET_API_KEY_ALIAS=<api_key_alias> -DBDS_OSS_CLIENT_REGION=<api_key_region> 
   -DOCI_SECRET_API_KEY_PASSPHRASE=<jceks_file_provider> -DBDS_OSS_CLIENT_REGION=<api_key_region>"

```

Was this article helpful?
YesNo


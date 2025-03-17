Updated 2025-03-13
# Managing Passphrase through JCEKS
We recommend using JCEKS file for storing passwords because they're secure. 
Create a JCEKS provider file and add the passphrase against both the key `OCI_PASSPHRASE_METADATA` and the key `BDS_OSS_CLIENT_AUTH_PASSPHRASE`.
**Note** The JCEKS file can be created on a local system or in HDFS.
Local JCEKS:
Copy
```
hadoop credential create OCI_PASSPHRASE_METADATA -value <passphrase_value> -provider 
   jceks://file/<location-on-cluster>/<file-name>.jceks
hadoop credential create BDS_OSS_CLIENT_AUTH_PASSPHRASE -value <passphrase_value> -provider 
   jceks://file/<location-on-cluster>/<file-name>.jceks
```

In HDFS:
Copy
```
hadoop credential create OCI_PASSPHRASE_METADATA -value <passphrase_value> -provider 
   jceks://hdfs@<hostname_for_active_namenode>:<dfs_port_active_namenode>/<file-name>.jceks
hadoop credential create BDS_OSS_CLIENT_AUTH_PASSPHRASE -value <passphrase_value> -provider 
   jceks://hdfs@<hostname_for_active_namenode>:<dfs_port_active_namenode>/<file-name>.jceks
```

Was this article helpful?
YesNo


Updated 2024-05-01
# Configuring Object Storage with Sqoop
Establish Object Storage connectivity with Sqoop.
**Note** You can use Big Data Service cluster nodes for service configuration and running examples. To use an Edge node, you must create and sign in to the Edge node.
  1. (Optional) To use an Edge node for setting up Object Storage, first create an Edge node, and then sign in to the node. Then, copy the API key from the un0 node to the Edge node.
Copy
```
sudo dcli rsync -a <un0-hostname>:/opt/oracle/bds/.oci_oos/ 
/opt/oracle/bds/.oci_oos/
```

  2. Create a user with sufficient permissions and a JCEKS file with the required passphrase value. If you're creating a local JCEKS file, copy the file to all nodes and change user permissions. 
Copy
```
sudo dcli -f <location_of_jceks_file> -d <location_of_jceks_file>
sudo dcli chown <user>:<group> <location_of_jceks_file>
```

  3. Add either of the following `HADOOP_OPTS` combinations to the user bash profile.
**Option 1** :
Copy
```
export HADOOP_OPTS="$HADOOP_OPTS -DOCI_SECRET_API_KEY_ALIAS=<api_key_alias> 
-DBDS_OSS_CLIENT_REGION=<api_key_region> 
-DOCI_SECRET_API_KEY_PASSPHRASE=<jceks_file_provider>"
```

**Option 2** :
Copy
```
export HADOOP_OPTS="$HADOOP_OPTS -DBDS_OSS_CLIENT_AUTH_FINGERPRINT=<api_key_fingerprint> 
-DBDS_OSS_CLIENT_AUTH_PASSPHRASE=<jceks_file_provider> -DBDS_OSS_CLIENT_AUTH_PEMFILEPATH=<api_key_pem_file_path> 
-DBDS_OSS_CLIENT_AUTH_TENANTID=<api_key_tenant_id> -DBDS_OSS_CLIENT_AUTH_USERID=<api_key_user_id> 
-DBDS_OSS_CLIENT_REGION=<api_key_region>"
```

  4. (Optional) Run the following example to see how to use Sqoop.
Copy
```
sqoop import -Dmapreduce.job.user.classpath.first=false -Dorg.apache.sqoop.splitter.allow_text_splitter=true 
-Dfs.oci.client.auth.fingerprint=<api_key_fingerprint> -Dfs.oci.client.auth.passphrase=<jceks-provider> 
-Dfs.oci.client.auth.pemfilepath=<api_key_pem_file_path> -Dfs.oci.client.auth.tenantId=<api_key_tenant_info> 
-Dfs.oci.client.auth.userId=<api_key_user_info> -Dfs.oci.client.regionCodeOrId=<api_key_region_code_info> 
--connect jdbc:mysql://<un0_hostname>/hive --username <username> --password <example-password> --table AUX_TABLE 
--hive-import --hive-database default --create-hive-table --hive-table <hive_table_name> --target-dir 
<object_storage_output_location> --as-parquetfile --validate

```



Was this article helpful?
YesNo


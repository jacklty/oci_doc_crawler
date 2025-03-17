Updated 2023-08-28
# Configuring Object Storage with Map Reduce
To run an example, create an input file including words with varying size, and then upload the file to Object Storage.
**Note** You can use Big Data Service cluster nodes for service configuration and running examples. To use an Edge node, you must create and sign in to the Edge node.
  1. (Optional) To use an Edge node for setting up Object Storage, first create an Edge node, and then sign in to the node.
  2. Create an Edge node, and then sign in to the node.
  3. Create an input file with words of varying frequency, and then upload to Object Storage.
  4. Copy the API key to the Edge node from the un0 node.
Copy
```
sudo dcli rsync -a <un0-hostname>:/opt/oracle/bds/.oci_oos/ /opt/oracle/bds/.oci_oos/
```

  5. Create a user with sufficient permissions and a JCEKS file with the required passphrase value. If you're creating a local JCEKS file, copy the file to all nodes and change user permissions. 
Copy
```
sudo dcli -f <location_of_jceks_file> -d <location_of_jceks_file>
sudo dcli chown <user>:<group> <location_of_jceks_file>
```

  6. Add either of the following `HADOOP_OPTS` combinations to the user bash profile.
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

  7. (Optional) To verify Object Storage connectivity:
    1. Create an input file including words of varying size, and then upload the file to Object Storage.
    2. Run:
Copy
```
hadoop jar /usr/odh/current/hadoop-mapreduce-client/hadoop-mapreduce-examples.jar wordcount 
-Dmapreduce.reduce.java.opts="${MAPRED_OPTS}" -Dmapreduce.map.java.opts="${MAPRED_OPTS}" 
-Dyarn.app.mapreduce.am.command-opts="${MAPRED_OPTS}" oci://<bucket-name>@<namespace>/<input_file_name> 
oci://<bucket-name>@<namespace>/<output_file_name>

```



Was this article helpful?
YesNo


Updated 2023-08-28
# Configuring Object Storage with Hadoop
In Hadoop, Object Storage connectivity is used for performing file operations on Object Storage. For example, list, read, write, copy, and so on.
**Note** You can use Big Data Service cluster nodes for service configuration and running examples. To use an Edge node, you must create and sign in to the Edge node.
  1. (Optional) To use an Edge node for setting up Object Storage, first create an Edge node, and then sign in to the node. Then, copy the API key from the un0 node to the Edge node.
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

  4. Verify the Object Storage connection was established:
[Configuring Object Storage with Hadoop](https://docs.oracle.com/en-us/iaas/Content/bigdata/hadoop-odh-os-config-hadoop.htm#hadoop "In Hadoop, Object Storage connectivity is used for performing file operations on Object Storage. For example, list, read, write, copy, and so on.")
Copy
```
hdfs dfs -ls oci://<bucket-name>@<namespace>/
hdfs dfs -cat oci://<bucket-name>@<namespace><file-on-object-storage>
hdfs dfs -mkdir oci://<bucket-name>@<namespace>/<test-directory-name>
hdfs dfs -cp /<file-on-hdfs> oci://<bucket-name>@<namespace>/<test-directory-name>
hadoop distcp -Dmapreduce.reduce.java.opts="${HADOOP_OPTS}" -Dmapreduce.map.java.opts="${HADOOP_OPTS}" 
-Dyarn.app.mapreduce.am.command-opts="${HADOOP_OPTS}" oci://<bucket-name>@<namespace>/<file-on-object-storage>
/<path_on_hdfs>
```



Was this article helpful?
YesNo


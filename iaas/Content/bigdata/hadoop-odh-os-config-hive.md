Updated 2023-08-28
# Configuring Object Storage with Hive
In Hive, Object Storage connectivity is used for performing queries on database hosted in Object Storage using `beeline`.
**Note** You can use Big Data Service cluster nodes for service configuration and running examples. To use an Edge node, you must create and sign in to the Edge node.
  1. (Optional) To use an Edge node for setting up Object Storage, first create an Edge node, and then sign in to the node. Then, copy the API key from the un0 node to the Edge node.
Copy
```
sudo dcli rsync -a <un0-hostname>:/opt/oracle/bds/.oci_oos/
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
export HADOOP_OPTS="$HADOOP_OPTS -DOCI_SECRET_API_KEY_ALIAS=api_key_alias> 
-DBDS_OSS_CLIENT_REGION=<api_key_region> -DOCI_SECRET_API_KEY_PASSPHRASE=<jceks_file_provider>"
```

**Option 2** :
Copy
```
export HADOOP_OPTS="$HADOOP_OPTS -DBDS_OSS_CLIENT_AUTH_FINGERPRINT=<api_key_fingerprint> 
-DBDS_OSS_CLIENT_AUTH_PASSPHRASE=<jceks_file_provider> -DBDS_OSS_CLIENT_AUTH_PEMFILEPATH=<api_key_pem_file_path> 
-DBDS_OSS_CLIENT_AUTH_TENANTID=<api_key_tenant_id> -DBDS_OSS_CLIENT_AUTH_USERID=<api_key_user_> 
-DBDS_OSS_CLIENT_REGION=<api_key_region>"
```

  4. For clusters created before Big Data Service 3.0.21, add the following key and value to the custom hive-site configuration. After Big Data Service 3.0.21, the property is already set.
    1. [Access](https://docs.oracle.com/en-us/iaas/Content/bigdata/hadoop-odh-open.htm#cluster-ambari) Apache Ambari.
    2. From the side toolbar, under **Services** click **Hive**.
    3. Click **Configs**.
    4. Click **Advanced**.
    5. Click **Custom hive-site** , and then click **Add Property**.
    6. Enter:
       * **Key** : `hive.security.authorization.sqlstd.confwhitelist.append`
       * **Value** : 
Copy
```
OCI_SECRET_API_KEY_ALIAS|OCI_SECRET_API_KEY_PASSPHRASE|BDS_OSS_CLIENT_AUTH_PEMFILEPATH|BDS_OSS_CLIENT_REGION|
BDS_OSS_CLIENT_AUTH_TENANTID|BDS_OSS_CLIENT_AUTH_USERID|BDS_OSS_CLIENT_AUTH_FINGERPRINT|BDS_OSS_CLIENT_AUTH_PASSPHRASE
```

  5. Add the Hadoop options to the **hive-env template** for Object Storage access.
    1. Remain in Ambari on the Hive **Advanced** tab. See previous step to access.
    2. In the **Performance** section, go to **Advanced hive-env**.
    3. Go to **hive-env template** , and add one of the following options under the line `if [ "$SERVICE" = "metastore" ]; then`.
**Option 1** :
Copy
```
export HADOOP_OPTS="$HADOOP_OPTS 
-DOCI_SECRET_API_KEY_ALIAS=<api_key_alias> 
-DBDS_OSS_CLIENT_REGION=<api_key_region> 
-DOCI_SECRET_API_KEY_PASSPHRASE=<jceks_file_provider>"
```

**Option 2** :
Copy
```
export HADOOP_OPTS="$HADOOP_OPTS -DBDS_OSS_CLIENT_AUTH_FINGERPRINT=
<api_key_fingerprint> -DBDS_OSS_CLIENT_AUTH_PASSPHRASE=<jceks_file_provider> 
-DBDS_OSS_CLIENT_AUTH_PEMFILEPATH=<api_key_pem_file_path> 
-DBDS_OSS_CLIENT_AUTH_TENANTID=<api_key_tenant_id> 
-DBDS_OSS_CLIENT_AUTH_USERID=<api_key_user_id> -DBDS_OSS_CLIENT_REGION=<api_key_region>"
```

  6. Restart all required services through Ambari.
  7. Run the following example command to launch the beeline shell:
**Example 1** :
Copy
```
beeline -hiveconf OCI_SECRET_API_KEY_ALIAS=<api_key_alias> 
-hiveconf OCI_SECRET_API_KEY_PASSPHRASE=<api_key_passphrase> 
-hiveconf BDS_OSS_CLIENT_REGION=<api_key_region> 

```

**Example 2** :
Copy
```
beeline -hiveconf BDS_OSS_CLIENT_AUTH_PEMFILEPATH=<api_key_pem_file_path> 
-hiveconf BDS_OSS_CLIENT_AUTH_FINGERPRINT=<api_key_fingerprint> 
-hiveconf BDS_OSS_CLIENT_REGION=<api_key_region 
-hiveconf BDS_OSS_CLIENT_AUTH_TENANTID=<api_key_tenant_id 
-hiveconf BDS_OSS_CLIENT_AUTH_USERID=<api_key_user_id 
-hiveconf BDS_OSS_CLIENT_AUTH_PASSPHRASE=<api_key_passphrase>

```

  8. (Optional) Alternatively, configure the parameters on the beeline. Use the `beeline` command to launch the beeline shell, and then run the following:
Copy
```
set BDS_OSS_CLIENT_REGION=<api_key_region>;
set BDS_OSS_CLIENT_AUTH_PEMFILEPATH=<api_key_pem_file_path>;
set BDS_OSS_CLIENT_AUTH_FINGERPRINT=<api_key_fingerprint>;
set BDS_OSS_CLIENT_AUTH_TENANTID=<api_key_tenant_id>;
set BDS_OSS_CLIENT_AUTH_USERID=<api_key_user_id>;
set BDS_OSS_CLIENT_AUTH_PASSPHRASE=<api_key_passphrase>;
```

  9. Verify Object Storage connectivity:
**Example for Managed Table** :
Copy
```
CREATE DATABASE IF NOT EXISTS <database_name> LOCATION 
'oci://<bucket-name>@<namespace>/';
USE <database_name>;
CREATE TABLE IF NOT EXISTS <table_name> (id int, name string) partitioned by 
(part int, part2 int) STORED AS parquet;
INSERT INTO <table_name> partition(part=1, part2=1) values (111, 'Object Storage 
Testing with Hive Beeline Managed Table');
SELECT * from <table_name>;
 
```

**Example for External Table** :
Copy
```
CREATE DATABASE IF NOT EXISTS <database_name> LOCATION 'oci://<bucket-name>@<namespace>/';
USE <database_name>;
CREATE EXTERNAL TABLE IF NOT EXISTS <table_name> (id int, name string) partitioned by (part int, part2 int) STORED AS parquet LOCATION 'oci://<bucket-name>@<namespace>/';
INSERT INTO <table_name> partition(part=1, part2=1) values (222, 'Object Storage Testing with Hive Beeline External Table');
SELECT * from <table_name>;
```



Was this article helpful?
YesNo


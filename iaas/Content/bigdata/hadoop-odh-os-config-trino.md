Updated 2023-08-28
# Configuring Object Storage with Trino
You can access Object Storage from Trino for both your HA and non-HA clusters.
You must [Creating an Object Storage API Key for a Cluster](https://docs.oracle.com/en-us/iaas/Content/bigdata/integrated-services-os-create.htm#os-create-key "Create an API key to connect a Big Data Service cluster to Object Storage.") in the cluster before configuring access to Object Storage from Trino.
  1. [Access](https://docs.oracle.com/en-us/iaas/Content/bigdata/hadoop-odh-open.htm#cluster-ambari) Apache Ambari.
  2. From the side toolbar, under **Services** click **HDFS**.
  3. Click **Configs**.
  4. Update the following configs under **Custom core-site**. The values of these configs can be found in the Object Storage [Viewing the Object Storage Public Key for a Cluster](https://docs.oracle.com/en-us/iaas/Content/bigdata/integrated-services-os-view-config.htm#os-config "View and copy the public key of the Object Storage API key file that a Big Data Service cluster uses to connect to Object Storage.") in the cluster.
     * `fs.oci.client.auth.fingerprint`
     * `fs.oci.client.auth.passphrase`
     * `fs.oci.client.auth.pemfilepath`
     * `fs.oci.client.auth.tenantId`
     * `fs.oci.client.auth.userId`
     * `fs.oci.client.regionCodeOrId`
  5. In Ambari, add either of the following `HADOOP_OPTS` combinations for Object Storage access.
    1. [Access](https://docs.oracle.com/en-us/iaas/Content/bigdata/hadoop-odh-open.htm#cluster-ambari) Apache Ambari.
    2. From the side toolbar, under **Services** click **Hive**.
    3. Click **Configs**.
    4. Click **Advanced**.
    5. In the **Performance** section, go to **Advanced hive-env**.
    6. Go to **hive-env template** , and then add one of the following options under the line `if [ "$SERVICE" = "metastore" ]; then`.
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

  6. Restart Trino.
  7. Set up a table in Object Storage, and then run:
Copy
```
/usr/lib/trino/bin/trino-cli --server https://<hostname>:7778 
--krb5-principal <trino_user_principal> --krb5-keytab-path <trino_keytab_path> 
--krb5-remote-service-name trino --user <trino_user_principal> 
--truststore-path=<truststore_jks_location> --catalog=hive --execute "<queries_separated_by_semicolon>"

```



## Configuring Object Storage with Trino Using `trino-cli` Configuration 🔗 
You can pass required parameters to access Object Storage through `trino-cli` configurations.
**Important** Only run this option if the cluster is older than Big Data Service 3.0.21. The properties set in this task are set by default beginning with Big Data Service 3.0.21.
To add the `hive.security.authorization.sqlstd.confwhitelist.append ` key and value to the **Custom hive-site** configuration, complete the following task. 
  1. [Access](https://docs.oracle.com/en-us/iaas/Content/bigdata/hadoop-odh-open.htm#cluster-ambari) Apache Ambari.
  2. From the side toolbar, under **Services** click **Hive**.
  3. Click **Configs**.
  4. Click **Advanced** , and then click **Custom hive-site**.
  5. Click **Add Property** , and then add the key and value information.
     * **Key** : `hive.security.authorization.sqlstd.confwhitelist.append `
     * **Value** : 
Copy
```
OCI_SECRET_API_KEY_ALIAS|OCI_SECRET_API_KEY_PASSPHRASE|BDS_OSS_CLIENT_AUTH_PEMFILEPATH|BDS_OSS_CLIENT_REGION|
BDS_OSS_CLIENT_AUTH_TENANTID|BDS_OSS_CLIENT_AUTH_USERID|BDS_OSS_CLIENT_AUTH_FINGERPRINT|BDS_OSS_CLIENT_AUTH_PASSPHRASE

```

  6. Add the Hadoop options to the **hive-env template** for Object Storage access.
    1. Remain in Ambari on the Hive **Advanced** tab. See previous step to access.
    2. In the **Performance** section, go to **Advanced hive-env**.
    3. Go to **hive-env template** , and add one of the following options under the line `if [ "$SERVICE" = "metastore" ]; then`.
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

  7. Restart Trino.
  8. To run a CLI example, set up a table in Object Storage, and then run one of the following examples.
  9. **Example 1** : After setting up the table, run the following CLI example:
Copy
```
/usr/lib/trino/bin/trino-cli --server https://<trino-coordinator>:<port> 
--krb5-config-path <krb5-conf-path> --krb5-principal <trino-user-principal> 
--krb5-remote-service-name trino --user trino/release2-un0.bmbdcsad1.bmbdcs.oraclevcn.com@BDSCLOUD.ORACLE.COM 
--truststore-path=<truststore-path> --extra-credential BDS_OSS_CLIENT_REGION=<Region> 
--extra-credential BDS_OSS_CLIENT_AUTH_TENANTID=<Tenant-id> 
--extra-credential BDS_OSS_CLIENT_AUTH_USERID=<User-id> 
--extra-credential BDS_OSS_CLIENT_AUTH_FINGERPRINT=<FingerPrint> 
--extra-credential BDS_OSS_CLIENT_AUTH_PEMFILEPATH=<pem-file-path> 
--extra-credential BDS_OSS_CLIENT_AUTH_PASSPHRASE=<Passphrase> 
--execute "<query>"

```

**Example 2 with sample content** :
Copy
```
/usr/lib/trino/bin/trino-cli --server https://host-mn0.xx.xx.xx.com:7778 --krb5-config-path /etc/krb5.conf 
--krb5-principal trino/host-mn0.xx.xx.xx.com@cloud.com --krb5-keytab-path /etc/security/keytabs/trino.service.keytab 
--krb5-remote-service-name trino --user trino/host-mn0.xx.xx.xx.com@cloud.com --truststore-path=/etc/security/serverKeys/truststore.jks 
--extra-credential BDS_OSS_CLIENT_REGION=us-ashburn-1 --extra-credential BDS_OSS_CLIENT_AUTH_TENANTID=xxxxxx 
--extra-credential BDS_OSS_CLIENT_AUTH_USERID=xxxxx --extra-credential BDS_OSS_CLIENT_AUTH_FINGERPRINT=xxxxxx 
--extra-credential BDS_OSS_CLIENT_AUTH_PEMFILEPATH=/tmp/key.pem --extra-credential BDS_OSS_CLIENT_AUTH_PASSPHRASE=xxxxx 
--execute "select name from hive.default.objectStoreTable limit 10"

```



Was this article helpful?
YesNo


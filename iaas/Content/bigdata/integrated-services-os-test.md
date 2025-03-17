Updated 2023-11-05
# Testing the Connection to Object Storage from a Cluster
Test an Object Storage API key connection from the Big Data Service cluster.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/bigdata/integrated-services-os-test.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/bigdata/integrated-services-os-test.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/bigdata/integrated-services-os-test.htm)


  *     1. Open the navigation menu and click **Analytics & AI**. Under **Data Lake** , click **Big Data Service**.
    2. Under **Compartment** , select the compartment that contains the cluster.
    3. In the list of clusters, click the name of the cluster that has the API key.
    4. On the Cluster details page, under **Resources** click **API keys**.
    5. From the Action menu of the API key you want to test, select **Test connection**.
    6. Enter the Object Storage URI for the bucket you want to connect to in the [URI format](https://docs.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat) `oci://MyBucket@MyNamespace/`.
    7. Enter the passphrase of the API key. You specified this passphrase when you created the API key.
    8. Click **Test connection**. The status of the test connection is displayed.
  * Use the [oci bds bds-api-key test-bds-object-storage-connection](https://docs.oracle.com/iaas/tools/oci-cli/3.36.0/oci_cli_docs/cmdref/bds/bds-api-key/test-bds-object-storage-connection.html) command and required parameters to test the connection to Object Storage.
Command
CopyTry It
```
oci bds bds-api-key test-bds-object-storage-connection --api-key-id <api_key_id> --bds-instance-id <bds_instance_id> --object-storage-uri <object_storage_uri> --passphrase <passphrase> [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference for Big Data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bds.html).
  * Use the [TestBdsObjectStorageConnection](https://docs.oracle.com/iaas/api/#/en/bigdata/20190531/BdsMetastoreConfiguration/TestBdsObjectStorageConnection) operation to test the connection to Object Storage.


Was this article helpful?
YesNo


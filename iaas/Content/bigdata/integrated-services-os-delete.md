Updated 2024-02-15
# Deleting an Object Storage API Key from a Cluster
Delete an API key that's used to connect a Big Data Service cluster to Object Storage
When you delete an Object Storage API key, all user access to run Object Storage jobs on the Big Data Service clusters is revoked.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/bigdata/integrated-services-os-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/bigdata/integrated-services-os-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/bigdata/integrated-services-os-delete.htm)


  *     1. Open the navigation menu and click **Analytics & AI**. Under **Data Lake** , click **Big Data Service**.
    2. Under **Compartment** , select the compartment that contains the cluster.
    3. In the list of clusters, click the **Name** of the cluster that has the API key.
    4. On the Cluster details page, under **Resources** click **API keys**.
    5. From the Action menu of the API key that you want to delete, select **Delete**.
    6. To confirm the deletion, enter the key alias of the key.
    7. Click **Delete**.
  * Use the [oci bds bds-api-key delete](https://docs.oracle.com/iaas/tools/oci-cli/3.36.0/oci_cli_docs/cmdref/bds/bds-api-key/delete.html) command and required parameters to delete an Object Storage API key.
Command
CopyTry It
```
oci bds bds-api-key delete --api-key-id <api_key_id> --bds-instance-id <bds_instance_id> [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference for Big Data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bds.html).
  * Use the [DeleteBdsApiKey](https://docs.oracle.com/iaas/api/#/en/bigdata/20190531/BdsMetastoreConfiguration/DeleteBdsApiKey) operation to delete an Object Storage API key.


Was this article helpful?
YesNo


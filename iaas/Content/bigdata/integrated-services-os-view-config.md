Updated 2023-11-05
# Viewing the Object Storage Public Key for a Cluster
View and copy the public key of the Object Storage API key file that a Big Data Service cluster uses to connect to Object Storage.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/bigdata/integrated-services-os-view-config.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/bigdata/integrated-services-os-view-config.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/bigdata/integrated-services-os-view-config.htm)


  *     1. Open the navigation menu and click **Analytics & AI**. Under **Data Lake** , click **Big Data Service**.
    2. Under **Compartment** , select the compartment that contains the cluster.
    3. In the list of clusters, click name of the cluster that has the API key.
    4. On the Cluster details page, under **Resources** click **API keys**.
    5. From the Actions menu of the API key that you want to view, select **View configuration file**.
    6. The public key details of the API key are displayed in the View configuration file dialog.
    7. View the configuration file details or copy the public key.
  * Use the [oci bds bds-api-key get](https://docs.oracle.com/iaas/tools/oci-cli/3.36.0/oci_cli_docs/cmdref/bds/bds-api-key/get.html) command and required parameters to view the Object Storage public key.
Command
CopyTry It
```
oci bds bds-api-key get --api-key-id <api_key_id> --bds-instance-id <bds_instance_id> [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference for Big Data](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bds.html).
  * Use the [GetBdsApiKey](https://docs.oracle.com/iaas/api/#/en/bigdata/20190531/BdsMetastoreConfiguration/GetBdsApiKey) operation to view the Object Storage public key.


Was this article helpful?
YesNo


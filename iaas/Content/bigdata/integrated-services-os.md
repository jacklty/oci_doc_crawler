Updated 2025-01-10
# Object Storage API Key Integration
Big Data Service uses the [OCI API signing key](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#two) mechanism to connect to Object Storage. You can access Object Storage buckets encrypted with [user managed keys](https://docs.oracle.com/iaas/Content/Object/Tasks/encryption.htm) from the Big Data Service cluster nodes. For details on data encryption, see [securing Object Storage](https://docs.oracle.com/iaas/Content/Security/Reference/objectstorage_security.htm#data-encryption).
**Note** To use the Object Storage API keys, you must create a Big Data Service cluster with version 3.0.4 or later. The Big Data Service version is displayed on the Cluster Information tab of the cluster details page. For earlier versions, use [Using OCI HDFS Connector](https://docs.oracle.com/en-us/iaas/Content/bigdata/hadoop-odh-hdfs.htm#hdfs "The OCI Hadoop Distributed File System \(HDFS\) connector lets your Apache Hadoop application read and write data to and from Object Storage.").
For information on manaing Object Storage API keys, see:
  * [Creating an Object Storage API Key for a Cluster](https://docs.oracle.com/en-us/iaas/Content/bigdata/integrated-services-os-create.htm#os-create-key "Create an API key to connect a Big Data Service cluster to Object Storage.")
  * [Viewing the Object Storage Public Key for a Cluster](https://docs.oracle.com/en-us/iaas/Content/bigdata/integrated-services-os-view-config.htm#os-config "View and copy the public key of the Object Storage API key file that a Big Data Service cluster uses to connect to Object Storage.")
  * [Testing the Connection to Object Storage from a Cluster](https://docs.oracle.com/en-us/iaas/Content/bigdata/integrated-services-os-test.htm#os-test "Test an Object Storage API key connection from the Big Data Service cluster.")
  * [Deleting an Object Storage API Key from a Cluster](https://docs.oracle.com/en-us/iaas/Content/bigdata/integrated-services-os-delete.htm#os-delete-key "Delete an API key that's used to connect a Big Data Service cluster to Object Storage")


Was this article helpful?
YesNo


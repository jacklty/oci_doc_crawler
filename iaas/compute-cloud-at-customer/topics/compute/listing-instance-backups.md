Updated 2023-10-19
# Listing Instance Backups
On Compute Cloud@Customer, you can list instance backups using the Compute Cloud@Customer Console and API.
When you list instance backups, you are able to identify these components of the backup:
  * Backup OCID
  * Boot volume OCID
  * Instance OCID
  * Image OCID


  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/listing-instance-backups.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/listing-instance-backups.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/listing-instance-backups.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click any of the following links.
       * **Instance Exports** : Displays the list of instance backups.
       * **Instance Imports** : Displays the list of imported instance backups that can be used to create new instances.
  * This task can't be performed using the CLI.
  * There are two API endpoints for viewing instance backups:
    * List All Instance Backups in a Bucket.
**API endpoint**
```
https://<mgmt_node_VIP>:30003/20160918/instances/instanceBackups?compartmentId=<bucket_compartment_OCID>
```

where: 
      * <mgmt_node_VIP> is the management node VIP host name or IP address.
      * <bucket_compartment_OCID> is the compartment ID where the Object Storage bucket is located.
    * **Get Instance Backup Details**
**API endpoint**
```
https://<mgmt_node_VIP>:30003/20160918/instanceBackups/<instance_backup_id>
```

where: 
      * <mgmt_node_VIP> is the management node VIP host name or IP address.
      * <instance_backup_id> is the backup ID, which you can get from the backup export output or from listing backups with the API.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


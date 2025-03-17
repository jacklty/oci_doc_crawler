Updated 2024-11-07
# Creating an Instance Backup
On Compute Cloud@Customer, you can use the Compute Cloud@Customer Console and API to back up an instance.
The instance can be running or stopped. The boot volume and any block volumes must be attached.
**Caution**
During the backup process, don't perform any volume attach or detach operations on the instance.
The duration of the backup varies based on the amount of data on the instance boot and block volumes. A small instance that only has a 50 GB boot volume takes only a few minutes to complete. If the instance volumes are as large as 32 TB, the backup can take up to 6 hours to complete.
## Prerequisites 🔗 
  * You must have an Object Storage bucket in the tenancy where the instance is located. See [Creating a Bucket](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/creating-a-bucket.htm#creating-a-bucket "On Compute Cloud@Customer, you can create Object Storage buckets.").
  * Quiesce instance activities such as running applications so that the backup is created at a known state.


  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-backup.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-backup.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-backup.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    2. At the top of the page, select the compartment that contains the instance.
    3. Perform one of the following actions:
       * Click the name of the instance you plan to back up. Then click **Controls** (upper right) and select **Export**.
       * Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), and select **Export**.
    4. In the dialog box, select these items:
       * If needed, change the compartment to the compartment where the bucket is located by clicking **(Change)**.
       * Select the bucket.
       * Click **Create Export**.
    5. To see the status of an instance backup, under **Resources** , click **Instance Exports**.
  * This task can't be performed using the CLI.
  * The `export` API creates an instance backup to an Object Storage bucket in the specified compartment.
**API Endpoint**
```
https://<mgmt_node_VIP>:30003/20160918/instances/<instance_OCID>/actions/export
```

where: 
    * <mgmt_node_VIP> is the management node VIP host name or IP address.
    * <instance_OCID> is the instance ID.
Pass these key-value pairs:
```
{
	"bucketName": "<bucket_name>",
	"destinationType": "objectStorageTuple",
	"namespaceName": "<namespace_name>",
	"compartmentId": "<bucket_compartment_OCID>"
}
```

For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


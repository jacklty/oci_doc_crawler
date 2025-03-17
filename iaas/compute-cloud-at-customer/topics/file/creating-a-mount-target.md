Updated 2024-12-16
# Creating a Mount Target
On Compute Cloud@Customer, A mount target is an NFS endpoint assigned to a subnet of your choice. The mount target provides the IP address or DNS name that's used in the mount command when connecting NFS clients to a file system. 
You can create at most two mount targets per VCN: at most one mount target per pool type. Pool type refers to the backing store pool for the file system, which can be either the default pool of the attached ZFS Storage Appliance or a high performance pool. See the _Backing store pool_ in [Creating a File System](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system.htm#creating-a-file-system "On Compute Cloud@Customer, you can create a shared file system using the File Storage service."). Two mount targets in a VCN are counted as one with regard to resource limits.
You can reuse a mount target to make many file systems available on the network. To reuse the same mount target for multiple file systems, create an export in the mount target for each file system. The file system and mount target must be in the same compartment and the same backing store pool when you create an export.
**Caution**
Don't use /30 or smaller subnets for mount target creation because they might not have enough available IP addresses.
**Important**
When exporting file systems to overlapping CIDRs in a VCN, exports to the longest CIDR (smallest network) must be done first. For more information and an example, see My Oracle Support article [PCA File system as a Service Exports (Doc ID 2823994.1)](https://support.oracle.com/epmos/faces/DocContentDisplay?id=2823994.1).
Before you can create a mount target, ensure that these items are configured:
  * At least one Virtual Cloud Network (VCN) and subnet is configured. See [Managing VCNs and Subnets](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/managing-vcns-and-subnets.htm#managing-vcns-and-subnets "On Compute Cloud@Customer,")
  * (Required for [Mounting File Systems Across Compute Cloud@Customer Infrastructures](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/mounting-file-systems-across-compute-cloud-customer.htm#mounting-file-systems-across-compute-cloud-customer)) A Dynamic Routing Gateway (DRG) with a route rule in the VCN. See [Dynamic Routing Gateways (DRGs)](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/dynamic-routing-gateway.htm#dynamic-routing-gateway "On Compute Cloud@Customer, a dynamic routing gateway, or DRG, provides a path for private network traffic between the VCN and an on-premises network. This traffic is routed to the data center network and on to its destination.").
  * (Optional) Security rules for the file system mount target. Security rules can be created in the security list for the mount target subnet, or in a Network Security Group (NSG) that you add the mount target to. See [Controlling Access to File Storage](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/controlling-access-to-file-storage.htm#controlling-access-to-file-storage "On Compute Cloud@Customer, before you can mount a file system, you must configure security rules to allow traffic to the mount target's VNIC using specific protocols and ports.").
You don't need security rules to create a mount target, but you do need security rules to eventually mount file systems that are associated with this mount target.
  * To ensure that the mount target is created using high performance storage, first configure the OraclePCA tag namespace and backing store pool (`poolName`) attribute in your OCI tenancy. See [Creating OraclePCA Tags](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/creating_oraclepca_tags.htm#creating_oraclepca_tags "On Oracle Compute Cloud@Customer you can use the OraclePCA tag namespace to enable resource attributes that aren't available as CLI options or API attributes."). Then when you create the mount target, assign the OraclePCA tag namesapce and `poolName` attribute to the mount target. The poolName property can be set only when the mount target is created. You cannot set or change this property value after the mount target is created.


Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-mount-target.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-mount-target.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-mount-target.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **File Storage** , then click **Mount Targets**.
    2. In the compartment drop-down menu above the mount targets list, select the compartment where you plan to create the file system.
If a mount target is listed, click the name of the mount target to open the details page and check the following parameters:
       * The mount target must be on the same subnet as the instance where you want to mount the file system.
       * Click the **Select Tag(s)** tab. The mount target must be in the same backing store pool that's specified for the file system. If the value of the **OraclePCA.poolName** tag is **PCA_POOL_HIGH** , then the mount target is in the high performance pool. If the value of the **OraclePCA.poolName** tag is **PCA_POOL** , or if no **OraclePCA.poolName** tag, then the mount target is in the default pool. For more information about these tags, see [Creating OraclePCA Tags](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/creating_oraclepca_tags.htm#creating_oraclepca_tags "On Oracle Compute Cloud@Customer you can use the OraclePCA tag namespace to enable resource attributes that aren't available as CLI options or API attributes.").
If the mount target meets your needs, skip this procedure and go to [Creating a File System](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system.htm#creating-a-file-system "On Compute Cloud@Customer, you can create a shared file system using the File Storage service.").
    3. Click **Create Mount Target**.
    4. Enter the mount target information:
       * **Name:** It doesn't have to be unique. An Oracle Cloud Identifier (OCID) uniquely identifies the mount target. Avoid entering confidential information.
**Note**
The mount target name is different than the DNS hostname.
       * **Create in Compartment:** Specify the compartment.
       * **VCN:** Select the VCN where you want to create the new mount target.
       * **Subnet:** Select a subnet to attach the mount target to.
       * **IP Address:** (Optional) You can specify an unused IP address in the subnet you selected for the mount target. If left blank, an IP address is automatically assigned.
       * **Host Name:** (Optional) You can specify a hostname you want to assign to the mount target.
**Note**
The File Storage service constructs a fully qualified domain name (FQDN) by combining the hostname with the FQDN of the mount target subnet. 
For example, `myhostname.subnet123.dnslabel.examplevcn.com`. 
       * **Enable Network Security Groups:** Select this option to add this mount target to an existing NSG.
**Important**
Rules for the NSG that you select must be configured to allow traffic to the mount target's VNIC using specific protocols and ports. For more information, see[Controlling Access to File Storage](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/controlling-access-to-file-storage.htm#controlling-access-to-file-storage "On Compute Cloud@Customer, before you can mount a file system, you must configure security rules to allow traffic to the mount target's VNIC using specific protocols and ports.") and [Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/configuring-vcn-security-rules-for-file-storage.htm#configuring-vcn-security-rules-for-file-storage "On Compute Cloud@Customer, you can add the required rules to a preexisting security list associated with a subnet, such as the default security list that is created along with the VCN.").
       * (Optional) Add one or more tags to this resource. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
By default, the mount target is created on the default storage pool. To create a mount target for a high performance pool, select the **OraclePCA** tag namespace, the **poolName** tag key, and the value **PCA_POOL_HIGH**. The poolName property can be set only when the mount target is created. You can't set or change this property value after the mount target is created.
    5. Click **Create Mount Target**.
Next, create a file system. See [Creating a File System](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system.htm#creating-a-file-system "On Compute Cloud@Customer, you can create a shared file system using the File Storage service.").
  * Use the [oci fs mount-target create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/create.html) command and required parameters to create a new mount target in the specified compartment and subnet.
Copy
```
oci fs mount-target create --availability-domain <availability_domain_name> --compartment-id <compartment_OCID>--subnet-id <subnet_OCID> --display-name <name_to_assign_to_mount-target> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**Procedure**
    1. Gather the information that you need to run the command:
       * OCID of the compartment where you plan to create the file system (`oci iam compartment list`)
       * OCID of the subnet of the instance where you want to mount a file system (`oci network subnet list`)
    2. Run the create mount target command.
By default, the mount target is for the default pool of the attached ZFS Storage Appliance. To create a mount target for a high performance pool, specify the ``OraclePCA`.poolName` tag with a value of `PCA_POOL_HIGH` as shown in the following example. The `poolName` property can be set only when the mount target is created. You can't set or change this property value with the `update` command.
Example:
```
oci fs mount-target create --availability-domain AD-1 \
--compartment-id ocid1.compartment.uniqueID --subnet-id ocid1.subnet.uniqueID \
--defined-tags '{"OraclePCA":{"poolName":"PCA_POOL_HIGH"}}' \
--display-name HighPerfPoolMT
{
 "data": {
  "availability-domain": "AD-1",
  "compartment-id": "ocid1.compartment._uniqueID_",
  "defined-tags": {
   "Oracle-Tags": {
    "CreatedBy": "pca_user",
    "CreatedOn": "2024-07-03T14:56:29.92Z"
   },
   "OraclePCA":{
    "poolName":"PCA_POOL_HIGH"
   }
  },
  "display-name": "HighPerfPoolMT",
  "export-set-id": "ocid1.exportset._uniqueID_",
  "freeform-tags": {},
  "id": "ocid1.mounttarget.**_uniqueID_**",
  "lifecycle-details": null,
  "lifecycle-state": "CREATING",
  "nsg-ids": [],
  "private-ip-ids": [],
  "subnet-id": "ocid1.subnet._uniqueID_",
  "time-created": "2024-07-03T14:56:29.921587+00:00"
 },
 "etag": "2d278b37-a74a-4fec-b74a-fd9e9a1c72de"
```

    3. Next, create a file system. See [Creating a File System](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system.htm#creating-a-file-system "On Compute Cloud@Customer, you can create a shared file system using the File Storage service.").
  * Use the [CreateMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/CreateMountTarget) operation to create a new mount target in the specified compartment and subnet.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


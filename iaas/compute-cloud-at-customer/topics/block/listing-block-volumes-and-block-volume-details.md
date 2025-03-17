Updated 2024-01-18
# Listing Block Volumes and Block Volume Details
On Compute Cloud@Customer, you can list all block volumes in a specific compartment, and detailed information about a single volume.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/listing-block-volumes-and-block-volume-details.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/listing-block-volumes-and-block-volume-details.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/listing-block-volumes-and-block-volume-details.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Block Volumes**.
    2. At the top of the page, select the compartment that contains the volume you want to see.
    3. To view block volume details, click the name of the block volume.
The details are displayed.
Detail Item | Description  
---|---  
Block volume icon |  Displays the status of the block volume.  
Block volume name |  The name of the block volume.  
Block Volume Information and Tags |  Tabs that you can click to display:
       * General Information
       * Tags that have been applied to this object  
Created |  The day and time that the volume was created.  
Compartment |  The compartment that the volume belongs to.  
OCID |  The volume's Oracle Cloud ID.  
Backup Policy |  The backup policy assigned to the volume.  
Size |  The size of the volume.  
High Performance Enabled |  Whether the volume is configured as a high performance volume, and the volume performance units (VPUs) per GB.  
  * Use these commands to list volumes: 
    * List all volumes in a compartment:
Use the [oci bv boot-volume list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/list.html) command.
Command
CopyTry It
```
oci bv volume list --compartment <compartment_OICD> [OPTIONS]
```

    * List the details for a single volume:
[oci bv boot-volume get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/get.html) command.
Command
CopyTry It
```
oci bv volume get --compartment <compartment_OICD> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the[ListVolumes](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/ListVolumes) operation to list all volumes in a compartment.
Use the [GetVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/GetVolume) operation to list the details for a single volume.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


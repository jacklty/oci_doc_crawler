Updated 2024-01-18
# Listing Block Volume Attachments
On Compute Cloud@Customer, you can list all Block Volume volume attachments in a specific compartment, and detailed information for a single volume attachment.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/listing-block-volume-attachments.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/listing-block-volume-attachments.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/listing-block-volume-attachments.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    2. At the top of the page, select the compartment that contains the instance that has the attached block volume.
    3. Click the instance name to display the details.
    4. Under **Resources** , click **Attached Block Volumes**.
Block volumes that are attached to this instance are listed in the table.
    5. To see details for a block volume, click the block volume name.
  * Use these commands to list volume attachments:
    * Use [xx](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/volume-attachment/list.html) to list all volume attachments in a compartment:
Copy
```
oci compute volume-attachment list --compartment-id <compartment_OCID> [OPTIONS]
```

    * Use [xx](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/volume-attachment/get.html) to list the details of a single volume attachment:
Copy
```
oci compute volume-attachment list --volume-id <volume_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use these APIs:
    * List all volume attachments in a compartment: [ListVolumeAttachments](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/ListVolumeAttachments)
    * List the details for a single volume attachment: [GetVolumeAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/GetVolumeAttachment)
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


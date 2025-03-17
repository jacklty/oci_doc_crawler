Updated 2024-10-07
# Listing Boot Volume Attachments
On Oracle Cloud Infrastructure, you can list the boot volume that is attached to an instance.
[Using the API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/listing-boot-volume-attachments.htm)
Use the [ListBootVolumeAttachments](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeAttachment/ListBootVolumeAttachments) operation to list the boot volume attached to an instance.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/listing-boot-volume-attachments.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/listing-boot-volume-attachments.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/listing-boot-volume-attachments.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    2. At the top of the page, select the compartment that contains the instance with boot volume attachment you want to see.
    3. Click the name of the instance for which you want to view the boot volume attachment.
    4. Under **Resources** , click **Attached Boot Volumes**.
The boot volume attachments are displayed.
    5. To view the details about an attachment, click the boot volume attachment name.
  * Use the [oci compute boot-volume-attachment list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/boot-volume-attachment/list.html) command and required parameters to list the boot volume attached to an instance.
Command
CopyTry It
```
oci compute boot-volume-attachment list --availability-domain <availability_domain_name> --compartment-id <compartment_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListBootVolumeAttachments](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeAttachment/ListBootVolumeAttachments) operation to list the boot volume attached to an instance.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


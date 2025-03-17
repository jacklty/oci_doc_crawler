Updated 2024-01-18
# Listing Boot Volumes
On Oracle Cloud Infrastructure, you can list all the boot volumes in a compartment. 
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/listing-boot-volumes.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/listing-boot-volumes.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/listing-boot-volumes.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Boot Volumes**.
    2. At the top of the page, select the compartment that contains the boot volume that you want to see.
A list of boot volumes is displayed.
    3. To view details about a boot volume, click the boot volume name.
  * Use the [oci bv boot-volume list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/list.html) command and required parameters to list the boot volumes in a compartment.
Command
CopyTry It
```
oci bv boot-volume list --availability-domain <availability_domain_name> --compartment-id <compartment_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListBootVolumes](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/ListBootVolumes) operation to list the boot volumes in a compartment.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


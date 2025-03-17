Updated 2024-01-18
# Deleting a Compute Cloud@Customer Infrastructure in OCI
You must delete only an infrastructure that is not connected to a Compute Cloud@Customer infrastructure in your data center. An infrastructure that is not connected is in the **Reject** state. 
If you need to disconnect an infrastructure, see [Connecting a Compute Cloud@Customer Infrastructure to OCI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/connecting.htm#connecting "The Compute Cloud@Customer infrastructure in the data center needs to be connected to Oracle Cloud Infrastructure \(OCI\) before it can be used. This task involves a bootstrap process during which a secure connection is established.")
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/delete-infrastructure.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/delete-infrastructure.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/delete-infrastructure.htm)


  *     1. In the Oracle Cloud Console, open the navigation menu, click **Hybrid** , and then click **Oracle Compute Cloud@Customer**.
    2. Click **Infrastructures**.
    3. In the list of infrastructures, find the one that you want to delete. If you don't see the infrastructure that you want, you might need to change compartments.
The connection state must be **Reject**.
    4. From the Actions menu for the infrastructure, select **Copy OCID**. You need the OCID to confirm deletion of the infrastructure.
    5. From the Actions menu for the infrastructure, select **Delete**.
    6. Confirm deletion by pasting the OCID of the infrastructure.
    7. Click **Delete**.
  * Use the [ccc infrastructure delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ccc/infrastructure/delete.html) command and required parameters to delete an infrastructure:
Command
CopyTry It
```
oci ccc infrastructure delete --infrastructure-id <infrastructure ocid> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteCccInfrastructure](https://docs.oracle.com/iaas/api/#/en/compute-cloud-at-customer/latest/CccInfrastructure/DeleteCccInfrastructure) operation to delete a Compute Cloud@Customer infrastructure.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


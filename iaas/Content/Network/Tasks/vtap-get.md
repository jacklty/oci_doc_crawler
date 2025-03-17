Updated 2025-02-18
# Getting a VTAP's Details
View the details for a Virtual Test Access Point (VTAP).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-get.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Network Command Center** , select **VTAPs**.
    2. Select the name of a VTAP to view its details.
The details page contains information about the VTAP, both general information and links to its resources. Some items in the page are read-only, while other items let you edit and update the VTAP's configuration. See [Updating a VTAP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-update.htm#top "Update the information for a Virtual Test Access Point \(VTAP\).").
  * Use the [vtap get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vtap/get.html) command and required parameters to view details about a VTAP:
Command
CopyTry It
```
oci network vtap get --vtap-id vtap_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetVtap](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vtap/GetVtap) operation to view details about a VTAP.


Was this article helpful?
YesNo


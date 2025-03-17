Updated 2025-02-18
# Listing VTAPs
List all Virtual Test Access Point (VTAPs) in a compartment. 
See [Virtual Test Access Points (VTAPs)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap.htm#vtap "A Virtual Test Access Point \(VTAP\) provides a way to mirror traffic from a selected source to a selected target to help in troubleshooting, security analysis, and data monitoring.") for more information and a feature overview.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-list.htm)


  * Open the **navigation menu** and select **Networking**. Under **Network Command Center** , select **VTAPs**.
The VTAPs and capture filters in the current compartment are listed.
  * Use the [vtap list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vtap/list.html) command and required parameters to list all VTAPs in a compartment:
Command
CopyTry It
```
oci network vtap list --compartment-id compartment_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListVtaps](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vtap/ListVtaps) operation to list all VTAPs in a compartment.


Was this article helpful?
YesNo


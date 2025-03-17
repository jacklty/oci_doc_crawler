Updated 2025-02-18
# Deleting a VTAP
Delete a Virtual Test Access Point (VTAP). 
For more information and a feature overview, see [Virtual Test Access Points (VTAPs)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap.htm#vtap "A Virtual Test Access Point \(VTAP\) provides a way to mirror traffic from a selected source to a selected target to help in troubleshooting, security analysis, and data monitoring.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-delete.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Network Command Center** , select **VTAPs**.
    2. Find the VTAP that you want to delete, select its the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Delete**.
    3. Confirm the deletion.
  * Use the [vtap delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vtap/delete.html) command and required parameters to delete a VTAP:
Command
CopyTry It
```
oci network vtap delete --vtap-id vtap_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteVtap](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vtap/DeleteVtap) operation to delete a VTAP.


Was this article helpful?
YesNo


Updated 2025-02-21
# Moving a Capture Filter to a Different Compartment
Move a capture filter from one compartment to another. 
For more information about capture filters and a feature overview, see [Virtual Test Access Points (VTAPs)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap.htm#vtap "A Virtual Test Access Point \(VTAP\) provides a way to mirror traffic from a selected source to a selected target to help in troubleshooting, security analysis, and data monitoring."). For information about compartments and access control, see [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-move.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-move.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-move.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Network Command Center** , select **Capture filters**.
    2. Find the capture filter that you want to move, select its the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Move Resource**.
    3. Select the destination compartment from the list, and then select **Move Resource**.
  * Use the [capture-filter change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/capture-filter/change-compartment.html) command and required parameters to move a capture filter to a different compartment:
Command
CopyTry It
```
oci network capture-filter change-compartment --capture-filter-id capture-filter_OCID --compartment-id compartment_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeCaptureFilterCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/CaptureFilter/ChangeCaptureFilterCompartment) operation to move a capture filter to a different compartment.


Was this article helpful?
YesNo


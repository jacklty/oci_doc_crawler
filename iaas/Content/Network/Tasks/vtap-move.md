Updated 2025-02-21
# Moving a VTAP to a Different Compartment
You can move a Virtual Test Access Point (VTAP) from one compartment to another.
For more information and a feature overview, see [Virtual Test Access Points (VTAPs)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap.htm#vtap "A Virtual Test Access Point \(VTAP\) provides a way to mirror traffic from a selected source to a selected target to help in troubleshooting, security analysis, and data monitoring.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-move.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-move.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-move.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Network Command Center** , select **VTAPs**.
    2. Find the VTAP that you want to move, select its the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Move Resource**.
    3. Select the destination compartment from the list, and then select **Move Resource**.
  * Use the [vtap change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vtap/change-compartment.html) command and required parameters to move a VTAP to a different compartment:
Command
CopyTry It
```
oci network vtap change-compartment --vtap-id vtap_OCID --compartment-id compartment_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeVtapCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vtap/ChangeVtapCompartment) operation to move a VTAP to a different compartment.


Was this article helpful?
YesNo


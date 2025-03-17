Updated 2025-02-18
# Updating a VTAP
Update the information for a Virtual Test Access Point (VTAP). 
For more information and a feature overview, see [Virtual Test Access Points (VTAPs)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap.htm#vtap "A Virtual Test Access Point \(VTAP\) provides a way to mirror traffic from a selected source to a selected target to help in troubleshooting, security analysis, and data monitoring.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-update.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-update.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-update.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Network Command Center** , select **VTAPs**.
    2. Select the VTAP that you want to update. 
    3. Select **Edit**.
       * If the VTAP is `RUNNING`, you can only update the name. 
       * If the VTAP is in the `STOPPED`, you can update the following options:
         * **Name**
         * **VCN**
         * **Source**
         * **Target**
         * **Capture filter**
       * Under **Show Advanced Options** , you can update the following options:
         * **VXLAN network identifier (VNI)**
         * **Max packet size**
         * **Priority Mode**
         * **Tagging**
For information about the options, see [Creating a VTAP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-create.htm#top "Create a Virtual Test Access Point \(VTAP\) to mirror traffic from a chosen source to a selected target to help troubleshooting, security analysis, and data monitoring.").
    4. Select **Save Changes**.
  * Use the [vtap update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vtap/update.html) command and required parameters to edit a VTAP:
Command
CopyTry It
```
oci network vtap update --vtap-id vtap_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateVtap](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vtap/UpdateVtap) operation to edit a VTAP.


Was this article helpful?
YesNo


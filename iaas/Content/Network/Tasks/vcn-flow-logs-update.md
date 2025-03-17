Updated 2025-02-18
# Editing a Flow Log
Change the configuration information for a VCN flow log.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-update.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-update.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-update.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Network Command Center** , select **Flow logs**.
    2. Under **List scope** , select the compartment that contains the flow log.
    3. Under **Filter** , select a lifecycle state and log group that contains the flow log.
    4. Select the name of the flow log you want to update.
    5. Select **Edit**.
    6. Make the changes and then select **Save changes**.
  * Use the [oci logging log update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log/update.htm) command and required parameters to edit a flow log:
Command
CopyTry It
```
oci logging log update --log-group-id log-group_ocid --log-id log_ocid [OPTIONS]
```

For a complete list of parameters and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateLog](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/Log/UpdateLog) operation to edit a log.


Was this article helpful?
YesNo


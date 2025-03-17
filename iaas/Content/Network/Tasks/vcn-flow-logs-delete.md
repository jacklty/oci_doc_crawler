Updated 2025-02-18
# Deleting a Flow Log
Delete a VCN flow log.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-delete.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Network Command Center** , select **Flow logs**.
    2. Under **List scope** , select a compartment that contains the flow log.
    3. Under **Filter** , select a lifecycle state and log group that contains the flow log. 
    4. Find the flow log that you want to delete, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Delete**.
    5. Confirm the deletion.
  * Run the [DeleteLog](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/Log/DeleteLog) operation to delete a flow log from a log group.
  * Use the [oci logging log delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/logging/log/delete.htm) command and required parameters to delete a flow log from a log group:
Command
CopyTry It
```
oci logging log delete --log-group-id log_group_ocid --log-id log_ocid [OPTIONS]
```

For a complete list of parameters and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).


Was this article helpful?
YesNo


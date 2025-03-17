Updated 2025-01-15
# Deleting a Remote Peering Connection
Delete a remote peering connection (RPC).
Deleting an RPC also terminates the peering connection. The RPC at the other side of the peering changes to the REVOKED state.
This is an asynchronous operation; the RPC's _lifecycleState_ changes to TERMINATING temporarily until the RPC is completely removed.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-delete.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select a compartment that you have permission to work in.The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Click the name of the DRG you're interested in.
    4. Under **Resources** , click **Remote Peering Connection attachments**.
    5. In the table, click the name of the remote peering connection you're interested in.
    6. Click **Terminate**.
    7. Click **Terminate peering connection** to confirm the deletion. 
  * Use the [network remote-peering-connection delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/remote-peering-connection/delete.html) command and required parameters to delete an RPC:
Command
CopyTry It
```
oci network remote-peering-connection delete --remote-peering-connection-id rcp-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteRemotePeeringConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RemotePeeringConnection/DeleteRemotePeeringConnection) operation to delete an RPC.


Was this article helpful?
YesNo


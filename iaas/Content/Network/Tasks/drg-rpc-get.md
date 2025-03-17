Updated 2025-01-15
# Getting Remote Peering Connection Details
Get details for the specified remote peering connection (RPC).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-get.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select a compartment that you have permission to work in.The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Click the name of the DRG you're interested in.
    4. Under **Resources** , click **Remote Peering Connections**.
    5. Click the name of the RPC you're interested in. 
  * Use the [network remote-peering-connection get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/remote-peering-connection/get.html) command and required parameters to get details for the specified RPC:
Command
CopyTry It
```
oci network remote-peering-connection get --remote-peering-connection-id rpc-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetRemotePeeringConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RemotePeeringConnection/GetRemotePeeringConnection) operation to get details for the specified RPC.


Was this article helpful?
YesNo


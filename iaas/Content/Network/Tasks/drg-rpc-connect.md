Updated 2025-01-15
# Connecting Two Remote Peering Connections
Connects an RPC object to an RPC object on another DRG.
**Prerequisite:** The requestor must have:
  * The region the acceptor's VCN is in (the requestor's tenancy must be subscribed to the region).
  * The OCID of the acceptor's RPC.


The requestor RPC must perform this task.
When the connection is no longer needed, the RPCs can be disconnected by deleting one of the RPCs.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-connect.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-connect.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-connect.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select a compartment that you have permission to work in.The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Click the name of the DRG you're interested in.
    4. Under **Resources** , click **Remote Peering Connections**.
    5. Click the name of the RPC of the requestor RPC from the list.
    6. Click **Establish Connection**.
Enter the following: 
       * **Region:** The region that contains the acceptor's VCN. The drop-down list includes only those regions that both support remote VCN peering and your tenancy is subscribed to.
       * **Remote Peering Connection OCID:** The OCID of the acceptor's RPC. 
    7. Click **Establish Connection**.
The connection is established and the RPC's state changes to PEERED.
  * Use the [network remote-peering-connection connect](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/remote-peering-connection/connect.html) command and required parameters to connect an RPC to an RPC on another DRG:
Command
CopyTry It
```
oci network remote-peering-connection connect --peer-id acceptor-ocid --peer-region-name region --remote-peering-connection-id rpc-ocid ... [OPTIONS]
```

The region names that could be used for `--peer-region-name` are listed in [Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). For example: `us-ashburn-1`.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ConnectRemotePeeringConnections](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RemotePeeringConnection/ConnectRemotePeeringConnections) operation to connect an RPC to an RPC on another DRG.


Was this article helpful?
YesNo


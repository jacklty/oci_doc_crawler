Updated 2025-01-15
# Listing Remote Peering Connections
List the remote peering connections (RPCs) for a specified DRG and compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-list.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select a compartment that you have permission to work in.The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Click the name of the DRG you're interested in.
    4. Under **Resources** , click **Remote Peering Connections**.
  * Use the [network remote-peering-connection list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/remote-peering-connection/list.html) command and required parameters to list the RPCs for a specified compartment:
Command
CopyTry It
```
oci network remote-peering-connection list --compartment-id compartment-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListRemotePeeringConnections](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RemotePeeringConnection/ListRemotePeeringConnections) operation to list the RPCs for a specified compartment.


Was this article helpful?
YesNo


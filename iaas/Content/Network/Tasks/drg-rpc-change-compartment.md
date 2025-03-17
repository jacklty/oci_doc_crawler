Updated 2025-01-15
# Moving an RPC to a Different Compartment
Move a remote peering connection (RPC) to a different compartment within the same tenancy.
For information about moving resources between compartments, see [Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-change-compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-change-compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rpc-change-compartment.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select a compartment that you have permission to work in.The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Click the name of the DRG you're interested in.
    4. Under **Resources** , click **Remote Peering Connections**.
    5. Find the RPC in the list, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Move Resource**.
    6. Choose the destination compartment from the list. 
    7. Click **Move Resource**.
  * Use the [network remote-peering-connection change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/remote-peering-connection/change-compartment.html) command and required parameters to move an RPC to a different compartment within the same tenancy:
Command
CopyTry It
```
oci network remote-peering-connection change-compartment --compartment-id target-compartment-ocid --remote-peering-connection-id rpc-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeRemotePeeringConnectionCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RemotePeeringConnection/ChangeRemotePeeringConnectionCompartment) operation to move an RPC to a different compartment within the same tenancy.


Was this article helpful?
YesNo


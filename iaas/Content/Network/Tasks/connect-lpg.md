Updated 2025-01-17
# Connecting to Another LPG
Connect a local peering gateway (LPG) to another one in a different virtual cloud network (VCN) in the same region.
The [requestor](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Importan) must perform this task, and must have the OCID of the acceptor's LPG. 
After you peer an LPG to an LPG in another VCN, you can't peer it to a different LPG. For details, see [Repurposing an LPG fails](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/vcn_troubleshooting.htm#lpg-delete).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/connect-lpg.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/connect-lpg.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/connect-lpg.htm)


  * **Tip** If you're using the Console and the peering is between two VCNs in the same tenancy: Instead of specifying the acceptor's LPG OCID, you can instead pick the acceptor's VCN and LPG from lists of resources in the tenancy. However, you need to know both the name and compartment of the acceptor's VCN and LPG instead of the LPG's OCID. For reference, see [Task B: Share information](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#share_info).
    1. In the Console, view the details for the requestor LPG that you want to connect to the acceptor LPG:
      1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
      2. Select the name of the VCN that the LPG belongs to. 
      3. Under **Resources** , select **Local Peering Gateways**. 
    2. For the requestor LPG, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Establish Peering Connection**.
    3. Specify the LPG that you want to peer with: 
       * If the VCNs are in different tenancies: Select **Enter Local Peering Gateway OCID** , and enter the acceptor LPG's OCID.
       * If the VCNs are in the same tenancy: Perform one of the following actions:
         * Select **Enter Local Peering Gateway OCID** , and enter the acceptor LPG's OCID.
         * Select **Browse Below** , and then select the acceptor's VCN and LPG from the lists provided. Remember that the VCN and LPG each might be in a different compartment than the one you're working in.
    4. Select **Establish Peering Connection**.
The connection is established, and the LPG's state changes to PEERED.
At this point, the details of each LPG update to show the **Peer VCN CIDR Block** value for the other VCN. This is the CIDR of the other VCN across the peering from the LPG. Each administrator can use this information to update the route tables and security rules for their own VCN.
  * Use the [network local-peering-gateway connect](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/local-peering-gateway/connect.html) command and required parameters to connect this local peering gateway (LPG) to another one in the same region:
Command
CopyTry It
```
oci network local-peering-gateway update --local-peering-gateway-id this-ocid --peer-id peer-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ConnectLocalPeeringGateways](https://docs.oracle.com/iaas/api/#/en/iaas/latest/LocalPeeringGateway/ConnectLocalPeeringGateways) operation to connect this local peering gateway (LPG) to another one in the same region.


Was this article helpful?
YesNo


Updated 2025-01-17
# Listing NAT Gateways
List the NAT gateway in a VCN.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-list.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the name of the VCN you're interested in.
    3. Under **Resources** , select **NAT Gateways**. 
  * Use the [network nat-gateway list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nat-gateway/list.htm) command and required parameters to list the NAT gateways in a compartment:
Command
CopyTry It
```
oci network nat-gateway list --compartment-id compartment-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListNatGateways](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NatGateway/ListNatGateways) operation to list the NAT gateways in a compartment.


Was this article helpful?
YesNo


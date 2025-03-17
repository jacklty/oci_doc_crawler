Updated 2025-01-17
# Getting Details for the NAT Gateway
Get detailed information for the specified NAT gateway.
A VCN only needs one NAT gateway.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-get.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the name of the VCN you're interested in.
    3. Under **Resources** , select **NAT Gateways**. 
  * Use the [network nat-gateway get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nat-gateway/get.htm) command and required parameters to get information about the NAT gateway:
Command
CopyTry It
```
oci network nat-gateway get --nat-gateway-id nat-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetNatGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NatGateway/GetNatGateway) operation to get information about the NAT gateway.


Was this article helpful?
YesNo


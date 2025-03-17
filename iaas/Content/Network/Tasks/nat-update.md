Updated 2025-01-17
# Updating a NAT Gateway
Update the display name for a NAT gateway in a Virtual Cloud Network (VCN) in Networking.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-update.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-update.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-update.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the name of the VCN that you're interested in.
    3. Under **Resources** , select **NAT Gateways**. 
    4. For the NAT gateway that you're interested in, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Edit**.
    5. Enter the new name and select **Save Changes**. 
  * Use the [network nat-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nat-gateway/update.htm) command and required parameters to update the display name for a NAT gateway:
Command
CopyTry It
```
oci network nat-gateway update --nat-gateway-id nat-ocid --display-name new-name ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateNatGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NatGateway/UpdateNatGateway) operation to update the display name for a NAT gateway.


Was this article helpful?
YesNo


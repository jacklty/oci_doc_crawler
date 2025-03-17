Updated 2025-01-17
# Updating the Name of an LPG
Change the name of a local peering gateway (LPG) in a virtual cloud network (VCN).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-lpg.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-lpg.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-lpg.htm)


  * This task can't be performed using the Console.
  * Use the [network local-peering-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/local-peering-gateway/update.html) command and required parameters to change the name of a local peering gateway (LPG):
Command
CopyTry It
```
oci network local-peering-gateway update --local-peering-gateway-id ocid --display-name new-name ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateLocalPeeringGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/LocalPeeringGateway/UpdateLocalPeeringGateway) operation to change the name of a local peering gateway.


Was this article helpful?
YesNo


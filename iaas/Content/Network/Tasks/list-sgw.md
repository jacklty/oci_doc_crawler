Updated 2025-01-15
# Listing Service Gateways
List the service gateways (SGWs) available in a given compartment.
The Console can only show the service gateway attached to a specific VCN (only one SGW is needed in a VCN), but the API and CLI can show all SGWs in a specified compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-sgw.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-sgw.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-sgw.htm)


  *     1. In the Console, confirm you're viewing the compartment that contains the VCN or VCNs that you're interested in. For information about compartments and access control, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). 
    2. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    3. Click the name of the VCN that has the SGW you're interested in.
    4. On the left side of the page, click **Service Gateways**.
A VCN only requires one service gateway.
  * Use the [network service-gateway list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/list.html) command and required parameters to list all service gateways in a specified compartment:
Command
CopyTry It
```
oci network service-gateway list --compartment-id compartment-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListServiceGateways](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/ListServiceGateways) operation to list service gateways in a specified compartment.


Was this article helpful?
YesNo


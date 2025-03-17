Updated 2025-01-15
# Getting Details for a Service Gateway
View the settings for a particular service gateway (SGW).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-sgw.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-sgw.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-sgw.htm)


  *     1. In the Console, confirm you're viewing the compartment that contains the VCN with the SGW you're interested in. For information about compartments and access control, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). 
    2. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    3. Click the name of the VCN that has the SGW you're interested in.
    4. On the left side of the page, click **Service Gateways**.
Details for the service gateway are shown in a table below the VCN information. 
  * Use the [network service-gateway get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/get.html) command and required parameters to get details for a service gateway:
Command
CopyTry It
```
oci network service-gateway get --service-gateway-id sgw-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetServiceGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/GetServiceGateway) operation to get details for a service gateway.


Was this article helpful?
YesNo


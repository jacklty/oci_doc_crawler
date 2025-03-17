Updated 2025-01-15
# Deleting a Service Gateway
Delete a service gateway in a Virtual Cloud Network (VCN) to remove access to the Oracle Services Network (OSN).
**Prerequisite:** The service gateway doesn't have to block traffic, but there must not be a route table that lists it as a target.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-sgw.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-sgw.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-sgw.htm)


  *     1. In the Console, confirm you're viewing the compartment that contains the VCN with the service gateway that you want to delete. For information about compartments and access control, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). 
    2. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    3. Click the name of the VCN with the service gateway that you want to delete.
    4. Under **Resources** , click **Service Gateways**.
    5. For the service gateway you want to delete, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Terminate**.
    6. Confirm when prompted.
  * Use the [network service-gateway delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/delete.html) command and required parameters to delete a service gateway:
Command
CopyTry It
```
oci network service-gateway delete --service-gateway-id sgw-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteServiceGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/DeleteServiceGateway) operation to delete a service gateway.


Was this article helpful?
YesNo


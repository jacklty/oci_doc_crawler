Updated 2025-01-15
# Updating a Service Gateway's Route Table Association 
You can update a service gateway in a Virtual Cloud Network (VCN) to associate it with a route table or change the existing route table association.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-sgw.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-sgw.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-sgw.htm)


  *     1. In the Console, confirm that you're viewing the compartment that contains the VCN with the service gateway that you're interested in. For information about compartments and access control, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). 
    2. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    3. Click the name of the VCN that has the service gateway that you want to update.
    4. Under **Resources** , click **Service Gateways**.
    5. For the service gateway you're interested in, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select one of the following options:
    6.        * **Associate With Route Table:** If the service gateway has no route table associated with it yet.
       * **Associate Different Route Table:** If you're changing which route table is associated with the service gateway.
    7. Select the compartment where the route table resides, and then select the route table itself.
    8. Click **Associate**.
  * Use the [network service-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/update.html) command and required parameters to update details for a service gateway:
Command
CopyTry It
```
oci network service-gateway update --service-gateway-id sgw-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateServiceGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/UpdateServiceGateway) operation to update details for a service gateway.


Was this article helpful?
YesNo


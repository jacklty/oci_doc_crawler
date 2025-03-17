Updated 2025-01-15
# Associating a Route Table with an Existing Service Gateway
Associate a route table with a service gateway.
You perform this task only if you're implementing an [advanced transit routing scenario](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm#Transit_Routing_Private_Access_to_Oracle_Services).
A service gateway can exist without a route table associated with it. However, after you associate a route table with a service gateway, there must always be a route table associated with it. But, you can associate a _different_ route table. You can also edit the table's rules, or delete some or all of the rules.
**Prerequisite:** The route table must exist and belong to the VCN that the service gateway belongs to.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/sgw-rt.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/sgw-rt.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/sgw-rt.htm)


  *     1. In the Console, confirm you're viewing the compartment that contains the VCN with the SGW you're interested in. For information about compartments and access control, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). 
    2. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    3. Click the name of the VCN that has the SGW you're interested in.
    4. On the left side of the page, click **Service Gateways**.
    5. For the service gateway you're interested in, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Edit**.
    6. (Optional) 
  * Use the [network service-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/update.html) command and required parameters to assign or update a route table to a service gateway:
Command
CopyTry It
```
oci network service-gateway update --service-gateway-id sgw-ocid --route-table-id rt-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateServiceGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/UpdateServiceGateway) operation to associate a route table with a service gateway, using the `routeTableId` parameter.


Was this article helpful?
YesNo


Updated 2025-01-15
# Moving a Service Gateway to a Different Compartment 
Move a service gateway into a different compartment within the same tenancy.
For information about moving resources between compartments, see [Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
When you move a service gateway to a new compartment, policies set for that new compartment apply immediately. 
The service gateway moves to the new compartment immediately. Depending on your permissions, you can select the compartment in the left side menu to view the service gateway. 
For more information about using compartments and policies to control access to your cloud network, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). For general information about compartments, see [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm). 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-sgw.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-sgw.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-sgw.htm)


  *     1. In the Console, confirm you're viewing the compartment that contains the VCN with the SGW you're interested in. For information about compartments and access control, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). 
    2. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    3. Click the name of the VCN that has the SGW you're interested in.
    4. On the left side of the page, click **Service Gateways**.
    5. For the service gateway you're interested in, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Move Resource**.
    6. Choose the destination compartment from the list. 
    7. Click **Move Resource**.
  * Use the [network service-gateway change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/change-compartment.html) command and required parameters to move a service gateway into a different compartment:
Command
CopyTry It
```
oci network service-gateway change-compartment --service-gateway-id sgw-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeServiceGatewayCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/ChangeServiceGatewayCompartment) operation to move a service gateway into a different compartment.


Was this article helpful?
YesNo


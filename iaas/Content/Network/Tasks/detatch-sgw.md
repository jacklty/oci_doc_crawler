Updated 2025-01-15
# Removing or Changing a Service Gateway's Service CIDR label
Remove or change a specified service CIDR label from the specified service gateway. 
**Important**
Because Object Storage is covered by both **OCI <region> Object Storage** and **All <region> Services in Oracle Services Network**, a service gateway can use **only one of those service CIDR labels**. Likewise, a route table can have a single rule for one of the service CIDR labels. It cannot have two separate rules, one for each label.
If the service gateway is configured to use **All <region> Services in Oracle Services Network**, the route rule can use either CIDR label. However, if the service gateway is configured to use **OCI <region> Object Storage** and the route rule uses **All <region> Services in Oracle Services Network**, traffic to services in the Oracle Services Network except Object Storage will be blackholed. The Console prohibits you from configuring the service gateway and corresponding route table in that manner.
If you want to switch the service gateway to use a different service CIDR label, see [When You Switch to a Different Service CIDR Label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/service-gateway_management.htm#switch_label).
Once you have assigned a service CIDR label to a service gateway, the Console will allow you to [switch to the other label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/service-gateway_management.htm#switch_label), but the service gateway must always have a service CIDR label. The API and CLI will allow you to remove the service CIDR label completely.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/detatch-sgw.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/detatch-sgw.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/detatch-sgw.htm)


  * You can't completely remove the service CIDR label using the Console after you've assigned this option. This operation is available in the CLI and API. The steps below can be used to change the assigned service CIDR label to the other option provided. 
    1. In the Console, confirm you're viewing the compartment that contains the VCN with the SGW you're interested in. For information about compartments and access control, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). 
    2. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    3. Click the name of the VCN that has the service gateway that you're interested in.
    4. Under **Resources** , click **Service Gateways**.
    5. For the service gateway that you're interested in, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Edit**.
    6. In the **Services:** field, choose the other [service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#overview). Without a service CIDR label enabled for the gateway, no traffic flows through it.
    7. Click **Save changes**.
**What's Next**
    * Remove any route rules for that service CIDR label and gateway. Do this for the route tables for any subnets that no longer need to access the service CIDR label through the gateway. See instructions in [Task 2: Update routing for the subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#task_update_routing).
    * Remove any security rules for that service CIDR label. Do this for the security lists for any subnets that no longer need to access the service CIDR label. See instructions in [Task 3: (Optional) Update security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#task_update_security_list).
  * Use the [network service-gateway detach](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/detach.html) command and required parameters to remove a [service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#overview) from a service gateway:
Command
CopyTry It
```
oci network service-gateway detach --service-gateway-id sgw-ocid --service-id service-ocid ... [OPTIONS]
```

The service gateway can only have one service CIDR label at a time. If you're trying to change the service CIDR label, remove the old service CIDR label and then use the [network service-gateway attach](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/attach.html) command and required parameters to add the desired [service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#overview) to the service gateway:
Command
CopyTry It
```
oci network service-gateway attach --service-gateway-id sgw-ocid --service-id service-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DetachServiceId](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/DetachServiceId) operation to remove a [service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#overview) for a service gateway.
The service gateway can only have one service CIDR label at a time. If you're trying to change the service CIDR label, first remove the old service CIDR label and then run the [AttachServiceId](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/AttachServiceId) operation to add a new service CIDR label to a service gateway. 
Use [ListServices](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Service/ListServices) to determine the available service CIDR labels. [GetService](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Service/GetService): Gets the details for a particular service CIDR label.


Was this article helpful?
YesNo


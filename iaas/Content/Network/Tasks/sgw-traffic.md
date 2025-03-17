Updated 2025-01-15
# Controlling Traffic for a Service Gateway
You can block or allow traffic for a service gateway in a virtual cloud network (VCN).
You create a service gateway in the context of a specific VCN. In other words, the service gateway is always attached to that one VCN. However, you can block or allow traffic through the service gateway at any time. By default, the gateway allows traffic flow upon creation. Blocking the service gateway traffic prevents all traffic from flowing, regardless of what service CIDR labels are enabled, or any existing route rules or security rules in your VCN. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/sgw-traffic.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/sgw-traffic.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/sgw-traffic.htm)


  *     1. In the Console, confirm that you're viewing the compartment that contains the VCN with the service gateway that you're interested in. For information about compartments and access control, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). 
    2. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    3. Click the name of the VCN that has the service gateway that you're interested in.
    4. Under **Resources** , click **Service Gateways**.
    5. For the service gateway that you're interested in, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Block Traffic** (or **Allow Traffic** if you're enabling traffic for the service gateway).
When the traffic is blocked, the service gateway's icon turns gray, and the State label changes to Blocked. When the traffic is allowed, the service gateway's icon turns green, and the State label changes to Available.
  * Use the [network service-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/update.html) command and required parameters to block or allow traffic for a service gateway:
Command
CopyTry It
```
oci network service-gateway update --service-gateway-id sgw-ocid --block-traffic [true|false] ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateServiceGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/UpdateServiceGateway) operation to block or allow traffic for a service gateway, using the `blockTraffic` attribute.


Was this article helpful?
YesNo


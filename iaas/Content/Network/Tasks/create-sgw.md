Updated 2025-01-15
# Creating a Service Gateway
Create a service gateway in a Virtual Cloud Network (VCN) to allow access to the Oracle Services Network (OSN).
Only one service gateway is needed for each VCN. All subnets within a VCN have access to the service gateway if the security rules and route table rules allow that access.
This task assumes that you already have a VCN with at least one subnet (either private or public).
**Important**
The service gateway allows access to supported Oracle services within the region to protect your data from the internet. Your applications might require access to public endpoints or services not supported by the service gateway (for example, to download updates or patches). Ensure you have a [NAT gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/NATgateway.htm#NAT_Gateway) or other access to the internet if necessary.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-sgw.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-sgw.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-sgw.htm)


  *     1. In the Console, confirm that you're viewing the compartment that contains the VCN that you want to add the service gateway to. For information about compartments and access control, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    2. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    3. Click the name of the VCN in which you want to create the service gateway.
    4. Under **Resources** , click **Service Gateways**.
    5. Click **Create Service Gateway**.
    6. Enter the following values: 
       * **Name:** A descriptive name for the service gateway. It doesn't have to be unique. Avoid entering confidential information.
       * **Create in Compartment** : The compartment in which you want to create the service gateway, if different from the compartment you're currently working in. 
       * **Services:** (Optional) Select the [service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#overview) that you're interested in. If you don't select one now, you can update the service gateway later and [add a service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-sgw.htm#attach-sgw "Add a specified service CIDR label to the service gateway.") then. Without a service CIDR label enabled for the gateway, no traffic flows through it.
       * **Route Table Association:** (Advanced option) You can associate a specific VCN route table with this gateway. If you associate a route table, afterwards the gateway must always have a route table associated with it. You can modify the rules in the current route table or replace it with another route table. 
       * **Tags:** (Advanced option) If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. 
    7. Click **Create Service Gateway**.
The service gateway is then created and displayed on the **Service Gateways** page in the compartment that you chose. The gateway allows traffic through it by default. At any time, you can [block or allow the traffic through it](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/sgw-traffic.htm#sgw-traffic "You can block or allow traffic for a service gateway in a virtual cloud network \(VCN\).").
  * Use the [network service-gateway create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/create.html) command and required parameters to create a service gateway:
Command
CopyTry It
```
oci network service-gateway create --compartment-id ocid --vcn-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateServiceGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/CreateServiceGateway) operation to create a service gateway.


Was this article helpful?
YesNo


Updated 2024-12-16
# Creating a Service Gateway
On Compute Cloud@Customer, you can create one service gateway per VCN. The service gateway is automatically attached to the VCN it's created in. Services use CIDR labels, and are allowed by default. 
For each enabled Service, you need a route rule with the Service object’s CIDR block as the rule destination and the service gateway as the rule target.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-service-gateway.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-service-gateway.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-service-gateway.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN for which you want to create a Service Gateway.
    3. Click the name of the VCN. 
    4. Under **Resources** , click **Service Gateways**.
The number of configured Service Gateways in parentheses must be zero (0).
    5. Click **Create Service Gateway**.
    6. Fill in the required information:
       * **Name:** Provide a name or description for the Service Gateway.
Avoid entering confidential information.
       * **Create in Compartment:** Select the compartment in which to create the Service Gateway.
       * **Services:** Select the service from the list.
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    7. Click **Create Service Gateway**.
The Service Gateway is now ready for the addition of route rules or security settings.
  * Use the [oci network service-gateway create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/service-gateway/create.html) command and required parameters to create a new service gateway in the specified compartment.
Copy
```
oci network service-gateway create [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateServiceGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ServiceGateway/CreateServiceGateway) operation to create a new service gateway in the specified compartment.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


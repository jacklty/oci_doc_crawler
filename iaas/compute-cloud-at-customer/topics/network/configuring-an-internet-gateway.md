Updated 2024-12-16
# Configuring an Internet Gateway
On Compute Cloud@Customer, you can configure an Internet Gateway (IGW) which provides the VCN with outside access through the on-premises data center network. 
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/configuring-an-internet-gateway.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/configuring-an-internet-gateway.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/configuring-an-internet-gateway.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN where the internet gateway will be created.
    3. Click the name of the VCN. 
The VCN details page is displayed.
    4. Under **Resources** , click **Internet Gateways**.
    5. Click **Create Internet Gateway**.
    6. Enter the following information:
       * **Name:** Provide a descriptive name for the internet gateway. Avoid entering confidential information
       * **Create in Compartment:** Select the compartment in which to create the Internet Gateway. 
       * **Enabled:** Use the toggle to decide if the gateway is enabled at creation or not. The default is to enable the gateway:
         * **(Yes: Gateway Enabled** : By default, the VCN uses the gateway when created.
         * **(No: Gateway Disabled)** : You can set the gateway not see traffic until it's explicitly enabled to do so.
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    7. Click **Create Internet Gateway**.
The Internet Gateway is now ready for the addition of route rules or security settings. See [Configuring VCN Rules and Options](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/configuring-vcn-rules-and-options.htm#configuring-vcn-rules-and-options "On Compute Cloud@Customer, VCNs and their subnets have various rules and options associated with them. The main categories are the use of DHCP, route tables, and security. If you do not configure these rules and options explicitly, the system uses default values.").
  * Use the [oci network internet-gateway create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/internet-gateway/create.html) command and required parameters to create a new internet gateway for the specified VCN.
Copy
```
oci network internet-gateway create [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateInternetGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InternetGateway/CreateInternetGateway) operation to create a new internet gateway for the specified VCN.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


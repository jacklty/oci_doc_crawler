Updated 2024-04-02
# Deleting an Internet Gateway
On Compute Cloud@Customer, If you have previously configured an IGW, you can delete it.
The internet gateway doesn't have to be disabled, but there must not be a route table that lists it as a target.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-an-internet-gateway.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-an-internet-gateway.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-an-internet-gateway.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN that has the internet gateway.
    3. Click the name of the VCN. 
The VCN details page is displayed.
    4. Under **Resources** , click **Internet Gateways**.
    5. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Delete**.
    6. Confirm the deletion.
  * Use the [oci network internet-gateway delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/internet-gateway/delete.html) command and required parameters to delete the specified internet gateway.
Copy
```
oci network internet-gateway delete [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteInternetGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InternetGateway/DeleteInternetGateway) operation to delete the specified internet gateway.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


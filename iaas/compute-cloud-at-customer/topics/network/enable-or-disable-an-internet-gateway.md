Updated 2024-04-02
# Enable or Disable an Internet Gateway
On Compute Cloud@Customer, you can enable or disable an Internet gateway.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/enable-or-disable-an-internet-gateway.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/enable-or-disable-an-internet-gateway.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/enable-or-disable-an-internet-gateway.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN that has the internet gateway.
    3. Click the name of the VCN. 
The VCN details page is displayed.
    4. Under **Resources** , click **Internet Gateways**.
    5. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Edit**.
    6. Set the **Enabled** toggle:
       * Slide the toggle right to enable the internet gateway.
       * Slide the toggle left to disable the internet gateway.
    7. Click **Update**.
  * Use the [oci network internet-gateway update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/internet-gateway/update.html) command and required parameters to update the specified internet gateway. You can disable/enable it, or change its display name or tags.
Copy
```
oci network internet-gateway update [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateInternetGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InternetGateway/UpdateInternetGateway) command and required parameters to the specified internet gateway. You can disable/enable it, or change its display name or tags.
Copy
```
SYNTX [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).


Was this article helpful?
YesNo


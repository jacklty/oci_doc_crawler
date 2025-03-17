Updated 2025-01-15
# Deleting an Ephemeral Public IP From an Instance
Deleting an ephemeral public IP automatically unassigns it from its private IP.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/deleting-ephemeral-public-ip-from-instance.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/deleting-ephemeral-public-ip-from-instance.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/deleting-ephemeral-public-ip-from-instance.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Click the instance to view its details. 
    3. Under **Resources** , click **Attached VNICs** to display the primary VNIC and any secondary VNICs attached to the instance.
    4. Click the VNIC that you're interested in.
    5. Under **Resources** , click **IP addresses** to display the VNIC's primary private IP and any secondary private IPs.
    6. For the VNIC's primary private IP, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Edit**.
    7. In the **Public IP address** section, for **Public IP type** , select the radio button for **No public IP**. 
    8. Click **Update**. 
  * Use the [network public-ip delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/delete.html) command and required parameters to delete an ephemeral public IP:
Command
CopyTry It
```
oci network public-ip delete --public-ip-id Public_IP_OCID ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeletePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/DeletePublicIp) operation to delete a public IP.


Was this article helpful?
YesNo


Updated 2025-01-15
# Changing the Display Name for an Ephemeral Public IP
You can change the display name of an ephemeral public IP.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/change-display-ephermal-ip.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/change-display-ephermal-ip.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/change-display-ephermal-ip.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Click the instance to view its details. 
    3. Under **Resources** , click **Attached VNICs** to display the primary VNIC and any secondary VNICs attached to the instance.
    4. Click the VNIC that you're interested in.
    5. Under **Resources** , click **IP addresses** to display the VNIC's primary private IP and any secondary private IPs.
    6. For the VNIC's primary private IP, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Edit**.
    7. In the **Public IP address** section, for **Public IP type** , select the radio button for **Ephemeral public IP**. 
    8. In the **Public IP Address** section, edit the **Ephemeral Public IP Name**. The name doesn't have to be unique, and you can change it later. Avoid entering confidential information.
    9. Click **Update**. 
  * Use the [network public-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/update.html) command and required parameters to change the display name of an ephemeral public IP:
Command
CopyTry It
```
oci network public-ip update --public-ip-id Public_IP_ID --display-name new_display_name ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/UpdatePublicIp) operation to update the display name for a public IP.


Was this article helpful?
YesNo


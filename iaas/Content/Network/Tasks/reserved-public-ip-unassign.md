Updated 2025-01-15
# Unassigning a Reserved Public IP
Unassign a reserved public IP object in Oracle Cloud Infrastructure.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-unassign.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-unassign.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-unassign.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Under **List scope** , select the compartment that contains the instance using the private IP address to which you want to assign a public IP object.
    3. Click the name of an instance to view its details.
    4. Under **Resources** , click **Attached VNICs** to display the primary VNIC and any secondary VNICs attached to the instance.
    5. Click the name of the VNIC that uses the private IP address.
    6. Under **Resources** , click **IPv4 Addresses** to display the VNIC's primary private IP address and any secondary private IP addresses.
    7. For the private IP to which you want to assign the public address, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and select **Edit**.
    8. If the private IP address already has a public IP assigned to it, unassign it as follows: 
      1. In the **Public IP Type** section of the **Edit Private IP Address** dialog box, select n for **No Public IP**. 
      2. Click **Update**.
      3. Again for private IP address, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and select **Edit**.
    9. In the **Public IP Type** section of the **Edit Private IP Address** dialog box, select **Reserved Public IP** , and then select **Select Existing Reserved IP Address**. 
    10. In the **Reserved IP Address in _< compartment>_** list, select the reserved public IP object that you want to assign, changing the compartment as needed. 
The public IP object is moved from the private IP address that it's currently assigned to. 
    11. Click **Update**. 
  * Use the [network public-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/update.html) command and required parameters to unassign a reserved public IP address from a private IP:
Command
CopyTry It
```
oci network public-ip update --public-ip-id public_IP_OCID --private-ip-id EMPTY_STRING ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/UpdatePublicIp) operation to unassign a reserved public IP address from a private IP address.


Was this article helpful?
YesNo


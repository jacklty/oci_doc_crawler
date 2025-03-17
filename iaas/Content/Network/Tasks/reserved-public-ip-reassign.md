Updated 2025-01-15
# Reassigning a Reserved Public IP to a Different Private IP
Move a reserved public IP object from one private IP address to another.
As an example, let's say that you want to move a reserved public IP object from private IP A to private IP B. First, you must ensure that private IP B doesn't have a public IP already assigned to it. Then, you assign the reserved public IP to private IP B. When you do so, it is automatically unassigned from private IP A.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-reassign.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-reassign.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-reassign.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Under **List scope** , select the compartment that contains the instance using the private IP address to which you want to unassign a public IP object.
    3. Under **Resources** , click **Attached VNICs** to display the primary VNIC and any secondary VNICs attached to the instance.
    4. Click the VNIC that you're interested in.
    5. Under **Resources** , click **IP Addresses** to display the VNIC's primary private IP and any secondary private IPs.
    6. For private IP 2, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Edit**.
    7. If private IP 2 already has a public IP assigned to it:
      1. In the **Public IP Type** section, select the radio button for **No Public IP**. 
      2. Click **Update**.
      3. Again for private IP 2, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Edit**.
    8. In the **Public IP Type** section, select the radio button for **Reserved Public IP**
    9. In the **Reserved Public IP** list, select the reserved public IP that you want to assign. The IP is moved from the public IP it's assigned to.
    10. Click **Update**. 
  * Use the [network public-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/update.html) command and required parameters to reassign a reserved public IP address to a different private IP:
Command
CopyTry It
```
oci network public-ip update --public-ip-id new_public_IP_OCID --private-ip-id EMPTY_STRING ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/UpdatePublicIp) operation to reassign a reserved public IP address from one private IP address to another.


Was this article helpful?
YesNo


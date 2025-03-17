Updated 2025-01-15
# Assigning an Ephemeral Public IP to an Existing Primary Private IP
Assign an ephemeral public IP address to an instance to enable communication with the internet.
Prerequisite: The primary private IP must not have a reserved or ephemeral public IP already assigned to it. If it does, first [delete the public ephemeral IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/deleting-ephemeral-public-ip-from-instance.htm#top "Deleting an ephemeral public IP automatically unassigns it from its private IP."), or [unassign the reserved public IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-unassign.htm#top "Unassign a reserved public IP object in Oracle Cloud Infrastructure.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assigning-ephemeral-public-existing-private-ip.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assigning-ephemeral-public-existing-private-ip.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assigning-ephemeral-public-existing-private-ip.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Click the instance to view its details. 
    3. Under **Resources** , click **Attached VNICs** to display the primary VNIC and any secondary VNICs attached to the instance.
    4. Click the VNIC that you're interested in.
    5. Under **Resources** , click **IP addresses** to display the VNIC's primary private IP and any secondary private IPs.
    6. For the VNIC's primary private IP, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Edit**.
    7. In the **Public IP address** section, for **Public IP type** , select the radio button for **Ephemeral public IP**. 
    8. In the **Ephemeral public IP name** field, enter an optional friendly name for the public IP. The name doesn't have to be unique, and you can change it later. Avoid entering confidential information.
    9. Click **Update**. 
  * Use the [network public-ip create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/create.html) command and required parameters to assign a public IP:
Command
CopyTry It
```
oci network public-ip create --compartment-id compartment_ID --lifetime EPHEMERAL
 --private-ip-id private_IP_OCID ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/CreatePublicIp) operation to create a public IP.


Was this article helpful?
YesNo


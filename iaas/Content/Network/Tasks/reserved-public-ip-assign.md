Updated 2025-01-15
# Assigning a Reserved Public IP to a Private IP
Assign a reserved public IP object to a private IP address in Oracle Cloud Infrastructure.
The VNIC's private IP address must not have an ephemeral or reserved public IP object already assigned to it. If it does, first either [delete the public ephemeral IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/deleting-ephemeral-public-ip-from-instance.htm#top "Deleting an ephemeral public IP automatically unassigns it from its private IP."), or [unassign the reserved public IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/deleting-ephemeral-public-ip-from-instance.htm#top "Deleting an ephemeral public IP automatically unassigns it from its private IP.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-assign.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-assign.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-assign.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Under **List scope** , select the compartment that contains the instance using the private IP address to which you want to assign a public IP object.
    3. Click the name of an instance to view its details.
    4. Under **Resources** , click **Attached VNICs** to display the primary VNIC and any secondary VNICs attached to the instance.
    5. Click the name of the VNIC that uses a private IP.
    6. Under **Resources** , click **IPv4 Addresses** to display the VNIC's primary private IP address and any secondary private IP addresses.
    7. For the private IP address to which you want to assign a public IP object, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and select **Edit**.
    8. In the **Public IP Type** section of the **Edit Private IP Address** dialog box, select **Reserved public IP**.
    9. Select one of the following options: 
       * **Select Existing Reserved IP Address** : If you select this option, next select the reserved public IP from the **Reserved IP Address in _< compartment>_** list, changing the compartment as needed. 
       * **Create new Reserved IP Address** : If you select this option, enter the following information:
         * **Public IP Name** : A descriptive name for the reserved public IP object. The name doesn't have to be unique, and you can change it later. Avoid entering confidential information.
         * **Create in Compartment:** The compartment in which you want to create the reserved public IP, which could be different from the compartment you're currently working in.
         * **IP Address Source in _< compartment>_:** (Optional) The [ IP pool](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_pools.htm#ip_pools) that the IP address is drawn from. If you don't select a pool that you've created, the default Oracle pool is used.
    10. Click **Update**. 
  * Use the [network public-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/update.html) command and required parameters to assign a reserved public IP address to a private IP:
Command
CopyTry It
```
oci network public-ip update --public-ip-id public_IP_OCID --private-ip-id private_IP_OCID ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/UpdatePublicIp) operation to assign a reserved public IP address to a private IP address.


Was this article helpful?
YesNo


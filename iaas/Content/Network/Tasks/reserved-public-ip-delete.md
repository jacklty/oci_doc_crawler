Updated 2025-01-15
# Deleting a Reserved Public IP
Delete a reserved public IP object in Oracle Cloud Infrastructure.
The reserved public IP object can be in the Assigned state. Deleting a reserved public IP object automatically unassigns it from the private IP address to which it's assigned and returns the public IP address to the pool of unused public IP addresses. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-delete.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **IP management** , select **Reserved public IPs**.
    2. Under **List scope** , select the compartment that contains the reserved public IP object that you want to delete.
    3. For the reserved public IP object you want to delete, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Terminate**.
    4. Confirm when prompted.
After a few seconds, the reserved public IP object is unassigned (if it was assigned) and the address is returned to the pool it came from.
  * Use the [network public-ip delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/delete.html) command and required parameters to delete a reserved public IP address:
Command
CopyTry It
```
oci network public-ip delete --public-ip-id public_IP_OCID ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeletePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/DeletePublicIp) operation to delete a reserved public IP.


Was this article helpful?
YesNo


Updated 2025-01-15
# Moving a Reserved Public IP to a Different Compartment
Move a reserved public IP address from one compartment to another. When you move a reserved public IP to a new compartment, inherent policies apply immediately. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-move.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-move.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-move.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **IP management** , select **Reserved public IPs**.
    2. For the reserved public IP you want to edit, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Move resource**. 
    3. Choose a destination compartment from the list, and then click **Move resource**.
For more information about using compartments and policies to control access to a cloud network, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). For general information about compartments, see [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm). 
  * Use the [network public-ip change-compartmnet](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/change-compartment.html) command and required parameters to move a public IP to a different compartment:
Command
CopyTry It
```
oci network public-ip change-compartmnet --public-ip-id public_IP_OCID --compartment-id compartment_OCID ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangePublicIpCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/ChangePublicIpCompartment) operation to move a reserved public IP address to a different compartment.


Was this article helpful?
YesNo


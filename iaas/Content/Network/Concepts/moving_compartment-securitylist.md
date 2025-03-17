Updated 2025-01-15
# Moving a Security List to a Different Compartment
Move a security list in a Virtual Cloud Network (VCN) to a different compartment.
You can move security lists from one compartment to another. Moving a security list doesn't affect its attachment to a subnet. When you move a security list to a new compartment, inherent policies apply immediately and affect access to the security list. For more information, see [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/moving_compartment-securitylist.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/moving_compartment-securitylist.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/moving_compartment-securitylist.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
    3. Under **Resources** , click **Security Lists**.
    4. Find the security list, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) to the right side of it, and then select **Move resource**.
    5. Select the destination compartment from the list. 
    6. Click **Move resource**.
  * Use the [network security-list change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/security-list/change-compartment.html) command and required parameters to move a security list to a different compartment:
Command
CopyTry It
```
oci network security-list change-compartment --security-list-id securitylist-ocid ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeSecurityListCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/ChangeSecurityListCompartment) operation to move a security list to a different compartment.


Was this article helpful?
YesNo


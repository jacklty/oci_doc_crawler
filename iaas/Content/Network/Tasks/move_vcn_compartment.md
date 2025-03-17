Updated 2025-01-15
# Moving a VCN Between Compartments
You can move a VCN from one compartment to another.
When you move a VCN, its associated VNICs, private IPs, and ephemeral IPs move with it to the new compartment. This changes the management of the resources with no changes to the routing of the traffic. 
The VCN is moved immediately. Resources attached to the VCN are moved asynchronously and don't appear in the new compartment until the move is complete.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move_vcn_compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move_vcn_compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move_vcn_compartment.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Find the VCN in the list, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Move Resource**.
    3. Choose the destination compartment from the list. 
    4. Click **Move Resource**.
    5. If alarms monitor the VCN, update the alarms to reference the new compartment. See [Updating an Alarm After Moving a Resource](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/update-alarm-after-resource-move.htm). 
  * Use the [network vcn change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/change-compartment.html) command and required parameters to move a VCN from one compartment to another.
Command
CopyTry It
```
oci network vcn change-compartment --compartment-id target-compartment-ocid --vcn-id vcn-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeVcnCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/ChangeVcnCompartment) operation to move a VCN from one compartment to another.


Was this article helpful?
YesNo


Updated 2025-01-14
# Moving a Compartment
Move a compartment in an IAM tenancy.
To move a compartment, you must belong to a group that has `manage all-resources` permissions on the lowest shared parent compartment of the current compartment and the destination compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_move_a_compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_move_a_compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_move_a_compartment.htm)


  *     1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Compartments**. 
A list of the compartments that you have access to in the tenancy is displayed. If the compartment you want to move isn't directly beneath the root compartment, select through the hierarchy of compartments to find the compartment. 
    2. For the compartment you want to move, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Move Resource**.
    3. Select the destination compartment.
    4. Confirm that you're aware of the [implications of the move](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/Working_with_Compartments.htm#Understa).
    5. Select **Move Resource**.
  * Use the [move](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/compartment/move.html) command and required parameters to move a compartment:
Command
CopyTry It
```
export compartment_id=compartment_ocid # https://docs.cloud.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/compartment/move.html#cmdoption-compartment-id
export target_compartment_id=target_compartment_ocid # https://docs.cloud.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/compartment/move.html#cmdoption-target-compartment-id
oci iam compartment move --compartment-id compartment_ocid --target-compartment-id target_compartment_ocid

```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [MoveCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/MoveCompartment) operation to move a compartment.


Was this article helpful?
YesNo


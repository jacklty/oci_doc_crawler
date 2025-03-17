Updated 2025-01-14
# Deleting a Compartment
Delete a compartment from an IAM tenancy.
To delete a compartment, it must be empty of all resources. Before you initiate deleting a compartment, ensure that you have moved, deleted, or terminated all its resources, including any policies attached to the compartment.
The delete action is asynchronous and initiates a work request. The state of the compartment changes to **Deleting** while the work request is executing. It typically takes several minutes for the work request to complete. While it's in the **Deleting** state, the compartment isn't displayed in the compartment picker. If the work request fails, the compartment isn't deleted and it returns to the **Active** state.
After a compartment is deleted, its state is updated to **Deleted** and a random string of characters is appended to its name, for example, `CompartmentA` might become `CompartmentA.qR5hP2BD`. Renaming the compartment allows you to reuse the original name for a different compartment. The deleted compartment is displayed on the Compartments page for 90 days before it's removed from the compartment picker. If any policy statements reference the deleted compartment, the name in the policy statement is updated to the new name.
If you have problems deleting a compartment, see [Compartment Fails to Delete](https://docs.oracle.com/en-us/iaas/Content/Identity/troubleshooting/compartments.htm#Troubleshooting_compartment_fails_to_delete).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_delete_a_compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_delete_a_compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_delete_a_compartment.htm)


  *     1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Compartments**. A list of the compartments in your tenancy is displayed.
    2. For the compartment you want to delete, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Delete**.
    3. At the prompt, select **OK**.
A work request is submitted to delete the compartment. The compartment state changes to **Deleting**. If the work request fails, the state returns to **Active**.
  * Use the [delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/compartment/delete.html) command and required parameters to delete a compartment:
Command
CopyTry It
```
oci iam compartment delete --compartment-id compartment_ocid

```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/DeleteCompartment) operation to delete a compartment.


Was this article helpful?
YesNo


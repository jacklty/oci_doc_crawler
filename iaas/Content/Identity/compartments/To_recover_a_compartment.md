Updated 2025-01-14
# Recovering a Compartment
Learn how to recover a compartment.
To recover a compartment, you must first select it from the list on the Compartment page. You may have to use the state filter to see the deleted compartment. Remember that deleted compartments are renamed by appending a random string of characters to the original compartment name. For example, CompartmentA might become CompartmentA.qR5hP2BD. Oracle displays the deleted compartment on the Compartments page for 90 days.
When you recover a deleted compartment, the name isn't changed. For example, if you recover a deleted compartment named CompartmentA.qR5hP2BD, the name remains the same. Because policy statements are updated to use the new names of deleted compartments, any policy statements that had referenced the deleted compartment now reference the recovered compartment. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_recover_a_compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_recover_a_compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_recover_a_compartment.htm)


  *     1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Compartments**. A list of the compartments in your tenancy is displayed.
    2. In **State** , select **Deleted**. 
    3. For the compartment you want to recover, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Restore**.
    4. At the prompt, select **Restore**.
  * Use the [recover](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/compartment/recover.html) command and required parameters to recover a compartment:
Command
CopyTry It
```
export compartment_id=compartment_ocid # https://docs.cloud.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/compartment/recover.html#cmdoption-compartment-id
oci iam compartment recover --compartment-id compartment_ocid

```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [RecoverCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/RecoverCompartment) operation to recover a compartment.


Was this article helpful?
YesNo


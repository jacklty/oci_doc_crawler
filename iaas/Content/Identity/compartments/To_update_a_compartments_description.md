Updated 2025-01-14
# Editing a Compartment's Description
Learn how to update a compartment's description in an IAM tenancy.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_update_a_compartments_description.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_update_a_compartments_description.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_update_a_compartments_description.htm)


  *     1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Compartments**.
A list of the compartments that you have access to in the tenancy is displayed.
    2. Locate the compartment you want to update, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Edit Description**.
    3. Enter the new description. Avoid entering confidential information.
    4. Select **Save**.
  * Use the [update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/compartment/update.html) command and required parameters to update a compartment's name:
Command
CopyTry It
```
export compartment_id=compartment_ocid # https://docs.cloud.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/compartment/update.html#cmdoption-compartment-id
oci iam compartment update --compartment-id compartment_ocid
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/UpdateCompartment) operation to edit a compartment's description.


Was this article helpful?
YesNo


Updated 2025-02-06
# Managing Tags for a VNIC
Learn to manage resource tags for a VNIC.
For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-tags.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-tags.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-tags.htm)


  *     1. Confirm you're viewing the compartment that contains the Compute instance you're interested in. 
    2. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    3. Select the name of the instance to view its details.
    4. Under **Resources** , select **Attached VNICs**.
The primary VNIC and any secondary VNICs attached to the instance are displayed. 
    5. Select the name of the VNIC you're interested in.
    6. Select the **Tags** tab to view or edit the existing tags. Or select **Add Tags** to add new ones.
  * Use the `oci network vnic update` command and required parameters to manage resource tags for a VNIC:
Command
CopyTry It
```
oci network vnic update --vnic-id ocid [--defined-tags | --freeform-tags] tags ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateVnic](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vnic/UpdateVnic) operation to manage resource tags for a VNIC.


Was this article helpful?
YesNo


Updated 2025-02-06
# Detaching and Deleting a Secondary VNIC
Detach and delete a specified secondary VNIC. 
You can't delete a Compute instance's primary VNIC. When you terminate a Compute instance, all attached VNICs (primary and secondary) are automatically detached and deleted.
**Note** If the VNIC has a private IP that's the target of a route rule, deleting the VNIC causes all traffic to the private IP to be dropped.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-detatch.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-detatch.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-detatch.htm)


  *     1. Confirm you're viewing the compartment that contains the Compute instance you're interested in. 
    2. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    3. Select the name of the instance to view its details.
    4. Under **Resources** , select **Attached VNICs**.
The primary VNIC and any secondary VNICs attached to the instance are displayed. 
    5. For the VNIC you want to delete, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Delete VNIC**.
    6. Confirm when prompted. 
It takes typically a few seconds before the VNIC is deleted. 
If the secondary VNIC is on a Linux instance: use the [oci-network-config](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm#oci-network-config) utility to update the OS configuration required for secondary VNICs on instances that run Oracle Linux.
  * Use the [oci iam domain get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/get.html) command and required parameters to detach and delete a specified secondary VNIC:
Command
CopyTry It
```
oci compute instance detach-vnic --compartment-id ocid --vnic-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DetachVnic](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VnicAttachment/DetachVnic) operation to detach and delete a specified secondary VNIC. 


Was this article helpful?
YesNo


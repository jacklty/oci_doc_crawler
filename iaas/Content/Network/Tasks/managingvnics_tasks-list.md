Updated 2025-02-06
# Listing an Instance's VNICs
List the VNICs attached to a Compute instance.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-list.htm)


  *     1. Confirm you're viewing the compartment that contains the Compute instance you're interested in. 
    2. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    3. Select the name of the instance to view its details.
    4. Under **Resources** , select **Attached VNICs**.
The primary VNIC and any secondary VNICs attached to the instance are displayed. If the instance has two [active physical NICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#overview), the VNICs are grouped by NIC 0 and NIC 1. 
  * Use the `oci compute vnic-attachment list` command and required parameters to list the VNICs attached to an instance:
Command
CopyTry It
```
oci compute vnic-attachment list --compartment-id ocid --instance-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListVnicAttachments](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VnicAttachment/ListVnicAttachments) operation to list the VNICs attached to an instance.


Was this article helpful?
YesNo


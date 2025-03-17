Updated 2025-01-15
# Getting a VNIC's properties
Get a VNIC's VLAN tag and other properties.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingvnics_tasks-get.htm)


  *     1. Confirm you're viewing the compartment that contains the Compute instance you're interested in. 
    2. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    3. Click the name of the instance to view its details.
    4. Under **Resources** , click **Attached VNICs**.
    5. Click the name of the primary or secondary VNIC to view its details.
  * Use the `oci compute vnic-attachment get` command and required parameters to get the VNIC's VLAN tag and other properties:
Command
CopyTry It
```
oci compute vnic-attachment get --vnic-attachment-id ocid ... [OPTIONS]
```

Use the `oci network vnic get` command and required parameters to get the VNIC's private IP address, MAC address, optional public IP address, optional DNS hostname, and other properties:
Command
CopyTry It
```
oci network vnic get --vnic-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetVnicAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VnicAttachment/GetVnicAttachment) operation to get the VNIC's VLAN tag and other properties. Run the [GetVnic](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vnic/GetVnic) operation to get the VNIC's private IP address, MAC address, optional public IP address, optional DNS hostname, and other properties.


Was this article helpful?
YesNo


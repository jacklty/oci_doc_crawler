Updated 2023-12-13
# Changing the Shape of an Instance on a Dedicated Virtual Machine Host
Change the shape of instances on a dedicated virtual machine host.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dvmh_changing_shape_dedicated_virtual_machine_host.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dvmh_changing_shape_dedicated_virtual_machine_host.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/dvmh_changing_shape_dedicated_virtual_machine_host.htm)


  * You can change the shape of an instance on a dedicated virtual machine host using the following steps.
    1. Open the navigation menu.
    2. Click **Compute**.
    3. Under **Compute** , click **Dedicated Virtual Machine Hosts**.
    4. Go to the **Details** page for the dedicated virtual machine host.
    5. Under **Resources** , click **Hosted Instances**. Perform this step for each compartment in your tenancy that has instances running on the dedicated virtual machine host. To change the compartment for the **Hosted Instances** list, select a different compartment from the **Table Scope** list.
    6. Click the **Action Menu** for the hosted instance you want to change.
    7. Select **View instance details** from the menu. The instance details are displayed.
    8. From the menu, click **More Actions**.
    9. Select **Edit** from the menu. The **Edit instance** dialog is displayed.
    10. Click **Edit Shape**. The **Shape summary** dialog is displayed.
    11. From the **Shape summary** select and change the options as needed. Options include: 
       * Shape series
       * Shape name
       * Number of OCPUs
       * Amount of memory
**Note** Only shapes that support dedicated version machine host are displayed.
    12. After making your shape selections, click **Save changes**. 
**Important** **For Dense I/O shapes** , select the **I understand that local storage will be deleted** box to confirm local storage is deleted and cannot be recovered when the change is made.
    13. Click **Reboot instance** to start the shape change process.
  * Use the [instance update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/update.html) command and required parameters to update an instance.
```
oci compute instance update --instance-id <ocid1> --dedicated-vm-host-id <ocid1> --fault-domain FAULT-DOMAIN-# --from-json <file://path/to/file.json>
```

`file://path/to/file.json` is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see [Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).
For a complete list of flags and variable options for the Compute Service CLI commands, see the [Compute command line reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
  * Use the [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance) operation to update an instance.


Was this article helpful?
YesNo


Updated 2024-08-06
# Deleting a Secondary VNIC
On Compute Cloud@Customer, you can delete a secondary VNIC.
This operation detaches and deletes the specified secondary VNIC. 
You can't delete an instance's primary VNIC. 
When you delete an instance, all attached VNICs (primary and secondary) are automatically detached and deleted.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-secondary-vnic.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-secondary-vnic.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-secondary-vnic.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    2. At the top of the page, select the compartment that contains the instance for which you want to delete a VNIC.
    3. Click the name of the instance.
The instance details page is displayed.
    4. Under **Resources** , click **Attached VNICs**.
The list of attached VNICs for that instance is displayed.
    5. For the VNIC that you want to delete, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Delete**.
    6. Click **Confirm**.
The VNIC state changes to **Detached**. After a few seconds, the VNIC is removed from the list.
    7. Log onto the instance and delete the configuration for the IP address from the instance OS.
Undo the configuration you did when you added the VNIC. See [Configuring the Instance OS for a Secondary IP Address](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/configuring-the-instance-os-for-a-secondary-ip-address.htm#configuring-the-instance-os-for-a-secondary-ip-address "On Compute Cloud@Customer, after you create a secondary private IP address on a VNIC, sign in to the instance to configure the instance OS to use the new IP address.").
  * Use the [oci compute instance detach-vnic](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/detach-vnic.html) command and required parameters to detach and delete the specified secondary VNIC.
Copy
```
oci compute instance detach-vnic [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DetachVnic](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VnicAttachment/DetachVnic) operation to detach and delete the specified secondary VNIC.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


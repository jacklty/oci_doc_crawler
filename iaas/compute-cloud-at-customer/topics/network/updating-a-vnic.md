Updated 2024-08-06
# Updating a VNIC
On Compute Cloud@Customer, you can update the VNIC name, the host name, and whether to disable source/destination checks. You can add the VNIC to an NSG and remove the VNIC from an NSG.
Avoid entering confidential information in names.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-vnic.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-vnic.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-vnic.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    2. At the top of the page, select the compartment that contains the instance for which you want to update a VNIC.
    3. Click the name of the instance.
The instance details page is displayed.
    4. Under **Resources** , click **Attached VNICs**.
The list of attached VNICs for that instance is displayed.
    5. For the VNIC that you want to update, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) and then click **Edit**.
    6. In the **Update VNIC** dialog box, update the VNIC name, the host name, whether to disable source/destination checks, or whether to attach this VNIC to an NSG or detach this VNIC from an NSG.
See [Creating and Attaching a Secondary VNIC](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-and-attaching-a-secondary-vnic.htm#creating-and-attaching-a-secondary-vnic "On Compute Cloud@Customer, you can add more VNICs to an instance.") for information about the Skip Source/Destination Check selection.
If you change the Enable Network Security Groups box from cleared to selected, then you must select an NSG from the drop-down list. You might need to change the compartment to find the NSG you want.
If the Enable Network Security Groups box is already checked, then you can click Add Another NSG to attach to another NSG.
If more than one NSG is already listed, you can click the trash can next to an existing NSG to detach this VNIC from that NSG. To detach the last NSG or all NSGs, clear the Enable Network Security Groups box.
See [Controlling Traffic with Network Security Groups](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/controlling-traffic-with-network-security-groups.htm#controlling-traffic-with-network-security-groups "On Compute Cloud@Customer, both network security groups \(NSGs\) and security lists are types of virtual firewalls for your compute instances. Both NSGs and security lists define network security rules that decide which types of traffic are allowed in and out of instances \(VNICs\).") for information about NSGs.
    7. Click **Update VNIC**.
  * Use the [oci network vnic update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vnic/update.html) command and required parameters to update the specified VNIC.
Copy
```
oci network vnic update [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateVnic](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vnic/UpdateVnic) operation to update the specified VNIC.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


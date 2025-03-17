Updated 2025-01-27
# Creating and Attaching a Secondary VNIC
On Compute Cloud@Customer, you can add more VNICs to an instance.
The number of secondary VNICs that you can add to an instance depends on the shape of the instance. See [Compute Shapes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/compute-shapes.htm#compute-shapes "A shape is a template that determines the type and amount of resources that are allocated to a compute instance. Compute Cloud@Customer offers a choice between a flexible shape for generic workloads, and dedicated shapes for GPU-accelerated workloads.").
After you attach a secondary VNIC, log onto the instance to configure the instance OS to use the new interface. See [Configuring the Instance OS for a Secondary VNIC](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/configuring-the-instance-os-for-a-secondary-vnic.htm#configuring-the-instance-os-for-a-secondary-vnic "On Compute Cloud@Customer, after you create a secondary VNIC, log in to the instance OS and configure the OS to use the new VNIC.").
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-and-attaching-a-secondary-vnic.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-and-attaching-a-secondary-vnic.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-and-attaching-a-secondary-vnic.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    2. At the top of the page, select the compartment that contains the instance to which you want to add a secondary VNIC.
    3. Click the name of the instance.
    4. Under **Resources** , click **Attached VNICs**.
The primary VNIC and any secondary VNICs attached to the instance are displayed.
    5. Click **Create VNIC Attachment**.
    6. In the **Subnet** section of the **Create VNIC Attachment** dialog box, specify the subnet to use for the VNIC. You might need to select a different compartment to find the VCN and subnet that you want.
**Note**
Specifying the same subnet for this VNIC that's specified for another VNIC for this instance can introduce asymmetric routing.
Instead of creating a VNIC in the same subnet as an existing VNIC for this instance, consider creating a secondary private IP address for the existing VNIC that's in this subnet.
    7. Specify whether to disable source/destination checks.
By default, a VNIC looks at the source and destination listed in the header of each network packet. If the VNIC isn't the source or destination, then the packet is dropped.
If the VNIC needs to forward traffic (for example, if the VNIC needs to perform Network Address Translation), check the box to disable this source/destination check.
    8. If you selected a public subnet, you can specify whether to automatically assign a public IPv4 address object to the VNIC private IP address object.
    9. (Optional) Specify the following private IP information.
       * **Private IP Address** : An address that's within the CIDR block range assigned to the subnet and not already in use. If you don't enter an address, an IP address is automatically assigned.
       * **Hostname** : A hostname to be used for DNS within the cloud network. This option is available only if the VCN and subnet both have DNS labels. The hostname can be up to 63 letters, numbers, and hyphens. No spaces are allowed.
    10. (Optional) Add this VNIC to an NSG.
By default, the new VNIC isn't attached to any NSG. Check the box labeled **Enable Network Security Groups** to add this VNIC to one or more NSGs.
      1. Select an NSG from the drop-down list. You might need to change the compartment to find the NSG you want.
      2. Click **Add Another NSG** to attach to another NSG.
      3. To remove an NSG from the list, click the trash can to the right of that NSG. To remove the last NSG or all NSGs, clear the **Enable Network Security Groups** box.
See [Controlling Traffic with Network Security Groups](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/controlling-traffic-with-network-security-groups.htm#controlling-traffic-with-network-security-groups "On Compute Cloud@Customer, both network security groups \(NSGs\) and security lists are types of virtual firewalls for your compute instances. Both NSGs and security lists define network security rules that decide which types of traffic are allowed in and out of instances \(VNICs\).") for information about NSGs.
    11. Click **Create Attachment**. 
The secondary VNIC is created and then displayed on the **Attached VNICs** list for the instance.
    12. Configure the instance OS to use the secondary VNIC. See [Configuring the Instance OS for a Secondary VNIC](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/configuring-the-instance-os-for-a-secondary-vnic.htm#configuring-the-instance-os-for-a-secondary-vnic "On Compute Cloud@Customer, after you create a secondary VNIC, log in to the instance OS and configure the OS to use the new VNIC.").
  * Use the [oci compute instance attach-vnics](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/attach-vnic.html) command and required parameters to create a secondary VNIC and attaches it to the specified instance. You can specify either –subnet-id or –vlan-id for this create request, but not both.
Copy
```
oci compute instance attach-vnic [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [AttachVnic](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VnicAttachment/AttachVnic) operation to create a secondary VNIC and attaches it to the specified instance.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


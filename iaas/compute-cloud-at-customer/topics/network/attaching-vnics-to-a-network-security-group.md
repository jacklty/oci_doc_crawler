Updated 2024-04-02
# Attaching VNICs to a Network Security Group
On Compute Cloud@Customer, an NSG has one or more VNICs. You can attach a VNIC to an NSG when you create an instance or when you create or update the VNIC.
See the following procedures:
  * [Creating an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance.htm#creating-an-instance "On Compute Cloud@Customer, you can create an instance using the Compute Cloud@Customer Console, CLI, and API.")
  * [Creating and Attaching a Secondary VNIC](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-and-attaching-a-secondary-vnic.htm#creating-and-attaching-a-secondary-vnic "On Compute Cloud@Customer, you can add more VNICs to an instance.")
  * [Updating a VNIC](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-vnic.htm#updating-a-vnic "On Compute Cloud@Customer, you can update the VNIC name, the host name, and whether to disable source/destination checks. You can add the VNIC to an NSG and remove the VNIC from an NSG.")


  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/attaching-vnics-to-a-network-security-group.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/attaching-vnics-to-a-network-security-group.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/attaching-vnics-to-a-network-security-group.htm)


  * You can view NSGs and VNICs in different ways:
    * To view the list of NSGs that a VNIC is attached to, perform the following steps.
      1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
      2. At the top of the page, select the compartment that contains the instance that has the VNIC.
      3. Click the name of the instance.
The instance details page is displayed.
      4. Under **Resources** , and click **Attached VNICs**.
      5. Click the name of the VNIC.
      6. Under **Resources** , click **Network Security Groups**.
    * To view the list of VNICs that are attached to an NSG, perform the following steps.
      1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
      2. At the top of the page, select the compartment that contains the VNC.
      3. Click the name of the VCN. 
The VCN details page is displayed.
      4. Under **Resources** , click **Network Security Groups**.
      5. In the list, click the name of the NSG.
      6. Under **Resources** , click **VNICs**.
    * To change the list of NSGs that a VNIC is attached to, update the VNIC. See [Updating a VNIC](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-vnic.htm#updating-a-vnic "On Compute Cloud@Customer, you can update the VNIC name, the host name, and whether to disable source/destination checks. You can add the VNIC to an NSG and remove the VNIC from an NSG.").
  * Use the [oci network vnic get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vnic/get.html) command and required parameters to view the list of NSGs that a VNIC is attached to.
Copy
```
oci network vnic get [OPTIONS]
```

Use the [oci network nsg list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/list.html) command and required parameters to view the list of VNICs that are attached to an NSG.
Copy
```
oci network nsg vnics list [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
To change the list of NSGs that a VNIC is attached to, update the VNIC.
  * Use the [GetVnic](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vnic/GetVnic) operation to view the list of NSGs that a VNIC is attached to.
Use the [ListNetworkSecurityGroupVnics](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NetworkSecurityGroupVnic/ListNetworkSecurityGroupVnics) operation to view the list of VNICs that are attached to an NSG.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


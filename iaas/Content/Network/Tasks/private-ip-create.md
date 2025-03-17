Updated 2025-02-28
# Assigning a New Secondary Private IP to a VNIC
Assign a new secondary private IP address to a VNIC.
You can add a _secondary private IP_ to an instance after it's created. You can add it to either the primary VNIC or a secondary VNIC on the instance. The secondary private IP address must come from the CIDR of the VNIC's subnet. You can move a secondary private IP from a VNIC on one instance to a VNIC on another instance if both VNICs belong to the same subnet.
For more information see [Private IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses.htm#Private_IP_Addresses).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-create.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-create.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-create.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Under **List scope** , select the compartment that contains the instance you want to add a private IP address to.
    3. Select the name of the instance to open its details page.
    4. Under **Resources** , select **Attached VNICs**.
    5. Select the VNIC that you're interested in.
    6. Under **Resources** , select **IPv4 Addresses**.
    7. Select **Assign Secondary Private IP Address** and then enter the private IP address information: 
       * **Private IP Address:** (Optional) An available private IP address from the subnet's CIDR (otherwise the private IP address is automatically assigned).
       * **Unassign if already assigned to another VNIC:** Select this checkbox to force reassignment of the IP address if it's already assigned to another VNIC in the subnet. Only relevant if you specify a private IP address in the preceding field.
       * **Hostname:** (Optional) A hostname to use for DNS within the cloud network. Only available if both the VCN and subnet have DNS labels. See [DNS in Your Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network). 
       * **Public IP Type:** (Optional) Only available if the VNIC is in a public subnet. See [Public IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm#Public_IP_Addresses).
       * **Route Table:** (Optional) Assign a custom route table to use with traffic sent from this IP address. See [Per-resource Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN__source_routing) for more details. If you use this option, remember that traffic from this IP address doesn't use the default VCN or subnet route tables.
    8. Select **Assign**.
  * Use the [network vnic assign-private-ip](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vnic/assign-private-ip.html) command and required parameters to assign a secondary private IP to a VNIC:
Command
CopyTry It
```
oci network vnic assign-private-ip --ip-address IP_address --unassign-if-already-assigned VNIC_OCID
--vnic-id destination_VNIC_OCID ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreatePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/CreatePrivateIp) operation to assign a new secondary private IP to a VNIC.


## Next Steps 🔗 
After assigning a secondary private IP to a VNIC, you must configure the OS to use it.
  * For instances running a variant of Linux, see [Configuring Linux to Use a Secondary Private IP Address](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses_topic-Linux_Details_about_Secondary_IP_Addresses.htm#Linux "Configure Linux to use a secondary private IP address.").
  * For Windows instances, see [Configuring Windows to Use a Secondary IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses_topic-Windows_Details_about_Secondary_IP_Addresses.htm#Windows "Configure the Windows OS to use a secondary private IP.").


Was this article helpful?
YesNo


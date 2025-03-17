Updated 2025-02-06
# Moving a Secondary Private IP Address to a Different VNIC
Move a secondary private IP address to another VNIC in the same subnet.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-move-vnic.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-move-vnic.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-move-vnic.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Select the name of the instance to open its details page.
    3. Under **Resources** , select **Attached VNICs**.
    4. Select the VNIC that you're interested in.
    5. Under **Resources** , select **IPv4 Addresses**.
The VNIC's associated IP addresses are listed in tabular form.
    6. Select **Assign Secondary Private IP Address** and enter assignment information:
       * **Private IP Address:** The secondary private IP address you want to move.
       * **Unassign if already assigned to another VNIC:** Select this checkbox to move the secondary IP address from the VNIC it's assigned to.
       * **Hostname:** (Optional) The hostname to use for DNS in the cloud network. Only available if the VCN and subnet both have DNS labels. See [DNS in Your Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network). 
       * **Public IP Type:** (Optional) Only available if the VNIC is in a public subnet. See [Public IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm#Public_IP_Addresses).
  * Use the [network vnic assign-private-ip](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vnic/assign-private-ip.html) command and required parameters to move a secondary private IP address from one VNIC to another:
Command
CopyTry It
```
oci network vnic assign-private-ip --ip-address IP_address --unassign-if-already-assigned VNIC_OCID
--vnic-ip-id destination_VNIC_OCID ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdatePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/UpdatePrivateIp) operation to move a private IP address from one VNIC to another.


Was this article helpful?
YesNo


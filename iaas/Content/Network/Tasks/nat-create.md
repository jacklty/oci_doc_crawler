Updated 2025-01-17
# Creating a NAT Gateway
Create a NAT gateway in a virtual cloud network (VCN) in Networking. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-create.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-create.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-create.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the name of the VCN that you're interested in.
    3. Under **Resources** , select **NAT Gateways**. 
    4. Select **Create NAT Gateway**. 
    5. Enter the following values:
       * **Name:** A friendly name for the NAT gateway. It doesn't have to be unique. Avoid entering confidential information. 
       * **Create in Compartment** : The compartment in which you want to create the NAT gateway, if different from the compartment you're working in. 
       * **Select IP Address Type:** Specify whether the public IP address is reserved or ephemeral. 
         * **Ephemeral IP Address:** Select this option to let Oracle specify an [ephemeral IP address](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm#overview__res_eph) for you from the Oracle IP pool. This option is the default.
         * **Reserved IP Address:** Select this option to specify an existing [reserved IP address](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm#overview__res_eph) by name, or to create a new reserved IP address by assigning a name and selecting a source [IP pool](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_pools.htm#ip_pools) for the address. If you don't select a pool, the default Oracle IP pool is used.
       * **Route Table Association:** (Advanced option) You can associate a specific VCN route table with this gateway. After you associate a route table, the gateway must always have a route table associated with it. You can change the rules in the current route table or replace it with another route table. 
       * **Tags:** (Advanced option) If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. 
    6. Select **Create NAT Gateway**.
The NAT gateway is then created and displayed on the **NAT Gateways** page in the compartment that you chose. The gateway allows traffic by default. At any time, you can [block or allow traffic](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-block.htm#nat-block "Block or allow traffic for a NAT gateway.") through it.
  * Use the [network nat-gateway create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nat-gateway/create.htm) command and required parameters to create a NAT gateway in a VCN:
Command
CopyTry It
```
oci network nat-gateway create --compartment-id compartment-ocid --vcn-id vcn-ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateNatGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NatGateway/CreateNatGateway) operation to create a NAT gateway in a VCN.


Was this article helpful?
YesNo


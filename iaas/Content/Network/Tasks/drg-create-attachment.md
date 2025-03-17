Updated 2025-01-15
# Attaching a DRG to a VCN
Create a VCN attachment on a Dynamic Routing Gateway (DRG) in Oracle Cloud Infrastructure.
To route traffic to a compute instance from an on-premises network or a DRG in another region, a DRG must be explicitly attached to a VCN. A VCN can be attached to only one DRG at a time, but a DRG can be attached to more than one VCN. The attachment is automatically created in the compartment that holds the VCN. An attached VCN doesn't need to be in the same compartment as the DRG. 
You can choose to connect two or more VCNs in the same region by attaching them to a single DRG instead of with local peering gateways (for more information about that use case see [Local VCN Peering Through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenariod "This scenario describes using a mutual connection to an upgraded DRG to enable traffic between two or more VCNs.")). If left unmodified, the default routing policies in a DRG allow traffic to be routed between all VCNs attached to it. If you're attaching a DRG to a VCN in another tenancy, you need to have IAM configurations in both tenancies as described in [IAM Policies for Routing Between VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m "Learn about IAM policies used with peering and dynamic routing gateways."). Also, refer to [Route Aggregation](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#managingDRGs_topic_drg_routing__rt_agg) for more details on controlling the VCN routes advertised by BGP. 
When you create a VCN attachment (the VCN can be in another tenancy in the same OCI region), attachments on both the DRG and VCN are created and connected in one step. If you create a remote peering connection (RPC) attachment, there are additional steps required to connect to the DRG on the other end. For more about using RPC attachments, see [Remote VCN Peering through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_e.htm#scenario_e "This topic is about remote VCN peering.").
You can't directly create other attachment types for a DRG (such as IPSEC TUNNEL, LOOPBACK, and VIRTUAL CIRCUIT attachments). When you create a FastConnect virtual circuit or IPSec tunnel for Site-to-Site VPN, a virtual circuit attachment or IPSec tunnel attachment is created for you. It's not necessary to explicitly create an attachment with those types.
Attaching a DRG to a VCN results in a `DrgAttachment` object with its own OCID. If you're setting up the advanced routing scenario called [transit routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region), you can optionally specify a route table for a DRG attachment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-attachment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-attachment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-attachment.htm)


  * The following instructions have you navigate to the DRG and then choose which VCN to attach. You could instead navigate to the VCN and then choose a DRG to attach (as described in [Attaching a VCN to a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-vcn-drg.htm#attach-vcn-drg "Attach a Virtual Cloud Network \(VCN\) to a Dynamic Routing Gateway \(DRG\).")). 
If the VCN is in another tenancy, see [Attaching a DRG to a VCN in a Different Tenancy](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-xten-attachment.htm#drg-create-xten-attachment "Learn to attach a Dynamic Routing Gateway \(DRG\) to a VCN in another tenancy .")
    1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG that you want to attach to a VCN.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Click the name of the DRG.
    4. Under **Resources** , click **VCN attachments**. 
    5. Click **Create virtual cloud network attachment**.
    6. Enter the following information:
       * (Optional) Enter a friendly descriptive name for the attachment. If you don't enter a name, one is created for you.
       * Select a VCN from the list. You can also click **Change compartment** and choose a different compartment that contains a VCN you want to attach to your DRG, then select a VCN from the list.
    7. (Optional)  If you're setting up an [advanced scenario for transit routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region), you can associate a VCN route table with the DRG attachment (or you can do this later):
      1. Click **Show Advanced options**.
      2. On the **VCN route table** tab, select the route table that you want to associate with the VCN attachment on the DRG. If you select **None** , the default VCN route table is used. 
      3. (Optional) If you're planning to use transit routing and need to associate a specific DRG route table with the attachment, switch to the **DRG route table** tab and select an existing DRG route table. See [Creating a DRG Route Table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-create.htm#drg-create_route_table "Create a Dynamic Routing Gateway \(DRG\) route table in Oracle Cloud Infrastructure.").
      4. (Optional)  To use BGP [route aggregation](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#managingDRGs_topic_drg_routing__rt_agg), specify that you want to import VCN CIDR blocks into a DRG route table from the VCN attachment. Switch to the **VCN route type** tab and select **VCN CIDR blocks**.
If you don't select **VCN CIDR blocks** , then **Subnet CIDR blocks** is chosen for you and the subnet CIDRs are imported into a DRG route table from the VCN attachment. Routes from the VCN ingress route table are always imported. 
    8. (Optional) On the **Tags** tab under the advanced options, specify tags for the attachment.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    9. Click **Create VCN attachment**.
The attachment is listed on the DRG details page. If you attached the DRG to a VCN in another compartment, switch to that compartment to see the attachment.
The attachment is in the Attaching state for a short period. When the attachment is ready, create a route rule in the subnet's route table directing subnet traffic to the DRG. See [To route a subnet's traffic to a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables_topic-working.htm#add_route_rule).
  * Use the [network drg-attachment create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-attachment/create.html) command and required parameters to attach a VCN to a DRG:
Command
CopyTry It
```
oci network drg-attachment create --drg-id drg-ocid --network-details [complex type] ...[OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateDrgAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgAttachment/CreateDrgAttachment) operation to create a DRG attachment to a VCN.


Was this article helpful?
YesNo


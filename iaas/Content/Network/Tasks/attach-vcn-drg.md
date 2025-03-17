Updated 2025-01-15
# Attaching a VCN to a DRG
Attach a Virtual Cloud Network (VCN) to a Dynamic Routing Gateway (DRG).
A VCN can be attached to only one DRG at a time, but a DRG can be attached to more than one VCN. The attachment is automatically created in the compartment that holds the VCN. The VCN and DRG do not need to be in the same compartment. You may optionally specify a _display name_ for the attachment itself, otherwise a default is provided. You can choose to connect VCNs in the same region using a single DRG instead of local peering gateways (see [Local VCN Peering Through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenariod "This scenario describes using a mutual connection to an upgraded DRG to enable traffic between two or more VCNs.") for more information about that use case). If left unmodified, the default routing policies in a DRG allow traffic to be routed between all VCNs attached to it. If you are attaching a DRG to a VCN in another tenancy, you need to have IAM configurations in both tenancies as described in [IAM Policies for Routing Between VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m "Learn about IAM policies used with peering and dynamic routing gateways."). You will also need the OCID of the VCN.
When you create an attachment to a DRG (the DRG can be in another tenancy in the same OCI region), attachments on both the DRG and VCN are created and connected in one step. Attaching a DRG to a VCN results in a `DrgAttachment` object with its own OCID. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-vcn-drg.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-vcn-drg.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-vcn-drg.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN that you want to update. You might need to change the compartment to find the VCN that you want.
    3. Under **Resources** , click **Dynamic Routing Gateways Attachments**.
    4. Click **Create DRG Attachment** and enter the following information:
       * (Optional) Give the DRG attachment a friendly name. If you don't specify a name, one is created for you.
       * Choose **Current Tenancy** or **Another tenancy** depending on the location of the DRG you want to attach.
         * If you choose **Current Tenancy** , select a DRG from the list. You can also click **Change compartment** and choose a different compartment that contains a DRG you want to attach to your VCN, then select a DRG from the list.
         * If you choose **Another tenancy** , enter the OCID of the desired DRG.
    5. (Optional) (Optional) If you're setting up an [advanced scenario for transit routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region), you can associate a VCN route table with the DRG attachment (you can do this later):
      1. Click **Show Advanced Options**.
      2. Click the **VCN route table association** tab.
      3. For **Associate Vcn Route Table** click **Select Existing** and choose a VCN route table that you want to associate with the VCN attachment to the DRG. If you click **None** , the default VCN route table is used.
    6. When you are finished, click **Create DRG attachment**.
The attachment is in the "Attaching" state for a short period. 
When the attachment is ready, create a route rule in the subnet's route table directing subnet traffic to the DRG. See [To route a subnet's traffic to a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables_topic-working.htm#add_route_rule).
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


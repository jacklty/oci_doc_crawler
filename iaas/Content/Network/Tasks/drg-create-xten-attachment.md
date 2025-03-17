Updated 2025-01-15
# Attaching a DRG to a VCN in a Different Tenancy
Learn to attach a Dynamic Routing Gateway (DRG) to a VCN in another tenancy .
The VCN you are connecting to must be in the same OCI region. Before you can create a cross-tenancy attachment, you must implement the IAM policies described in [Attaching to VCNs in Other Tenancies](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__xtenancy-VCN). Attaching a VCN in another tenancy requires knowing the OCID of the VCN, but otherwise isn't very different from [attaching a VCN in the same tenancy](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-attachment.htm#drg-create_attachment "Create a VCN attachment on a Dynamic Routing Gateway \(DRG\) in Oracle Cloud Infrastructure."). 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-xten-attachment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-xten-attachment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-xten-attachment.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select a compartment that you have permission to work in.The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Click the name of the DRG you want to attach to a VCN in another tenancy.
    4. Under **Resources** , click **Cross-tenancy attachments**. 
    5. Click **Cross-tenancy attachment** and enter the following information:
       * (Optional) Give the attachment point a friendly name. If you don't specify a name, one is created for you.
       * Enter the OCID of the desired VCN.
    6. (Optional) If you're setting up an [advanced scenario for transit routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region), you can associate a VCN route table with the DRG attachment (you can do this later):
      1. Click **Show Advanced Options**.
      2. Click the **VCN route table** tab.
      3. Select the route table that you want to associate with the VCN attachment on the DRG. If you select **None** , the default VCN route table is used. 
      4. (Optional) If you are planning to use transit routing and need to associate a specific DRG route table to the attachment, switch to the **DRG route table** tab and choose an existing DRG route table. See [Creating a DRG Route Table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-create.htm#drg-create_route_table "Create a Dynamic Routing Gateway \(DRG\) route table in Oracle Cloud Infrastructure.").
      5. (Optional) If you need to specify that you want to import VCN CIDRs into a DRG route table from the VCN attachment, switch to the **VCN Route type** tab and choose **VCN CIDRs**.
If you don't explicitly choose **VCN CIDRs** , **Subnet CIDRs** is chosen for you and the subnet CIDRs are imported into a DRG route table from the VCN attachment. Routes from the VCN ingress route table are always imported.
    7. When you are finished, click **Create cross-tenancy attachment**.
  * Use the [network drg-attachment create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-attachment/create.html) command and required parameters to attach a VCN in another tenancy to a DRG:
Command
CopyTry It
```
oci network drg-attachment create --drg-id drg-ocid --network-details [complex type] ...[OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateDrgAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgAttachment/CreateDrgAttachment) operation to create a DRG attachment to a VCN in another tenancy.


Was this article helpful?
YesNo


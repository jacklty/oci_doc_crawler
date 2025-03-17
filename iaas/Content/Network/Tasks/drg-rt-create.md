Updated 2025-01-17
# Creating a DRG Route Table
Create a Dynamic Routing Gateway (DRG) route table in Oracle Cloud Infrastructure.
When you create a DRG, two default route tables are created for you: one for VCN attachments and one for all other attachments. You can assign a new DRG route table to a DRG attachment to change the routing behavior. 
For details about DRG routing, see [Working with DRG Route Tables and Route Distributions](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__rd_rt).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-create.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-create.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rt-create.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG for which you want to create a route table.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Select the name of the DRG.
    4. Under **Resources** , select **DRG route tables**. 
    5. Select **Create DRG route table**.
    6. (Optional)  Enter a descriptive name for the route table. Avoid entering confidential information.
    7. Under **Static route rules** , specify a destination for the route table. The route table must include at least one destination, but you can specify more if needed.
       * **Destination CIDR block:** Enter a destination CIDR block, enable import route distribution, or enter nothing and the default CIDR 0.0.0.0/0 is applied which allows all traffic.
       * **Next hop attachment type:** Select the intended target attachment type for the static rule. The attachment type can be **Virtual Cloud Network** , **Remote peering connection** , or **Cross-tenancy** attachment to a VCN. 
       * **Next hop attachment:** Select a specific attachment of the selected type as the next hop for this static route rule.
    8. (Optional) Select **Show Advanced options** , and provide the following information: 
       * **Enable import route distribution:** Select this option to assign an import route distribution to the route table so it dynamically learns new routes based on BGP advertisements.
       * **Enable ECMP:** Select this checkbox to enable equal-cost multi-path routing (ECMP), which disambiguates routing decisions when the same destination can be reached from several paths.
       * **Tags:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. 
    9. Select **Create DRG route table**.
The route table is created and displayed in the **DRG route tables** area of the DRG details page. 
  * Use the [network drg-route-table create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-table/create.html) command and required parameters to create a DRG route table:
Command
CopyTry It
```
oci network drg-route-table create --drg-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateDrgRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteTable/CreateDrgRouteTable) operation to create a DRG route table.


Was this article helpful?
YesNo


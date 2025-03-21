Updated 2025-01-17
# Creating a Route Distribution
Create an import or export route distribution for a Dynamic Routing Gateway (DRG) in Oracle Cloud Infrastructure.
A newly created DRG has two autogenerated import route distributions. After you create a new import route distribution, you can assign it to a route table so it dynamically learns new routes based on BGP advertisements. 
A newly created DRG has a single autogenerated export route distribution. If the default export route distribution is assigned to an attachment, the entire contents of the attachment's assigned DRG route table are dynamically exported to the attachment.
For more details about DRG routing, see [Working with DRG Route Tables and Route Distributions](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__rd_rt).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-create.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-create.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rd-create.htm)


  * You can only create an import route distribution using the Console. You must use the CLI or API to create and assign an export route distribution.
    1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG for which you want to create a route distribution.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Select the name of the DRG.
    4. Under **Resources** , select **Import route distributions**. 
    5. Select **Create import route distribution**. 
    6. (Optional) Enter a descriptive name for the route distribution. Avoid entering confidential information. If you don't enter a name, one is created for the distribution. A name is created for you if you leave the field blank.
    7. Enter the following values to create a route distribution statement:
       * **Priority** : Enter 10 or select some other priority number between 1 and 65535. Statements are evaluated in ascending order and carried out when a match is found, so lower numbers effectively have a higher priority.
       * **Match type** : Select **Attachment type** , **Attachment** , or **Match all**. 
         * If you select **Attachment Type** , then select one of the possible DRG attachment types. When you use this option, the import route distribution includes routes from all attachments to this DRG with the chosen type.
         * If you select **Attachment** , then select the type of DRG attachment and then select the specific attachment, changing compartments as necessary. 
    8. (Optional) Select **+Another statement** to add another route distribution statement to the import route distribution.
    9. (Optional) Select **Show Advanced options** and specify tags for the distribution. 
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    10. Select **Create import route distribution**.
The distribution is created and displayed in the **Import route distributions** area of the DRG details page. 
To assign the import route distribution to an existing DRG route table:
      1. Under **Resources** , select **DRG route tables**.
      2. Select the name of the route table you want to assign to the new import route distribution.
      3. Select **Edit**.
      4. Select **Enable import route distribution** and select the new import route distribution from the list of available options.
  * Use the [network drg-route-distribution create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-distribution/create.html) command and required parameters to create a new route distribution for the specified DRG:
Command
CopyTry It
```
oci network drg-route-distribution create --drg-id ocid --distribution-type import  ... [OPTIONS]
```

Assign the route distribution as an import distribution to a DRG route table using the `network drg-route-table update` or `network           drg-route-table create` commands. Assign the route distribution as an export distribution to a DRG attachment using the `network drg-attachment           update` or `network drg-attachment create` commands.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateDrgRouteDistribution ](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteDistribution/CreateDrgRouteDistribution) operation to create a new route distribution for the specified DRG. 
You can then assign the route distribution as an import distribution to a DRG route table using the `UpdateDrgRouteTable` or `CreateDrgRouteTable` operations or assign the route distribution as an export distribution to a DRG attachment using the `UpdateDrgAttachment` or `CreateDrgAttachment` operations.


Was this article helpful?
YesNo


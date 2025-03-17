Updated 2025-01-17
# Adding a Route Distribution Statement
Add a statement to an import or export route distribution for a dynamic routing gateway (DRG) in Oracle Cloud Infrastructure.
All match criteria in a statement must be met for the action to take place.
For details about DRG routing, see [Working with DRG Route Tables and Route Distributions](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__rd_rt).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-add.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-add.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-rds-add.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG with the route distribution to which you want to add a statement.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Select the name of the DRG.
    4. Under **Resources** , select either **Import route distributions** or **Export route distributions**. 
    5. Select on the name of the route distribution you want to you want to add a statement to.
    6. Select **Add route distribution statements**. 
    7. Enter the following values:
       * **Priority** : Enter 10 or some other priority number between 1 and 65535. Statements are evaluated in ascending order and carried out when a match is found, so lower numbers effectively have a higher priority.
       * **Match type** : Select **Attachment type** , **Attachment** , or **Match all**. 
         * If you select **Attachment Type** , then select one of the possible DRG attachment types. When you use this option, the import route distribution includes routes from all attachments to this DRG with the chosen type.
         * If you select **Attachment** , then select the type of DRG attachment and then select the specific attachment, changing compartments as necessary. 
    8. (Optional) Select **+Another statement** to add another route distribution statement to the import route distribution.
    9. Select **Add import route distribution statements**.
The statement is added to the list of existing statements for the distribution, in priority order. 
  * Use the [network drg-route-distribution-statement add](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg-route-distribution-statement/add.html) command and required parameters to add a statement to a specified import or export route distribution:
Command
CopyTry It
```
oci network drg-route-distribution-statement add --route-distribution-id ocid --statements [complex type] ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [AddDrgRouteDistributionStatements](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DrgRouteDistributionStatement/AddDrgRouteDistributionStatements) operation to add a statement to a specified import or export route distribution.


Was this article helpful?
YesNo


Updated 2025-01-14
# Listing Infrastructure Regions
View a list of all infrastructure regions in IAM. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/To_view_the_list_of_infrastructure_regions.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/To_view_the_list_of_infrastructure_regions.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/To_view_the_list_of_infrastructure_regions.htm)


  * Open the Console, open the **Region** menu, and then select **Manage regions**. A list of the regions offered by Oracle Cloud Infrastructure is displayed. Regions that you haven't subscribed to provide a button to create a subscription.
  * Use the [list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/region/list.html) command and required parameters to view a list of your infrastructure regions:
Command
CopyTry It
```
oci iam region list
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListRegions](https://docs.oracle.com/iaas/api/#/en/identity/latest/Region/ListRegions) operation to view a list of your infrastructure regions.
**Note** Returns a list of regions offered by Oracle Cloud Infrastructure in your selected **realm**.


Was this article helpful?
YesNo


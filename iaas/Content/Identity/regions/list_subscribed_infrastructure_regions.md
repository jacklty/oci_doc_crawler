Updated 2025-01-14
# Listing Subscribed Infrastructure Regions
View a list of regions you're subscribed to in IAM.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/list_subscribed_infrastructure_regions.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/list_subscribed_infrastructure_regions.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/list_subscribed_infrastructure_regions.htm)


  *     1. Open the Console, open the **Region** menu, and then select **Manage regions**. The list of regions you've subscribed to is displayed. Your home region is labeled.
    2. Open the Console, open the **Region** menu, and then select **Manage regions**. A list of the regions offered by Oracle Cloud Infrastructure is displayed. Regions that you haven't subscribed to provide a button to create a subscription.
To switch to the new region, use the **Region** menu in the Console. See [Switching Regions](https://docs.oracle.com/iaas/Content/GSG/Concepts/working-with-regions.htm#Switchin) for more information.
You can't unsubscribe from a region.
  * Use the [region-subscription](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/region-subscription/list.html) command and required parameters to view a list of regions you're subscribed to:
Command
CopyTry It
```
oci iam region-subscription list
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListRegionSubscriptions](https://docs.oracle.com/iaas/api/#/en/identity/latest/RegionSubscription/ListRegionSubscriptions) operation to view a list of regions you're subscribed to.


Was this article helpful?
YesNo


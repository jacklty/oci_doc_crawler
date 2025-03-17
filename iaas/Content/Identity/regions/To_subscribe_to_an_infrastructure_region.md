Updated 2025-01-14
# Subscribing to an Infrastructure Region
Subscribe to an infrastructure region in IAM.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/To_subscribe_to_an_infrastructure_region.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/To_subscribe_to_an_infrastructure_region.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/To_subscribe_to_an_infrastructure_region.htm)


  *     1. Open the Console, open the **Region** menu, and then select **Manage regions**. The list of regions available to your tenancy is displayed. Your home region is labeled.
    2. Locate the region you want to subscribe to and select **Subscribe**.
**Note** It could take several minutes to activate your tenancy in the new region.
    3. To switch to the new region, use the Region menu in the Console. See for more information. 
Remember, IAM resources are global, so when the subscription becomes active, all your existing policies are enforced in the new region. 
You can't unsubscribe from a region.
  * Use the [create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/region-subscription/create.html) command and required parameters to subscribe to an infrastructure region:
Command
CopyTry It
```
export region_key=region_ocid # https://docs.cloud.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/region-subscription/create.html#cmdoption-region-key
export tenancy_id=tenancy_ocid # https://docs.cloud.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/region-subscription/create.html#cmdoption-tenancy-id
oci iam region-subscription create --region-key region_ocid --tenancy-id tenancy_ocid
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateRegionSubscription](https://docs.oracle.com/iaas/api/#/en/identity/latest/RegionSubscription/CreateRegionSubscription) operation to subscribe to an infrastructure region.


Was this article helpful?
YesNo


Updated 2025-02-28
# Replicating an Identity Domain to Multiple Regions
You can replicate an identity domain in IAM to additional regions to enable users in that domain to interact with OCI resources in those regions.
Replication is always enabled for the Default identity domain. The Default identity domain always replicates to all regions to which the tenant is subscribed. When an administrator subscribes to another region, the Default identity domain automatically replicates to that region. Additional identity domains are created in a _home region_ that's specified at creation time. They don't replicate to other regions unless replication is specifically enabled.
You should enable replication if users in an identity domain need to interact with OCI resources in regions beyond that domain's home region. For example, if the domain was created with Germany Central (Frankfurt) as its home region, replication to France Central (Paris) lets users in the domain interact with OCI resources in Frankfurt or Paris, but not US East (Ashburn), even if the tenancy is subscribed to that region.
**Note** Enabling or disabling replication doesn't affect [disaster recovery](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/disaster_recovery_and_domains.htm#disaster_recovery_and_domains "A disaster can be any event that puts applications at risk, for example failures caused by natural disasters. In regions with cross-region disaster recovery \(DR\) enabled, identity domains have built-in cross-region DR to minimize data loss. Data for a region is replicated to a nearby region in the event of a disaster. If an entire OCI region becomes unavailable, traffic is routed to the disaster recovery region to speed service recovery and retain as much data as possible. Oracle pairs regions with disaster recovery \(DR\) regions for you.").
**Before you begin:** Ensure that the tenancy is subscribed to the regions to which you want to replicate the identity domain. For more information about the home regions and the basics of managing your region subscriptions, see [Managing Regions](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/managingregions.htm#Managing_Regions).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-manage-regions-for-domains.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-manage-regions-for-domains.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-manage-regions-for-domains.htm)


  * Ensure that the tenancy is subscribed to the regions to which you want to replicate the identity domain. For more information about the home regions and the basics of managing your region subscriptions, see [Managing Regions](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/managingregions.htm#Managing_Regions).
    1. On the **Domains** list page, under **List scope** , select the compartment that contains the identity domain that you want to replicate. If you need help finding the list page, see [Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm#view-identity-domains "Retrieve a list of the identity domains in a specific compartment in a tenancy in IAM.").
    2. Select the name of the identity domain you want to replicate.
    3. Select **More actions** , and then select **Manage regions**.
The **Manage regions** window displays a list of regions that the tenancy is subscribed to. 
    4. For the region you want to replicate to, select **Enable replication**.
    5. Confirm the replication.
  * Use the [oci iam domain enable-replication-to-region](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/enable-replication-to-region.html) command and required parameters to replicate an identity domain to multiple regions:
Command
CopyTry It
```
oci iam domain enable-replication-to-region --domain-id domain_ocid [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [EnableReplicationToRegion](https://docs.oracle.com/iaas/api/#/en/identity/latest/Domain/EnableReplicationToRegion) operation to replicate an identity domain to multiple regions.


Was this article helpful?
YesNo


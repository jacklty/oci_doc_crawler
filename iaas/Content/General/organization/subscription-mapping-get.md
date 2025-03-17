Updated 2025-02-11
# Getting a Subscription Mapping's Details
Get the details of a subscription mapping.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-get.htm)


  *     1. From the parent tenancy, open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Subscription Mapping**.
    2. On the **Subscription Mapping** list page, select the subscription that you want to work with.
The subscription mapping details page displays the subscription details.
The **Mapped tenancies** section displays the tenancies mapped to the subscription and the date they were mapped.
  * Use the [oci organizations subscription-mapping get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/subscription-mapping/get.html) command and required parameters to get subscription mapping details by the subscription mapping ID:
Command
CopyTry It
```
oci organizations subscription-mapping get --subscription-mapping-id [text] [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetSubscriptionMapping](https://docs.oracle.com/iaas/api/#/en/organizations/latest/SubscriptionMapping/GetSubscriptionMapping) operation to get subscription mapping details by the subscription mapping ID.


Was this article helpful?
YesNo


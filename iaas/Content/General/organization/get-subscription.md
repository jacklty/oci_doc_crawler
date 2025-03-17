Updated 2025-02-11
# Getting a Subscription's Details
View the details of a subscription by subscription ID.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/get-subscription.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/get-subscription.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/get-subscription.htm)


  *     1. From the parent tenancy, open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Subscription Mapping**.
    2. On the **Subscription Mapping** list page, select the subscription that you want to work with.
The details page displays the subscription details, along with tenancies that are assigned to the subscription.
  * Use the [oci organizations subscription get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/subscription/get.html) command and required parameters to get subscription details by subscription ID:
Command
CopyTry It
```
oci organizations subscription get --subscription-id [text] [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetSubscription](https://docs.oracle.com/iaas/api/#/en/organizations/latest/Subscription/GetSubscription) operation to get subscription details by subscription ID.


Was this article helpful?
YesNo


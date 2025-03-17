Updated 2025-02-11
# Listing Subscription Mappings
List all subscription mappings.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-list.htm)


  * To list the mapped tenancies for a particular subscription:
    1. From the parent tenancy, open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Subscription Mapping**.
    2. On the **Subscription Mapping** page, select the subscription name from the **Subscription ID** field. 
Under **Mapped tenancies** , the tenancies mapped to the subscription are listed with the tenancy name and mapped date.
  * Use the [oci organizations subscription-mapping list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/subscription-mapping/list.html) command and required parameters to list the subscription mappings for all the subscriptions owned by a particular compartment ID. Only the root compartment is allowed:
Command
CopyTry It
```
oci organizations subscription-mapping list --subscription-id [text] [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListSubscriptionMappings](https://docs.oracle.com/iaas/api/#/en/organizations/latest/SubscriptionMapping/ListSubscriptionMappings) operation to list the subscription mappings for all the subscriptions owned by a particular compartment ID. Only the root compartment is allowed.


Was this article helpful?
YesNo


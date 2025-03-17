Updated 2024-10-30
# Activating an Order
Triggers an order activation workflow on behalf of the tenant, given by compartment ID in the body.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/order-activate.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/order-activate.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/order-activate.htm)


  * For more information, see [Activate Your Order from Your Welcome Email](https://docs.oracle.com/iaas/Content/GSG/Tasks/buysubscription.htm#activate_order).
  * Use the [oci organizations order activate](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/order/activate.html) command and required parameters to activate an order:
Command
CopyTry It
```
oci organizations order activate --activation-token [text] --compartment-id, -c [text] [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ActivateOrder](https://docs.oracle.com/iaas/api/#/en/organizations/latest/Order/ActivateOrder) operation to activate an order.


Was this article helpful?
YesNo


Updated 2023-12-08
# Moving Multiple Resources Between Compartments
Learn how to move multiple resources between compartments at one time.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/bulk-move-resources-compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/bulk-move-resources-compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/bulk-move-resources-compartment.htm)


  * This task can't be performed using the Console.
  * Use the [bulk-move-resources](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/compartment/bulk-move-resources.html) command and required parameters to move multiple resources between compartments:
Command
CopyTry It
```
oci iam compartment bulk-move-resources --generate-param-json-input resources > resources.json

```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [BulkMoveResources](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/BulkMoveResources) operation to move multiple resources between compartments.


Was this article helpful?
YesNo


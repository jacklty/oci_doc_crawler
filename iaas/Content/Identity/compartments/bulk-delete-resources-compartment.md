Updated 2023-12-08
# Deleting Multiple Resources in a Compartment
Learn how to delete multiple resources between compartments at one time.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/bulk-delete-resources-compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/bulk-delete-resources-compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/bulk-delete-resources-compartment.htm)


  * This task can't be performed using the Console.
  * Use the [bulk-delete-resources](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/compartment/bulk-delete-resources.html) command and required parameters to delete multiple resources between compartments at one time:
Command
CopyTry It
```
oci iam compartment bulk-delete-resources --generate-param-json-input resources > resources.json
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [BulkDeleteResources](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/BulkDeleteResources) operation to delete multiple resources in a compartment.


Was this article helpful?
YesNo


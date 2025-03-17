Updated 2025-01-13
# Getting a Compartment's Resources
Learn how to view a compartment's resources.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_view_the_contents_of_a_compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_view_the_contents_of_a_compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_view_the_contents_of_a_compartment.htm)


  * **Tip** In the Console, the tenancy explorer allows you to get a list of resources in a compartment, across regions, with some limitations. For more information, see [Viewing All Resources in a Compartment](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/compartmentexplorer.htm#Viewing_All_Resources_in_a_Compartment).
    1. Open the navigation menu and select the type of resource you want to view. For example, to view Compute resources: Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Choose the compartment from the list on the left side of the page. The page updates to show only the resources in that compartment.
Remember that most IAM resources reside in the tenancy. Policies can reside in either the tenancy (root compartment) or other compartments.
  * Use the [get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/compartment/get.html) command and required parameters to view a compartment's resources:
Command
CopyTry It
```
export compartment_id=compartment_ocid # https://docs.cloud.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/compartment/get.html#cmdoption-compartment-id
oci iam compartment get --compartment-id compartment_ocid

```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * You can retrieve the contents of a compartment only by resource type. There's no API call that lists _all_ resources in the compartment. For example, to list all the instances in a compartment, call the Core Services API [ListInstances](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/ListInstances) operation and specify the compartment ID as a query parameter. 
**Note** You can also list all the resources of a specific type in the compartment (for example, all the instances, all the block storage volumes, and so on). 
Run the [GetCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/GetCompartment) operation to view a compartment's resources.


Was this article helpful?
YesNo


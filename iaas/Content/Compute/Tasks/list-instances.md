Updated 2025-02-27
# Listing Instances
Get a list of the Compute instances in a Oracle Cloud Infrastructure compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/list-instances.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/list-instances.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/list-instances.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
The **Instances** list page opens. All existing instances in the selected compartment are displayed in a list table.
    2. To view the resources in a different compartment, use the **Compartment** filter to switch compartments.
**Note** You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see [Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
Optionally, you can do the following with an instance from the list.
    * Select an instance to view the details page.
    * Select the instance check-box. From the **Actions** menu, reboot, stop, start, or terminate the instance. The operations can be applied to multiple instances.
  * Use the [instance list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/list.html) command and required parameters to list instances:
Copy
```
oci compute instance list --from-json <file://path/to/file.json>
```

<file://path/to/file.json> is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see [Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).
For a complete list of flags and variable options for the Compute service CLI commands, see the [command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use this API operation to list instances:
    * [ListImages](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/ListImages)


Was this article helpful?
YesNo


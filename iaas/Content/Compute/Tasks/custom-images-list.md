Updated 2025-02-27
# Listing Custom Images
Get a list of the Compute custom images in an Oracle Cloud Infrastructure compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-list.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Custom Images**.
The **Custom Images** list page opens. All existing custom images in the selected compartment are displayed in a list table.
    2. To view the resources in a different compartment, use the **Compartment** filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see [Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
Optionally, you can do the following with a custom image from the list.
    * Select an custom image to view the details page.
    * For a custom image, from the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), export the custom image, create an instance from the custom image, or delete the custom image.
  * Use the [image list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/list.html) command and required parameters to list custom images:
Copy
```
oci compute image list --from-json <file://path/to/file.json>
```

<file://path/to/file.json> is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see [Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).
For a complete list of flags and variable options for the Compute service CLI commands, see the [command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use this API operation to list instances:
    * [ListImages](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/ListImages)


Was this article helpful?
YesNo


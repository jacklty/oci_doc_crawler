Updated 2025-03-05
# Getting a Custom Image
Get the details of a Compute custom image in an Oracle Cloud Infrastructure compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-get.htm)


  *     1. On the Compute custom images list page, select the custom image that you want to view. If you need help finding the custom images list page, see [Listing Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-list.htm#listing-custom-images "Get a list of the Compute custom images in an Oracle Cloud Infrastructure compartment.").
From the selected image you can:
    * View the image capabilities. Image capabilities are the configuration options available when launching an instance from an image.
    * View the compatible shapes for this image.
    * View any work requests related to this image.
    * View tags assigned to this image.
  * Use the [image get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/get.html) command and required parameters to get a custom image:
Copy
```
oci compute image get --from-json <file://path/to/file.json>
```

Use the [image-shape-compatibility-entry list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image-shape-compatibility-entry/list.html) command and required parameters to get the list of compatible shapes:
Copy
```
oci compute image-shape-compatibility-entry list --from-json <file://path/to/file.json>
```

<file://path/to/file.json> is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see [Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).
For a complete list of flags and variable options for the Compute service CLI commands, see the [command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use this API operation to get an instance:
    * [GetImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/GetImage)
    * [ListImageShapeCompatibilityEntries](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ImageShapeCompatibilityEntry/ListImageShapeCompatibilityEntries)


Was this article helpful?
YesNo


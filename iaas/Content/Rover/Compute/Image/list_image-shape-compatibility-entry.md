Updated 2024-09-16
# Listing Image Shape Compatibility Entries for a Roving Edge Infrastructure Device
Describes how to list the image shape compatibility entries for the image on your Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/list_image-shape-compatibility-entry.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/list_image-shape-compatibility-entry.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/list_image-shape-compatibility-entry.htm)


  *     1. Open the navigation menu and select **Compute > Images**. The **Custom Images** page appears. All custom images are listed in tabular form.
    2. Select a **State** from the list to limit the images displayed to that state.
    3. Click the image whose details you want to get. The image's **Details** page appears.
    4. Click **Edit Details**. The list of compatible shapes for the image is displayed.
  * Use the [oci compute image-shape-compatibility-entry list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image-shape-compatibility-entry/list.html) command and required parameters to list the image shape compatibility entries for the image on your Roving Edge Infrastructure devices:
Copy
```
oci compute image-shape-compatibility-entry list --image-id image_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [ListImageShapeCompatibilityEntries](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ImageShapeCompatibilityEntry/ListImageShapeCompatibilityEntries) operation to list the image shape compatibility entries for the image on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo


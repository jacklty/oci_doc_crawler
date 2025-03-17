Updated 2024-09-16
# Removing an Image Shape Compatibility Entry from a Roving Edge Infrastructure Device
Describes how to remove an image shape compatibility entry on your Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/remove_image-shape-compatibility-entry.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/remove_image-shape-compatibility-entry.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/remove_image-shape-compatibility-entry.htm)


  *     1. Open the navigation menu and select **Compute > Images**. The **Custom Images** page appears. All custom images are listed in tabular form.
    2. Select a **State** from the list to limit the custom images displayed to that state.
    3. Click the image entry whose details you want to get. The image's **Details** page appears.
    4. Click **Edit Details**.
    5. Remove the compatible shape entry.
  * Use the [oci compute image-shape-compatibility-entry remove](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image-shape-compatibility-entry/remove.html) command and required parameters to remove an image shape compatibility entry on your Roving Edge Infrastructure devices:
Copy
```
oci compute image-shape-compatibility-entry remove --image-id image_ocid --shape-name shape_name [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [RemoveImageShapeCompatibilityEntry](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ImageShapeCompatibilityEntry/RemoveImageShapeCompatibilityEntry) operation to remove an image shape compatibility entry on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo


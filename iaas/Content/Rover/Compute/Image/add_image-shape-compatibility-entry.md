Updated 2024-09-16
# Adding an Image Shape Compatibility Entry to a Roving Edge Infrastructure Device
Describes how to add a shape to the compatible shapes list for the image on your Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/add_image-shape-compatibility-entry.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/add_image-shape-compatibility-entry.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/add_image-shape-compatibility-entry.htm)


  *     1. Open the navigation menu and select **Compute > Images**. The **Custom Images** page appears. All custom images are listed in tabular form.
    2. Select a **State** from the list to limit the custom images displayed to that state.
    3. Click the custom image whose details you want to get. The custom image's Details page appears.
    4. Click **Edit Details**.
    5. Add and compatible shapes for the custom image.
    6. To configure the minimum and maximum number of OCPUs that users can select when they use this image on a flexible shape:
      1. Click the down arrow in the row for the shape.
      2. Enter the minimum and maximum OCPU counts.
    7. Click **Save Changes**.
**Note**
After you add shape compatibility to an image, test the image on the shape to ensure that the image actually works on the shape. Some images (especially Windows) might never be cross-compatible with other shapes because of driver or hardware differences.
  * Use the [oci compute image-shape-compatibility-entry add](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image-shape-compatibility-entry/add.html) command and required parameters to add a shape to the compatible shapes list for the image on your Roving Edge Infrastructure devices:
Copy
```
oci compute image-shape-compatibility-entry add --image-id image_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [AddImageShapeCompatibilityEntry](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ImageShapeCompatibilityEntry/AddImageShapeCompatibilityEntry) operation to add a shape to the compatible shapes list for the image on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo


Updated 2024-09-16
# Editing an Image for a Roving Edge Infrastructure Device
Describes how to edit a custom image for use in launching an instance on your Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/update_image.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/update_image.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/update_image.htm)


  *     1. Open the navigation menu and select **Compute > Images**. The **Custom Images** page appears. All custom images are listed in tabular form.
    2. Select a **State** from the list to limit the images displayed to that state.
    3. Click the image whose details you want to get. The image's **Details** page appears.
    4. Click **Edit Details**.
    5. Make your edits. See [Importing a Custom Image](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/import_from-object_image.htm#top "Describes how to import a custom image from an object storage bucket for use in launching an instance on your Roving Edge Infrastructure device.") for descriptions of the settings.
    6. Click **Save Changes**.
**Note**
After you add shape compatibility to an image, test the image on the shape to ensure that the image actually works on the shape. Some images (especially Windows) might never be cross-compatible with other shapes because of driver or hardware differences.
  * Use the [oci compute image update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/update.html) command and required parameters to edit a custom image for use in launching an instance on your Roving Edge Infrastructure devices:
Copy
```
oci compute image update --image-id image_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [UpdateImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/UpdateImage) operation to edit a custom image for use in launching an instance on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo


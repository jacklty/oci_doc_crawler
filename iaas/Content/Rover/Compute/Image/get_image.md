Updated 2024-09-16
# Getting an Image's Details for a Roving Edge Infrastructure Device
Describes how to get the details of a custom image for use in launching an instance on your Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/get_image.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/get_image.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/get_image.htm)


  *     1. Open the navigation menu and select **Compute > Images**. The **Custom Images** page appears. All custom images are listed in tabular form.
    2. Select a **State** from the list to limit the images displayed to that state.
    3. Click the image whose details you want to get. The image's **Details** page appears.
  * Use the [oci compute image get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/get.html) command and required parameters to get the details of a custom image for use in launching an instance on your Roving Edge Infrastructure devices:
Copy
```
oci compute image get --image-id image_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [GetImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/GetImage) operation to get the details of a custom image for use in launching an instance on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo


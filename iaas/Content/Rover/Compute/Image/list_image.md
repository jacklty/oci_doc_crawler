Updated 2024-09-16
# Listing Images for a Roving Edge Infrastructure Device
Describes how to list the custom images for use in launching an instance on your Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/list_image.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/list_image.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/list_image.htm)


  *     1. Open the navigation menu and select **Compute > Images**. The **Custom Images** page appears. All custom images are listed in tabular form.
    2. Select a **State** from the list to limit the custom images displayed to that state.
  * Use the [oci compute image list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/list.html) command and required parameters to list the custom images for use in launching an instance on your Roving Edge Infrastructure devices:
Copy
```
oci compute image list --compartment-id compartment_ocid [OPTIONS]
```

To determine your Roving Edge Infrastructure device compartment OCID, see [Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/compartments.htm#comparments "Describes how the Roving Edge Infrastructure device uses its compartment, and how to gain information on it.").
Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [ListImages](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/ListImages) operation to list the custom images for use in launching an instance on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo


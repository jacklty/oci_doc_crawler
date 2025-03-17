Updated 2024-09-16
# Exporting a Custom Image to Object Storage for a Roving Edge Infrastructure Device
Describes how to export a custom image to object storage on your Roving Edge Infrastructure device.
Export custom compute images to object service in qcow2 format. The exported images are exported to a specified bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/export_to-object_image.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/export_to-object_image.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/export_to-object_image.htm)


  *     1. Open the navigation menu and select **Compute > Images**. The **Custom Images** page appears. All custom images are listed in tabular form.
    2. (Optional) Select a **State** from the list to limit the images displayed to that state.
    3. Click the image that you want to export to object storage. The image's **Details** page appears.
    4. Click **Export**. The **Export Image** dialog box appears.
    5. Select the object storage **Bucket** on your Roving Edge Infrastructure device where you want to export the image
    6. Enter the **Name** of the exported image. The image is exported in `.qcow2` format.
    7. Click **Export Image**.
After you click **Export Image** , the image state changes to **Exporting**. You can still launch instances while the image is exporting, but you can't delete the image until the export has finished. To track the progress of the operation, you can monitor the associated work request. For more information, see [Using the Console to View Work Requests](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr) in the Oracle Cloud Infrastructure documentation.
When the export is complete, the image state changes to **Available**. If the image state changes to **Available** , but you do not see the exported image in the object storage bucket location you specified, this means that the export failed, and you will need to go through the steps again to export the image.
  * Use the [oci compute image export to-object](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/export/to-object.html) command and required parameters to export a custom image to object storage on your Roving Edge Infrastructure devices:
```
oci compute image export to-object --bucket-name bucket_name --image-id image_ocid --namespace rover-namespace [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [ExportImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/ExportImage) operation to export a custom image to object storage on your Roving Edge Infrastructure devices


Was this article helpful?
YesNo


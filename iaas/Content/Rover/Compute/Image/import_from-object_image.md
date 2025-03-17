Updated 2024-09-16
# Importing a Custom Image from a Bucket into a Roving Edge Infrastructure Device
Describes how to import a custom image from an object storage bucket for use in launching an instance on your Roving Edge Infrastructure device.
Roving Edge Infrastructure supports importing QCOW2 and OCI type images.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/import_from-object_image.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/import_from-object_image.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/import_from-object_image.htm)


  *     1. Open the navigation menu and select **Compute > Images**. The **Custom Images** page appears. All custom images are listed in tabular form.
    2. Click **Import Image**. The **Import Image** dialog box appears.
    3. Enter a **Name** for the image.
    4. Select the **Operating System** :
       * For Linux images, select **Linux**.
       * For Windows images, select **Windows**. Select the **Operating System Version** , and then certify that the selected operating system complies with Microsoft licensing agreements.
    5. Click the **Import from an Object Storage bucket** option.
    6. Select the **Bucket** that contains the image.
    7. Select the image file from the **Object Name** list.
    8. Select the **Image Type** option:
       * **QCOW2**
       * **OCI**
    9. Click **Import Image**.
After you click **Import Image** , you'll see the imported image in the **Custom Images** list for the compartment, with a state of **Importing**. To track the progress of the operation, you can monitor the associated work request.
When the import completes successfully, the state changes to **Available**. If the state does not change, or no entry appears in the **Custom Images** list, the import failed. If the import failed, ensure you have read access to the Object Storage object, and that the object contains a supported image.
  * Use the [oci compute image import from-object](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/import/from-object.html) command and required parameters to import a custom image for use in launching an instance on your Roving Edge Infrastructure devices:
Copy
```
oci compute image import from-object --compartment-id compartment_ocid --bucket-name bucket_name --name name [OPTIONS]
```

To determine your Roving Edge Infrastructure device compartment OCID, see [Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/compartments.htm#comparments "Describes how the Roving Edge Infrastructure device uses its compartment, and how to gain information on it.").
Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [CreateImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/CreateImage) operation and specify [ImageSourceDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/ImageSourceDetails) in the request body to import an image from object storage.


Was this article helpful?
YesNo


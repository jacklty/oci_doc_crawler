Updated 2024-09-16
# Importing a Custom Image from a URL for a Roving Edge Infrastructure Device
Describes how to import a custom image from an object storage URL for use in launching an instance on your Roving Edge Infrastructure device.
Roving Edge Infrastructure supports importing QCOW2 type images. Roving Edge Infrastructure also supports importing some OCI type images, but in some instances importing an OCI type image fails.
Roving Edge Infrastructure supports importing an image from a Roving Edge Infrastructure source URL and OCI Pre-authenticated request (PAR) URL only. See [Using Pre-Authenticated Requests](https://docs.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm) in the Oracle Cloud Infrastructure documentation for more information on this feature.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/import_from-object_image-uri.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/import_from-object_image-uri.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/import_from-object_image-uri.htm)


  *     1. Open the navigation menu and select **Compute > Images**. The **Custom Images** page appears. All custom images are listed in tabular form.
    2. Click **Import Image**. The **Import Image** dialog box appears.
    3. Enter a **Name** for the image.
    4. Select the **Operating System** :
       * For Linux images, select **Linux**.
       * For Windows images, select **Windows**. Select the **Operating System Version** , and then certify that the selected operating system complies with Microsoft licensing agreements.
    5. Click the **Import from an Object Storage URL** option.
    6. Enter the URL to the image in the **Object Storage URL** box.
    7. Select the **Image Type** option:
       * **QCOW2**
       * **OCI**
    8. Click **Import Image**.
After you click **Import Image** , you'll see the imported image in the **Custom Images** list for the compartment, with a state of **Importing**. To track the progress of the operation, you can monitor the associated work request.
When the import completes successfully, the state changes to **Available**. If the state does not change, or no entry appears in the **Custom Images** list, the import failed. If the import failed, ensure you have read access to the Object Storage object, and that the object contains a supported image.
  * Use the [oci compute image import from-object-uri](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/import/from-object-uri.html) command and required parameters to import a custom image from a URI for use in launching an instance on your Roving Edge Infrastructure devices:
Copy
```
oci compute image import from-object-uri --compartment-id compartment_ocid --uri uri --name name [OPTIONS]
```

To determine your Roving Edge Infrastructure device compartment OCID, see [Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/compartments.htm#comparments "Describes how the Roving Edge Infrastructure device uses its compartment, and how to gain information on it.").
Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [CreateImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/CreateImage) operation and specify [ImageSourceDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/ImageSourceDetails) in the request body to import an image from object storage.


Was this article helpful?
YesNo


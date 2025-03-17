Updated 2024-01-18
# Exporting an Image to a URL
On Compute Cloud@Customer, you can export an image to a URL.
Exported images are a copy of the boot volume and metadata when the image was created.
**Note**
As an alternative, you can export an image to a URL as described in [Exporting an Image to an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/exporting-an-image-to-object-storage.htm#exporting-an-image-to-object-storage "On Compute Cloud@Customer, you can export an image to an Object Storage bucket.").
**Prerequisite**
  * You need write access to the to the export location.


  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/exporting-an-image-to-a-url.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/exporting-an-image-to-a-url.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/exporting-an-image-to-a-url.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Custom Images**.
    2. At the top of the page, select the compartment that contains the image you want to export.
    3. Click the name of the custom image that you want to export. 
    4. On the image details page, click **Controls** (upper right corner), and then click **Export Image**.
    5. In the **Export Custom Image** dialog box, enter the following information:
       * **Export Destination:** Select the **Export to an Object Storage URL** option.
       * **Object Storage URL:** Enter the URL where you want to export the image. The URL doesn't need to be an Object Storage URL. It can be any URL that provides access to the image.
       * **Export Format:** Select one of the following options based on the type of image you're exporting.
         * **VMDK:** Virtual machine disk file format (`.vmdk`), used for virtual machine disk images.
         * **QCOW2:** For disk image files (`.qcow2`) used by QEMU copy on write.
         * **OCI:** For Oracle Cloud Infrastructure files with a QCOW2 image and OCI metadata (`.oci`).
    6. Click **Export Image**.
The image state changes to Exporting. Exporting a custom image copies the data to the Object Storage location that you specified. To track the progress of the operation, view the associated work request.
You can still create instances while the image is exporting, but you can't delete the image until the export has finished.
When the export is complete, the image state changes to Available. If the image state changes to Available, but you don't see the exported image in the Object Storage location you specified, the export failed, and you need to go through the steps again to export the image.
  * Use the [oci compute image export to-object-uri](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/export/to-object-uri.html) command and required parameters to export the specified image to the Object Storage service using the Object Storage URL to identify the location to export to.
Copy
```
oci compute image export to-object-uri --image-id <image_OCID> --uri <url_to_export_to> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ExportImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/ExportImage) operation to export the specified image to the Object Storage service using the Object Storage URL to identify the location to export to.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


Updated 2024-01-18
# Exporting an Image to an Object Storage Bucket
On Compute Cloud@Customer, you can export an image to an Object Storage bucket. 
Exported images are a copy of the boot volume and metadata when the image was created.
**Note**
As an alternative, you can export an image to a URL as described in [Exporting an Image to a URL](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/exporting-an-image-to-a-url.htm#exporting-an-image-to-a-url "On Compute Cloud@Customer, you can export an image to a URL.").
**Prerequisites**
  * Ensure that a bucket is available. See [Listing Buckets](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/listing-buckets.htm#listing-buckets "On Oracle Compute Cloud@Customer, you can list buckets.") and [Creating a Bucket](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/creating-a-bucket.htm#creating-a-bucket "On Compute Cloud@Customer, you can create Object Storage buckets.").
  * You need write access to the to the export location.


  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/exporting-an-image-to-object-storage.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/exporting-an-image-to-object-storage.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/exporting-an-image-to-object-storage.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Custom Images**.
    2. At the top of the page, select the compartment that contains the image you want to export.
    3. Click the name of the custom image that you want to export. 
    4. On the image details page, click **Controls** (upper right corner), and then click **Export Image**.
    5. In the **Export Custom Image** dialog box, enter the following information:
       * **Export Destination:** Select the **Export to an Object Storage Bucket** option.
       * **Bucket:** Select a bucket. If needed, use the menu to select a different compartment.
       * **Object Name:** Enter a name for the exported image.
       * **Export Format:** Select one of the following options based on the type of image you're exporting.
         * **VMDK:** Virtual machine disk file format (`.vmdk`), used for virtual machine disk images.
         * **QCOW2:** For disk image files (`.qcow2`) used by QEMU copy on write.
         * **OCI:** For Oracle Cloud Infrastructure files with a QCOW2 image and OCI metadata (`.oci`).
    6. Click **Create Export**.
The image state changes to Exporting. Exporting a custom image copies the data to the Object Storage location that you specified. To track the progress of the operation, view the associated work request.
You can still create instances while the image is exporting, but you can't delete the image until the export has finished.
When the export is complete, the image state changes to Available. If the image state changes to Available, but you don't see the exported image in the Object Storage location you specified, the export failed, and you need to go through the steps again to export the image.
  * Use the [oci compute image export to-object](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/export/to-object.html) command and required parameters to export the specified image to an Object Storage bucket.
Copy
```
oci compute image export to-object --bucket-name bucketname --image-id image_OCID --namespace namespace --name exported_image_object_name --export-format VMDK [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ExportImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/ExportImage) operation to export the specified image to an Object Storage bucket.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


Updated 2024-08-06
# Importing an Image from an Object Storage Bucket
On Compute Cloud@Customer, you can import an image into a compartment from an Object Storage bucket.
**Note**
Alternatively, you can import an image from a URL as described in [Importing an Image from a URL](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/importing-an-image-from-a-url.htm#importing-an-image-from-a-url "On Compute Cloud@Customer, you can import an image into a compartment by specifying the URL of the image file.").
**Before You Begin**
Ensure you have read access to the Object Storage bucket, and that the bucket contains the image that you want to use. See [Managing Object Storage Buckets](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/managing-object-storage-buckets.htm#managing-object-storage-buckets "On Compute Cloud@Customer, a bucket is a container for storing objects in a compartment within an Object Storage namespace.").
If the bucket doesn't contain the image that you want to use, perform the procedure described in [Uploading an Image to an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/uploading-an-image-to-an-object-storage-bucket.htm#uploading-an-image-to-an-object-storage-bucket "On Compute Cloud@Customer, you can store images in an object storage bucket.").
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/importing-an-image-from-an-object-storage-bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/importing-an-image-from-an-object-storage-bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/importing-an-image-from-an-object-storage-bucket.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Custom Images**.
    2. Click **Import Image**.
    3. In the **Import Image** dialog box, enter the following information:
       * **Name:** Enter a descriptive name for the image.
Avoid entering confidential information.
       * **Create in Compartment:** Select the compartment for the image.
       * **Source Type:** Select the Import from an Object Storage Bucket option.
       * **Bucket:** Select a bucket. You might need to change the compartment to locate the bucket.
       * **Object Name:** Select the name of an image object from the list.
       * **Image Type:** Select one of the following options based on the type of image you're importing.
         * **VMDK:** Virtual machine disk file format (`.vmdk`), used for virtual machine disk images.
         * **QCOW2:** For disk image files (`.qcow2`) used by QEMU copy on write.
         * **OCI:** For Oracle Cloud Infrastructure files with a QCOW2 image and OCI metadata (`.oci`).
       * **Launch Mode:** Paravirtualized is the default and can't be changed.
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    4. Click **Import Image**.
The imported image appears in the **Custom Images** list for the compartment, with a state of Importing. To track the progress of the operation, view the associated work request.
When the import completes successfully, the image state changes to available, and the image can be used to create instances as described in [Creating an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance.htm#creating-an-instance "On Compute Cloud@Customer, you can create an instance using the Compute Cloud@Customer Console, CLI, and API.").
  * Use the [oci compute image import from-object](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/import/from-object.html) command and required parameters to import an image from an Object Storage bucket.
Copy
```
oci compute image import from-object --compartment-id compartment_OCID --bucket-name bucket_name --name bucket_image_object_name --namespace namespace [OPTIONS]
```

**Important**
If you are importing a Microsoft Windows image, specify the `--operating-system` option and include the case-insensitive string "Windows" in the value to ensure optimal performance of the instance.
If you specify the `--operating-system` option and this is _not_ a Microsoft Windows image, make sure the value does not contain the case-insensitive string "Windows".
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * This operation can't be performed using the API.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


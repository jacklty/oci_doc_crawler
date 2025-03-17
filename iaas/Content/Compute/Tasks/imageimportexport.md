Updated 2025-03-05
# Image Import/Export
You can share custom images across tenancies and regions using image import/export.
**Important** To import or export custom images from Object Storage buckets, [federated users](https://docs.oracle.com/iaas/Content/Identity/Concepts/federation.htm) and users authenticating with instance principals tied to a dynamic group need to create a [pre-authenticated request](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/imageimportexport.htm#URLs__PAR). For more information, see the known issue [Invalid bucketName error when importing or exporting a custom image](https://docs.oracle.com/en-us/iaas/Content/Compute/known-issues.htm#invalid-bucketName).
Platform images, Marketplace images, and custom images that are created from Marketplace images cannot be exported.
## Linux-Based Operating Systems 🔗 
The following operating systems support image import/export:
  * Oracle Linux 7.x
  * Oracle Linux 8.x
  * Oracle Linux 9.x
  * Oracle Linux Cloud Developer 8.x
  * Ubuntu 20.04
  * Ubuntu 22.04
  * Ubuntu 24.04


## Windows-Based OSs 🔗 
The following Windows versions support image import/export:
  * Windows Server 2016 Standard, Data center
  * Windows Server 2019 Standard, Data center
  * Windows Server 2022 Standard, Data center


**Important**
When exporting Windows-based images, you are responsible for complying with the [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/) and all product use conditions, as well as verifying your compliance with Microsoft.
For information about the licensing requirements for Windows images, see [Microsoft Licensing on Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Compute/References/microsoftlicensing.htm#Microsoft_Licensing_on_Oracle_Cloud_Infrastructure).
### Verify The Windows OS 🔗 
When importing custom Windows images, ensure that the version you select matches the Windows image that you imported. Failure to provide the correct version and SKU information could be a violation of the Microsoft Licensing Agreement. 
### Windows System Time Issue on Custom Windows Instances 🔗 
If you change the time zone from the default setting on Windows VM instances, when the instance reboots or syncs with the hardware clock, the system time will revert back to the time for the default time zone. However, the time zone setting will stay set to the new time zone, so the system clock will be incorrect. You can fix this by setting the `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation` registry key to 1.
Windows platform images already have the `RealTimeIsUniversal` registry key set by default, but you must set this for any custom Windows images that you import.
To fix this issue for custom Windows images:
  1. Open the Windows Registry Editor and navigate to the `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation` registry key.
  2. Create a new `DWORD` key named `RealTimeIsUniversal` and set the value to 1.
  3. Reboot the instance.
  4. Reset the time and time zone manually.


## Bring Your Own Image Scenarios 🔗 
You can also use image import/export to share custom images from [Bring Your Own Image (BYOI)](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bringyourownimage.htm#Bring_Your_Own_Image_BYOI) scenarios across tenancies and regions, so you don't need to recreate the image manually in each region. You must go through the steps required to manually create the image in one of the regions, but after this is done, you can export the image, making it available for import in additional tenancies and regions. Export the image in the `.oci` format, which is a file format that contains a QCOW2 image file and Oracle Cloud Infrastructure-specific metadata.
### Best practices for replicating an image across regions 🔗 
You can replicate an image from one region to another region using the Console or API. At a high level:
  1. [Export the image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/imageimportexport.htm#Exporting) to an Object Storage bucket in the same region as the image.
  2. [Copy the image](https://docs.oracle.com/iaas/Content/Object/Tasks/copyingobjects.htm) to an Object Storage bucket in the destination region.
  3. [Obtain the URL path to the image object](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects_topic-To_get_object_details.htm).
  4. In the destination region, [import the image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/imageimportexport.htm#Importing). Use the URL path as the Object Storage URL.


### Best practices for sharing an image across tenancies 🔗 
You can replicate an image from one tenancy to another tenancy using the Console or API. At a high level:
  1. [Export the image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/imageimportexport.htm#Exporting) to an Object Storage bucket in the same region as the image.
  2. [Working with Pre-Authenticated Requests](https://docs.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-Working_with_PreAuthenticated_Requests.htm) with read-only access for the image in the destination region.
  3. In the destination tenancy, [import the image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/imageimportexport.htm#Importing). Use the pre-authenticated request URL as the Object Storage URL.


## Object Storage Service URLs 🔗 
When you import or export custom images using the Console, you might need to specify the Object Storage URL pointing to the location that you want to import the image from or export the image to. Object Storage URLs are structured as follows:
```
https://<host_name>/n/<namespace_name>/b/<bucket_name>/o/<object_name>
```

For example:
```
https://objectstorage.us-phoenix-1.oraclecloud.com/n/MyNamespace/b/MyBucket/o/MyCustomImage.qcow2
```

### Pre-Authenticated Requests 🔗 
When using import/export across tenancies, you need to use an Object Storage pre-authenticated request. See [Working with Pre-Authenticated Requests](https://docs.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-Working_with_PreAuthenticated_Requests.htm) for steps to create a pre-authenticated request. When you go through these steps, after you click **Create Pre-Authenticated Request** , the **Pre-Authenticated Request Details** dialog box opens. You must make a copy of the pre-authenticated request URL displayed here, because this is the only time this URL is displayed. This is the Object Storage URL that you specify for import/export. 
**Note**
Pre-authenticated requests for a bucket
With image export, if you create the pre-authenticated request for a bucket, you need to append the object name to the generated URL. For example:
```
/o/MyCustomImage.qcow2
```

## Exporting an Image 🔗 
You can use the Console or API to export images, and the exported images are stored in the Oracle Cloud Infrastructure Object Storage service. To perform an image export, you need write access to the Object Storage bucket for the image. For more information, see [Overview of Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm) and [Let users write objects to Object Storage buckets](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#write-objects-to-buckets). 
### To export an image using the Console 🔗 
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Custom Images**.
  2. Click the custom image that you're interested in.
  3. Click **Export**.
  4. Specify the Object Storage location to export the image to:
     * **Export to an Object Storage bucket:** Select a bucket. Then, enter a name for the exported image. Avoid entering confidential information.
     * **Export to an Object Storage URL:** Enter the Object Storage URL.
  5. In the **Image format** list, select the format that you want to export the image to. The following formats are available:
     * Oracle Cloud Infrastructure file with a QCOW2 image and OCI metadata (.oci). Use this format to export a custom image that you want to import into other tenancies or regions.
     * QEMU Copy On Write (.qcow2)
     * Virtual Disk Image (.vdi) for Oracle VM VirtualBox
     * Virtual Hard Disk (.vhd) for Hyper-V
     * Virtual Machine Disk (.vmdk)
  6. Click **Export image**.


After you click **Export image** , the image state changes to **Exporting**. Images are a copy of the VM or BM instance boot volume and metadata when the image is created, capturing the current state of the instance. Exporting a custom image copies the data to the Object Storage location that you specified. You can still launch instances while the image is exporting, but you can't delete the image until the export has finished. To track the progress of the operation and [troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances-monitoring-work-requests.htm#work-requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") that occur during instance creation, use the associated [work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
When the export is complete, the image state changes to **Available**. If the image state changes to **Available** , but you don't see the exported image in the Object Storage location you specified, the export failed, and you need to go through the steps again to export the image.
## Importing an Image 🔗 
You can use the Console or API to import exported images from Object Storage. To import an image, you need read access to the Object Storage object containing the image. For more information, see [Let users download objects from Object Storage buckets](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#download-objects-from-buckets). 
### To import an image using the Console 🔗 
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Custom Images**.
  2. Click **Import image**.
  3. In the **Create in compartment** list, select the compartment that you want to import the image to.
  4. Enter a **Name** for the image. Avoid entering confidential information.
  5. Select the **Operating system** :
     * For Linux images, select **Linux**.
     * For Windows images, select **Windows**. Select the **Operating system version** , and then certify that the selected operating system complies with Microsoft licensing agreements.
  6. Specify the [Object Storage location](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/imageimportexport.htm#URLs) to import the image from:
     * **Import from an Object Storage bucket:** Select the **Bucket** that contains the image. In the **Object name** list, select the image file.
     * **Import from an Object Storage URL:** Enter the **Object Storage URL** of the image. When importing across tenancies, you must specify a pre-authenticated request URL.
  7. In the **Image type** section, select the format of the image. The following formats are available:
     * **VMDK:** Virtual Machine Disk (.vmdk)
     * **QCOW2:** QEMU Copy On Write (.qcow2)
     * **OCI:** Oracle Cloud Infrastructure file with a QCOW2 image and OCI metadata (.oci). Use this format when importing a custom image that was exported from another tenancy or region.
  8. Select the **Launch mode** :
     * For custom images where the image type is `.oci`, the launch mode is disabled. Oracle Cloud Infrastructure selects the appropriate launch mode based on the launch mode for the source image.
     * For custom images exported from Oracle Cloud Infrastructure where the image type is QCOW2, select **Native mode**.
     * To import other custom images, select **Paravirtualized mode** or **Emulated mode**. For more information, see [Bring Your Own Image](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bringyourownimage.htm#options__launchmodes).
  9. **Show tagging options:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
  10. Click **Import image**.


After you click **Import image** , you'll see the imported image in the **Custom images** list for the compartment, with a state of **Importing**. To track the progress of the operation and [troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances-monitoring-work-requests.htm#work-requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") that occur during instance creation, use the associated [work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
When the import completes successfully, the state changes to **Available**. If the state does not change, or no entry appears in the **Custom images** list, the import failed. If the import failed, ensure you have read access to the Object Storage object, and that the object contains a supported image.
## Editing Image Details 🔗 
You can edit the details of custom images, such as the image name and compatible shapes for the image. For more information, see [Custom Image Tasks](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm#Managing_Custom_Images__console-custom-image-tasks) in [Managing Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm#Managing_Custom_Images "You can create a custom image of an instance's boot disk and use it to launch other instances. Instances you launch from your image include the customizations, configuration, and software installed when you created the image.").
## Managing Tags for an Image 🔗 
Apply tags to resources to help organize them according to business needs. Apply tags at the time you create a resource, or update the resource later with the wanted tags. For general information about applying tags, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
[To manage tags for an image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/imageimportexport.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Custom Images**.
  2. Click the image that you're interested in.
  3. Click the **Tags** tab to view or edit the existing tags. Or click **More Actions** , and then click **Add Tags** to add new ones.


## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following API operations for custom image import/export:
  * [ExportImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/ExportImage): Exports a custom image to Object Storage. 
  * [CreateImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/CreateImage): To import an exported image, specify [ImageSourceDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/ImageSourceDetails) in the request body. 
  * [AddImageShapeCompatibilityEntry](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ImageShapeCompatibilityEntry/AddImageShapeCompatibilityEntry): Adds a shape to the compatible shapes list for the image.
  * [ListImageShapeCompatibilityEntries](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ImageShapeCompatibilityEntry/ListImageShapeCompatibilityEntries)
  * [GetImageShapeCompatibilityEntry](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ImageCompatibilityEntry/GetImageCompatibilityEntry)
  * [RemoveImageShapeCompatibilityEntry](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ImageShapeCompatibilityEntry/RemoveImageShapeCompatibilityEntry): Removes a shape from the compatible shapes list for the image.


## X5 and X7 Compatibility for Image Import/Export 🔗 
Oracle X5, X6, and X7 servers have different host hardware. As a result, using an X5 or X6 image on an X7 bare metal or virtual machine (VM) instance may not work without additional modifications. Oracle recommends for X7 hosts that you use the platform images for X7. See [Image Release Notes](https://docs.oracle.com/iaas/images/) for more information about which images support X7. These images have been explicitly created and tested with X7 hardware.
If you attempt to use an existing X5 image on X7 hardware, note the following:
  * No Windows versions are cross-compatible.
  * Oracle Autonomous Linux 7 and Oracle Linux 8 are cross-compatible.
  * Oracle Linux 7, Oracle Linux 8, Oracle Linux 9, Ubuntu 18.04, Ubuntu 20.04, Ubuntu 22.04, CentOS 7, and CentOS Stream 8 are cross-compatible. You may have to update the kernel, however, to the most recent version to install the latest device drivers. To update the kernel, run one of the following commands from a terminal session:
    * **Oracle Linux**
Copy
```
yum update
```

    * **CentOS 7** , **CentOS Stream 8**
Copy
```
yum update
```

    * **Ubuntu 18.04** , **Ubuntu 20.04** , **Ubuntu 22.04**
Copy
```
apt-get update
              apt-get dist-upgrade
```



If you attempt to use an X6 image on non-X6 hardware, then note the following:
  * All CentOS versions and all Windows versions are not cross-compatible.
  * Oracle Autonomous Linux 7 and Oracle Linux 8 are cross-compatible.
  * Oracle Linux 7, Ubuntu 22.04, Ubuntu 20.04, and Ubuntu 18.04 are cross-compatible. Use the platform images for X6.


The primary device drivers that are different between X5, X6, and X7 hosts are:
  * Network device drivers
  * NVMe drive device drivers
  * GPU device drivers


Additional updates might be required depending on how you have customized the image.
Was this article helpful?
YesNo


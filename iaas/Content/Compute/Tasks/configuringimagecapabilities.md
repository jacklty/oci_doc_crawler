Updated 2025-02-13
# Configuring Image Capabilities for Custom Images
Image capabilities are the configuration options available when launching an instance from an image. Some image capability examples are the firmware used to boot the instance, the volume attachment types supported, and so on. The full set of image capabilities provided by Oracle Cloud Infrastructure Compute are defined in the global image capability schema. You can also create your own custom image capability schemas based on the global image capability schema to specify and configure image capabilities for your custom images. Using these schemas, you can customize the image configuration and options available when users launch instances from your custom images.
**Caution** Using this feature allows you to customize image capabilities from the default capabilities that Oracle recommends and should be used for advanced custom image scenarios only. Ensure that you understand the optimal configuration options for your custom image.
## Global Image Capability Schema 🔗 
The following JSON is what's returned when you use the `GetComputeGlobalImageCapabilitySchemaVersion` API operation or the `global-image-capability-schema-version` CLI command. It represents the full set of image capabilities available for images. The default values specified for each element are the recommended values for each option.
You can customize these options by creating image capability schemas. When you create an image capability schema, you can specify a subset of the values that are included in the global capabilities schema. Values that are not included in the global capabilities schema cannot be provided in an image capability schema.
Copy
```
{
 "Compute.AMD_SecureEncryptedVirtualization": {
  "descriptorType": "boolean",
  "source": "IMAGE",
  "defaultValue": false
 },
 "Compute.Firmware": {
  "descriptorType": "enumstring",
  "values": [
   "BIOS",
   "UEFI_64"
  ],
  "defaultValue": "UEFI_64"
 },
 "Compute.SecureBoot": {
   "descriptorType": "boolean",
   "defaultValue": false
 },
 "Compute.LaunchMode": {
  "descriptorType": "enumstring",
  "values": [
   "NATIVE",
   "EMULATED",
   "PARAVIRTUALIZED",
   "CUSTOM"
  ],
  "defaultValue": "PARAVIRTUALIZED"
 },
 "Network.AttachmentType": {
  "descriptorType": "enumstring",
  "values": [
   "E1000",
   "VFIO",
   "PARAVIRTUALIZED"
  ],
  "defaultValue": "PARAVIRTUALIZED"
 },
 "Storage.BootVolumeType": {
  "descriptorType": "enumstring",
  "values": [
   "ISCSI",
   "SCSI",
   "IDE",
   "PARAVIRTUALIZED"
  ],
  "defaultValue": "PARAVIRTUALIZED"
 },
 "Storage.LocalDataVolumeType": {
  "descriptorType": "enumstring",
  "values": [
   "ISCSI",
   "SCSI",
   "IDE",
   "PARAVIRTUALIZED"
  ],
  "defaultValue": "PARAVIRTUALIZED"
 },
 "Storage.RemoteDataVolumeType": {
  "descriptorType": "enumstring",
  "values": [
   "ISCSI",
   "SCSI",
   "IDE",
   "PARAVIRTUALIZED"
  ],
  "defaultValue": "PARAVIRTUALIZED"
 },
 "Storage.ConsistentVolumeNaming": {
  "descriptorType": "boolean",
  "defaultValue": "true"
 },
 "Storage.ParaVirtualization.EncryptionInTransit": {
  "descriptorType": "boolean",
  "defaultValue": "true"
 },
 "Storage.ParaVirtualization.AttachmentVersion": {
  "descriptorType": "enuminteger",
  "values": [
   1,
   2
  ],
  "defaultValue": 2
  },
  "Storage.Iscsi.MultipathDeviceSupported": {
  "descriptorType": "boolean",
  "defaultValue": false
  }
}
```

### Schema Elements 🔗 
The following list describes all the available elements in the global image capabilities schema.
  * **Compute.AMD_SecureEncryptedVirtualization** : Provides confidential computing to virtual machine users leveraging AMD Secure Encrypted Virtualization (SEV) on AMD shapes. Data is encrypted in-use and you can verify the confidentiality through a secure attestation process. The default value is false.
  * **Compute.Firmware** : The firmware used to boot the virtual machine instance. The default value is UEFI_64.
  * **Compute.SecureBoot** : Whether the instance can use Secure Boot. The default value is false.
**Important** Custom images do not support Secure Boot.
  * **Compute.LaunchMode** : The configuration mode for launching instances. The default value is PARAVIRTUALIZED.
  * **Network.AttachmentType** : The emulation type for the primary VNIC, which is automatically created and attached when the instance is launched. The default value is PARAVIRTUALIZED.
  * **Storage.BootVolumeType** : Specifies the driver options for the image's boot volume. The default value is PARAVIRTUALIZED.
  * **Storage.LocalDataVolumeType** : Specifies the driver options for the image to access local storage volumes. The default value is PARAVIRTUALIZED.
  * **Storage.RemoteDataVolumeType** : Specifies the driver options for the image to access remote storage volumes. The default value is PARAVIRTUALIZED.
  * **Storage.ConsistentVolumeNaming** : Specifies whether consistent device paths for iSCSI and paravirtualized attached block volumes are enabled for the image. If enabled, the image must support consistent device names. The default value is true.
  * **Storage.ParaVirtualization.EncryptionInTransit** : Specifies whether in-transit encryption is enabled for the image's boot volume attachment. Applies only to paravirtualized boot volume attachments. The default value is true.
  * **Storage.ParaVirtualization.AttachmentVersion** : Specifies the paravirtualization version for boot volume and block volume attachments. Applies only to paravirtualized volume attachments. The default value is 2. 
  * **Storage.Iscsi.MultipathDeviceSupported** : Specifies whether multipath-enabled attachments are supported for the image. Applies only to iSCSI volume attachments. The default value is false. 


## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
If you're new to policies, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for Core Services](https://docs.oracle.com/iaas/Content/Identity/Reference/corepolicyreference.htm). 
For administrators, the following policy provides full access to the image capability schema framework:
```
Allow group _IAM_group_name_ to manage compute-image-capability-schema in tenancy
```

## Using the Console 🔗 
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Custom Images**.
  2. Click the custom image that you're interested in.
  3. Click **Edit image capabilities**.
  4. Edit the image capabilities that you want to configure. For details about each image capability, see [Schema Elements](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringimagecapabilities.htm#configuringimagecapabilities_topic-schema_elements).
  5. Click **Save changes**.


## Using the CLI 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). To work with image capability schemas using the CLI, open a command prompt and run any of the following commands.
To list out the global image capability schema:
Command
CopyTry It
```
oci compute global-image-capability-schema list
```

To list out the global image capability schema versions:
Command
CopyTry It
```
oci compute global-image-capability-schema-version list --global-image-capability-schema-id <global_image_capability_schema_OCID>
```

To retrieve the global image capability schema version:
Command
CopyTry It
```
oci compute global-image-capability-schema-version get --global-image-capability-schema-id <global_image_capability_schema_OCID> --global-image-capability-schema-version-name <version_name>
```

To list the image capability schemas in the specified compartment:
Command
CopyTry It
```
oci compute image-capability-schema list --compartment-id <compartment_OCID>
```

To retrieve the image capability schema for the specified ID:
Command
CopyTry It
```
oci compute image-capability-schema get --image-capability-schema-id <image_capability_schema_OCID>
```

To update the specified image capability schema:
Command
CopyTry It
```
oci -d compute image-capability-schema update --image-capability-schema-id <image_capability_schema_OCID> --schema-data file://<schema_data_file>.json
```

To create an image capability schema:
Command
CopyTry It
```
oci compute image-capability-schema create --schema-data file://<schema_data_file>.json --compartment-id <compartment_OCID> --image-id <image_OCID> --global-image-capability-schema-version-name <version_name>
```

When you create the schema, you specify the image OCID for the custom image you want to apply the image capability schema to.
To delete the specified image capability schema:
Command
CopyTry It
```
oci -d compute image-capability-schema delete --image-capability-schema-id <image_capability_schema_OCID>
```

## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following API operations for working with image capability schemas: 
  * [ListComputeGlobalImageCapabilitySchemas](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGlobalImageCapabilitySchemaSummary/ListComputeGlobalImageCapabilitySchemas)
  * [ListComputeGlobalImageCapabilitySchemaVersions](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGlobalImageCapabilitySchemaVersionSummary/ListComputeGlobalImageCapabilitySchemaVersions)
  * [GetComputeGlobalImageCapabilitySchema](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGlobalImageCapabilitySchema/GetComputeGlobalImageCapabilitySchema)
  * [GetComputeGlobalImageCapabilitySchemaVersion](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeGlobalImageCapabilitySchemaVersion/GetComputeGlobalImageCapabilitySchemaVersion)
  * [ListComputeImageCapabilitySchemas](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeImageCapabilitySchemaSummary/ListComputeImageCapabilitySchemas)
  * [GetComputeImageCapabilitySchema](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeImageCapabilitySchema/GetComputeImageCapabilitySchema)
  * [CreateComputeImageCapabilitySchema](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeImageCapabilitySchema/CreateComputeImageCapabilitySchema)
  * [UpdateComputeImageCapabilitySchema](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeImageCapabilitySchema/UpdateComputeImageCapabilitySchema)
  * [DeleteComputeImageCapabilitySchema](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeImageCapabilitySchema/DeleteComputeImageCapabilitySchema)
  * [ChangeComputeImageCapabilitySchemaCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeImageCapabilitySchema/ChangeComputeImageCapabilitySchemaCompartment)


## Example 🔗 
This example shows how to use the CLI to update the image capability schema for a custom image. For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
  1. Open a command prompt, and run the following command to retrieve the current global schema for the region:
Command
CopyTry It
```
oci compute global-image-capability-schema list
```

The response is similar to the following:
```
{
 "data":
 [
  {
   "compartment-id": null,
   "current-version-name": "<version_name>",
   "defined-tags":
   {},
   "display-name": "OCI.ComputeGlobalImageCapabilitySchema",
   "freeform-tags":
   {},
   "id": "ocid1.computeglobalimgcapschema.oc1.phx.<unique_ID>",
   "time-created": "2020-03-23T19:20:39.656000+00:00"
  }
 ],
 "opc-next-page": "<unique_ID>"
}
```

  2. Using the OCID and version name of the global image capability schema that you retrieved in the previous step, run the following command to get the global image capability schema:
Command
CopyTry It
```
oci compute global-image-capability-schema-version get --global-image-capability-schema-id <global_image_capability_schema_OCID> --global-image-capability-schema-version-name <version_name>
```

The response contains the [global image capability schema](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringimagecapabilities.htm#configuringimagecapabilities_topic-global_image_capability_schema).
  3. Locate the schema element that you want to update, and then do the following:
    1. Copy the schema element that you want to update. This example uses the **Storage.ParaVirtualization.EncryptionInTransit** schema element.
    2. If the schema element contains a `source` field, change the value from GLOBAL to IMAGE. For example:
```
{
 "Storage.ParaVirtualization.EncryptionInTransit":
 {
  "default-value": true,
  "descriptor-type": "boolean",
  "source": "IMAGE"
 }
}
```

    3. Save the updated schema elements as a `.json` file.
  4. To verify whether the image is already using image capability, run the following command:
Command
CopyTry It
```
oci compute image-capability-schema list --image-id <image_OCID>
```

     * If the image is using image capability, the response contains a line similar to the following:
```
"compute-global-image-capability-schema-version-name": "<version_name>"
```

The response also contains the image capability schema OCID.
     * If the image is not using image capability, create an image capability schema for the image by running the following command:
Command
CopyTry It
```
oci compute image-capability-schema create --global-image-capability-schema-version-name <version_name> --image-id <image_OCID> --schema-data file://<schema_data_file>.json --compartment-id <compartment_OCID>
```

<schema_data_file> is the path to the `.json` file that contains the schema elements that you want to update, which you created in the previous step.
The response is similar to the following:
```
{
 "data":
 {
  "compartment-id": "ocid1.compartment.oc1..<unique_ID>",
  "compute-global-image-capability-schema-id": "ocid1.computeglobalimgcapschema.oc1.phx.<unique_ID>",
  "compute-global-image-capability-schema-version-name": "<version_name>",
  "defined-tags":
  {},
  "display-name": "<compute_img_capability_schema_name>",
  "freeform-tags":
  {},
  "id": "ocid1.computeimgcapschema.oc1.phx.<unique_ID>",
  "image-id": "ocid1.image.oc1.phx.<unique_ID>",
  "schema-data":
  {
   "Storage.ParaVirtualization.EncryptionInTransit":
   {
    "default-value": false,
    "descriptor-type": "boolean",
    "source": "IMAGE"
   }
  },
  "time-created": "2021-07-01T22:42:56.140000+00:00"
 },
 "etag": "<etag>"
}
```

  5. To update the image capability schema, run the following command:
Command
CopyTry It
```
oci compute image-capability-schema update --image-capability-schema-id <image_capability_schema_OCID> --schema-data file://<schema_data_file>.json
```

<schema_data_file> is the path to the `.json` file that contains the schema elements that you want to update.


Was this article helpful?
YesNo


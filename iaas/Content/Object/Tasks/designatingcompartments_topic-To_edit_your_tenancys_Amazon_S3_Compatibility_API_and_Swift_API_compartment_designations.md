Updated 2025-01-30
# Editing the Amazon S3 Compatibility API and Swift API Compartment Designations
Change your tenancy's Amazon S3 Compatibility API and Swift API compartment designations in your tenancy.
If your permissions allow, you can change the Amazon S3 Compatibility API and Swift API compartment designations. Use the following guidance when creating designated compartment names:
  * Must be unique across all the compartments in your tenancy.
  * Can be from 1 to 100 characters in length.
  * Must not contain confidential information.
  * Valid are letters (upper or lowercase), numbers, hyphens, and underscore.


See [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/designatingcompartments.htm#permissions) for more information on permissions associated with this feature.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/designatingcompartments_topic-To_edit_your_tenancys_Amazon_S3_Compatibility_API_and_Swift_API_compartment_designations.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/designatingcompartments_topic-To_edit_your_tenancys_Amazon_S3_Compatibility_API_and_Swift_API_compartment_designations.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/designatingcompartments_topic-To_edit_your_tenancys_Amazon_S3_Compatibility_API_and_Swift_API_compartment_designations.htm)


  *     1. In the navigation bar, select the **Profile** menu and then select **Tenancy: <your_tenancy_name>**. Your tenancy's **Details** page appears.
    2. Select **Edit object storage settings**. The **Edit object storage settings** dialog box appears.
    3. Select the compartment that you want for the **Amazon S3 Compatibility API Designated Compartment**
    4. Select the compartment that you want for the **Swift API Designated Compartment**.
    5. Select **Save**.
The new **Object Storage Settings** are displayed in the tenancy's **Details** page.
  * Use the [oci os ns update-metadata](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/ns/update-metadata.html) command and required parameters to change the compartment designation of a Amazon S3 Compatibility API and Swift API in your tenancy.
**Amazon S3 Compatibility API**
Use this command to specify the default Amazon S3 compartment for the specified namespace in your tenancy.
Command
CopyTry It
```
oci os ns update-metadata --namespace namespace --default-s3-compartment-id compartment_ocid
```

`compartment_ocid` specifies a compartment that's not the root compartment of your tenancy.
For example:
```
oci os ns update-metadata --namespace MyNamespace --default-s3-compartment-id ocid.compartment.oc1..exampleuniqueID
{
  "data": {
  "default-s3-compartment-id": "ocid.compartment.oc1..exampleuniqueID",
  "default-swift-compartment-id": null,
	"namespace": null
  }
}				
```

**Swift API**
Use this command to specify the default Swift compartment for the specified namespace in your tenancy.
Command
CopyTry It
```
oci os ns update-metadata --namespace namespace --default-swift-compartment-id compartment_ocid
```

`compartment_ocid` specifies a compartment that's not the root compartment of your tenancy.
For example:
```
oci os ns update-metadata --namespace MyNamespace --default-swift-compartment-id ocid.compartment.oc1..exampleuniqueID
{
  "data": {
  "default-s3-compartment-id": null,
  "default-swift-compartment-id": "ocid.compartment.oc1..exampleuniqueID",
	"namespace": null
  }
}								 
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateNamespaceMetadata](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Namespace/UpdateNamespaceMetadata) operation to change the compartment designation of a Amazon S3 Compatibility API and Swift API in your tenancy.


Was this article helpful?
YesNo


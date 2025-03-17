Updated 2025-01-30
# Object Storage Namespaces
Learn about how to access and use your namespace for running Object Storage tasks.
Object Storage namespace serves as the top-level container for all buckets and objects. At account creation time, each Oracle Cloud Infrastructure tenant is assigned one unique system-generated and immutable Object Storage namespace name. The namespace spans all compartments across all regions. You control bucket names, but those bucket names must be unique within a namespace. While the namespace is region-specific, the namespace name itself is the same in all regions.
**Important**
You can't customize, change, or request a namespace name change.
**Tip**
For some older tenancies, the namespace name string might be based on your tenancy name instead of being machine generated. If your namespace was created based on your tenancy name, your namespace uses all lower-case letters (regardless of the presence of capital letters in your tenancy name). When using the [API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm), [CLI](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm), or [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm), do not use capital letters in your namespace name string.
If your tenancy is assigned a namespace name of `axaxnpcrorw5`, that's your namespace name in all regions. You can create a bucket named **MyBucket** in US West (Phoenix). You can't create another bucket named **MyBucket** in US West (Phoenix). You can, however, create a bucket named **MyBucket** in Germany Central (Frankfurt). Because the namespace name is unique to a tenant, other customers can create buckets named **MyBucket** in their own namespaces. 
Within a namespace, buckets and objects exist in flat hierarchy, but you can simulate a directory structure to help navigate a large set of objects. See [Object Naming Using Prefixes and Hierarchies](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects.htm#nameprefix) for details.
The namespace metadata stores the default compartment assignments for the Amazon S3 Compatibility API and the Swift API. For more information, see [Compartments for the Amazon S3 Compatibility API and Swift API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/designatingcompartments.htm#compartments-s3-swift "Learn about how Object Storage provides API support for both Amazon S3 Compatibility API and Swift API. You can choose the default the compartment where this data is stored.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/understandingnamespaces.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/understandingnamespaces.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/understandingnamespaces.htm)


  * To view your Object Storage namespace string, do the following:
In the navigation bar, select the **Profile** menu and then select **Tenancy: <your_tenancy_name>**. Your namespace string is listed under **Object Storage Settings**.
**Note**
While the Object Storage namespace string is displayed under **Object Storage Settings** , you can't edit the namespace string. The namespace string appears here for information only.
  * Run the following command get your Object Storage namespace:
Command
CopyTry It
```
oci os ns get [OPTIONS]
```

Your Object Storage namespace is returned:
```

{
  "data": "MyNamespace"
}		
```

**Tip** You can use `-ns`, `--namespace`, or `--namespace-name` for CLI commands that require you to specify the Object Storage namespace string. 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [GetNamespace](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Namespace/GetNamespace) operation to get your Object Storage namespace. If you have the `OBJECTSTORAGE_NAMESPACE_READ` permission and supply the compartment or tenancy OCID in the optional `compartmentId` parameter, you can also get the namespace of a different tenancy's Object Storage namespace.


Was this article helpful?
YesNo


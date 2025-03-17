Updated 2025-02-05
# Object Storage Amazon S3 Compatibility API
Learn how to use Oracle Cloud Infrastructure's Amazon S3 Compatibility API, where you can use existing Amazon S3 tools to work with Object Storage.
Using the Amazon S3 Compatibility API, customers can continue to use their existing Amazon S3 tools (for example, SDK clients) and make minimal changes to their applications to work with Object Storage. The Amazon S3 Compatibility API and Object Storage datasets are congruent. If data is written to the Object Storage using the Amazon S3 Compatibility API, the data can be read back using the native Object Storage API and conversely.
**Note**
The Amazon S3 Compatibility API supports only path style URLs. V2 (virtual hosted) styled URLs aren't supported.
For information on how Object Storage supports the Amazon S3 Compatibility API, see [Amazon S3 Compatibility API Support](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/s3compatibleapi_topic-Amazon_S3_Compatibility_API_Support.htm#s3-api-support "Learn about how Object Storage supports Amazon S3 Compatibility API.").
For information about how Object Storage provides API support for both Amazon S3 Compatibility API and Swift API, see [Compartments for the Amazon S3 Compatibility and Swift APIs](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/designatingcompartments.htm#compartments-s3-swift "Learn about how Object Storage provides API support for both Amazon S3 Compatibility API and Swift API. You can choose the default the compartment where this data is stored.")
## Differences Between the Object Storage API and the Amazon S3 Compatibility API 🔗 
The Object Storage Service provided by Oracle Cloud Infrastructure and Amazon S3 use similar concepts and terminology. In both cases, data is stored as objects in buckets. The differences are in the implementation of features and tools for working with objects. 
The following highlights the differences between the two storage technologies:
  * **Compartments**
Amazon S3 doesn't use compartments. By default, buckets created using the Amazon S3 Compatibility API or the Swift API are created in the root compartment of the Oracle Cloud Infrastructure tenancy. Instead, you can [designate a different compartment](https://docs.oracle.com/iaas/Content/Object/Tasks/designatingcompartments.htm) for the Amazon S3 Compatibility API or Swift API to create buckets in.
  * **Global bucket namespace**
Object Storage doesn't use a global bucket namespace. The Object Storage namespace serves as the top-level container for all buckets and objects. At account creation time, each Oracle Cloud Infrastructure tenant is assigned one unique system-generated and immutable Object Storage namespace name. The namespace spans all compartments within a region. You control bucket names, but those bucket names must be unique within a namespace. While the namespace is region-specific, the namespace name itself is the same in all regions. You can have a bucket named **MyBucket** in US West (Phoenix) and a bucket named **MyBucket** in Germany Central (Frankfurt).
  * **Encryption**
The Object Storage service encrypts all data at rest by default. Encryption can't be turned on or off using the API.
  * **Object Level Access Control Lists (ACLs)**
Oracle Cloud Infrastructure doesn't use ACLs for objects. Instead, an administrator needs to set up **groups** , **compartments** , and **policies** that control which users can access which services, which resources, and the type of access. For example, the policies control who can create users and groups, create buckets, download objects, and manage Object Storage-related policies and rules. 


For more information, see [Overview](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorageoverview.htm#overview "Learn how to use Object Storage to store and easily access an unlimited amount of data at low cost.").
## Amazon S3 Compatibility API Prerequisites 🔗 
To enable application access from Amazon S3 to Object Storage, you need to set up access to Oracle Cloud Infrastructure and modify your application as described in the following sections. 
### Setting Up Access to Oracle Cloud Infrastructure
  1. [Sign Up for Oracle Cloud Infrastructure](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingup.htm) and obtain a unique namespace.
  2. Any user of the Amazon S3 Compatibility API with Object Storage needs permission to work with the service. If you're not sure if you have permission, contact your administrator. For basic information about policies, see [How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm). For policies that enable use of Object Storage, see [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm) and the [Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).
  3. Use an existing or create a Customer Secret Key. A Customer Secret Key consists of an Access Key/Secret Key pair. See [Working with Customer Secret Keys](https://docs.oracle.com/iaas/Content/Identity/access/managing-user-credentials.htm#Working2) for details. To use or create the key pair:
     * To use an existing Customer Secret Key, you must already know the Secret Key. For security reasons, you can't retrieve a Secret Key after generation. To show or copy the Access Key: In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see. On the left side of the page, select **Customer Secret Keys**. Hover over the Access Key associated with the **Name** of a particular Customer Secret key, then select **Copy**.
     * To create a Customer Secret Key using the Console, see [To create a Customer Secret key](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm#create-secret-key). 
     * To create a Customer Secret Key using the Command Line Interface (CLI), see [oci iam customer-secret-key create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/customer-secret-key/create.html).


### Modifying Your Application
  1. Configure a new endpoint for the application that includes the [namespace name](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/understandingnamespaces.htm#namespaces "Learn about how to access and use your namespace for running Object Storage tasks.") and the [region identifier](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). Use the following syntax:
```
https://{object-storage-namespace}.compat.objectstorage.{region}.oraclecloud.com
```

  2. Set the target region as one of the Oracle Cloud Infrastructure regions.
**Important** If your application doesn't support setting the region identifier to the correct Oracle Cloud Infrastructure identifier, you must either set the region to `us-east-1` or leave it blank. Using this configuration, you can only use the Amazon S3 Compatibility API in your Oracle Cloud Infrastructure home region. If you can manually set the region, you can use the application against any Oracle Cloud Infrastructure region.
  3. Configure the application to use the [Customer Secret key](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm#create-secret-key). The Customer Secret Key consists of an Access Key and Secret Key. Both of these keys must be supplied to the application.
  4. Include path-based access in your application. Use the following syntax:
```
https://{object-storage-namespace}.compat.objectstorage.{region}.oraclecloud.com/{bucket}
```



**Note**
The following items aren't supported:
  * Virtual host-style access
  * AWS Signature Version 2 (SigV2)


You can now use the Amazon S3 Compatibility API to access Object Storage in Oracle Cloud Infrastructure.
Was this article helpful?
YesNo


Updated 2025-01-22
# Overview of Object Storage
Learn how to use Object Storage to store and easily access an unlimited amount of data at low cost.
The Object Storage service is an internet-scale, high-performance storage platform that offers reliable and cost-efficient data durability. The Object Storage service can store an unlimited amount of unstructured data of any content type, including analytic data and rich content, like images and videos.
With Object Storage, you can safely and securely store or retrieve data directly from the internet or from within the cloud platform. Object Storage offers multiple [management interfaces](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorageoverview.htm#accessways) that let you easily manage storage at scale. The elasticity of the platform lets you start small and scale seamlessly, without experiencing any degradation in performance or service reliability. 
Object Storage is a regional service and is not tied to any specific compute instance. You can access data from anywhere inside or outside the context of the Oracle Cloud Infrastructure, as long you have internet connectivity and can access one of the [Object Storage endpoints](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/). Authorization and resource limits are discussed later in this topic.
Oracle Cloud Infrastructure supports multiple [storage tiers](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm#storage-tiers "Learn how Object Storage uses storage tiers to help you maximize access performance where appropriate and minimize storage costs where possible.") that offer cost and performance flexibility. Standard is the default storage tier for Object Storage buckets.
Object Storage also supports private access from Oracle Cloud Infrastructure resources in a VCN through a _service gateway_. A service gateway allows connectivity to the Object Storage public endpoints from private IP addresses in private subnets. For example, you can back up DB systems to an Object Storage bucket over the Oracle Cloud Infrastructure backbone instead of over the internet. You can optionally use IAM policies to control which VCNs or ranges of IP addresses can access Object Storage. See [Access to Oracle Services: Service Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm) for details.
Object Storage is Always Free eligible. For more information about Always Free resources, including capabilities and limitations, see [Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm).
## Object Storage Resources 🔗 
Use the following Object Storage resources to store and manage data. Authorization and resource limits are discussed later in this topic.
### Buckets 🔗 
Buckets are logical containers for storing objects. Users or systems create buckets as needed [within a region](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm#regionalresources). A bucket is associated with a single **compartment** that has **policies** that determine what actions a user can perform on a bucket and on all the objects in the bucket.
### Objects 🔗 
Any type of data, regardless of content type, is stored as an object. An object is composed of the object itself and metadata about the object. Each object is stored in a bucket.
### Namespace 🔗 
The Object Storage namespace serves as the top-level container for all buckets and objects. At account creation time, each Oracle Cloud Infrastructure tenant is assigned one unique system-generated and immutable Object Storage namespace name. The namespace spans all compartments within a region. You control bucket names, but those bucket names must be unique within a namespace. While the namespace is region-specific, the namespace name itself is the same in all regions. See [Object Storage Namespaces](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/understandingnamespaces.htm#namespaces "Learn about how to access and use your namespace for running Object Storage tasks.") for more details, including information about older tenancy names, illustrative examples of namespaces, and how to obtain your namespace string.
### Compartment 🔗 
A compartment is the primary building block used to organize your cloud resources. When your tenancy is provisioned, a root compartment is created for you. You can then create compartments under your root compartment to organize your resources. You control access by creating policies that specify what actions groups of users can take on the resources in those compartments. An Object Storage bucket can only exist in one compartment.
## Object Storage Characteristics 🔗 
Object Storage provides the following features: 

STRONG CONSISTENCY
    When a read request is made, Object Storage always serves the most recent copy of the data that was written to the system.  

DURABILITY
    Object Storage is a regional service. Data is stored redundantly across multiple storage servers. Object Storage actively monitors data integrity using checksums and automatically detects and repairs corrupt data. Object Storage actively monitors and ensures data redundancy. If a redundancy loss is detected, Object Storage automatically creates more data copies. For more details about Object Storage durability, see the [Object Storage FAQ](https://oracle.com/cloud/storage/object-storage-faq.html). 

custom metadata
    You can define your own extensive metadata as key-value pairs for any purpose. For example, you can create descriptive tags for objects, retrieve those tags, and sort through the data. You can assign custom metadata to objects and buckets using the Oracle Cloud Infrastructure CLI or SDK. See [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm) for details. 

SECURITY
    Object Storage ensures security of the stored data using data encryption. Data encryption is a method used to protect data confidentiality. The data can be accessed using decryption keys created while uploading objects to a bucket. This is used in conjunction with IAM policies that authenticate the users performing the task. See [Object Storage Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/encryption.htm#data-encryption "Learn about how Object Storage service encrypts and decrypts all objects using 256-bit Advanced Encryption Standard \(AES-256\) to encrypt object data on the server.") for details.
## Ways to Access Object Storage 🔗 
You can access Object Storage using any of the following options, based on your preference and its suitability for the task you want to complete:
  * The Console is an easy-to-use, browser-based interface. To access the [Console](https://cloud.oracle.com/), you must use a [supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#supported-browsers). To go to the Console sign-in page, open the navigation menu at the top of this page and select **Infrastructure Console**. You are prompted to enter your cloud tenant, your user name, and your password.
Oracle Cloud Infrastructure supports the following browsers and versions:
Browser | Version | Notes  
---|---|---  
Edge | Latest three major versions only | None  
Firefox | Latest three major versions only | Private Browsing mode isn't supported  
Google Chrome | Latest three major versions only | None  
Safari | Latest three major versions only | None  
  * The command line interface (CLI) provides both quick access and full functionality without the need for programming. For more information, see [Using the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#Using_the_CLI).
  * The REST API provides the most functionality, but requires programming expertise. [API Reference and Endpoints](https://docs.oracle.com/iaas/api/) provides endpoint details and links to the available API reference documents. For general information about using the API, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm). Object Storage is accessible with the following APIs: 
    * [Object Storage Service](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/)
    * [Amazon S3 Compatibility API](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/)
    * Swift API (for use with Oracle RMAN)
  * Oracle Cloud Infrastructure provides SDKs that interact with Object Storage without you having to create a framework. For general information about using the SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm). 


## Using Object Storage 🔗 
If you are ready to use Object Storage, you can find more information in the following topics: 
  * For instructions on how to create a bucket and store an object in the bucket, see [Putting Data into Object Storage](https://docs.oracle.com/iaas/Content/GSG/Tasks/addingbuckets.htm).
  * For task documentation related to buckets, see [Object Storage Buckets](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets.htm#buckets "Learn about Object Storage buckets, in which you can store objects in a compartment."), [Object Storage Replication](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication.htm#replication "Learn how to manage the replication of Object Storage objects across buckets."), and [Object Storage Data Retention Rules](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules.htm#data-retention-rules "Learn how to use retention rules to preserve Object Storage data."). 
  * For task documentation related to objects, see [Object Storage Objects](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects.htm#objects "Learn about how to manageObject Storage objects, which are files or unstructured data that you can upload to an Object Storage bucket to a compartment."), [Object Storage Versioning](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning.htm#object-versioning "Learn how to use object versioning to apply data protection against the accidental or malicious object updating or deleting of Object Storage objects."), and [Copying an Object to Another Bucket in Object Storage](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/copyingobjects.htm#copying_objects "Copy an object to another bucket in Object Storage.").
  * For task documentation related to lifecycle management, see [Object Storage Object Lifecycle Management](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm#object-lifecycle "Learn how to use Object Lifecycle Management to automatically manage the archiving and deletion of objects.").
  * For API reference documentation, see [Object Storage Service API](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/).
  * For SDK and CLI information, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
  * For more information about using Archive Storage, see [Overview of Archive Storage](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm).


## Authentication and Authorization 🔗 
Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API). IAM also manages user credentials for things like API signing keys, auth tokens, and customer secret keys for Amazon S3 Compatibility API. See [User Credentials](https://docs.oracle.com/iaas/Content/Identity/usercred/usercredentials.htm) for details.
An administrator in your organization needs to set up **groups** , **compartments** , and **policies** that control which users can access which services, which resources, and the type of access. For example, the policies control who can create users and groups, create buckets, download objects, and manage Object Storage-related policies and rules. For more information, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see the [Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm). For specific details about writing policies for Object Storage, see [Details for Object Storage, Archive Storage, and Data Transfer](https://docs.oracle.com/iaas/Content/Identity/policyreference/objectstoragepolicyreference.htm).
If you’re a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that your company owns, contact your administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you should be using.
## Security 🔗 
In addition to creating IAM policies, follow these security best practices for Object Storage.
  * Encrypt objects with a custom key, and rotate keys
  * Take regular backups
  * Use Oracle Cloud Guard to detect and respond to security problems
  * Perform a security audit


See [Securing Object Storage](https://docs.oracle.com/iaas/Content/Security/Reference/objectstorage_security.htm).
## Blocking Access to Object Storage Resources from Unauthorized IP Addresses 🔗 
You can enhance the security of your Object Storage policies by restricting access only to requests that originate from an allowed IP address. First, you create a **network source** to specify the allowed IP addresses, then you add a condition to your policy to restrict access to the IP addresses in the network source. An example of a policy that restricts access to only IP addresses in a network source is:
Copy
```
allow group CorporateUsers to manage object-family in tenancy where request.networkSource.name='corpnet'
```

For information on creating network sources and using them in a policy, see [Managing Network Sources](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingnetworksources.htm).
## Object Storage IP Addresses 🔗 
The Oracle Cloud Infrastructure Object Storage service uses the CIDR block IP range 134.70.0.0/16 for all regions.
## Limits on Object Storage Resources 🔗 
See [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm) for a list of applicable limits and instructions for requesting a limit increase.
To set tenancy or compartment-specific storage limits, administrators can use [object storage quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas_topic-Object_Storage_Quotas.htm).
Other limits include:
  * Number of Object Storage namespaces per root compartment: 1
  * Maximum object size: 10 TiB
  * Maximum object part size in a multipart upload: 50 GiB
  * Maximum number of parts in a multipart upload: 10,000
  * Maximum object size allowed by PutObject API: 50 GiB
  * The total size of all the metadata assigned to an object is limited to 4000 bytes.


Was this article helpful?
YesNo


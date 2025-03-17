Updated 2023-08-15
# Object Storage
On Compute Cloud@Customer, the Object Storage service provides reliable and cost-efficient data durability.
The Object Storage service stores unstructured data of any content type, including analytic data and rich content, such as images and videos.
The data is stored as an object in a bucket. Buckets are associated with a compartment within a tenancy. 
An Object Storage namespace serves as the top-level container for all buckets and objects. At account creation time, each tenant is assigned one unique system-generated and immutable Object Storage namespace name. The namespace spans all compartments.
With Object Storage, you can safely and securely store and retrieve data directly from the internet or from within Compute Cloud@Customer.
## Object Storage Resources 🔗 
The Object Storage service uses these components to organize the data stored in object storage:
**Objects**
Any type of data, regardless of content type, is stored as an object. 
An object is composed of the object itself and metadata about the object. Each object is stored in a bucket. The object is processed as a single entity.
**Buckets**
Buckets are logical containers for storing objects. 
Users or systems create buckets as needed. A bucket is associated with a single compartment that has policies that determine what actions a user can perform on a bucket and on all the objects in the bucket. Buckets can't be nested.
You determine the bucket names, but each bucket name must be unique within a namespace.
**Namespace**
An Object Storage namespace serves as the top-level container for all buckets and objects.
When your tenancy is provisioned, the tenancy is assigned one unique system-generated and immutable Object Storage namespace name. The namespace spans all compartments within the tenant. 
Within a namespace, buckets and objects exist in flat hierarchy, but you can simulate a directory structure to help navigate a large set of objects.
**Compartment**
A compartment is the primary building block used to organize your cloud resources. 
When your tenancy is provisioned, a root compartment is created for you. You can then create compartments under your root compartment to organize your resources. You control access by creating policies that specify what actions groups of users can take on the resources in those compartments. An Object Storage bucket can only exist in one compartment.
Was this article helpful?
YesNo


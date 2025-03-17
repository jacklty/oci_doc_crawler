Updated 2023-11-21
# Managing Storage Objects
On Compute Cloud@Customer, you can manage objects in a bucket using the Compute Cloud@Customer Console, CLI, and API.
## Object Naming Prefixes and Hierarchies 🔗 
Within an Object Storage namespace, buckets and objects exist in a flat structure. However, you can simulate a directory structure by adding a prefix string that includes one or more forward slashes (/) to an object name. Doing so lets you list one directory at a time, which is helpful when navigating a large set of objects.
For example:
```
marathon/finish_line.jpg
marathon/participants/p_21.jpg
```

If you add prefixes to object names, you can:
  * Use the CLI or API to perform bulk downloads and bulk deletes of all objects at a specified level of the hierarchy.
  * Use the Console to display a hierarchical view of your objects in virtual folders. In the previous example, `marathon` would be displayed as a folder containing an object named `finish_line.jpg` and `participants` would be a subfolder of `marathon`, containing an object named `p_21.jpg`. You can bulk upload objects to any level of the hierarchy and perform bulk deletes of all the objects in a bucket or folder. 


Bulk operations at a specified level of the hierarchy do not affect objects in any level above.
When naming objects, you can also use prefix strings without a delimiter. No delimiters allow search operations and certain bulk operations in to match on the prefix portion of the object name. For example, in the object names below, the string `gloves_27_` can serve as a prefix for matching purposes when performing bulk operations:
```
gloves_27_dark_green.jpg
gloves_27_light_blue.jpg	
```

When you perform bulk uploads, you can add a prefix string to the names of the files you are uploading.
## Object Names 🔗 
Unlike other resources, objects don't have Cloud Identifiers (OCIDs). Instead, you define an object name when you upload an object.
Use the following guidelines when naming an object:
  * The maximum length for an object and bucket name is 255 characters.
  * Valid characters are letters (upper or lowercase), numbers, and characters other than line feed, carriage return, and NULL.
  * Bucket names and object names are case-sensitive.
  * Use only Unicode characters for which the UTF-8 encoding doesn't exceed 1024 bytes. Clients are responsible for URL-encoding characters.
  * Make the name unique within the bucket. 
  * Object names can include one or more slash (/) characters in the name. See [Object Naming Prefixes and Hierarchies](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/managing-storage-objects.htm#managing-storage-objects__object-storage-prefixes-hierarchies).
  * Avoid entering confidential information in names.


## Optional Response Headers and Metadata 🔗 
When you upload objects, you can provide optional response headers and user-defined metadata. Response headers are HTTP headers sent from Object Storage to Object Storage clients when objects are downloaded. 
User-defined metadata are name-value pairs stored with an object. 
**Important**
No validation is performed on the response headers or metadata you provide. 
You can specify values for the following response headers:
  * **Content-Disposition**
Defines presentation only information for the object. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to let users download objects with custom file names in a browser. For Example:
```
attachment; filename="fname.ext"
```

  * **Cache-Control**
Defines the caching behavior for the object. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify objects that require caching restrictions. For Example:
```
no-cache, no-store
```



**Metadata**
You specify user-defined metadata in the form of name-value pairs. User-defined metadata names are stored and returned to Object Storage clients with the mandatory prefix of `opc-meta-`.
Was this article helpful?
YesNo


Updated 2024-08-06
# Constructing the Preauthenticated Request URL
On Compute Cloud@Customer, after you have a unique `access-uri`, you can construct the access URL that enables users to access preauthenticated objects. The `access-uri` is generated when you create a preauthenticated request. 
Construct the URL using this syntax.
```
https://objectstorage.<ccc_fqdn><access-uri>
```

where:
  * <ccc_fqdn> is the fully qualified domain name of your Compute Cloud@Customer infrastructure.
  * <access-uri> is the access URI that was obtained from one of these procedures:
    * [Creating a Preauthenticated Request for All Objects in a Bucket](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/creating-a-pre-authenticated-request-for-all-objects-in-a-bucket.htm#creating-a-pre-authenticated-request-for-all-objects-in-a-bucket "On Compute Cloud@Customer, you can create preauthenticated requests for all objects in a bucket using the CLI and API.")
  * [Creating a Preauthenticated Request for a Specific Object](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/creating-a-pre-authenticated-request-for-a-specific-object.htm#creating-a-pre-authenticated-request-for-a-specific-object "On Compute Cloud@Customer, you can create a preauthenticated request for a specific object in a bucket using the CLI and API.")


Example:
```
https://objectstorage.myccc01.us.example.com/p/MrxLFkKlFkIlNDhvhcZnrjbUAlsoeah/n/mynamespace/b/my-bucket/o/my-object
```

Was this article helpful?
YesNo


Updated 2025-01-22
# Getting an Object Storage Object's Details
View the details for an object in an Object Storage bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_get_object_details.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_get_object_details.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_get_object_details.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Objects**.
    3. From the **Actions** menu for the object you want, select **View Object Details**.
    4. (Optional) Select **Download** to download the selected object.
Object details include basic information, response headers, metadata, and a preview of object contents, if applicable.
  * Use the [oci os object head](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/head.html) command and required parameters to get the details of an object in a bucket:
Command
CopyTry It
```
oci os object head --bucket-name bucket_name --name object_name [OPTIONS]
```

For example:
```
oci os object head --bucket-name MyBucket --name MyFile.txt
      {
      "accept-ranges": "bytes",
      "access-control-allow-credentials": "true",
      "access-control-allow-methods": "POST,PUT,GET,HEAD,DELETE,OPTIONS",
      "access-control-allow-origin": "*",
      "access-control-expose-headers": "accept-ranges,access-control-allow-credentials,access-control-allow-methods,access-control-allow-origin,content-length,content-md5,content-type,etag,last-modified,opc-client-info,opc-client-request-id,opc-request-id,x-api-id",
      "content-length": "823",
      "content-md5": "9P61OSaYe4fXxaeK8siuDw==",
      "content-type": "application/octet-stream",
      "date": "Fri, 11 Dec 2020 14:22:51 GMT",
      "etag": "cadb9f8a-3292-45e6-a1e8-f075699fb619",
      "last-modified": "Fri, 11 Dec 2020 14:04:19 GMT",
      "opc-client-request-id": "C732DB8E25BC406FBD359740D18C78D4",
      "opc-request-id": "phx-1:EzxtLDJJxPWDLUQ30AEYB8RX__EYrxKK2rEYq23k8EQd749g2YtKOlhx4jjDwVh3",
      "storage-tier": "InfrequentAccess",
      "version-id": "82d3a264-08c4-4732-a9b1-e246ee0e4fa1", 
      "x-api-id": "native"
      }
```

If the object resides in an Archive tier bucket, the output also includes `archival-state`.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [HeadObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/HeadObject) operation to get the details of an object in a bucket.
Object Storage prepends the Object Storage namespace string and bucket name to the object name when constructing a URL for use with the API:
```
/n/object_storage_namespace/b/bucket/o/object_name
```

The object name is everything after the `/o/`, which could include hierarchy levels and prefix strings. 


Was this article helpful?
YesNo


Updated 2024-01-18
# Creating a Preauthenticated Request for All Objects in a Bucket
On Compute Cloud@Customer, you can create preauthenticated requests for all objects in a bucket using the CLI and API.
**Important**
Immediately after creating the request, copy the `access-uri` to durable storage.
The unique `access-uri` provided by the system is the only way to construct a URL that a user can use to access the bucket or object specified as the request target. 
**The** `access-uri` **is displayed only at the time of creation and can't be retrieved later.**
To construct a URL from the unique `access-uri`, see [Constructing the Preauthenticated Request URL](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/constructing-the-pre-authenticated-request-url.htm#constructing-the-pre-authenticated-request-url "On Compute Cloud@Customer, after you have a unique access-uri, you can construct the access URL that enables users to access preauthenticated objects. The access-uri is generated when you create a preauthenticated request.").
**Note**
Listing objects in a bucket is denied by default. If the `--access-type` is `AnyObjectRead` or `AnyObjectReadWrite`, you can specify the optional `--bucket-listing-action ListObjects` parameter when creating the preauthenticated request that lets users list the objects in the bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/creating-a-pre-authenticated-request-for-all-objects-in-a-bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/creating-a-pre-authenticated-request-for-all-objects-in-a-bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/creating-a-pre-authenticated-request-for-all-objects-in-a-bucket.htm)


  * This task isn't available in the Console.
  * Use the [oci os preauth-request create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/preauth-request/create.html) command and required parameters to create a preauthenticated request for all objects in a bucket.
Copy
```
oci os preauth-request create --namespace-name <object_storage_namespace> --bucket-name <bucket_name> --name <preauthenticated_request_name> --access-type <access_value> --time-expires <timestamp> [OPTIONS]
```

For access type, use one of these values:
    * `AnyObjectRead` permits reads on all objects in the bucket.
    * `AnyObjectWrite` permits writes to all objects in the bucket.
    * `AnyObjectReadWrite` permits reads and writes to all objects in the bucket.
`time-expires` is a required argument and must be an [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339.html) timestamp. For example: `2017-09-01T00:09:51.000+02:00`. 
This example creates a preauthenticated request that allows reads and writes to all objects in the bucket:
```
 oci os preauth-request create --namespace-name examplenamespace --bucket-name MyBucket --name PAR-all-objectsRW --access-type AnyObjectWrite --time-expires '2021-07-30 23:55'
{
 "data": {
  "access-type": "AnyObjectWrite",
  "access-uri": "/p/KOCRWzqBilJmIsaBbJNelKLWcOxwRLq/n/examplenamespace/b/MyBucket/o/",
  "id": "783cd56b-9df5-4518-aacf-f523deae5102",
  "name": "PAR-all-objectsRW",
  "object-name": null,
  "time-created": "2021-06-10T20:49:11+00:00",
  "time-expires": "2021-07-30T23:54:59+00:00"
 }
}
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreatePreauthenticatedRequest](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/PreauthenticatedRequest/CreatePreauthenticatedRequest) operation to create a preauthenticated request for all objects in a bucket.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


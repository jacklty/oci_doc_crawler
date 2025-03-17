Updated 2025-01-30
# Pre-Authenticated Request Object URLs in Object Storage
Use a tool such as curl to read and write data using the pre-authenticated requests for an object.
**Important**
  * The unique URL provided by the system when you create a pre-authenticated request is the only way a user can access the request target. Copy the URL to durable storage. The URL is displayed only at the time of creation, isn't stored in Object Storage, and can't be retrieved later.
  * The URL generated when you create a pre-authenticated request for an object with a prefix doesn't contain the prefix by default. The user must manually add the prefix to the URL to access the object.


Using the unique request URL, you can use a tool such as curl to read and write data using the pre-authenticated request. Object Storage now supports [writing large files](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-Working_with_PreAuthenticated_Requests.htm#To_put_a_large_object) using [multipart uploads](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads.htm#multipart-uploads "Learn how to use multipart uploads to move objects larger than 100 MB more efficiently and with greater resiliance.") with pre-authenticated requests.
## Putting an Object 🔗 
Command
CopyTry It
```
$ curl -X PUT --data-binary '@local_filename' unique_PAR_URL
```

For example:
Copy
```
$ curl -X PUT --data-binary '@using-dita-guide.pdf' https://objectstorage.us-phoenix-1.oraclecloud.com/p/j3DoSvgQHbUaw6ADzHkDlnaqMuXWef_lhTxCiS9ngCw/n/MyNamespace/b/MyParBucket/o/using-dita-guide.pdf
```

## Putting an Object with Custom Metadata 🔗 
You can also provide custom metadata for any object using `opc-meta-name:value` headers.
Command
CopyTry It
```
$ curl -X PUT -H "opc-meta-name:value" --data-binary '@local_filename' unique_PAR_URL
```

For example:
Copy
```
$ curl -X PUT -H "opc-meta-version:2020May" PUT --data-binary '@CorporateTerminologyUsageGuide.pdf' https://objectstorage.us-phoenix-1.oraclecloud.com/p/71LzRt_V8LVT7BVLbeQOB5KAx67AxzeKXwJ8mIA5dN0WheYH39a7KiY2UXnUBhaX/n/MyNamespace/b/MyParBucket/o/CorporateTerminologyUsageGuide.pdf
```

## Putting a Large Object 🔗 
Multipart uploads accommodate objects that are too large for a single upload operation. We recommend that you use multipart uploads to upload objects larger than 100 MiB. The maximum size for an uploaded object is 10 TiB. Object parts must be no larger than 50 GiB. Using multipart uploads, you have the flexibility of pausing between the uploads of individual parts, and resuming the upload when your schedule and resources allow.
**Step 1** : To direct Object Storage to create a multipart upload, include the header `opc-multipart: true` in the `PUT` command.
Command
CopyTry It
```
$ curl -X PUT -H "opc-multipart:true" unique_PAR_URL
```

For example:
Copy
```
$ curl -X PUT -H "opc-multipart:true" https://objectstorage.us-phoenix-1.oraclecloud.com/p/j3DoSvgQHbUaw6ADzHkDlnaqMuXWef_lhTxCiS9ngCw/n/MyNamespace/b/MyParBucket/o/OCI_User_Guide.pdf
```

The `PUT` with the `opc-multipart: true` header returns an access URI to use to upload parts and commit the multipart upload, for example: ```
{"namespace":"MyNamespace","bucket":"MyParBucket","object":"OCI_User_Guide.pdf","uploadId":"b5bb4079-9d50-ac59-182e-4d133a962382","timeCreated":"2021-03-05T14:48:53.738Z","storageTier":"Standard","accessUri":"/p/8dFlNPzKOl2s9R6EGCxtdRKr-zSG45X2BA1k63dIm_SMrgg_HMzg9FblpOWEs5Lh/n/MyNamespace/b/MyParBucket/u/OCI_User_Guide.pdf/id/b5bb4079-9d50-ac59-182e-4d133a962382/"}
```

**Step 2** : Use the access URI together with the Object Storage hostname for the target region to upload parts, specifying the part number at the end of the URI. For example, to upload an object in three parts, issue the following `PUT` commands:
Copy
```
$ curl -X PUT --data-binary '@data.1' https://objectstorage.us-phoenix-1.oraclecloud.com/p/8dFlNPzKOl2s9R6EGCxtdRKr-zSG45X2BA1k63dIm_SMrgg_HMzg9FblpOWEs5Lh/n/MyNamespace/b/MyParBucket/u/OCI_User_Guide.pdf/id/b5bb4079-9d50-ac59-182e-4d133a962382/1
$ curl -X PUT --data-binary '@data.2' https://objectstorage.us-phoenix-1.oraclecloud.com/p/8dFlNPzKOl2s9R6EGCxtdRKr-zSG45X2BA1k63dIm_SMrgg_HMzg9FblpOWEs5Lh/n/MyNamespace/b/MyParBucket/u/OCI_User_Guide.pdf/id/b5bb4079-9d50-ac59-182e-4d133a962382/2
$ curl -X PUT --data-binary '@data.3' https://objectstorage.us-phoenix-1.oraclecloud.com/p/8dFlNPzKOl2s9R6EGCxtdRKr-zSG45X2BA1k63dIm_SMrgg_HMzg9FblpOWEs5Lh/n/MyNamespace/b/MyParBucket/u/OCI_User_Guide.pdf/id/b5bb4079-9d50-ac59-182e-4d133a962382/3
```

**Step 3** : To commit the multipart upload, use the `POST` command with the access URI. For example:
Copy
```
$ curl -X POST https://objectstorage.us-phoenix-1.oraclecloud.com/p/8dFlNPzKOl2s9R6EGCxtdRKr-zSG45X2BA1k63dIm_SMrgg_HMzg9FblpOWEs5Lh/n/MyNamespace/b/MyParBucket/u/OCI_User_Guide.pdf/id/b5bb4079-9d50-ac59-182e-4d133a962382/
```

You can delete all parts of an uncommitted or failed multipart upload using the `DELETE` command with the access URI. For example:
Copy
```
$ curl -X DELETE https://objectstorage.us-phoenix-1.oraclecloud.com/p/8dFlNPzKOl2s9R6EGCxtdRKr-zSG45X2BA1k63dIm_SMrgg_HMzg9FblpOWEs5Lh/n/MyNamespace/b/MyParBucket/u/OCI_User_Guide.pdf/id/b5bb4079-9d50-ac59-182e-4d133a962382/
```

You can also provide custom metadata for any object using `opc-meta-` headers. The `"`-H opc-meta-name:value`"` is only needed on the first pre-authenticated request that creates the multipart upload, not on each individual part. See [Putting an Object with Custom Metadata](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-Working_with_PreAuthenticated_Requests.htm#To_put_an_object_with_metadata) for more information.
## Getting an Object 🔗 
Command
CopyTry It
```
$ curl -X GET unique_PAR_URL
```

For example:
Copy
```
$ curl -X GET https://objectstorage.us-phoenix-1.oraclecloud.com/p/MR7rGASetBbu4L1R5ZH91meUZJjVkOGmd4rtnjDhazP9o6s2KzLyFUxILQzSamEp/n/MyNamespace/b/MyParBucket/o/OCI_User_Guide.pdf
'@data.1''@data.2''@data.3'
```

## Getting a List of Objects 🔗 
For pre-authenticated requests that apply to several objects, the request creator can optionally let you list objects.
Command
CopyTry It
```
$ curl -X GET unique_PAR_URL
```

For example:
Copy
```
$ curl -X GET https://objectstorage.us-phoenix-1.oraclecloud.com/p/2WOshPVWv9uqIqy6abokChGEXYdCZ8l75CoO26YkSARiRevWlDWJD_QUvtFPUocn/n/MyNamespace/b/MyParBucket/o/
{"objects":[{"name":"InfoWorld DeepDive - Tips for Git and GitHub Users.pdf"},{"name":"OCI_User_Guide.pdf"},{"name":"OracleCorporateTerminologyUsageGuideRedwood.pdf"},{"name":"VPN.png"},{"name":"eventslogreference.htm"},{"name":"functionslogreference.htm"},{"name":"glob.txt"},{"name":"loadbalancerreference.htm"},{"name":"objectstoragelogreference.htm"},{"name":"servicechanges.html"},{"name":"servicediscovery.dita"},{"name":"serviceessentials.html"},{"name":"servicelogreference.htm"},{"name":"services.html"},{"name":"udx-1494-lifecycle-rule-glob.pdf"}]}
```

By default, the object list returns only the names of the objects. Optionally, you can use the `fields` query parameter to also include the `size` (object size in bytes), `etag`, `md5`, `timeCreated` (object creation date and time), `timeModified` (object modification date and time), `storageTier`, and `archivalState` fields. Specify the value of this parameter as a comma-separated, case-insensitive list of those field names that you want to include in the object list. For example:
Copy
```
$ curl -X GET https://objectstorage.us-phoenix-1.oraclecloud.com/p/2WOshPVWv9uqIqy6abokChGEXYdCZ8l75CoO26YkSARiRevWlDWJD_QUvtFPUocn/n/MyNamespace/b/MyParBucket/o/?fields="name,etag,timeCreated,md5,timeModified,storageTier,archivalState"
{"objects":[{"name":"InfoWorld DeepDive - Tips for Git and GitHub Users.pdf","timeCreated":"2021-04-01T14:27:13.039Z","timeModified":"2021-04-01T14:27:27.552Z","etag":"e5032a35-07d7-476f-88aa-a95c5d07f0d9","storageTier":"Standard","md5":"3OPjerv2zKJdf9fzFeP9BQ=="},{"name":"OCI_User_Guide.pdf","timeCreated":"2021-04-01T14:27:20.359Z","timeModified":"2021-04-02T23:18:01.299Z","etag":"0dd28308-b821-47e7-9685-111eedef1c5c","storageTier":"Standard","md5":"/2+fTemSy7CsR00OnFK87Q=="},{"name":"OracleCorporateTerminologyUsageGuideRedwood.pdf","timeCreated":"2021-04-01T14:27:12.228Z","timeModified":"2021-04-01T14:27:21.302Z","etag":"1948d01b-9611-4a79-a9dd-f5b24888c0bc","storageTier":"Standard","md5":"JIdR+kCzQNkl0riH08Ktpw=="},{"name":"VPN.png","timeCreated":"2021-04-01T14:27:11.943Z","timeModified":"2021-04-01T14:27:12.047Z","etag":"b4f20050-e268-42e5-8980-29f6a972b6bf","storageTier":"Standard","md5":"aWFjq5fe+hsDT/x5cWhasA=="},{"name":"eventslogreference.htm","timeCreated":"2021-04-01T14:27:10.725Z","timeModified":"2021-04-01T14:27:10.746Z","etag":"84362592-0a18-438d-8773-7dcc702103aa","storageTier":"Standard","md5":"As+3syaEbvMhPm8fM+DSAw=="},{"name":"functionslogreference.htm","timeCreated":"2021-04-01T14:27:10.865Z","timeModified":"2021-04-01T14:27:10.900Z","etag":"4d494efa-5d48-491a-84ba-254be2aa8549","storageTier":"Standard","md5":"lt28WcIiqKklMS5p2LbECQ=="},{"name":"glob.txt","timeCreated":"2021-04-05T16:12:31.925Z","timeModified":"2021-04-05T16:12:31.952Z","etag":"c330ce8c-4c61-4342-9ac5-4bc0fd846944","storageTier":"Standard","md5":"BeMbbI+uOOGzmFA/NXwwxQ=="},{"name":"loadbalancerreference.htm","timeCreated":"2021-04-01T14:27:11.480Z","timeModified":"2021-04-01T14:27:11.574Z","etag":"522a3b1d-f736-4e30-9b5d-feed3867912d","storageTier":"Standard","md5":"u2GP2ngLVEq9xUAykRg2ug=="},{"name":"objectstoragelogreference.htm","timeCreated":"2021-04-01T14:27:11.416Z","timeModified":"2021-04-01T14:27:11.479Z","etag":"fbf7a035-7b80-4c91-a932-53bf0917bef9","storageTier":"Standard","md5":"skstBGw3YcHBomI6X/YwEA=="},{"name":"servicechanges.html","timeCreated":"2021-04-01T14:27:11.702Z","timeModified":"2021-04-01T14:27:11.716Z","etag":"016df222-128d-4e7f-a191-b5c0a5dbc7e0","storageTier":"Standard","md5":"sVzYaODHww3Qw1jwbtj7SA=="},{"name":"servicediscovery.dita","timeCreated":"2021-04-02T17:16:04.134Z","timeModified":"2021-04-02T17:16:04.149Z","etag":"7997226d-e2ba-460a-be75-97436dcb30e8","storageTier":"Standard","md5":"I/ZjF5rcoaJXH6abpbDPag=="},{"name":"serviceessentials.html","timeCreated":"2021-04-01T14:27:11.700Z","timeModified":"2021-04-01T14:27:11.737Z","etag":"687d0914-19c7-4ff6-8ceb-90ab0bbd1fc1","storageTier":"Standard","md5":"HSf0uMVHxFCuVr/I5insxQ=="},{"name":"servicelogreference.htm","timeCreated":"2021-04-01T14:27:11.767Z","timeModified":"2021-04-01T14:27:11.775Z","etag":"240f2d71-da38-461c-a821-506b85b7e6e7","storageTier":"Standard","md5":"jxyWxK9z8OW0zsozadNRkQ=="},{"name":"services.html","timeCreated":"2021-04-01T14:27:11.780Z","timeModified":"2021-04-01T14:27:11.913Z","etag":"6e570928-a5b2-4e49-8e54-22186825350a","storageTier":"Standard","md5":"fDuH2Y7LDAafjlyUCQZohQ=="},{"name":"udx-1494-lifecycle-rule-glob.pdf","timeCreated":"2021-04-01T14:27:12.044Z","timeModified":"2021-04-01T14:27:12.686Z","etag":"a92174a2-cad3-4239-b4c9-48f2abd4dd8c","storageTier":"Standard","md5":"4ltcJZgQ80sNz8RHu7TJlQ=="}]}
```

In addition to `fields`, pre-authenticated requests support all other [ListObjects](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/ListObjects) query parameters and [list pagination](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#nine).
## Getting Metadata from an Object 🔗 
Command
CopyTry It
```
$ curl --head unique_PAR_URL
```

For example:
Copy
```
$ curl --head https://objectstorage.us-phoenix-1.oraclecloud.com/p/MR7rGASetBbu4L1R5ZH91meUZJjVkOGmd4rtnjDhazP9o6s2KzLyFUxILQzSamEp/n/MyNamespace/b/MyParBucket/o/OCI_User_Guide.pdf
HTTP/1.1 200 OK
accept-ranges: bytes
Content-Length: 27
opc-multipart-md5: AgQlttlYM7ya/tH0Fosu9A==-3
last-modified: Fri, 05 Mar 2021 15:15:44 GMT
etag: 9b9093ab-bdc6-49af-b261-b2d1d111d952
version-id: d3346446-e1f3-46e3-97e5-ee3c8e57ee30
storage-tier: Standard
Content-Type: application/x-www-form-urlencoded
date: Thu, 18 Mar 2021 22:11:11 GMT
opc-request-id: phx-1:odm8FLV-LC7yR7sskUL955sjFjOqaKrQ-cO3JbGhSbcwYcovlRa2QtABQPfeW_Q_
x-api-id: native
access-control-allow-origin: *
access-control-allow-methods: POST,PUT,GET,HEAD,DELETE,OPTIONS
access-control-allow-credentials: true
access-control-expose-headers: accept-ranges,access-control-allow-credentials,access-control-allow-methods,access-control-allow-origin,content-length,content-type,date,etag,last-modified,opc-client-info,opc-multipart-md5,opc-request-id,storage-tier,version-id,x-api-id
```

## Getting an Object with Custom Response Headers 🔗 
You can override the response headers in the PAR GET requests by using the following query parameters:
  * `httpResponseContentDisposition`
  * `httpResponseCacheControl`
  * `httpResponseContentType`
  * `httpResponseContentLanguage`
  * `httpResponseContentEncoding`
  * `httpResponseExpires`


For example:
Copy
```
Default URL (shows inline) - https://objectstorage.us-phoenix-1.oraclecloud.com/p/bDh0EOiY_C0K0NYn8YIhC_fgVOj96BM8S6YApdmlr7pwv4Xuie-6IiLbF1eQdcWi/n/bmcostests/b/bucket-20220302-1236/o/example.txt
```

```
Download and save with default filename - https://objectstorage.us-phoenix-1.oraclecloud.com/p/bDh0EOiY_C0K0NYn8YIhC_fgVOj96BM8S6YApdmlr7pwv4Xuie-6IiLbF1eQdcWi/n/bmcostests/b/bucket-20220302-1236/o/example.txt?httpResponseContentDisposition=attachment
```
```
Download and save with custom filename - https://objectstorage.us-phoenix-1.oraclecloud.com/p/bDh0EOiY_C0K0NYn8YIhC_fgVOj96BM8S6YApdmlr7pwv4Xuie-6IiLbF1eQdcWi/n/bmcostests/b/bucket-20220302-1236/o/example.txt?httpResponseContentDisposition=attachment%3B%20filename%3Ddownload.txt
```

Was this article helpful?
YesNo


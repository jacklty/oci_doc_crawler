Updated 2023-08-15
# Listing Preauthenticated Requests
On Compute Cloud@Customer, you can list preauthenticated requests using the unique request URL.
For information about the unique request URL, see [Constructing the Preauthenticated Request URL](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/constructing-the-pre-authenticated-request-url.htm#constructing-the-pre-authenticated-request-url "On Compute Cloud@Customer, after you have a unique access-uri, you can construct the access URL that enables users to access preauthenticated objects. The access-uri is generated when you create a preauthenticated request.").
**Using curl**
  * Syntax:
```
$ curl -X GET <unique-PAR-URL>
```

Example:
```
$ curl -X GET  \
https://objectstorage.us-example-1.example.com/p/CoO26YkSARiRevWlDWJD_QUvtFPUocn/n/examplenamespace/b/MyParBucket/o/
{"objects":[{"name":"InfoWorld DeepDive - Tips for Git and GitHub Users.pdf"},{"name":"OCI_User_Guide.pdf"},
{"name":"OracleCorporateTerminologyUsageGuideRedwood.pdf"},{"name":"VPN.png"},{"name":"eventslogreference.htm"},
{"name":"functionslogreference.htm"},{"name":"glob.txt"},{"name":"loadbalancerreference.htm"},{"name":"objectstoragelogreference.htm"},
{"name":"servicechanges.html"},{"name":"servicediscovery.dita"},{"name":"serviceessentials.html"},{"name":"servicelogreference.htm"},
{"name":"services.html"}]}
```



Was this article helpful?
YesNo


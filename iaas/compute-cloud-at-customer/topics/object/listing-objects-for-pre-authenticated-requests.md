Updated 2023-08-15
# Listing Objects for Preauthenticated Requests
On Compute Cloud@Customer, using the unique request URL, you can use a tool like curl to list, read, and write data using the preauthenticated request.
## Using curl 🔗 
  * Syntax (entered on a single line):
```
$ curl -X GET **_<unique-PAR-URL>_**
```

Example:
```
$ curl -X GET  \
https://objectstorage.us-example-1.example.com/p/CoO26YkSARiRevWlDWJD_QUvtFPUocn/n/examplenamespace/b/MyParBucket/o/
{"objects":[{"name":"InfoWorld DeepDive - Tips for Git and GitHub Users.pdf"},{"name":"developer-reference.pdf"},
{"name":"OracleCorporateTerminologyUsageGuideRedwood.pdf"},{"name":"VPN.png"},{"name":"eventslogreference.htm"},
{"name":"functionslogreference.htm"},{"name":"glob.txt"},{"name":"loadbalancerreference.htm"},{"name":"objectstoragelogreference.htm"},
{"name":"servicechanges.html"},{"name":"servicediscovery.dita"},{"name":"serviceessentials.html"},{"name":"servicelogreference.htm"},
{"name":"services.html"}]}
```



Was this article helpful?
YesNo


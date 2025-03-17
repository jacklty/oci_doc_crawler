Updated 2023-08-15
# Downloading an Object Using a Preauthenticated Request
On Compute Cloud@Customer, using the unique request URL, you can use a tool like curl to read and write data using the preauthenticated request.
## Using curl 🔗 
  * Syntax (entered on a single line):
```
$ curl -X GET **_<unique-PAR-URL>_**
```

Example:
```
$ curl -X GET https://objectstorage.us.example.com/p/tnjDhazP9o6s2KzLyFUxILQzSamEp/n/examplenamespace/b/MyParBucket/o/developer_reference.pdf 
'@data.1''@data.2''@data.3'
```



Was this article helpful?
YesNo


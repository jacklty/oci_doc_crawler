Updated 2023-08-15
# Uploading an Object Using a Preauthenticated Request
On Compute Cloud@Customer, using the unique request URL, you can use a tool like curl to read and write data using the preauthenticated request. 
## Using curl 🔗 
  * Syntax (entered on a single line):
```
$ curl -X PUT --data-binary '@**_<local-filename>_**' **_<unique-PAR-URL>_**
```

Example:
```
$ curl -X PUT  \
--data-binary '@using-dita-guide.pdf'  \
https://objectstorage.us-example-1.example.com/p/lnaqMuXWef_lhTxCiS9ngCw/n/examplenamespace/b/MyParBucket/o/using-dita-guide.pdf
```



Was this article helpful?
YesNo


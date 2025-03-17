Updated 2024-01-18
# Performing a Bulk Object Upload
On Compute Cloud@Customer, you can perform bulk object uploads to a bucket using the CLI.
Bulk operations at a specific level of the hierarchy do not affect objects in any level above.
## Using the CLI 🔗 
Use the [oci os object bulk-upload](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/bulk-upload.html) command and required parameters to bulk upload objects.
Syntax:
Copy
```
oci os object bulk-upload --namespace-name <object_storage_namespace> --bucket-name <bucket_name> --src-dir <source_directory_location> [OPTIONS]
```

Example:
```
oci os object bulk-upload
--namespace-name examplenamespace \ 
--bucket-name MyBucket  \ 
--src-dir /home/log-dir/ 
Uploaded Jan-logs [####################################] 100%
Uploaded Feb-logs [####################################] 100%
Uploaded Mar-logs [####################################] 100%
Uploaded Apr-logs [####################################] 100%
{
 "skipped-objects": [],
 "upload-failures": {},
 "uploaded-objects": {
  "Jan-logs": {
   "etag": "33ed1aff724eac56f00616552fc61f3e",
   "last-modified": "2021-06-01T20:42:50.000Z",
   "opc-content-md5": "Ucf+fZbCK/RN5gGsEl7G5w=="
  },
  "Feb-logs": {
   "etag": "e1875449257cc6ac6ab93cc9c7921c87",
   "last-modified": "2021-06-01T20:42:50.000Z",
   "opc-content-md5": "1B2M2Y8AsgTpgAmY7PhCfg=="
  },
  "Mar-logs": {
   "etag": "c784ac5216d889f55138ecfb428eee3c",
   "last-modified": "2021-06-01T20:42:51.000Z",
   "opc-content-md5": "1B2M2Y8AsgTpgAmY7PhCfg=="
  },
  "Apr-logs": {
   "etag": "3b4571c73bdb9e44bec0512a5e48fba7",
   "last-modified": "2021-06-01T20:42:51.000Z",
   "opc-content-md5": "1B2M2Y8AsgTpgAmY7PhCfg=="
  }
 }
}
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
Was this article helpful?
YesNo


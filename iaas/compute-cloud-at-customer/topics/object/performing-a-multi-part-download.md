Updated 2024-01-18
# Performing a Multipart Download
On Compute Cloud@Customer, you can download an object in multiple parts using CLI and API operations.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/performing-a-multi-part-download.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/performing-a-multi-part-download.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/performing-a-multi-part-download.htm)


  * This task isn't available in the Console. 
  * Use the [oci os object get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/get.html) command and required parameters to operation to download an object in multiple parts.
Syntax (entered on a single line):
Copy
```
oci os object get --namespace-name <object_storage_namespace> --bucket-name <bucket_name> --name <object_name> --file <file_location> --range bytes=<byte_range> [OPTIONS]
```

The byte-range for the download. Multipart object downloading is available using the byte-range request standard defined in [RFC 7233, section 2.1](https://www.rfc-editor.org/rfc/rfc7233)
Example:
```
oci os object get  \
--namespace-name examplenamespace \
--bucket-name MyBucket  \
--name MyObject.mp4  \
--file c:\workspace\Downloads\MyObject.mp4  \
--range bytes=0-50
cusobjstorenamespace --range bytes=0-50
Downloading object [#-----------------------------------] 3%
# ls -l
total 12
-rw-r--r-- 1 root root 1363 Jun 1 17:56 abc.mp41
-rw-r--r-- 1 root root 51 Jun 1 21:50 def.mp4
-rw-r--r-- 1 root root 1363 Jun 1 21:40 ghi.mp4
-rw-r--r-- 1 root root 0 Jun 1 20:42 jkl.mp4
-rw-r--r-- 1 root root 0 Jun 1 20:42 mno.mp4
-rw-r--r-- 1 root root 0 Jun 1 20:42 pqr.mp4
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the[GetObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/GetObject) operation to download an object in multiple parts.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


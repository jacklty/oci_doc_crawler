Updated 2024-09-16
# Bulk Object Management for Roving Edge Infrastructure
Describes how to upload, download, and delete objects in bulk on your Roving Edge Infrastructure devices.
## Bulk Uploading Objects Using the CLI 🔗 
Use the [oci os object bulk-upload](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/bulk-upload.html) command and required parameters to upload objects in bulk on a Roving Edge Infrastructure device:
```
oci os object bulk-upload --bucket-name bucket_name --src-dir src_dir [OPTIONS]
```

where `src_dir` is the source directory on your devices.
For example:
```
oci os object bulk-upload --bucket-name my_bucket --src-dir test_directory
Uploaded file1.txt [####################################] 100%
Uploaded file2.txt [####################################] 100%
{
 "skipped-objects": [],
 "upload-failures": {},
 "uploaded-objects": {
  "file1.txt": {
   "etag": "6e3fc5a09cf1f4912946fee5f8251a99",
   "opc-content-md5": "bj/FoJzx9JEpRv7l+CUamQ=="
  },
  "file2.txt": {
   "etag": "9f69ca10c97395570d0f9734e7f95e87",
   "opc-content-md5": "n2nKEMlzlVcND5c05/lehw=="
  }
 }
}
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
## Bulk Downloading Objects using the CLI 🔗 
Use the [oci os object bulk-download](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/bulk-download.html) command and required parameters to download objects in bulk on a Roving Edge Infrastructure device:
Copy
```
oci os object bulk-download --bucket-name bucket-name --download-dir download-dir [OPTIONS]
```

For example:
```
oci os object bulk-download --bucket-name my_bucket --download-dir test_directory_download
Downloaded file1.txt [####################################] 100%
Downloaded file2.txt [####################################] 100%
{
 "download-failures": {},
 "downloaded-objects": [
  "file1.txt",
  "file2.txt"
 ],
 "skipped-objects": []
}
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
## Bulk Deleting Objects using the CLI 🔗 
Enter the [oci os object bulk-delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/bulk-delete.html) command and required parameters to delete objects in bulk on a Roving Edge Infrastructure device:
```
oci os object bulk-delete --bucket-name bucket_name [OPTIONS]
```

For example:
```
oci os object bulk-delete --bucket-name my_bucket
WARNING: This command will delete at least 2 objects. Are you sure you wish to continue? [y/N]: y
Deleted object file1.txt [####################################] 100%
Deleted object file2.txt [####################################] 100%
{
 "delete-failures": {},
 "deleted-objects": [
  "file1.txt",
  "file2.txt"
 ]
}
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
## Bulk Deleting Object Versions using the CLI 🔗 
Enter the [oci os object bulk-delete-versions](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/bulk-delete-versions.html) command and required parameters to delete all object versions in bulk on a Roving Edge Infrastructure device:
```
oci os object bulk-delete-versions --bucket-name bucket_name [OPTIONS]
```

For example:
```
oci os object bulk-delete-versions --bucket-name my_bucket "
{
 "delete-failures": {},
 "deleted-objects": [
  "20MB.bin,SgXGrKMkxsNFm8.nhr4fFGU3qz4M7VY",
  "20MB.bin,pajzkAEvTJJQWE78Bog3nSnOtRdjBLS"
 ]
}
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
Was this article helpful?
YesNo


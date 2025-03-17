Updated 2025-03-13
# Assigning a Custom URL to a Citation
When an agent uses the RAG for its responses, you can get citations. By default, the citations point to Object Storage where the files are stored. To reference a URL instead of the file that's being referenced, you can add a custom URL to the `metadata` object for that file. 
This topic shows how to add or update the `metadata` object through OCI CLI.
  1. Start OCI CLI in an environment or in Cloud Shell. We recommend that you try it in Cloud Shell first to become familiar with the commands.
See [Get Started with the Command Line Interface](https://docs.oracle.com/iaas/Content/GSG/Tasks/gettingstartedwiththeCLI.htm).
  2. Get the object name for the file that you want to add a custom URL to:
Command
CopyTry It
```
oci os object list --bucket-name <the-bucket-name> 
--file <the-file-name>
```

Example output:```
"data": [
  {
   "archival-state": null,
   "etag": "xxx",
   "md5": "xxx==",
   "name": "<the-object-name>",
   "size": 1117630,
   "storage-tier": "Standard",
   "time-created": "2025-03-12T22:21:26.991000+00:00",
   "time-modified": "2025-03-12T22:38:10.217000+00:00"
  },
Other objects are listed similarly after this comma.
```

You can also find the object name in the Console. In the bucket details page, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the object, select **View Object Details** and copy the name. 
**Note** If a file is in a folder, then the file name and its object name differ. For example, for a file named `file1.pdf`, its object name could be `folder1/file1.pdf`. Otherwise, the file name and its object name are the same.
  3. Download the file into the current working directory.
To add or update a file's `metadata` object, you replace the file with the same file that has a new `metadata` object. That's why you're copying the file into the current working directory first.
Command
CopyTry It
```
oci os object get 
--bucket-name <the-bucket-name> 
--file <the-file-name>
--name <the-object-name>
```

  4. Find the `metadata` object values for the current file.
Command
CopyTry It
```
oci os object head 
--bucket-name <the-bucket-name> 
--name <the-object-name>
```

Example output:```
{
 some data
 "opc-client-request-id": "xxx",
 "opc-meta-key1": "value1",
 "opc-meta-key2": "value2",
 "opc-request-id": "xxx",
 ...
}

```

This example shows that the `metadata` object value is `'{"key1":"value1","key2":"value2"}'`. The `metadata` name is saved with a prefix of `opc-meta-`, but you don't have to add this prefix when you add the `metadata` name in the next steps. This prefix is added automatically to each `metadata` name.
  5. Replace the file that's in Object Storage with the same file that's in the current working directory, and add a new `metadata` object.
To keep the current metadata and add the custom URL name and values, '`{"customized_url_source":"<the-custom-url>"` to the `metadata` object:
Command
CopyTry It
```
oci os object put 
--bucket-name <the-bucket-name> 
--file <the-file-name> 
--name <the-object-name>
--force --metadata 
'{"customized_url_source":"<the-custom-url>",
"<existing-metadata-name-1>":"<existing-metadata-value-1>"
"<existing-metadata-name-2>":"<existing-metadata-value-2>"}'
```

For example, to keep the `metadata` names and values displayed in the step 4 example:
Command
CopyTry It
```
oci os object put 
--bucket-name <the-bucket-name> 
--file <the-file-name> 
--name <the-object-name>
--force --metadata 
'{"customized_url_source":"<the-custom-url>",
"key1":"value1",
"key2":"value2"}'
```

To replace the existing `metadata` object **to only include the custom URL** run the following command
Command
CopyTry It
```
oci os object put 
--bucket-name <the-bucket-name> 
--file <the-file-name> 
--name <the-object-name>
--force --metadata '{"customized_url_source":"<the-custom-url>"}'
```

  6. Ensure that the `metadata` object for the custom URL is replaced.
Command
CopyTry It
```
oci os object head 
--bucket-name <the-bucket-name> 
--name <the-object-name>
```

Example output:```
{
 some data
 "opc-meta-customized_url_source": "some-new-link",
 ...
}

```



**Important**
  * The `metadata` object that overrides the default citation must have the name, `customized_url_source`.
  * You can have one `metadata` object with the name, `customized_url_source`
  * Each `customized_url_source` can have only one URL.
  * The commands in step 5 works for both adding and updating the `metadata` object, because they replace the current `metadata` object's value. 
  * Ensure that you pass the values for the `--metadata` object with the format shown in the commands in step 5.



Links
    
  * [OCI CLI format for metadata objects](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#ManagingCLIInputandOutput)
  * [OCI CLI put reference](https://docs.oracle.com/iaas/tools/oci-cli/3.52.1/oci_cli_docs/cmdref/os/object/put.html)


Was this article helpful?
YesNo


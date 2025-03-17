Updated 2025-01-30
# Object Storage Data Encryption
Learn about how Object Storage service encrypts and decrypts all objects using 256-bit Advanced Encryption Standard (AES-256) to encrypt object data on the server.
Each object is encrypted with its own data encryption key. Data encryption keys are always encrypted with a master encryption key that's assigned to the bucket. Encryption is enabled by default and cannot be turned off. By default, Oracle manages the master encryption key. 
In addition to this default encryption, you can use these strategies to encrypt data:
  * Use client-side encryption to encrypt objects with their encryption keys before storing them in Object Storage buckets. An available option is to use the Amazon S3 Compatibility API, along with client-side object encryption support available in AWS SDK for Java. See [Amazon S3 Compatibility API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/s3compatibleapi.htm#amazon-s3-compabality "Learn how to use Oracle Cloud Infrastructure's Amazon S3 Compatibility API, where you can use existing Amazon S3 tools to work with Object Storage.") for more details about on this SDK. 
  * Use server-side encryption with your own keys. For more information, see [Using Your Own Keys for Server-Side Encryption](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/encryption.htm#Using_Your_Own_Keys_for_ServerSide_Encryption).
  * Assign an Oracle Cloud Infrastructure Vault master encryption key that you control and rotate on your own schedule. For more information, see [Using Your Own Keys in Vault for Server-Side Encryption](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/encryption.htm#UsingYourKMSKeys).


## Using Your Own Keys for Server-Side Encryption 🔗 
This topic provides the details for implementing and using server-side encryption with customer-provided keys (SSE-C).
### About SSE-C 🔗 
Using optional API headers, you can provide your own 256-bit AES encryption key that is used to encrypt and decrypt objects uploaded to and downloaded from Object Storage:
  * When you upload an object, you supply the encryption key. Object Storage encrypts the object using that key and immediately deletes the key. 
  * When you want to download an object, you supply the same key that was used to encrypt the object and Object Storage decrypts and returns the object to you.


You manage the encryption keys and Object Storage manages the encryption and decryption.
**Important** Object Storage does not store your encryption keys. You are responsible for tracking the key that is associated with each object and rotating the key as necessary. If you lose your encryption key, you cannot retrieve your object.
### Scope and Constraints 🔗 
Understand the following scope and constraints regarding SSE-C:
  * An SSE-C key cannot be associated with a bucket and can only be used to encrypt individual objects.
  * You can encrypt objects using your own encryption key using pre-authenticated requests. To retrieve an SSE-C encrypted object using a pre-authenticated request, you need to specify your encryption key. 
  * To delete or rename an SSE-C encrypted object, you do not need to specify your encryption key.
  * You can only specify either a kmsKeyId or an sseCustomerKey in the [ReencryptObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/ReencryptObject) request payload, not both. If the request payload is empty, the object is encrypted using the encryption key assigned to the bucket. The bucket encryption mechanism can either be a master encryption key managed by Oracle or the Vault service.
  * You can only use the Object Storage APIs and the CLI to provide SSE-C keys. You can't use the Console to upload or retrieve objects using a customer-provided key.
  * The [Amazon S3 Compatibility API](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/) also supports SSE-C.


### Using the REST API for SSE-C 🔗 
If you want to use your own keys for server-side encryption, specify the following three request headers with the encryption key information:
Headers | Description | APIs Supported  
---|---|---  
`opc-sse-customer-algorithm` | Specifies "AES256" as the encryption algorithm. | [CopyObject ](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/CopyObject) [GetObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/GetObject) [HeadObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/HeadObject) [PutObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/PutObject) [CreateMultipartUpload](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/MultipartUpload/CreateMultipartUpload) [UploadPart](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/MultipartUpload/UploadPart)  
`opc-sse-customer-key` | Specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the data.  
`opc-sse-customer-key-sha256` | Specifies the base64-encoded SHA256 hash of the encryption key.   
**For[CopyObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/CopyObject)**:
If the source object is encrypted with an SSE-C key, you must also specify the following three headers so that Object Storage can decrypt the object.
Headers | Description | APIs Supported  
---|---|---  
`opc-source-sse-customer-algorithm` | Specifies "AES256" as the encryption algorithm to use to decrypt the source object. | [CopyObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/CopyObject)  
`opc-source-sse-customer-key` | Specifies the base64-encoded 256-bit encryption key to use to decrypt the source object.  
`opc-source-sse-customer-key-sha256` | Specifies the base64-encoded SHA256 hash of the encryption key used to decrypt the source object.  
### Using the CLI for SSE-C 🔗 
You can also use your own encryption keys to encrypt objects using the CLI. 
You can supply your own encryption key using the optional parameter `--encryption-key-file` `filename` for the following commands:
  * `oci os object put`
  * `oci os object get`
  * `oci os object head`
  * `oci os object resume-put`
  * `oci os object bulk-upload`
  * `oci os object bulk-download`
  * `oci os object copy`
  * `oci os object reencrypt`


`filename` points to a file containing the base64-encoded string of the AES-256 encryption key. No other parameters are required. Object Storage decodes the key to compute the SHA256 hash of the encryption key.
If the source object is encrypted with an SSE-C key, you must also specify the optional parameter `--source-encryption-key-file` filename for the following commands:
  * `oci os object copy`
  * `oci os object reencrypt`


`filename` points to a file containing the base64-encoded string of the AES-256 source encryption key. No other parameters are required. Object Storage decodes the key to compute the SHA256 hash of the source encryption key.
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
## Using Your Own Keys in Vault for Server-Side Encryption 🔗 
This topic provides the details for implementing server-side encryption using your own keys in Vault. 
The Oracle Cloud Infrastructure Object Storage service encrypts your data and metadata (customer-provided key value pairs) using randomly generated Data Encryption Keys (DEKs). Object Storage allows you to specify your own Master Encryption Key (MEK) managed by the Vault service for buckets (See [Using the Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_assign_a_Vault_master_encryption_key_to_a_bucket.htm#console)) and individual objects. You can specify the MEK to be used for a given object without having to maintain and manage your own keys. 
You must have the required permissions in the IAM policies to be able to specify your own MEK. See [Required IAM Policy](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/assigningkeys.htm#permissions), and [Let a user group delegate key usage in a compartment](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#os-bv-admins-use-key-id).
### Using the CLI for SSE With Your Keys in Vault 🔗 
You can use your own encryption keys in Vault to encrypt objects using the CLI. 
You can supply your own encryption key using the optional parameter `--opc-sse-kms-key-id ` `target_key_id` for the following commands:
  * `oci os object put`
  * `oci os object copy`


`target_key_id` is the [OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of an existing key in the Vault to be used to encrypt the object.
An example to upload an object to the bucket using a key in Vault:
```
oci os object put -bn "MyKeyBucket" --name "MyObjectName" --file "InputFile" --opc-sse-kms-key-id "ocid1.key.region1.sea..exampleuniqueID"
Uploading object [####################################] 100%
{
 "etag": "cadb9f8a-3292-45e6-a1e8-f075699fb619",
 "last-modified": "Tue, 13 Jul 2021 05:52:47 GMT",
 "opc-content-md5": "9KJsgOK/X5C1sARb2tkhVA=="
}
```

An example to perform a multipart upload using a key in Vault:
```
oci os object put --bucket-name MyBucket --name MyObjectName --file ~/path/to/file --parallel-upload-count 10 --part-size 500 --opc-sse-kms-key-id ocid1.key.oc1.region1.sea..exampleuniqueID
Upload ID: 813bb394-377d-d5cf-cb3f-31b025346199
Split file into 1 parts for upload.
Uploading object [####################################] 100%
{
"etag": "a55f1c69-1cf4-4134-9113-7a866bac712f",
"last-modified": "Wed, 29 May 2024 21:54:55 GMT",
"opc-multipart-md5": "sAVJt/6nEVizTbwRblZZSg==-1"
}
```

An example to copy an object using a key in Vault:
```
oci os object copy --bucket-name MyBucket1 --destination-bucket MyBucket2 --source-object-name MyObjectName --opc-sse-kms-key-id ocid1.key.oc1.region1.sea..exampleuniqueID
{
"opc-work-request-id": "115e230c-04b8-4dc6-89eb-7e1269b4ab47"
}
```

**Note** The examples in this section use the full syntax for parameters, for example `--namespace` and `--bucket-name`. Sometimes, there are shortened parameter terms that you can use instead of the full ones, for example `-ns` for `--namespace` and `-bn` for `--bucket-name`. The CLI online `--help` for a particular command displays the shortened parameters that you can use.
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
### Using the REST API for SSE With Keys in Vault 🔗 
If you want to use your own keys in Vault for server-side encryption, specify the following request header with the OCID of the key in Vault:
Headers | Description | APIs Supported  
---|---|---  
`opc-sse-kms-key-id` | Specifies the OCID of an existing key in Vault to be used to encrypt the object. | [PutObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/PutObject) [CopyObject ](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/CopyObject) [CreateMultipartUpload](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/MultipartUpload/CreateMultipartUpload) [UploadPart](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/MultipartUpload/UploadPart)  
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
## Bucket Re-encryption 🔗 
If you've rotated a master encryption key since the time you assigned it to a bucket, you might want to re-encrypt the bucket. Until you explicitly re-encrypt a bucket, the key version associated with the bucket when an object was inserted into the bucket continues to decrypt all data encryption keys. 
To encrypt and decrypt all data encryption keys with the same, most recent version of the assigned master encryption key, re-encrypt the bucket. See [Re-encrypting a Bucket's Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_reencrypt_a_buckets_data_encryption_keys.htm#top "Re-encrypt the unique data encryption key that encrypts each object written to an Object Storagebucket by using the most recent version of the master encryption key.") for more information.
## Object Re-encryption 🔗 
To encrypt and decrypt an object's data encryption keys with a different master encryption key, you can re-encrypt the object. When re-encrypting an object, you can select either a different key from the one assigned to the bucket or the most recent version of the key assigned to the bucket. Until you explicitly re-encrypt an object, the key version associated with the bucket (when the object was inserted into the bucket) continues to decrypt all the object's data encryption keys.
You can re-encrypt an object's data encryption keys with a key managed by Oracle, a key that you created and control through a vault that you manage, or a customer-provided encryption key (SSE-C).
**Note** If you use server-side encryption with customer-provided keys (SSE-C), you must use the CLI to provide the SSE-C key during the encryption or re-encryption process. Using the CLI, you can re-encrypt an object with a different SSE-C key, a key managed by Oracle, or a key that you manage through the Vault service. In the Console, you can only re-encrypt an object to use the latest version of the Oracle-managed key assigned to the bucket or the latest version of a Vault key. It doesn't matter whether the chosen key version is the one assigned to the bucket.
See [Re-encrypting an Object](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_reencrypt_an_object.htm#top "Re-encrypt an object's data encryption keys with a different master encryption key in an Object Storage bucket.") for more information.
Was this article helpful?
YesNo


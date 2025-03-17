Updated 2024-04-16
# Object Storage Amazon S3 Compatibility API Support
Learn about how Object Storage supports Amazon S3 Compatibility API.
Amazon S3 Compatibility API support is provided at the bucket level and object level. Amazon S3 Compatibility API supports version ids.
## Bucket APIs 🔗 
The following bucket APIs are supported: 
  * [DeleteBucket](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/DeleteBucket)
  * [GetLocation](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/GetLocation)
  * [HeadBucket](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/HeadBucket)
  * [GetService](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/GetService) (list all my buckets)
  * [ListObjects](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/ListObjects)
  * [PutBucket](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/PutBucket)


## Object APIs 🔗 
The following object APIs are supported:
  * [BulkDelete](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/BulkDelete)
  * [DeleteObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/DeleteObject)
  * [GetObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/GetObject)
  * [HeadObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/HeadObject)
  * [PutObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/PutObject)
  * [RestoreObjects](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/RestoreObjects)


## Multipart Upload APIs 🔗 
The following multipart upload APIs are supported: 
  * [AbortMultipartUpload](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/AbortMultipartUpload)
  * [CompleteMultipartUpload](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/CompleteMultipartUpload)
  * [InitiateMultipartUpload](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/InitiateMultipartUpload)
  * [ListParts](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/ListParts)
  * [ListUploads](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/ListUploads)
  * [UploadPart](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/UploadPart)


## Tagging APIs 🔗 
The following tagging APIs are supported: 
  * [DeleteBucketTagging](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Tagging/DeleteBucketTagging)
  * [GetBucketTagging](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Tagging/GetBucketTagging)
  * [PutBucketTagging](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Tagging/PutBucketTagging)


## SSE-C Support 🔗 
Using optional API headers, you can provide your own 256-bit AES encryption key that's used to encrypt and decrypt objects uploaded to and downloaded from Object Storage. 
To use your own keys for server-side encryption, specify the following three request headers with the encryption key information:
Headers | Description | APIs Supported  
---|---|---  
`x-amz-server-side-encryption-customer-algorithm` | Specifies "AES256" as the encryption algorithm. |  [GetObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/GetObject) [HeadObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/HeadObject) [PutObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/PutObject) [InitiateMultipartUpload](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/InitiateMultipartUpload) [UploadPart](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/UploadPart)  
`x-amz-server-side-encryption-customer-key` | Specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the data.  
`x-amz-server-side-encryption-customer-key-md5` | Specifies the base64-encoded 128-bit MD5 digest of the encryption key. This value is used to check the integrity of the encryption key.  
Object Storage has distinct APIs for copying objects and copying parts. Amazon S3 uses the presence of the following headers in [PutObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/PutObject) and [UploadPart](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/UploadPart) to determine copy operations. To copy a source object that's encrypted with an SSE-C key, you must specify these three headers so that Object Storage can decrypt the object.
Headers | Description | APIs Supported  
---|---|---  
`x-amz-copy-source-server-side-encryption-customer-algorithm` | Specifies "AES256" as the encryption algorithm to use to decrypt the source object. |  [PutObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/PutObject) [UploadPart](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/UploadPart)  
`x-amz-copy-source-server-side-encryption-customer-key` | Specifies the base64-encoded 256-bit encryption key to use to decrypt the source object.  
`x-amz-copy-source-server-side-encryption-customer-key-md5` | Specifies the base64-encoded 128-bit MD5 digest of the encryption key used to decrypt the source object.  
##  Support for Encryption Using Your Own Keys in Vault 🔗 
Using optional API headers, you can provide your own encryption key in Vault to encrypt objects uploaded to Object Storage. 
To use your own keys in Vault for server-side encryption, specify the following request header with the OCID of the key in Vault:
Headers | Description | APIs Supported  
---|---|---  
`x-amz-server-side-encryption-aws-kms-key-id` | OCID of an existing key in Vault to be used to encrypt the object. |  [PutObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/PutObject) [InitiateMultipartUpload](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/InitiateMultipartUpload) [UploadPart](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/UploadPart)  
## Supported Amazon S3 Clients 🔗 
You can configure various client applications to talk to Object Storage's Amazon S3-compatible endpoints. This topic provides some configuration examples for supported Amazon S3 Clients. Review the prerequisites in [Amazon S3 Compatibility API Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/s3compatibleapi.htm#usingAPI).
### AWS SDK for Java
The AWS SDK for Java repository, file download, and documentation links are available on GitHub: <https://github.com/aws/aws-sdk-java>.
Here is an example of configuring AWS SDK for Java to use Object Storage
Copy
```

        // Put the Access Key and Secret Key here
        
AWSCredentialsProvider credentials = new AWSStaticCredentialsProvider(new BasicAWSCredentials(
 "gQ4+YC530sBa8qZI6WcbUbtH8oar0exampleuniqueID",
 "7fa22331ebe62bf4605dc9a42aaeexampleuniqueID"))));
// Your namespace
String namespace = "namespace";
// The region to connect to
String region = "us-ashburn-1";
// Create an S3 client pointing at the region
String endpoint = String.format("%s.compat.objectstorage.%s.oraclecloud.com",namespace,region);
AwsClientBuilder.EndpointConfiguration endpointConfiguration = new AwsClientBuilder.EndpointConfiguration(endpoint, region);
AmazonS3 client = AmazonS3Client.builder()
 .standard()
 .withCredentials(credentials)
 .withEndpointConfiguration(endpointConfiguration)
 .disableChunkedEncoding()
 .enablePathStyleAccess()
 .build();
```

### AWS SDK for Javascript
The AWS SDK for Javascript repository, documentation links, and installation instructions are available on GitHub: <https://github.com/aws/aws-sdk-js>.
Here is an example of configuring AWS SDK for Javascript to use Object Storage
Copy
```
s3 = new AWS.S3({
 region: 'us-ashburn-1',
 endpoint: 'https://' + mynamespace + '.compat.objectstorage.us-ashburn-1.oraclecloud.com',
 accessKeyId: 'gQ4+YC530sBa8qZI6WcbUbtH8oar0exampleuniqueID',
 secretAccessKey: '7fa22331ebe62bf4605dc9a42aaeexampleuniqueID',
 s3ForcePathStyle: true,
 signatureVersion: 'v4',
});
```

### AWS SDK for Python (Boto3)
The AWS SDK for Python (Boto3) repository, documentation links, and installation instructions are available on GitHub: <https://github.com/boto/boto3>.
Here is an example of configuring AWS SDK for Python to use Object Storage
Copy
```
import boto3
 
s3 = boto3.resource(
  's3',
  aws_access_key_id="gQ4+YC530sBa8qZI6WcbUbtH8oar0exampleuniqueID",
  aws_secret_access_key="7fa22331ebe62bf4605dc9a42aaeexampleuniqueID",
  region_name="us-phoenix-1", # Region name here that matches the endpoint
  endpoint_url="https://mynamespace.compat.objectstorage.us-phoenix-1.oraclecloud.com" # Include your namespace in the URL
)
 
# Print out the bucket names
for bucket in s3.buckets.all():
  print bucket.name
```

### Mounting Object Storage Buckets Using s3fs
s3fs lets Linux and macOS mount Object Storage as a file system. The s3fs repository, documentation links, installation instructions, and examples are available on GitHub: <https://github.com/s3fs-fuse/s3fs-fuse>.
s3fs isn't suitable for all applications. Understand the following limitations:
  * Object storage services have high latency compared to local file systems for time to first-byte and lack random write access. s3fs achieves the best throughput on workloads that only read large files.
  * You can't partially update a file, so changing a single byte requires uploading the entire file.
  * Random writes or appends to files require rewriting the entire file.
  * s3fs doesn't support partial downloads, so even if you only want to read one byte of a file, you need to download the entire file.
  * s3fs doesn't support server-side file copies. Copied files must first be downloaded to the client and then uploaded to the new location.
  * Metadata operations, such as listing directories, have poor performance because of network latency.
  * s3fs doesn't support hard links or the atomic renames of files or directories.
  * s3fs provides no coordination between several clients mounting the same bucket.


To mount an Object Storage bucket as a file system
  1. Follow the installation instructions provided on GitHub: <https://github.com/s3fs-fuse/s3fs-fuse>.
If you're unable to install using a pre-built package, follow the compilation instructions here: <https://github.com/s3fs-fuse/s3fs-fuse/blob/master/COMPILATION.md>.
  2. Review and perform the prerequisites in [Amazon S3 Compatibility API Prerequisites](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/s3compatibleapi.htm#usingAPI). You need an Access Key/Secret Key pair and a proper IAM policy that lets you mount a bucket as a file system. For example:
Copy
```
Allow group s3fsAdmins to manage object-family in compartment MyCompartment
```

  3. Enter your Access Key/Secret Key pair credentials in a ${HOME}/.passwd-s3fs credential file:
Command
CopyTry It
```
cat ${HOME}/.passwd-s3fs
access_key:secret_key
```

For example:
Copy
```
cat ${HOME}/.passwd-s3fs
gQ4+YC530sBa8qZI6WcbUbtH8oar0exampleuniqueID:7fa22331ebe62bf4605dc9a42aaeexampleuniqueID
```

Then, set owner-only permissions for the credential file:
Command
CopyTry It
```
chmod 600 ${HOME}/.passwd-s3fs
```

  4. Create a mount point to mount an Object Storage bucket:
Command
CopyTry It
```
mkdir /path/to/<local_directory_name>
s3fs bucket_name local_directory_name -o passwd_file=${HOME}/.passwd-s3fs -o url=https://<namespace_name>.compat.objectstorage.<region_ID>.oraclecloud.com -o use_path_request_style -o kernel_cache -o multipart_size=128 -o parallel_count=50 -o multireq_max=100 -o max_background=1000 [-o endpoint=<region_ID>]
```

Where:
     * `bucket_name` is the name of the bucket that you want to mount. 
     * `local_directory_name` is the name of the local directory where you want to mount the bucket.
     * `namespace_name` is the unique system-generated assigned to your tenancy at account creation time. You can use the CLI or the Console to obtain your namespace name. See [Object Storage Namespaces](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/understandingnamespaces.htm#namespaces "Learn about how to access and use your namespace for running Object Storage tasks.") for details.
     * `region_ID` is the region identifier where the bucket resides. See [Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm) for details.
     * `endpoint`: If you want to mount a bucket that was created in your home region, you do not need to specify the `endpoint` parameter. If you want to mount a bucket that was created in a different region, you need to specify the `endpoint` parameter.
  5. To automatically mount the bucket as a file system on system startup using s3fs, add following to the `/etc/fstab` file:
Command
CopyTry It
```
bucket_name /path/to/local_directory_name fuse.s3fs use_path_request_style,passwd_file=/root/.s3fs-password,url=https://namespace_name.compat.objectstorage.region_ID.oraclecloud.com,endpoint=region_ID kernel_cache,multipart_size=128,parallel_count=50,multireq_max=100,max_background=1000,_netdev
```

  6. To verify the s3fs bucket mount, run the `df -h` command. The output shows the new mount point for the bucket. Navigate to the new mount point and run the `ls` command to list all objects in the bucket.


To troubleshoot mounting an Object Storage bucket
  * If you get authorization errors, review your IAM policies and ensure you have one that lets you mount a bucket as a file system. For example:
Copy
```
Allow group s3fsAdmins to manage object-family in compartment MyCompartment
```

  * Ensure that you're using the correct namespace name in the URL in the s3fs command. To verify your namespace name, see [Object Storage Namespaces](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/understandingnamespaces.htm#namespaces "Learn about how to access and use your namespace for running Object Storage tasks."). 
  * Ensure that the named bucket that you are trying to mount exists and is in a compartment that you have access to. Use one of the following ways to verify the bucket name: 
    * Log into the Console and find the named bucket in the compartment that you have access to.
    * Use the CLI command `oci os bucket list --namespace <object_storage_namespace> --compartment-id <target_compartment_id>`.
  * To mount a bucket that was created in a region other than your home region, you need to specify that other region in both the `url` and `endpoint` parameters.
  * If you mount a bucket as the root user, other users can't list or access objects in the bucket unless you add `-o allow_other` to the s3fs command or `allow_other` to the `/etc/fstab` mount options. You can also supply specific UID and GID parameters to specify user access details.
  * If you reviewed and verified the troubleshooting solutions and need to contact Support, run the mount command again in DEBUG mode to get more failure details. Add the following to the end of the command and save the output: 
Command
CopyTry It
```
-o dbglevel=info -f -o curldbg
```



To unmount an Object Storage bucket from a file system
Run the following command, specifying the mount point:
Command
CopyTry It
```
umount /path/to/<local_directory_name>
```

Was this article helpful?
YesNo


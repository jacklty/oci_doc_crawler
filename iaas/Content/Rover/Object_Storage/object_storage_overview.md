Updated 2025-02-21
# Object Storage for Roving Edge Infrastructure 
Describes how to manage object storage tasks, including those for buckets and objects, on your Roving Edge Infrastructure devices.
This section describes the following Roving Edge Infrastructure on-device services related to object storage:
  * [Buckets](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Bucket/bucket_management.htm#BucketManagement "Learn about managing the Object Storage bucket tasks, including creating, updating, and deleting buckets, on your Roving Edge Infrastructure devices.")
  * [Objects](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/object_management.htm#ObjectManagement "Describes how to manage the object storage object tasks, including creating, updating, and deleting objects, on your Roving Edge Infrastructure.")


## Performance and Usage Thresholds 🔗 
We recommend that you keep your storage thresholds below 80%. Maintaining this level is important to optimize performance, especially for intensive writing operations. If the Roving Edge Infrastructure device capacity nears 80%, transfer data to your OCI tenancy until the storage level falls below 80% to achieve optimal operation of services.
Regularly monitor the available storage space for all your Roving Edge Infrastructure devices. See [Roving Edge Infrastructure Device Monitoring](https://docs.oracle.com/en-us/iaas/Content/Rover/Device_Monitoring/device_monitoring.htm#NodeManagement "Describes how to monitor the system health and storage capacities of your Roving Edge Infrastructure components.").
## Amazon S3 Compatibility API 🔗 
Using the Amazon S3 Compatibility API, customers can continue to use their existing Amazon S3 tools (for example, SDK clients) and make minimal changes to their applications to work with Object Storage. The Amazon S3 Compatibility API and Object Storage datasets are congruent. If data is written to the Object Storage using the Amazon S3 Compatibility API, the data can be read back using the native Object Storage API and conversely.
### Differences between the Object Storage API and the Amazon S3 Compatibility API 🔗 
The Object Storage service provided by Oracle Cloud Infrastructure and Amazon S3 use similar concepts and terminology. In both cases, data is stored as objects in buckets. The differences are in the implementation of features and tools for working with objects. 
The following highlights the differences between the two storage technologies:
  * **Compartments**
Amazon S3 does not use compartments. By default, buckets created using the Amazon S3 Compatibility API or the Swift API are created in the root compartment of the Oracle Cloud Infrastructure tenancy. Instead, you can designate a different compartment for the Amazon S3 Compatibility API or Swift API to create buckets in.
  * **Global bucket namespace**
Object Storage does not use a global bucket namespace. Instead, the namespace serves as the top-level container for all buckets and objects. At account creation time, each tenant is assigned one unique system-generated and immutable namespace name. The namespace spans all compartments within a region. You control bucket names, but those bucket names must be unique within a namespace. While the namespace is region-specific, the namespace name itself is the same in all regions. You can have a bucket named **MyBucket** in US West (Phoenix) and a bucket named **MyBucket** in Germany Central (Frankfurt).
  * **Encryption**
The Object Storage service encrypts all data at rest by default. Encryption can't be turned on or off using the API.
  * **Object Level Access Control Lists (ACLs)**
Oracle Cloud Infrastructure does not use ACLs for objects. Instead, an administrator needs to set up **groups** , **compartments** , and **policies** that control which users can access which services, which resources, and the type of access. For example, the policies control who can create users and groups, create buckets, download objects, and manage Object Storage-related policies and rules. 


For more information, see [Overview of Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm).
### Setting up Access to Oracle Cloud Infrastructure 🔗 
To enable application access from Amazon S3 to Object Storage, you need to set up access to Oracle Cloud Infrastructure and modify your application. 
  1. Sign up for Oracle Cloud Infrastructure and obtain a unique namespace.
  2. Any user of the Amazon S3 Compatibility API with Object Storage needs permission to work with the service. If you are not sure if you have permission, contact your administrator. For basic information about policies, see [How Policies Work](https://docs.oracle.com/iaas/Content/Identity/policieshow/how-policies-work.htm). For policies that enable use of Object Storage, see [Common Policies](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm) and the [Policy Reference](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference.htm).
  3. Use an existing or create a customer secret key. A customer secret key consists of an access key/secret key pair. The creation and use of these keys is described in the following section on setting up the S3 configuration file.


### Setting Up the S3 Configuration File 🔗 
Object Storage on Roving Edge Infrastructure supports the Amazon S3cmd tool in addition to supporting the Oracle Cloud Infrastructure command line interface. Support of the Amazon S3cmd tool requires you to set up the S3 configuration file but also supports S3cmd.
You can download s3cmd from the following site:
<https://s3tools.org/download>
On Macintosh and Linux, the s3cmd configuration file is named `.s3cfg` and it is located in the your home directory, for example:
```
/home/username/($HOME)
```

On Windows, the s3cmd configuration file is named `s3cmd.ini` and it is located in `%USERPROFILE% -> Application Data`, which is typically the following:
```
c:\users\username\AppData\Roaming\s3cmd.ini
```

For more details, reference: <https://s3tools.org/kb/item14.htm>
The following example shows contents the S3cmd configuration file:
```
[default]
**access_key = 9aa40ec9-bec3-4fab-9e5a-3584a5979d48**
access_token =
add_encoding_exts =
add_headers =
bucket_location = US
cache_file =
**ca_certs_file = <Full path to the bundle.pem file>**
**check_ssl_hostname = False**
default_mime_type = binary/octet-stream
delay_updates = False
delete_after = False
delete_after_fetch = False
delete_removed = False
dry_run = False
enable_multipart = True
encoding = UTF-8
encrypt = False
expiry_date =
expiry_days =
expiry_prefix =
follow_symlinks = False
force = False
get_continue = False
gpg_command = /usr/bin/gpg
gpg_decrypt = %(gpg_command)s -d --verbose --no-use-agent --batch --yes --passphrase-fd %(passphrase_fd)s -o %(output_file)s %(input_file)s
gpg_encrypt = %(gpg_command)s -c --verbose --no-use-agent --batch --yes --passphrase-fd %(passphrase_fd)s -o %(output_file)s %(input_file)s
gpg_passphrase =
guess_mime_type = True
**host_base = <rover_node_ip>:8019**
**host_bucket = <rover_node_ip>:8019**
human_readable_sizes = False
ignore_failed_copy = False
invalidate_default_index_on_cf = False
invalidate_default_index_root_on_cf = True
invalidate_on_cf = False
list_md5 = False
log_target_prefix =
max_delete = -1
mime_type =
multipart_chunk_size_mb = 15
preserve_attrs = True
progress_meter = True
proxy_host =
proxy_port = 0
put_continue = False
recursive = False
recv_chunk = 4096
reduced_redundancy = False
restore_days = 1
**secret_key = <Your secret key, see below>**
send_chunk = 4096
server_side_encryption = False
skip_existing = False
socket_timeout = 300
urlencoding_mode = normal
use_https = True
use_mime_magic = True
verbosity = WARNING
**website_endpoint = https://<rover_node_ip>:8015**
website_error =
```

To set up the S3cmd configuration file for use with Roving Edge Infrastructure:
  1. Update the **access_key** field:
    1. Log into the Roving Edge Infrastructure Device Console of the appropriate device.
    2. Open the navigation menu and select **Identity Management > Users**. The **Users** page appears. All users are listed in tabular form.
    3. Click the user whose access key you want to use in the S3cmd configuration file. The user's **Details** page appears.
    4. Click **Customer Secret Keys** under **Resources**. The **Customer Secret Keys** page appears. All customer secret keys are listed in tabular form.
    5. Copy the access key and past it into the **access_key** field value in the s3cmd configuration file.
  2. Update the **ca_certs_file** field: Enter the full path of your `bundle.pem` file, for example:
```
/Users/user_name/.oci/bundle.pem
```

If you do not have the ca certs file, download it using the following command:
```
echo -n | openssl s_client -showcerts -connect rover_node_IP:8015 | 
sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > bundle.pem
```

  3. Set the **check_ssl_hostname** field to `false`.
  4. Update the **host_base** field: Enter the `rover_node_IP:8019`.
  5. Update the **host_bucket** field: Enter the `rover_node_IP:8019`.
  6. Update the **secret_key** field: 
    1. Log into the Roving Edge Infrastructure Device Console of the appropriate device.
    2. Open the navigation menu and select **Identity Management > Users**. The **Users** page appears. All users are listed in tabular form.
    3. Click the user whose secret key you want to use in the S3cmd configuration file. The user's **Details** page appears.
    4. Click **Customer Secret Keys** under **Resources**. The **Customer Secret Keys** page appears. All customer secret keys are listed in tabular form.
    5. Click **Generate Secret Key**. The generated **Secret Key** is displayed in the **Generate Secret Key** dialog box. At the same time, Oracle generates the **Access Key** that is paired with the **Secret Key**. The newly generated Customer Secret key is added to the list of **Customer Secret Keys**.
    6. Copy the key and past it into the **secret_key** field value in the s3cmd configuration file.
  7. Save and close the s3cmd configuration file.


### Amazon S3 Compatibility API Support 🔗 
Amazon S3 Compatibility API support is provided at the bucket level and object level.
**Bucket APIs**
The following bucket APIs are supported:
  * [DeleteBucket](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/DeleteBucket)
  * [HeadBucket](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/HeadBucket)
  * [GetService](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/GetService) (list all my buckets) 
  * [ListObjects](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/ListObjects)
  * [PutBucket](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/PutBucket)


**Object APIs**
The following object APIs are supported:
  * [BulkDelete](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/BulkDelete)
  * [DeleteObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/DeleteObject)
  * [GetObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/GetObject)
  * [HeadObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/HeadObject)
  * [PutObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/PutObject)


**Multipart Upload APIs**
The following multipart upload APIs are supported: 
  * [AbortMultipartUpload](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/AbortMultipartUpload)
  * [CompleteMultipartUpload](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/CompleteMultipartUpload)
  * [InitiateMultipartUpload](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/InitiateMultipartUpload)
  * [ListParts](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/ListParts)
  * [ListUploads](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/ListUploads)
  * [UploadPart](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/UploadPart)


### SSE-C Support 🔗 
Using optional API headers, you can provide your own 256-bit AES encryption key that is used to encrypt and decrypt objects uploaded to and downloaded from Object Storage. 
If you want to use your own keys for server-side encryption, specify the following three request headers with the encryption key information:
Headers | Description | APIs Supported  
---|---|---  
`x-amz-server-side-encryption-customer-algorithm` | Specifies "AES256" as the encryption algorithm. |  [GetObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/GetObject) [HeadObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/HeadObject) [PutObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/PutObject) [InitiateMultipartUpload](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/InitiateMultipartUpload) [UploadPart](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/UploadPart)  
`x-amz-server-side-encryption-customer-key` | Specifies the base64-encoded 256-bit encryption key to use to encrypt or decrypt the data.  
`x-amz-server-side-encryption-customer-key-md5` | Specifies the base64-encoded 128-bit MD5 digest of the encryption key. This value is used to check the integrity of the encryption key.  
Object Storage has distinct APIs for copying objects and copying parts. Amazon S3 uses the presence of the following headers in [PutObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/PutObject) and [UploadPart](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/UploadPart) to determine copy operations. To copy a source object that is encrypted with an SSE-C key, you must specify these three headers so that Object Storage can decrypt the object.
Headers | Description | APIs Supported  
---|---|---  
`x-amz-copy-source-server-side-encryption-customer-algorithm` | Specifies "AES256" as the encryption algorithm to use to decrypt the source object. |  [PutObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/PutObject) [UploadPart](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/UploadPart)  
`x-amz-copy-source-server-side-encryption-customer-key` | Specifies the base64-encoded 256-bit encryption key to use to decrypt the source object.  
`x-amz-copy-source-server-side-encryption-customer-key-md5` | Specifies the base64-encoded 128-bit MD5 digest of the encryption key used to decrypt the source object.  
### Support for Encryption Using Your Own Keys in Vault 🔗 
Using optional API headers, you can provide your own encryption key in Vault that is used to encrypt objects uploaded to Object Storage. 
If you want to use your own keys in Vault for server-side encryption, specify the following request header with the OCID of the key in Vault:
Headers | Description | APIs Supported  
---|---|---  
`x-amz-server-side-encryption-aws-kms-key-id` | OCID of an existing key in Vault to be used to encrypt the object. |  [PutObject](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Object/PutObject) [InitiateMultipartUpload](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/InitiateMultipartUpload) [UploadPart](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/MultipartUpload/UploadPart)  
### Supported Amazon S3 Clients 🔗 
You can configure various client applications to talk to Object Storage's Amazon S3-compatible endpoints. This topic provides some configuration examples for supported Amazon S3 Clients. Review the prerequisites in [Setting up Access to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/object_storage_overview.htm#usingAPI).
#### AWS SDK for Java 🔗 
The AWS SDK for Java repository, file download, and documentation links are available on GitHub: <https://github.com/aws/aws-sdk-java>.
Here is an example of configuring AWS SDK for Java to use Object Storage
Copy
```

        // Put the Access Key and Secret Key here
        
AWSCredentialsProvider credentials = new AWSStaticCredentialsProvider(new BasicAWSCredentials(
 "gQ4+YC530sBa8qZI6WcbUbtH8oar0exampleuniqueID",
 "7fa22331ebe62bf4605dc9a42aaeexampleuniqueID"))));
// Your namespace
String namespace = "rover-namespace";
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

#### AWS SDK for Javascript
The AWS SDK for Javascript repository, documentation links, and installation instructions are available on GitHub: <https://github.com/aws/aws-sdk-js>.
Here is an example of configuring AWS SDK for Javascript to use Object Storage
Copy
```
s3 = new AWS.S3({
 region: 'us-ashburn-1',
 endpoint: 'https://' + rover-namespace + '.compat.objectstorage.us-ashburn-1.oraclecloud.com',
 accessKeyId: 'gQ4+YC530sBa8qZI6WcbUbtH8oar0exampleuniqueID',
 secretAccessKey: '7fa22331ebe62bf4605dc9a42aaeexampleuniqueID',
 s3ForcePathStyle: true,
 signatureVersion: 'v4',
});
```

#### AWS SDK for Python (Boto3)
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
  endpoint_url="https://rover-namespace.compat.objectstorage.us-phoenix-1.oraclecloud.com" # Include your rover-namespace in the URL
)
 
# Print out the bucket names
for bucket in s3.buckets.all():
  print bucket.name
```

#### Mounting Object Storage Buckets Using s3fs
s3fs lets Linux and macOS mount Object Storage as a file system. The s3fs repository, documentation links, installation instructions, and examples are available on GitHub: <https://github.com/s3fs-fuse/s3fs-fuse>.
s3fs is not suitable for all applications. Understand the following limitations:
  * Object storage services have high latency compared to local file systems for time to first-byte and lack random write access. s3fs achieves the best throughput on workloads that only read large files.
  * You cannot partially update a file, so changing a single byte requires uploading the entire file.
  * Random writes or appends to files require rewriting the entire file.
  * s3fs does not support partial downloads, so even if you only want to read one byte of a file, you need to download the entire file.
  * s3fs does not support server-side file copies. Copied files must first be downloaded to the client and then uploaded to the new location.
  * Metadata operations, such as listing directories, have poor performance because of network latency.
  * s3fs does not support hard links or the atomic renames of files or directories.
  * s3fs provides no coordination between multiple clients mounting the same bucket.


To mount an Object Storage bucket as a file system:
  1. Follow the installation instructions provided on GitHub: <https://github.com/s3fs-fuse/s3fs-fuse>.
If you are unable to install using a pre-built package, follow the compilation instructions here: <https://github.com/s3fs-fuse/s3fs-fuse/blob/master/COMPILATION.md>.
  2. Review and perform the prerequisites in [Setting up Access to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/object_storage_overview.htm#usingAPI). You need an Access Key/Secret Key pair and a proper IAM policy that lets you mount a bucket as a file system. For example:
Copy
```
Allow group s3fsAdmins to manage object-family in tenancy
```

  3. Enter your Access Key/Secret Key pair credentials in a ${HOME}/.passwd-s3fs credential file:
```
cat ${HOME}/.passwd-s3fs
access_key:secret_key
```

For example:
```
cat ${HOME}/.passwd-s3fs
gQ4+YC530sBa8qZI6WcbUbtH8oar0exampleuniqueID:7fa22331ebe62bf4605dc9a42aaeexampleuniqueID
```

Then, set owner-only permissions for the credential file:
```
chmod 600 ${HOME}/.passwd-s3fs
```

  4. Create a mount point to mount an Object Storage bucket:```
mkdir /path/to/local_directory_name
s3fs bucket_name local_directory_name -o passwd_file=${HOME}/.passwd-s3fs 
-o url=https://rover-namespace.compat.objectstorage.region_ID.oraclecloud.com 
-o use_path_request_style -o kernel_cache -o multipart_size=128 -o parallel_count=50 -o multireq_max=100 -o max_background=1000 
[-o endpoint=region_ID]
```

Where:
     * bucket_name is the name of the bucket that you want to mount.
     * local_directory_name is the name of the local directory where you want to mount the bucket.
     * namespace_name is the unique system-generated assigned to your tenancy at account creation time. You can use the CLI or the Console to obtain your namespace name. See [Understanding Object Storage Namespaces](https://docs.oracle.com/iaas/Content/Object/Tasks/understandingnamespaces.htm) for details.
     * region_ID is the region identifier where the bucket resides. See [Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm) for details.
     * `endpoint`: If you want to mount a bucket that was created in your home region, you do not need to specify the `endpoint` parameter. If you want to mount a bucket that was created in a different region, you need to specify the `endpoint` parameter.
  5. If you want to automatically mount the bucket as a file system on system startup using s3fs, add following to the `/etc/fstab` file:
```
bucket_name /path/to/local_directory_name fuse.
s3fs use_path_request_style,passwd_file=/root/.s3fs-password,url=https://rover-namespace.
compat.objectstorage.region_ID.oraclecloud.com,endpoint=region_ID 
kernel_cache,multipart_size=128,parallel_count=50,multireq_max=100,max_background=1000,_netdev
```

  6. To verify the s3fs bucket mount, run the `df -h` command. The output shows the new mount point for the bucket. Navigate to the new mount point and run the `ls` command to list all objects in the bucket.


To troubleshoot mounting an Object Storage bucket
  * If you get authorization errors, review your IAM policies and ensure you have one that lets you mount a bucket as a file system. For example:
Copy
```
Allow group s3fsAdmins to manage object-family in tenancy
```

  * If you are trying to mount a bucket that was created in a region other than your home region, you need to specify that other region in both the `url` and `endpoint` parameters.
  * If you mount a bucket as the root user, other users are not able to list or access objects in the bucket unless you add `-o allow_other` to the s3fs command or `allow_other` to the `/etc/fstab` mount options. You can also supply specific UID and GID parameters to specify user access details.
  * If you reviewed and verified the troubleshooting solutions and need to contact Support, run the mount command again in DEBUG mode to get more failure details. Add the following to the end of the command and save the output: ```
-o dbglevel=info -f -o curldbg
```



To unmount an Object Storage bucket from a file system, run the following command, specifying the mount point:```
umount /path/to/local_directory_name
```

Was this article helpful?
YesNo


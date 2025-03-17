Updated 2023-08-15
# Uploading an Image to an Object Storage Bucket
On Compute Cloud@Customer, you can store images in an object storage bucket.
Advantages of storing an image in an Object Storage bucket are that you can implement object versioning or preauthenticated requests as described in [Managing Object Versioning](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/managing-object-versioning.htm#managing-object-versioning "On Compute Cloud@Customer, object versioning provides data protection against accidental or malicious object update, overwrite, or deletion.") and [Using Preauthenticated Requests](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/using-pre-authenticaed-requests.htm#using-pre-authenticaed-requests "On Compute Cloud@Customer, preauthenticated requests provide a way to let users access a bucket or an object without having their own credentials, as long as the request creator has permissions to access those objects.").
  1. Create an Object Storage bucket as described in [Creating a Bucket](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/creating-a-bucket.htm#creating-a-bucket "On Compute Cloud@Customer, you can create Object Storage buckets.").
  2. Upload an image from a local file system to the bucket. See [Uploading an Object](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/uploading-an-object.htm#uploading-an-object "On Compute Cloud@Customer, you can upload an object using the CLI and API.").
  3. Import the image from the Object Storage bucket to a compartment so that the image is available to select when you create an instance. See [Importing an Image from an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/importing-an-image-from-an-object-storage-bucket.htm#importing-an-image-from-an-object-storage-bucket_0 "On Compute Cloud@Customer, you can import an image into a compartment from an Object Storage bucket.").


Was this article helpful?
YesNo


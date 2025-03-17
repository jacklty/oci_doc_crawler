Updated 2024-08-06
# Sharing Custom Images Across Tenancies
On Compute Cloud@Customer, you can use image import and export to share custom images across tenancies so that you don't need to recreate the image manually in each tenancy. You create the image in one of the tenancies, and then export the image, making it available for import in additional tenancies.
These are the high-level tasks:
  1. Export the image to an Object Storage bucket. See [Exporting an Image to an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/exporting-an-image-to-object-storage.htm#exporting-an-image-to-object-storage "On Compute Cloud@Customer, you can export an image to an Object Storage bucket.").
  2. Create a preauthenticated request with read-only access for the image in the bucket. See [Using Preauthenticated Requests](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/using-pre-authenticaed-requests.htm#using-pre-authenticaed-requests "On Compute Cloud@Customer, preauthenticated requests provide a way to let users access a bucket or an object without having their own credentials, as long as the request creator has permissions to access those objects.").
  3. In the destination tenancy, import the image. Use the preauthenticated request URL as the Object Storage URL. See [Importing an Image from a URL](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/importing-an-image-from-a-url.htm#importing-an-image-from-a-url "On Compute Cloud@Customer, you can import an image into a compartment by specifying the URL of the image file.").


Was this article helpful?
YesNo


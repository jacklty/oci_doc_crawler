Updated 2024-08-06
# Listing Images and Viewing Details
On Compute Cloud@Customer, in both the Compute Cloud@Customer Console and CLI, Oracle provided images are listed first, followed by custom images. 
The list of Oracle provided images includes the three most recently published versions of each major distribution. Any older versions that were previously listed are still available by specifying the image OCID.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/listing-images-and-viewing-details.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/listing-images-and-viewing-details.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/listing-images-and-viewing-details.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Images**.
    2. At the top of the page, select the compartment that contains the images you want to see.
    3. To see details of an image, click the name of the image in the list.
  * Use the [oci compute image list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/list.html) command and required parameters to list the images in the specified compartment.
Copy
```
oci compute image list [OPTIONS]
```

Use the [oci compute image get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/get.html) command and required parameters to get the image details for just one image.
Copy
```
oci compute image get [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListImages](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/ListImages) and [GetImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/GetImage) operations to list all images or get one image.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


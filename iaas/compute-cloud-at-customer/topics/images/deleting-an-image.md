Updated 2024-08-06
# Deleting an Image
On Compute Cloud@Customer, you can delete custom images.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/deleting-an-image.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/deleting-an-image.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/deleting-an-image.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Images**.
    2. At the top of the page, select the compartment that contains the image you want to delete.
    3. For the custom image that you want to delete, click Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Delete image**.
The image is deleted.
  * Use the [oci compute image delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/delete.html) command and required parameters to delete a custom image.
Copy
```
oci compute image delete [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/DeleteImage) operation to delete a custom image.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


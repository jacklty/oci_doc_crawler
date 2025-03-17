Updated 2024-08-06
# Updating an Image Name
On Compute Cloud@Customer, you change a custom image's display name.
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/updating-the-image-name.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/updating-the-image-name.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/updating-the-image-name.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Images**.
    2. At the top of the page, select the compartment that contains the image you want to edit.
    3. Use one of the following methods to open the **Update Image** dialog box.
       * For the image that you want to update, click Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), and click **Edit**.
       * Click the name of the image that you want to update. On the image details page, click **Controls** (upper right corner), then click **Edit Details**.
    4. In the **Update Image** dialog box, modify the image name.
The image name doesn't need to be unique.
Avoid entering confidential information
    5. Click **Save Changes**.
  * Use the [oci compute image update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/update.html) command and required parameters to change an image name.
Copy
```
oci compute image update [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/UpdateImage) operation to update the specified image.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


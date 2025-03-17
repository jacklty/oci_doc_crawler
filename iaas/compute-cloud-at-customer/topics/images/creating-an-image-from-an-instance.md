Updated 2024-08-06
# Creating an Image from an Instance
On Compute Cloud@Customer, you can create a custom image of a compute instance's boot disk and use that custom image to create other compute instances. Instances that you create from this image include the customizations, configuration, and software that were installed on the boot disk when you created the image.
Custom images don't include the data from any attached block volumes.
After the new custom image reaches the Available state, you can use it to create new instances. See [Creating an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance.htm#creating-an-instance "On Compute Cloud@Customer, you can create an instance using the Compute Cloud@Customer Console, CLI, and API.").
**Limitations and Considerations**
  * Certain IP addresses are reserved for Compute Cloud@Customer use and can not be used in your address numbering scheme. For details, refer to [Reserved Network Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/reserved-network-resources.htm#reserved-network-resources "On Compute Cloud@Customer, the network infrastructure and system components need many IP addresses and several VLANs for internal operation. It's critical to avoid conflicts with the addresses in use in the customer data center and the CIDR ranges configured in the virtual cloud networks \(VCNs\).").
  * When you create an image of an instance, the instance must be in the stopped state. After the custom image is created, you can restart the instance.
  * You can't create extra custom images of a compute instance while the compute instance is engaged in the image creation process. You can, however, create images of different compute instances at the same time.
  * Custom images are available to all users authorized for the compartment in which the image was created. 
  * Custom images inherit the compatible shapes that are set by default from the base image.


Avoid entering confidential information in names.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/creating-an-image-from-an-instance.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/creating-an-image-from-an-instance.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/creating-an-image-from-an-instance.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    2. At the top of the page, select the compartment that contains the instance you plan to use.
    3. Click the name of the instance that you want to use as the basis for the custom image.
    4. Ensure that the instance is in the Stopped state:
      1. On the details page for the instance, click **Controls** (upper right corner), and then click **Stop**.
      2. Wait for the instance status to change to Stopped. The status is displayed above the icon of the object.
    5. Click **Controls** and then click **Create Custom Image**.
    6. In the **Create Image From Instance** dialog box, enter the following information:
       * **Name:** Replace the name with the name you want for the image.
       * **Create in Compartment:** Select the compartment where the image will be stored.
    7. Click **Create Custom Image**.
The status of the instance changes to Creating Image.
    8. Monitor the image creation progress.
The time required to create the custom image depends on the size of the instance's boot volume.
To monitor the progress, on the navigation menu, click **Compute** and then click **Custom Images**. Select the correct compartment, and click the image name in the list. On the details page for the image, under **Resources** click **Work Requests**.
    9. (Optional) Restart the instance.
When the instance status changes from Creating Image to Stopped, you can restart the instance.
  * Use the [oci compute image create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/create.html) command and required parameters to create an image from an instance.
Copy
```
oci compute image create [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/CreateImage) operation to create an image from an instance.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


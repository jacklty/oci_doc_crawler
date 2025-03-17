Updated 2024-09-16
# Creating a Custom Image from an Instance for a Roving Edge Infrastructure Device
Describes how to create a custom image from an existing compute instance on your Roving Edge Infrastructure device.
You can create a custom image of a compute instance's boot disk and use that custom image to create other compute instances. Instances that you create from this image include the customizations, configuration, and software that were installed on the boot disk when you created the image. See [Creating an Image from an Instance](https://docs.oracle.com/iaas/compute-cloud-at-customer/topics/images/creating-an-image-from-an-instance.htm) in the Oracle Cloud Infrastructure Cloud-based help for more information.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/clone_instance.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/clone_instance.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Image/clone_instance.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance whose details you want to get. The instance's **Details** page appears.
    4. Click **More Actions** and select **Create Custom Image** from the menu. The **Create Custom Image** dialog box appears.
    5. (optional) Enter a name for the custom image in the **Display Name** box. If you do not enter a name, the Roving Edge Infrastructure device assigns a random name for the custom image.
    6. Click **Create Custom Image**. A banner appears indicating either that the request for the custom image is accepted, or it has been rejected for some reason. When the custom image request is being processed, the state of the instance changes to **Creating Image**. 
    7. Return to the **Instances** page and click **Custom Images**. The**Custom Images** page appears. After the instance is in the available/provisioning state, the **Custom Images** list has the newly created image.
    8. Next, open the navigation menu and select **Compute > Custom Images**. The **Custom Images** page appears. All images are listed in tabular form.
    9. After the custom image you requested is created, it is listed here. Click it to view its details.
You can launch the custom image you created by clicking the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)) and selecting **Create Instance**. See [Instances](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/instance_management.htm#ComputeInstanceManagement "Describes how to perform compute instance management tasks, including creating, updating, and deleting instances, on your Roving Edge Infrastructure devices.") for more information on managing instances of a Roving Edge Infrastructure device.
  * Use the [oci compute image create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/create.html) command and required parameters to create a custom image from an existing compute instance on your Roving Edge Infrastructure devices:
```
oci compute image create --instance-id instance_ocid [OPTIONS]
```

where instance_ocid is the OCID of the instance from which you are creating the custom image.
Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [CreateImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/CreateImage) operation to create a custom image from an existing compute instance on your Roving Edge Infrastructure devices. Include the `instanceId` attribute which is the OCID of the instance you want to use as the basis for the image.


Was this article helpful?
YesNo


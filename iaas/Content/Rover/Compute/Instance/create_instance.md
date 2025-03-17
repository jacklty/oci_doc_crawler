Updated 2024-09-16
# Creating an Instance for a Roving Edge Infrastructure Device
Describes how to create a compute instance on your Roving Edge Infrastructure device.
You must have at least one VCN and one subnet created before creating an instance. Otherwise, an error message appears when you submit your instance for creation.
If you require more disk space on your VM, you can create and attach a block volume. See the following topics for more information:
  * [Creating a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/create_block_volume.htm#top "Describes how to create a block volume on your Roving Edge Infrastructure device.")
  * [Attaching a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/attach_volume-attachment.htm#top "Describes how to attach a block volume to a compute instance on your Roving Edge Infrastructure device.")


  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/create_instance.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/create_instance.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/create_instance.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. Click **Create Instance**. The **Create Compute Instance** dialog box appears.
    3. Complete the following:
       * **Name** : Enter a name for the instance.
       * **Image or operating system** : Click **Change Image**. The **Browse All Images** dialog box appears. Select one of the following image options:
         * **Platform Images** tab: Check the pre-built image you want for the instance from the list and click **Select Image**.
         * **Custom Images** tab: Click **Select Image**. The image you selected is displayed in the **Image or operating system** box.
       * **Shape** : Click **Change Shape**. The **Browse All Shapes** dialog box appears. Select a **Standard** or **Specialty** shape type, then select one of the corresponding shapes that appear. Click **Select Shape**. The shape you selected is displayed in the **Shape** box.
       * **Select a virtual cloud network** : Select a virtual cloud network from the list.
       * **Select a subnet** : Select a subnet associated with the virtual cloud network from the list.
       * **IP address** : Select an IP address option:
         * **Assign a public IP address** (if selected, an IP address from the external CIDR is used)
         * **Do not assign a public IP address**
       * **Specify a custom boot volume size** : Check if you do not want to use the default boot volume size. Enter the size in the **Boot volume size** box.
       * **SSH key** : Select an SSH key option:
         * **Choose SSH key file** : Click **browse to a location** and navigate to your SSH key file where you can select it for upload. You can also drag the file into the **SSH keys** box.
         * **Paste SSH keys** : Copy and paste the SSH key directly into the **SSH keys** box.
**Note**
If the original image had the user keys on it, the new keys might not be added to the resulting instance, depending on the image specifics.
    4. Click **Create**. Upon creation of the instance, the new instance's **Details** page opens automatically.
    5. Review the contents of the instance's **Details** page. It contains information such as its current state (indicated by the image in the upper left corner), IP addresses used, the image used, shape settings. You can view the boot volume, and attached VNICs by clicking their respective links in the lower left corner. Creation of the instance can take several minutes. During this time, the state is **Provisioning**. When the creation is complete, the state changes to **Running**. This state indicates that the instance is now launched.
**Note**
Your instance capacity is limited by the available cores and available memory. If you see "out of capacity" messages on instance creation, terminate some of the existing instances that are not used and try again. Stopped instances count toward the resources used. Terminate the instance to free up the resources.
  * Use the [oci compute instance launch](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html) command and required parameters to create a compute instance on your Roving Edge Infrastructure devices:
Copy
```
oci compute instance launch --compartment-id compartment_ocid --availability-domain orei-1-ad-1 --shape shape [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
To determine your Roving Edge Infrastructure device compartment OCID, see [Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/compartments.htm#comparments "Describes how the Roving Edge Infrastructure device uses its compartment, and how to gain information on it.").
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance) operation to create a compute instance on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo


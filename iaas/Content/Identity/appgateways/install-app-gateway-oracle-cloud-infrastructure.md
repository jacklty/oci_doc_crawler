Updated 2025-01-14
# Install App Gateway on OCI
To install App Gateway on OCI, you need to upload the App Gateway virtual disk image file to a **Bucket** in Oracle Cloud Infrastructure, create a **Custom Image** using the App Gateway virtual disk image file, and then create a **Compute** instance based on this custom image.
## Uploading the App Gateway VM disk image file to an object storage bucket in OCI 🔗 
Before creating a compute instance on OCI to run App Gateway, you need create a `Virtual Machine Disk Image` (`VMDK`) file using the App Gateway `Open Virtual Appliance` (`OVA`) file, and then upload this `VMDK` file to OCI.
  1. To create the `VMDK` file:
    1. Log in to the Windows server, and upload the App Gateway `OVA` file from your desktop to a working folder in the server. For example, `c:\temp`.
    2. Start the **Oracle VM Virtual Box Manager** software, and then select **Import Appliance** from the **File** menu.
    3. Locate the `OVA` file on the Windows server, and then select **Next**.
    4. In the **Import Virtual Appliance** window, update the **Name** field with the value `App Gateway Server`.
    5. To define a new MAC address to the App Gateway server network component, select **Reinitialize the MAC address of all network cards**.
    6. Select **Import**.
    7. Verify `App Gateway server` is listed in the **Oracle VM Virtual Box Manager**.
  2. To upload the `VMDK` file to OCI:
    1. Open the **navigation menu** and select **Storage**. Under **Object Storage & Archive Storage**, select **Buckets**.
    2. Select the compartment where the bucket is to upload the image. Select **Create Bucket** , then select **Create** in the Create Bucket dialog.
Contact your OCI administrator for more information about which compartment to create buckets.
    3. On the **Bucket Detail** page, select **Upload Object** in the **Objects** section.
    4. Select **select files** to browse and open the App Gateway's `VMDK` file, and then select **Upload Objects**.
    5. After the file uploads, select **Close**.
    6. Select the menu on the right for your object entry, and then record the **URL Path (URI)** value.


## Creating a Custom Image in OCI Based on the App Gateway VM disk Image File 🔗 
To create a compute instance on OCI to run App Gateway, you need to create a custom image from the App Gateway's `Virtual Machine Disk Image` (`VMDK`) file you uploaded to a bucket on OCI.
Ensure your OCI account has compartments, a virtual cloud network, and subnets previously set up.
Ensure you have selected a compartment in the IAM Console, before proceeding.
**Note** The components design must align with your OCI operational model. Contact your OCI administrator for more information.
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Custom Images**.
  2. Select the same compartment where you uploaded your VMDK file, and then select **Import Image**.
  3. In the **Import Image** dialog box, enter or select the following values, and then select **Import Image**.
     * **CREATE IN COMPARTMENT** : Select the compartment to import the image. The compartment must be the same where your compute instance is created.
     * **NAME** : `App Gateway Custom               Image`
     * **OPERATING SYSTEM** : Select **Linux**.
     * **OBJECT STORAGE URL** : Enter the URL path you recorded after you uploaded the VMDK file.
     * **IMAGE TYPE** : Select **VMDK**.
     * **LAUNCH MODE** : Select **EMULATED MODE**.
Wait until the custom image creation finishes.


## Creating a Compute Instance using App Gateway's Custom Image 🔗 
After you uploaded the App Gateway's `Virtual Machine Disk Image` (`VMDK`) file to a bucket in OCI and created a custom image using this `VMDK` file, you can create a compute instance to run App Gateway.
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Select **Create Instance**.
  3. In the **Create Compute Instance** page, enter `My App Gateway Server` in the **Name your instance** field, and then select **Change Image**.
  4. In the **Select an Image** dialog, select **My Images** , then select **Custom Images**. Select the appropriate compartment, select **App Gateway Custom Image** , and then select **Select Image**.
  5. In the **Add SSH Key** section, add a public SSH key, by either uploading a public key file or pasting the public key value in the **SSH Key** field.
See **Creating an SSH Key Pair Using PuTTY Key Generator** section in [ Managing Key Pairs on Linux Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingkeypairs.htm).
  6. In the **Configure networking** section, select a compartment in **Virtual cloud network compartment**.
If your compartment doesn't have virtual cloud network configured, then enter `App Gateway VCN` as **Name** in the **New virtual cloud network** section. If your compartment has virtual cloud network configured, then select the values for **Virtual cloud network** , **Subnet compartment** , and **Subnet** in which your compute instance will be created.
**Note** The component design must align with your OCI operational model. Contact your OCI administrator for more information.
  7. Select **Create** , and wait until your compute instance is provisioned and running.
  8. Record the value of the **Public IP Address** assigned to this compute instance.


Ensure that you have a **Security List** configured so that you can connect to the `My App Gateway Server` compute instance using a SSH client software such as `PuTTY`. Contact your OCI administrator for more information. 
Was this article helpful?
YesNo


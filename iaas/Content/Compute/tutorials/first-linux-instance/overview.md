Updated 2025-02-13
# Launching Your First Linux Instance
In this tutorial, perform the steps to create and connect to an OCI Compute instance. After your instance is up and running, optionally create and attach a block volume.
Key tasks:
  * Create a Compartment
  * Create a cloud network and subnet that enables internet access
  * Create an instance
  * Connect to the instance
  * (Optional) Create and attach a block volume
  * (Optional) Clean up after completing the tutorial


The following figure depicts the components you create in the tutorial.
[![Cloud resources to be created in the tutorial.](https://docs.oracle.com/en-us/iaas/Content/Compute/images/gsg-instance-linux.png)](https://docs.oracle.com/en-us/iaas/Content/Compute/images/gsg-instance-linux.png)
## Before You Begin
To successfully complete this tutorial, you must have the following: 

Requirements
    
  * An [Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/iaas/Content/FreeTier/freetier.htm) account or paid account.
  * A MacOS, Linux, or Windows computer with `ssh` installed. All current versions of each OS include `ssh` as a default.


## Authentication and Authorization
Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).
An administrator in an organization needs to set up **groups** , **compartments** , and **policies** that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see [Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm). 
If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.
## 1. Create a Compartment 🔗 
Compartments help you organize and control access to resources. A compartment is a collection of related resources (such as cloud networks, Compute instances, or block volumes). Only users in groups given permission by an administrator in your organization, have access to specific compartments. For example, one compartment could contain all the servers and storage volumes that make up the production version of a company's Human Resources system. Only users with permission to that compartment can manage those servers and volumes.
[Steps to Create a Compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-linux-instance/overview.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Compartments**. 
  2. Click **Create Compartment**. 
  3. Enter the following:
     * **Name:** Enter `<your-compartment-name>`
     * **Description** : Enter a description (required), for example: "`<your-compartment-name>` compartment for the getting started tutorial". Avoid entering confidential information.
     * **Parent Compartment:** Select the compartment you want this compartment to reside in. Defaults to the root compartment (or tenancy).
  4. Click **Create Compartment**.
Your compartment is displayed in the list.


When you select your compartment, you only see resources in that compartment. When you create new resources you select the compartment to create them in. The compartment control defaults to the last compartment selected.
## 2. Create a Virtual Cloud Network 🔗 
Before you can launch an instance, create a virtual cloud network (VCN) and subnet to launch the instance into. A subnet is a subdivision of your VCN defined using a range of IP addresses with public or private access. The subnet directs traffic according to a **route table**. In addition, a subnet's security list controls traffic in and out of the instance. For this tutorial, access the instance over the internet using the instance's public IP address. The route table directs traffic to an internet gateway.
For information about VCN features, see [Networking Overview](https://docs.oracle.com/iaas/Content/Network/Concepts/overview.htm).
Use the **Start VCN Wizard** workflow to create a new Virtual Cloud Network (VCN). The workflow does several things when installing the VCN: 
  * Creates a VCN.
  * Adds an **Internet Gateway** which enables internet connections.
  * Creates and configures public and private subnets for the VCN.
  * Sets up route tables and security lists for the subnets.


For more information on VCNs, see: [VCN and Subnet Management](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm).
[Steps to Create a VCN](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-linux-instance/overview.htm)
To create a VCN, follow these steps:
**Important** The steps provided are for a Free Tier account. If you are using a paid account, the steps might differ from those shown here.
  1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
  2. If needed, select the compartment you created in the preceding step from the compartments list in the left navigation.
  3. Click **Start VCN Wizard**.
  4. Select **Create VCN with Internet Connectivity**.
  5. Click **Start VCN Wizard**.
  6. Configure the VCN. The configure dialog contains the following sections. 
**Basic Information**
Enter the VCN **Name** and select a **Compartment**.
     * **Name:** `<name-for-the-vcn>`
Enter a name for your VCN. Avoid entering confidential information.
     * **Compartment:** `<your-compartment-name>`
Select your compartment.
**Configure VCN**
     * Keep the default values for **VCN IPv4 CIDR block** and **DNS resolution**.
**Configure public subnet**
     * Keep the default values for **IP address type** and **IPv4 CIDR block**.
**Configure private subnet**
     * Keep the default values for **IP address type** and **IPv4 CIDR block**.
  7. Click **Next**.
  8. Review you selections. Click **Previous** to go back and make changes.
  9. Click **Create** to create the VCN. 
The system creates the VCN and all its resources. This might take a moment.
After the creation is complete, click **View VCN** to see your new VCN.


## 3. Create a Virtual Machine Instance 🔗 
Next, launch an instance with an Oracle Linux image and basic shape. Use the **Create a VM Instance** workflow to create a new compute instance. The workflow does several things when installing the instance:
  * Creates and installs a compute instance running Oracle Linux.
  * Selects your VCN and public subnet to connect the Oracle Linux instance to the internet.
  * Creates an `ssh` key pair you use to connect to the instance.


[Steps to Create a Virtual Machine Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-linux-instance/overview.htm)
To get started installing an instance with the **Create a VM instance** workflow, follow these steps:
**Important** The steps provided are for a Free Tier account. If you are using a paid account, the steps might differ from those shown here.
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**. 
  2. Click **Create Instance**. 
The **Create compute instance** page is displayed.
  3. Choose the **Name** and **Compartment**. 
**Initial Options**
     * **Name:** `<name-for-the-instance>`
Enter a name for your instance. Avoid entering confidential information.
     * **Create in compartment:** `<your-compartment-name>`
Select your compartment. Use the compartment created in the preceding step.
  4. Review the **Placement** settings. 
     * Take the default values. An availability domain is assigned to you.
The default values are similar to the following:
     * **Availability domain:** AD-1
     * **Capacity type:** On-demand capacity
     * **Fault domain:** Let Oracle choose the best fault domain
**Note** For Free Tier, use the **Always Free Eligible** option for availability domain.
  5. Review the **Security** settings. 
     * Take the default settings.
The default values are similar to the following:
     * **Shielded instance:** Disabled
     * **Confidential computing:** Disabled
  6. Review the **Image and shape** settings. Click **Edit**. 
**Note** The following is sample data for an Ampere A1 virtual machine. The actual values might differ.
     * Keep the default **Oracle Linux 8** image.
     * Click **Change shape**.
     * Select **Virtual Machine**.
     * For shape series select **Ampere**.
     * Select **VM.Standard.A1.Flex** the "Always Free" shape.
     * Select 1 OCPUs.
     * Click **Select Shape**.
Selected values are similar to the following:
     * **Image:** Oracle Linux 8
     * **Image build:** `<current-build-date>`
     * **Shape:** VM.Standard.A1.Flex
     * **OCPU:** 1
     * **Memory (GB):** 6
     * **Network bandwidth (Gbps):** 1
**Note** For Free Tier, use **Always Free Eligible** shape options.
  7. Review the **Networking** settings. Select the VCN you created in the preceding step. The networking values are similar to the following: 
     * **Virtual cloud network:** <your-vcn>
     * **Subnet:** <pubic-subnet-for-your-vcn>
     * **Launch options:** -
     * **DNS record:** Yes
     * **Use network security groups to control traffic:** No
     * **Assign a public IPv4 address:** Yes
     * **Private IPv4 address:** Automatically assigned on creation
     * **IPv6 address:** Not available
  8. Review the **Add SSH keys** settings. Take the default values provided by the workflow. 
     * Select the **Generate a key pair for me** option.
     * Click **Save Private Key** and **Save Public Key** to save the private and public SSH keys for this compute instance.
To use your own SSH keys, select one of the options to provide your public key. To generate your own key pairs see: [Managing Key Pairs on Linux Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingkeypairs.htm).
**Note** Put your private and public key files in a safe location. You can't retrieve keys again after the compute instance has been created.
**Important** To use a key pair that is generated by OCI, access the instance from a system with OpenSSH installed. OpenSSH is included by default on all current versions of Linux, MacOS, Windows, and Windows Server. For more information, see [Managing Key Pairs on Linux Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingkeypairs.htm).
  9. Review the **Boot volume** settings. 
Select the **Use in-transit encryption** setting. Leave the other two settings blank.
  10. Review the **Block Volume** settings. Take the default values provided by the workflow which does not select any block volumes. You can add block volumes later. 
  11. Click **Create** to create the instance.


The instance is displayed in the Console in a provisioning state. Expect provisioning to take several minutes before the state updates to running. Do not refresh the page. After the instance is running, allow another few minutes for the operating system to boot before you attempt to connect.
## 4. Connect to Your Instance 🔗 
Connect to your Linux instance using a Secure Shell (SSH) connection. Current versions of Linux, MacOS, Windows, and Windows Server include an OpenSSH client by default. (For Windows, see: [OpenSSH client](https://docs.microsoft.com/windows-server/administration/openssh/openssh_install_firstuse).) Use the SSH keys you generated when you created your instance.
Log in to your instance using the instructions for the operating system you're connecting from.
[Connect to a Linux Instance from a Windows System Using OpenSSH](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-linux-instance/overview.htm)
Using the OCI generated key pair or your own generated key pair used to create the instance, connect to the Linux instance. 

Set the Permissions for the Private Key File
    
Set the file permissions for the private key file so that only the current user has read-only access. Do the following:
  1. Locate the SSH key files you created by or created for your instance.
  2. In Windows Explorer, navigate to the private key file, right-click the file.
  3. Select **Properties**.
  4. On the **Security** tab, select **Advanced**.
  5. On the **Permissions** tab, for **Permission entries** , under **Principal** , ensure that your user account is listed.
  6. Select **Disable Inheritance** , and then select **Convert inherited permissions into explicit permissions on this object**.
  7. For **Permission entries** , select each permission entry that isn't your user account and select **Remove**.
  8. Ensure that the access permission for your user account is **Full control**.
  9. Save your changes.



Connect to the Instance with PowerShell
    
Next, connect to the instance with PowerShell.
  1. Open Windows PowerShell and run the following command:
Copy
```
ssh -i <private_key_file> <username>@<public-ip-address>
```

<private_key_file> is the full path and name of the `.key` file that contains the private key associated with the instance you want to access.
<username> is the default username for the instance. For Oracle Linux and Redhat Enterprise Linux compatible images, the default username is `opc`. For Ubuntu images, the default username is `ubuntu`.
<public-ip-address> is the instance's IP address that you retrieved from the Console.
  2. If you're connecting to this instance for the first time, you need to accept the fingerprint of the key. To accept the fingerprint, type **yes** and press **Enter**.
  3. You are connected to the default shell for the instance.
  4. When you have finished your session, type `exit` at the shell prompt to end the session.


[Connect to a Linux Instance from a Unix-Style System](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-linux-instance/overview.htm)
Use the OCI generated key pair or the key pair used to create the instance. Then use the following steps to connect to an OCI Linux instance.
  1. Open a terminal.
  2. Locate the private key file for your key pair. The default directory location for SSH keys is `<your-home-directory>/.ssh`.
  3. Use the following command to set the file permissions so that only you can read the file:
Set the file permissions for the private key file so that only the current user has read-only access:
Copy
```
chmod 400 <private_key_file>
```

<private_key_file> is the full path and name of the file that contains the private key associated with the instance you want to access.
  4. Use the following SSH command to access the instance.
Copy
```
ssh -i <private_key_file> <username>@<public-ip-address>
```

<private_key_file> is the full path and name of the file that contains the private key associated with the instance you want to access.
<username> is the default username for the instance. For Oracle Linux and Redhat Enterprise Linux compatible images, the default username is `opc`. For Ubuntu images, the default username is `ubuntu`.
<public-ip-address> is the instance's IP address that you retrieved from the Console.
  5. If you're connecting to this instance for the first time, you need to accept the fingerprint of the key. To accept the fingerprint, type **yes** and press **Enter**.
  6. You are connected to the default shell for the instance.
  7. When you have finished your session, type `exit` at the shell prompt to end the session.


**Tip** If you're using an older version of the Windows operating system, you can use PuTTY to create keys and connect to a Linux instance. For details on connecting to a Linux instance with PuTTY, see [Connecting to a Linux Instance from a Windows System Using PuTTY](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance-from-windows-putty.htm#linux-from-windows-putty__connect-to-linux-from-windows-putty).
**Note** Windows now supports [Windows Subsystem for Linux](https://msdn.microsoft.com/commandline/wsl/about) (WSL). With WSL, you can install a free version of Linux, like Oracle Linux or Ubuntu, on your Windows system. Then from WSL, the steps to connect with SSH are the same as a regular Linux system. See: [Connecting to a Linux Instance from a MacOS or Linux System](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm#linux-from-unix).
## 5. (Optional) Add a Block Volume 🔗 
Block Volume provides network storage to use with your Oracle Cloud Infrastructure instances. After you create, attach, and mount a volume to your instance, you can use it just as you would a physical hard drive on your computer. A volume can be attached to a single instance, but you can detach the volume from one instance and attach it to another instance, keeping your data intact.
For complete details on Block Volume, see [Overview of Block Volume](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm). 
[Create a Volume](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-linux-instance/overview.htm)
  1. Open the **navigation menu** and select **Storage**. Under **Block Storage** , select **Block Volumes**.
  2. Click **Create Block Volume**.
  3. In the **Create Block Volume** dialog, enter the following:
     * **Name:** Enter a user-friendly name. Avoid entering confidential information.
     * **Create in Compartment:** This field defaults to your current compartment. Select the compartment you want to create the volume in, if not already selected. 
     * **Availability domain:** Select the same **availability domain** that you selected for your instance. If you followed the tutorial instructions when launching your instance, this is the first AD in the list. The volume and the instance must be in the same availability domain.
     * **Cluster Placement Group** : Keep default of `**none**`. (This option may not appear depending on the account type.)
     * **Volume size and performance**
       * Select **Default**. This selects the following defaults: 
         * **Volume size** : 50GB
         * **Volume performance** : Balanced
         * **IOPS** : 3,000 IOPS (60 IOPS/GB)
         * **Throughput** : 24 MB/s (480 KB/s/GB)
**Important** The values listed are for a Free Tier account. The defaults might change for a paid account.
**Note** Select the **Custom** option, to change the size and performance options.
     * **Backup Policy:** Do not select a backup policy.
     * **Cross region replication** : Select **OFF**.
     * **Volume Encryption** : Select **Encrypt using Oracle-managed keys**.
     * **Tags:** Leave the tagging fields blank.
     * Leave **View detail page after this block volume is created** checked.
  4. Click **Create Block Volume**.


The block volume provisioning starts. After the volume is provisioned, you can attach it to your instance.
[Attach the Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-linux-instance/overview.htm)
Next, attach the volume to your instance:
  1. Find your instance: Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click your instance name to view its details.
  3. In the **Resources** section, click **Attach block volumes**.
  4. Click **Attach block volume**.
  5. Enter the following:
     * **Volume:** select the **Select volume** option.
     * If you need to change the compartment, click **Change Compartment** , and then select the compartment where you created the block volume.
     * **Volume in <compartment>:** Select the block volume from the list.
     * **Attachment type:**
       * Select **Recommended**. 
This selects **Paravirtualized**.
       * Leave **Use in-transit encryption** unchecked.
**Note** The **Custom** option allows you select iSCSI or NVMe attachment types.
     * **Access:** Select **Read/Write**.
  6. Click **Attach**.


The attachment process takes about a minute. You'll know the volume is ready when the **Attachment State** for the volume is ATTACHED.
[Connect to the Volume](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-linux-instance/overview.htm)
For volumes attached with Paravirtualized as the attachment type, you don't need to perform any additional steps after attaching the volumes. The volume is connected automatically.
To verify your volume is connected:
  1. Log on to your instance as described in [4. Connect to Your Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-linux-instance/overview.htm#connect-to-vm-instance). 
  2. You are ready to format and mount the volume. To get a list of mountable devices on the instance, run the following command:```
sudo fdisk -l
```

If your disk attached successfully, you'll see the volume listed in the returned list with data similar to the following:
```
Disk /dev/sdb: 50.0 GB, 50010783744 bytes, 97677312 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 4096 bytes / 1048576 bytes
```

**Important** **Connecting to Volumes on Linux Instances**
When connecting to volumes on Linux instances, to automatically mount these volumes on instance boot, you need to use some specific options in the `/etc/fstab` file, or the instance can fail to launch. See [Traditional fstab Options](https://docs.oracle.com/iaas/Content/Block/References/fstaboptions.htm) and [fstab Options for Block Volumes Using Consistent Device Paths](https://docs.oracle.com/iaas/Content/Block/References/fstaboptionsconsistentdevicepaths.htm) for more information.


## 6. (Optional) Clean up Resources 🔗 
After you've finished with the resources that you created for this tutorial, clean up by terminating the instance and deleting the resources that you don't intend to continue working with.
[Detach and Delete the Block Volume](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-linux-instance/overview.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Find your instance in the **Instances** list and click its name to display its details. 
  3. In the **Resources** section on the **Instance Details** page, click **Attached Block Volumes**.
  4. Find your volume, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Detach**.
  5. Click **Continue Detachment** and then click **OK**.
  6. When the Console shows the volume status as Detached, you can delete the volume. Open the **navigation menu** and select **Storage**. Under **Block Storage** , select **Block Volumes**.
  7. Find your volume, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Terminate**. Confirm when prompted.


[Terminate the Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-linux-instance/overview.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. In the list of instances, find the instance you created in the tutorial.
  3. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Terminate**.
  4. Select the **Permanently delete the attached boot volume** check box, and then click **Terminate instance**.


[Delete the Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-linux-instance/overview.htm)
  1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
  2. In the list of VCNs, find the one you created in the tutorial.
  3. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Terminate**.
  4. Click **Terminate All** to delete all the underlying resources of your VCN.
When all the resources are successfully deleted you can close the dialog.


## What's Next 🔗 
Now that you've got a Compute instance running and attached some storage, consider the following next steps:
  * Install your own software on the instance.
  * Add more users to work with Oracle Cloud Infrastructure. See [Adding Users to an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/addingusers.htm#Adding_Users_on_an_Instance).


Was this article helpful?
YesNo


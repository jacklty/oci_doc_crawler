Updated 2025-01-13
# Creating an Instance from an Instance Configuration
You can create an instance by using an instance configuration as a template.
Many of the settings that are defined in the instance configuration cannot be changed when you create an instance from the instance configuration. For example, the availability domain, compartment, image, shape, and subnet cannot be changed.
## Before You Begin 🔗 
Before you create an instance from an instance configuration, you need an [instance configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstanceconfig.htm#Creating_an_Instance_Configuration) to use as a template for the instance. In addition, there are specific requirements for Linux and Windows.
### Linux Instance Requirements
To connect to your Linux instance, consider the following.
  * If the instance configuration does not include a public key, and you want to use your own Secure Shell (SSH) key to connect to the instance using SSH, you need the public key from the SSH key pair that you plan to use. The key must be in OpenSSH format. For more information, see [Managing Key Pairs on Linux Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingkeypairs.htm#Managing_Key_Pairs_on_Linux_Instances).
  * If the instance configuration does include an SSH key, that SSH key must be used to connect to all instances created from the instance configuration.


### Windows Instance Requirements
For Windows, you need a VCN security rule that enables Remote Desktop Protocol (RDP) access so that you can connect to your instance. Specifically, you need a stateful ingress rule for TCP traffic on destination port 3389 from source 0.0.0.0/0 and any source port. For more information, see [Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). You can implement this security rule in a network security group that you add this Windows instance to. Or, you can implement this security rule in a security list that is used by the instance's subnet.
[To enable RDP access:](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-instance-from-instance-configuration.htm)
  1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**. 
  2. Under **List Scope** , select a compartment that you have permission to work in. The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator.
  3. Click the VCN you want to create the security rule in.
  4. Do one of the following:
     * Add the rule to a network security group that the instance belongs to:
       1. Under **Resources** , click **Network Security Groups**. 
       2. Click the network security group to add the rule to.
       3. Click **Add Rules**.
       4. Enter the following values for the rule:
          * **Stateless:** Leave the check box cleared.
          * **Direction:** Ingress
          * **Source Type:** CIDR
          * **Source CIDR:** 0.0.0.0/0
          * **IP Protocol:** RDP (TCP/3389)
          * **Source Port Range:** All
          * **Destination Port Range:** 3389
          * **Description:** An optional description of the rule.
       5. Click **Add**.
     * To add the rule to a security list that is used by the instance's subnet:
       1. Under **Resources** , click **Security Lists**.
       2. Click the security list that you're interested in.
       3. Click **Add Ingress Rules**.
       4. Enter the following values for the rule:
          * **Stateless:** Leave the check box cleared.
          * **Source Type:** CIDR
          * **Source CIDR:** 0.0.0.0/0
          * **IP Protocol:** RDP (TCP/3389)
          * **Source Port Range:** All
          * **Destination Port Range:** 3389
          * **Description:** An optional description of the rule.
       5. Click **Add Ingress Rules**.


## Using the Console 🔗 
  1. Open the navigation menu and click **Compute**. Under **Compute** , click **Instance Configurations**.
  2. Click the instance configuration that you want to use as a template to create the instance.
  3. Click **Launch instance**.
  4. Enter a name for the instance. You can add or change the name later. The name doesn't need to be unique, because an Oracle Cloud Identifier (OCID) uniquely identifies the instance. Avoid entering confidential information.
  5. For **Placement** , **Image and shape** , and **Networking** , you can change some advanced options, including the [capacity type](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/capacity-types.htm#capacity_types), [fault domain](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bestpracticescompute.htm#Fault), [shielding options](https://docs.oracle.com/en-us/iaas/Content/Compute/References/shielded-instances.htm#shielded), and [launch options](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/recommended-networking-launch-types.htm#top "When you create a VM instance, by default, Oracle Cloud Infrastructure chooses a recommended networking type for the VNIC based on the instance shape and OS image. The networking interface handles functions such as disk input/output and network communication."). For more information about the settings in these sections, see [Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service.").
  6. **Linux instances:** If the instance configuration does not include an SSH public key for the instance, you can provide one now. If the instance configuration does include an SSH public key for the instance, that SSH key must be used to connect to all instances created from the instance configuration.
In the **Add SSH keys** section, generate an SSH key pair or upload your own public key. Select one of the following options:
     * **Generate a key pair for me:** Oracle Cloud Infrastructure generates an RSA key pair for the instance. Select **Save Private Key** , and then save the private key on your computer. Optionally, select **Save Public Key** and then save the public key.
**Caution** Anyone who has access to the private key can connect to the instance. Store the private key in a secure location.
**Important** To use a key pair that is generated by OCI, access the instance from a system with OpenSSH installed. OpenSSH is included by default on all current versions of Linux, MacOS, Windows, and Windows Server. For more information, see [Managing Key Pairs on Linux Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingkeypairs.htm).
     * **Upload public key files (.pub):** Upload the public key portion of your key pair. Either browse to the key file that you want to upload, or drag and drop the file into the box. To provide multiple keys, press and hold down the Command key (on Mac) or the Ctrl key (on Windows) while selecting files. 
     * **Paste public keys:** Paste the public key portion of your key pair in the box. 
     * **No SSH keys:** Select this option only if you do not want to connect to the instance using SSH. You can't provide a public key or save the key pair that is generated by Oracle Cloud Infrastructure after the instance is created. 
  7. Specify the **Boot volume** details for the instance. For more information about the settings in this section, see [Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service.").
  8. To configure live migration, click **Show advanced options** , and on the **Availability configuration** tab, make your selections. For more information about the settings in this section, see [Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service.").
  9. Click **Create**.
To track the progress of the operation and [troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances-monitoring-work-requests.htm#work-requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") that occur during instance creation, use the associated [work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).


## What's Next 🔗 
  * After the instance is provisioned, details about it appear in the instance list. To view more details, including IP addresses and the initial password (for Windows instances), click the instance name.
  * When the instance is fully provisioned and running, you can connect to the instance. You [connect to a Linux instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm#top "You can connect to a running Linux instance by using a Secure Shell \(SSH\) connection.") by using a Secure Shell (SSH) connection, and you [connect to a Windows instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm#top "You connect to a Windows instance by using a Remote Desktop connection. Most Windows systems include a Remote Desktop client by default.") by using a Remote Desktop connection.
  * You can attach a [block volume](https://docs.oracle.com/iaas/Content/Block/Concepts/overview.htm) to the instance, provided the volume is in the same availability domain.
  * You can [let additional users connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/addingusers.htm#Adding_Users_on_an_Instance).


Was this article helpful?
YesNo


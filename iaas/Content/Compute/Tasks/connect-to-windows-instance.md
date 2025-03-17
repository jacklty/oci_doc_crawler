Updated 2025-01-13
# Connecting to a Windows Instance
You connect to a Windows instance by using a Remote Desktop connection. Most Windows systems include a Remote Desktop client by default.
For permissions, see [Required IAM Policy for Working with Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#permissions).
## Before You Begin 🔗 
You must have the following information to connect to a Windows instance:
  * **Public IP address for an instance:** Use the public IP address assigned when you created the instance. If you didn't note the address, get the address from the Instance Details page: 
    * Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    * Select your instance.
    * Look at the **Instance access** section. If a public IP address is assigned, the address will be labeled: **Public access IP address**.
    * If no public IP address is assigned, see [Assigning an Ephemeral Public IP to an Existing Primary Private IP](https://docs.oracle.com/iaas/Content/Network/Tasks/assigning-ephemeral-public-existing-private-ip.htm#top).
  * **Username:** The username used to connect to the Windows instance. If you used a Windows platform image to create the instance, the username is `opc`.
  * **Initial password:** If you are connecting to the instance for the first time, then you must have the initial password for the instance. You can [get the initial password](https://docs.oracle.com/iaas/Content/GSG/Tasks/launchinginstanceWindows.htm#Getting) from the Instance Details page in the Console.


**Enable RDP access:** To use Remote Desktop Protocol (RDP) to access a Windows instance, you need to add a stateful ingress [security rule](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm) for TCP traffic on destination port 3389 from source 0.0.0.0/0 and any source port. You can implement this security rule in either a [network security group](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm) that the Windows instance belongs to, or a [security list](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm) that is used by the instance's subnet.
  * Option 1 - Add a rule to a network security group:
    1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**. 
    2. Click the instance that you're interested in.
    3. Under **Instance details** , for **Virtual cloud network** , click the name of the cloud network.
    4. Add the rule to a network security group that the instance belongs to:
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
    5. Return to the **Instance details** page: Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**. Click the instance.
    6. In the **Primary VNIC** section, for **Network security groups** , click **Edit**.
    7. In the **Network security group** list, select the network security group that you edited. Then click **Save changes**.
  * Option 2 - Add a rule to a security list used by the instance's subnet:
    1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Click the instance that you're interested in.
    3. In the **Primary VNIC** section, for **Subnet** , click the name of the subnet. The **Subnet Details** page opens.
    4. To add the rule to a security list that is used by the instance's subnet:
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


## Connecting to a Windows Instance from a Remote Desktop Client 🔗 
Ensure that the instance meets the criteria for connecting to a Windows instance listed in the [Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm#prerequisites) section before performing the following steps.
  1. Open the Remote Desktop client.
  2. In the **Computer** field, enter the public IP address of the instance. You can [get the instance's public IP address](https://docs.oracle.com/iaas/Content/GSG/Tasks/launchinginstanceWindows.htm#Getting) from the Console.
  3. The **User name** is `opc`. Depending on the Remote Desktop client you are using, you might have to connect to the instance before you can enter this credential.
  4. Click **Connect** to start the session.
  5. Accept the certificate if you are prompted to do so. 
  6. If you are connecting to the instance for the first time, enter the initial password that was provided to you by Oracle Cloud Infrastructure when you created the instance. You can [get the instance's initial password](https://docs.oracle.com/iaas/Content/GSG/Tasks/launchinginstanceWindows.htm#Getting) from the Console. You will be prompted to change the password as soon as you log in. Your new password must be at least 12 characters long and must comply with [Microsoft's password policy](https://technet.microsoft.com/library/hh994562\(v=ws.11\).aspx?f=255&MSPPError=-2147217396).
Otherwise, enter the password that you created. If you are using a custom image, you might need to know the password for the instance that the image was created from. For details about Windows custom images, see [Creating Windows Custom Images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/windowsimages.htm#Creating_Windows_Custom_Images).
  7. Press **Enter**.


**Note** If you fail to connect to the Windows instance, try rebooting the instance as detailed in [Stopping, Starting, or Restarting an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm#top "You can stop, start, or restart an instance as needed to update software or resolve error conditions.").
## Connecting to a Windows Instance Using PowerShell 🔗 
You can connect to a Windows instance from within PowerShell and open the authentication window directly with no RDP client configuration required.
Ensure that the instance meets the criteria for connecting to a Windows instance listed in the [Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm#prerequisites) section before performing the following steps.
  1. Open a PowerShell terminal.
  2. At the command prompt, type `Start-Process mstsc /v:<Windows_instance_IP_address>`.
  3. Press Enter to display the authentication window.


**Note** If you fail to connect to the Windows instance, try rebooting the instance as detailed in [Stopping, Starting, or Restarting an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm#top "You can stop, start, or restart an instance as needed to update software or resolve error conditions.").
Was this article helpful?
YesNo


Updated 2025-01-13
# Connecting to a Linux Instance
You can connect to a running Linux instance by using a Secure Shell (SSH) connection.
**Important** Alternatively, for advanced control of the boot process or OS troubleshooting, you can use the serial console to connect to an instance. For details, see 
  * [Making a Local Connection to the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Compute/References/serialconsole.htm#Connecti2)
  * [Using Cloud Shell to Connect to the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Compute/References/serialconsole.htm#cloud-shell)


## Connecting to a Linux Instance with SSH 🔗 
Current versions of Windows, MacOS, and Linux include an OpenSSH client by default. (Windows has included the [OpenSSH client](https://docs.microsoft.com/windows-server/administration/openssh/openssh_install_firstuse) since Windows 10 and Windows Server 2019.) When you create an instance, OCI Compute generates OpenSSH keys for you. You download the keys and use them to connect to your instance.
**Important** **SSH keys required:** To connect to your instance with SSH, you must have SSH keys. 
  * If you lost your SSH keys, terminate the instance and create a new instance using the SSH keys provided or SSH keys you generated. See [Managing Key Pairs on Linux Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingkeypairs.htm#Managing_Key_Pairs_on_Linux_Instances).
  * If you created an instance without SSH keys, you can use the [serial console](https://docs.oracle.com/en-us/iaas/Content/Compute/References/serialconsole.htm#Instance_Console_Connections) to connect to your instance and configure SSH. For Oracle Linux, see this [example on how to reset the SSH key for the `opc` user](https://docs.oracle.com/en-us/iaas/Content/Compute/References/serialconsole.htm#instcon_linux_trouble__resetsshkey) using the serial console.


For SSH troubleshooting suggestions, see [Troubleshooting the SSH Connection](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/troubleshooting-ssh-connection.htm#troubleshooting-ssh-connection "If you're unable to connect to a compute instance using SSH, review the following troubleshooting error messages and suggestions to resolve the issue.").
**Note** For older Windows versions, you can also use the free PuTTY SSH client. See: [Connecting to a Linux Instance using PuTTY and Windows](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance-from-windows-putty.htm#linux-from-windows-putty "PuTTY is a free implementation of SSH and Telnet for Windows. The program includes an xterm terminal emulator. PuTTY generates its own public and private SSH keys but can interoperate with OpenSSH keys.").
## Before You Begin 🔗 
You must have the following information to connect to a Linux instance:
  * **Public IP address for an instance:** Use the public IP address assigned when you created the instance. If you didn't note the address, get the address from the Instance Details page: 
    * Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    * Select your instance.
    * Look at the **Instance access** section. If a public IP address is assigned, the address will be labeled: **Public access IP address**.
    * If no public IP address is assigned, see [Assigning an Ephemeral Public IP to an Existing Primary Private IP](https://docs.oracle.com/iaas/Content/Network/Tasks/assigning-ephemeral-public-existing-private-ip.htm#top).
  * **Username:** The username used to connect to the Linux instance. Default users names are assigned based on the Linux distribution used. 
    * For Oracle Linux or Redhat Enterprise Linux compatible platform images the username is `opc`.
    * For Ubuntu platform images to create the instance, the username is `ubuntu`.
  * **SSH private key:** The full path to the private key file from the SSH key pair used to create the instance. For more information about key pairs, see [Managing Key Pairs on Linux Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingkeypairs.htm#Managing_Key_Pairs_on_Linux_Instances). 


## Connecting to a Linux Instance from a Windows System Using OpenSSH 🔗 
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


**Note** For SSH troubleshooting suggestions, see [Troubleshooting the SSH Connection](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/troubleshooting-ssh-connection.htm#troubleshooting-ssh-connection "If you're unable to connect to a compute instance using SSH, review the following troubleshooting error messages and suggestions to resolve the issue.").
**Tip** If you are using an older version of the Windows operating system, you can use PuTTY to create keys and connect to a Linux instance. For details on connecting to a Linux instance with PuTTY, see [Connecting to a Linux Instance from a Windows System Using PuTTY](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance-from-windows-putty.htm#linux-from-windows-putty__connect-to-linux-from-windows-putty).
**Note** Windows now supports [Windows Subsystem for Linux](https://msdn.microsoft.com/commandline/wsl/about) (WSL). With WSL, you can install a free version of Linux, like Oracle Linux or Ubuntu, on your Windows system. Then from WSL, the steps to connect with SSH are the same as a regular Linux system. See: [Connecting to a Linux Instance from a MacOS or Linux System](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm#linux-from-unix).
## Connecting to a Linux Instance from a MacOS or Linux System 🔗 
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


**Note** For SSH troubleshooting suggestions, see [Troubleshooting the SSH Connection](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/troubleshooting-ssh-connection.htm#troubleshooting-ssh-connection "If you're unable to connect to a compute instance using SSH, review the following troubleshooting error messages and suggestions to resolve the issue.").
**Note** **Connecting from macOS Ventura using OpenSSH 9.0:** If you connect to an instance from a client running macOS Ventura (version 13) or a client running OpenSSH 9.0, you might encounter a connection issue. For more information and a workaround, see the known issue [SSH connection issues with macOS Ventura using OpenSSH 9.0](https://docs.oracle.com/en-us/iaas/Content/Compute/known-issues.htm#ssh_connection_issues_with_macos_ventura_using_openssh).
Was this article helpful?
YesNo


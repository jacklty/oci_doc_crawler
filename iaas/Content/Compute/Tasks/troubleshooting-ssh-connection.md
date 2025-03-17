Updated 2025-02-03
# Troubleshooting the SSH Connection
If you're unable to connect to a compute instance using SSH, review the following troubleshooting error messages and suggestions to resolve the issue.
**Tip** If this is your first time creating an instance, for a guided tutorial consider one the following: 
  * [Launching Your First Linux Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-linux-instance/overview.htm "In this tutorial, perform the steps to create and connect to an OCI Compute instance. After your instance is up and running, optionally create and attach a block volume.")
  * [Free Tier: Install Apache and PHP on an Oracle Linux Instance](https://docs.oracle.com/iaas/developer-tutorials/tutorials/apache-on-oracle-linux/01-summary.htm)


**Tip** If this is your first time creating an instance, we recommend creating a Virtual Cloud Network (VCN) first. You can use the "Start VCN Wizard" workflow and select the "Create VCN with Internet Connectivity" option. The workflow creates a VCN which automatically configures both a public and a private subnet along with any required gateways and route rules. In addition, the workflow provides an option to configure IPv6. For details on running the workflow see: [Virtual Networking Quickstart](https://docs.oracle.com/iaas/Content/Network/Tasks/quickstartnetworking.htm).
## SSH Error: connect to host w.x.y.z port 22: Operation timed out 🔗 
The error means SSH can't connect to the host at the IP address specified. Check the following scenarios to resolve the issue.
## Ensure the System has Internet Access 🔗  

Ensure the Environment the SSH command is executing and has Internet Access
    
  * **Windows:** Open a command prompt window.
  * **MacOS/Linux:** Open a terminal window.
  * Ping a well known host like google.com or amazon.com. 
  * If the ping command is successful, continue to the next option.



Ping Failed
    
Your SSH environment might not have access to the internet. If you unsure about your organizations firewall settings for internet access, consider using OCI Cloud Shell to SSH to the instance. See the [OCI Cloud Shell Section](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/troubleshooting-ssh-connection.htm#troubleshooting-ssh-connection__ssh-trouble-using-cloud-shell) on this page for details. 

Proxy Servers
    If your organization uses proxy servers to connect to the internet, make sure your proxy settings are correct. Please consult your organizations proxy documentation as the settings can vary depending upon the proxy configuration and the operating system used.
## Check the OCI Settings 🔗 
Next, check the OCI settings to verify your configuration. 

Open the Instance Details
    
  * [Log into the OCI Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm).
  * Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  * Select the instance you are interested in. The instance details page is displayed.



Check the following Settings
    
  * Ensure the instance is running and is not stopped.
  * Ensure the instance has a public IP address.
    * Look at the **Instance access** section. If a public IP address is assigned, the address will be labeled: **Public access IP address:**
    * If the **Instance Access** section is empty, then no public IP address is assigned.
  * If you have a public address, ensure you are using the correct IP address in your SSH command.
  * If you don't have a public IP address, check your VCN subnet.
    * If you're on a private subnet, you can't connect to your instance from the Internet. See the [Using a Private Subnet](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/troubleshooting-ssh-connection.htm#troubleshooting-ssh-connection__ssh-trouble-private-subnet) section.
  * If you created an instance on a public subnet, but didn't assign a public IP address at instance creation, you can still assign the address, see: [Assigning an Ephemeral Public IP to an Existing Primary Private IP](https://docs.oracle.com/iaas/Content/Network/Tasks/assigning-ephemeral-public-existing-private-ip.htm#top).
    * After setting the IP address, restart the instance and try using SSH to connect to your instance.


## The Instance has a Public IP Address on a Public Subnet and I still Can't Connect 🔗 
If you are new to OCI, the following troubleshooting steps are more advanced. To speed things up, consider setting up a new VCN and a new Compute instance as described in the following tips.
**Tip** If this is your first time creating an instance, for a guided tutorial consider one the following: 
  * [Launching Your First Linux Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-linux-instance/overview.htm "In this tutorial, perform the steps to create and connect to an OCI Compute instance. After your instance is up and running, optionally create and attach a block volume.")
  * [Free Tier: Install Apache and PHP on an Oracle Linux Instance](https://docs.oracle.com/iaas/developer-tutorials/tutorials/apache-on-oracle-linux/01-summary.htm)


**Tip** If this is your first time creating an instance, we recommend creating a Virtual Cloud Network (VCN) first. You can use the "Start VCN Wizard" workflow and select the "Create VCN with Internet Connectivity" option. The workflow creates a VCN which automatically configures both a public and a private subnet along with any required gateways and route rules. In addition, the workflow provides an option to configure IPv6. For details on running the workflow see: [Virtual Networking Quickstart](https://docs.oracle.com/iaas/Content/Network/Tasks/quickstartnetworking.htm). 

Open the Instance Details
    
  * [Log into the OCI Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm).
  * Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  * Select the instance you are interested in. The instance details page is displayed.



Review the VCN Configuration
    
  * Click the VCN assigned to this instance.
  * Ensure at least one Internet Gateway is available in the Internet Gateways resource.
    * If no Internet Gateway is assigned, go to the next section.
  * If an Internet Gateway is assigned, ensure your public subnet has a route rule assigned for the gateway.
    * Under the **Subnets** resource, select your public subnet.
    * Under **Subnet Information** click the **Route table** link.
    * Ensure there is a static route with a destination of ` 0.0.0.0/0`.
    * If the route entry is missing, go to the next section.



My Public Subnet isn't Properly Configured
    
If it appears your public subnet isn't configured properly, you have two options to reconfigure your subnet.
**(1) Use the Compute Quick Action**.
From the instance details page:
  * In the **Resources** list, select **Quick Actions**.
  * Click **Connect** on the **Connect public subnet to internet** quick action.
  * Follow the workflow to connect your instance.


**(2) Manually create a public subnet.**
  * Use the [Scenario A: A Public Subnet](https://docs.oracle.com/iaas/Content/Network/Tasks/scenarioa.htm) document to walk through the steps to setup and configure a new public subnet.
  * Create a new Compute instance in the new public subnet.



Check Security Lists
    
If you're continuing to have issues, ensure your security lists allow traffic on port 22. See [Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm) for details. 

Advanced Troubleshooting
    
If you're an advanced user, you can use the Network Path Analyzer to further troubleshoot the network connection. See [Network Path Analyzer](https://docs.oracle.com/iaas/Content/Network/Concepts/path_analyzer.htm) for details.
## SSH: Connect to host w.x.y.z port 22: Connection refused 🔗 
This error message is caused because a host is listening at the target address, but you can't connect to port 22.
## Use Netcat(nc) to verify that SSH is Running 🔗 
**Linux or MacOS**
In a terminal window, run the following command:
Copy
```
nc <public ip> 22
```

  * **If the command returns a message similar to:** `SSH-2.0-OpenSSH_9.4`
You successfully connected to the instance and verified SSH is running. Double check the IP address in your SSH command, ensure it is correct.
  * **If the command returns nothing:**
    * Check the public IP address on the instance detail page to ensure you are using the correct address.
    * Double check the IP address used in the command, ensure it is correct.
Otherwise, continue to the next section.


**Windows**
In a PowerShell window, run the following command:
Copy
```
tnc <public ip> -p 22
```

  * **If the command returns a message similar to:**
```
ComputerName   : <public ip>
                RemoteAddress  : <public ip>
                RemotePort    : 22
                InterfaceAlias  : Ethernet
                SourceAddress  : <source ip>
                TcpTestSucceeded : True
```

You successfully connected to the instance and verified SSH is running. Double check the IP address in the SSH command, ensure it is correct.
  * **If the command returns:** `WARNING: TCP connect to (<public ip>) failed`
    * Check the public IP address on the instance detail page to ensure you're using the correct address.
    * Double check the IP address used in the command, ensure it is correct.
Otherwise, continue troubleshooting with the next section.


## SSH is not Running 🔗 
  * Check that the instance is on a public subnet. 
    * If the instance is on a private subnet, you can't connect to the instance directly. See the [Using a Private Subnet](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/troubleshooting-ssh-connection.htm#troubleshooting-ssh-connection__ssh-trouble-private-subnet) section.
  * Ensure the security lists are configured to allow connections to port 22. See [Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm) for details.
  * Reboot the instance to restart the SSH daemon.
  * **Advanced:** If you're using a custom image and need to start or install the SSH service, use [the Serial Console](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm) to connect to the instance.


## <user-name>@w.x.y.z: Permission denied (publickey,gssapi-keyex,gssapi-with-mic) 🔗 
This error message indicates SSH is connecting to the SSH service host, but there is an issue with the SSH command.
## Check for the following Issues with your SSH Command 🔗 
  * Double check all the command line options for SSH. Any incorrect option might cause this error message.
    * The following is an example of a correctly formatted SSH command to connect to Oracle Linux. ```
ssh -i <my-private-key-file> opc@x.x.x.x
```

  * Ensure you're using the correct user name for the instance: 
    * For Oracle Linux or other Red Hat compatible OSes, use `opc`.
    * For Ubuntu Linux, use `ubuntu`.
  * Ensure you are using the correct private key. Using the wrong private key file will result in this error message. 
    * Ensure you're in the directory containing the key.
    * Alternatively, ensure the path to the private key is correct.
  * I lost my private key.
    * Make a new instance and download the new public and private keys.
    * Make a new public and private key set. Create a new instance.


## SSH Login Denied Using PuTTYgen Key Files: "Permission denied (publickey,gssapi-keyex,gssapi-with-mic)" 🔗 
This occurs because Linux instances supports OpenSSH generated SSH keys and PuTTYgen generated SSH keys use a different format.
## Make SSH Key Formats Match
If you're using .ppk keys generated with PuTTYgen to log into a Linux instance using the OpenSSH SSH command, the connection fails. For example:
```
$ ssh -i deployment_key.txt opc@<IP_ADDRESS>
Enter passphrase for key 'deployment_key.txt':
Permission denied (publickey,gssapi-keyex,gssapi-with-mic).
```

This error occurs because Linux instances support OpenSSH generated SSH keys and PuTTYgen generated SSH keys use a different format. To resolve this issue, use PuTTYgen to convert the keys to OpenSSH key format. Then, the keys can then be used with the SSH command to log into a Linux instance.
  1. If you do not have PuTTYgen, download it from <https://www.puttygen.com/> and install it. 
  2. Open PuTTYgen.
  3. Click **File** and then click **Load private key**.
  4. Navigate to your PuTTY private key file (.ppk) and then click **Open**.
  5. (Optional) Enter a key passphrase.
  6. Click **Conversions** and then click **Export OpenSSH key**. 
If you did not use as passphrase, click **Yes** at the **PuTTYgen Warning** to proceed.
  7. In the **Save private key as:** window enter a file name for the converted key and then click **Save**.


You can now use the converted key to log into your Linux instance.
## SSH Fails with Error: "Authentication Refused: Bad Ownership Or Modes For Directory " 🔗 
This error occurs because incorrect permissions are set on the `/home/<USERNAME>` directory or the `.ssh/authorized_keys` file.
**Note** The example home directory paths in this troubleshooting tip use Oracle Linux. The home path may differ based on the operating system. For example, the home path in MacOS is `/Users/<USERNAME>`.
## Set correct Permissions
If you have incorrect permissions set on the `/home/<USERNAME>` directory or the `.ssh/authorized_keys` file, connecting to a Linux instance using SSH can fail. 
For example:
```
login as: <username>
Server refused our key
```

If you review the `/var/log/secure` log files on the Linux instance, you see the reason for the error:
```
<SERVER> sshd[6245]: Authentication refused: bad ownership or modes for directory /home/<USERNAME>
```

To correct the error, set the permissions on the home directory or `.ssh/authorized_keys` file, use the `chmod` command:
```
# chmod 700 /home/<username>
# chmod 700 /home/<username>/.ssh/
# chmod 600 /home/username/.ssh/authorized_keys
```

## Using Cloud Shell to connect to an OCI Instance 🔗 
OCI Cloud Shell is a web browser-based terminal accessible from the OCI Console. Cloud Shell is free to use (within monthly tenancy limits), and provides access to a Linux shell, with a pre-authenticated OCI CLI, a pre-authenticated Ansible installation, and other useful tools.
If you are having connectivity issues with your instance, Cloud Shell is an effective option for connecting with SSH. Since Cloud Shell is browser based, it eliminates any potential connectivity issues due to laptop or corporate firewall settings. This section links you to the information about the ways you can use Cloud Shell.
  * For information on Cloud Shell, see [Cloud Shell](https://docs.oracle.com/iaas/Content/API/Concepts/cloudshellintro.htm).
  * For information on how to access Cloud Shell, see [Using Cloud Shell](https://docs.oracle.com/iaas/Content/API/Concepts/cloudshellgettingstarted.htm).
  * For information on how to connect a Cloud Shell session to a private network, see [Cloud Shell Private Networking](https://docs.oracle.com/iaas/Content/API/Concepts/cloudshellintro_topic-Cloud_Shell_Networking.htm#Cloud_Shell_Private_Access).


## Using a Private Subnet 🔗 
If your Compute instance is on a private subnet, there are generally two scenarios. 

(1) The Instance is on a Private Subnet but should be on a Public Subnet
    
To have the instance on a public subnet you have the following options.
  * Create a new instance in a public subnet in the current VCN. Terminate the old instance.
  * Create a new public subnet in the current VCN. Create a new instance in the new public subnet. Terminate the old instance.
  * Create a new VCN with a public subnet and then create a new instance in the public subnet. Terminate the old instance.


**Tip** If this is your first time creating an instance, for a guided tutorial consider one the following: 
  * [Launching Your First Linux Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/tutorials/first-linux-instance/overview.htm "In this tutorial, perform the steps to create and connect to an OCI Compute instance. After your instance is up and running, optionally create and attach a block volume.")
  * [Free Tier: Install Apache and PHP on an Oracle Linux Instance](https://docs.oracle.com/iaas/developer-tutorials/tutorials/apache-on-oracle-linux/01-summary.htm)


**Tip** If this is your first time creating an instance, we recommend creating a Virtual Cloud Network (VCN) first. You can use the "Start VCN Wizard" workflow and select the "Create VCN with Internet Connectivity" option. The workflow creates a VCN which automatically configures both a public and a private subnet along with any required gateways and route rules. In addition, the workflow provides an option to configure IPv6. For details on running the workflow see: [Virtual Networking Quickstart](https://docs.oracle.com/iaas/Content/Network/Tasks/quickstartnetworking.htm). 

(2) The Instance is intentionally on a Private Subnet
    
When the Compute instance is on a private subnet, you can connect to it using:
  * **Cloud Shell** : See the [OCI Cloud Shell Section](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/troubleshooting-ssh-connection.htm#troubleshooting-ssh-connection__ssh-trouble-using-cloud-shell) on this page for details.
  * **[Bastion](https://docs.oracle.com/iaas/Content/Bastion/Concepts/bastionoverview.htm)** provides restricted and time-limited access to target resources that don't have public endpoints. See the [Bastion Overview](https://docs.oracle.com/iaas/Content/Bastion/Concepts/bastionoverview.htm) for more details.


## Additional Connection and Instance Troubleshooting Options 🔗 
The focus of this page is using the SSH command to connect to an instance. Here are other tools available to troubleshoot Compute instances.
## Troubleshooting with the Serial Console 🔗 
Using an OCI console connection, you can use the instance's serial console to connect to the instance. This allows you to remotely troubleshoot and configure an instance. For more information, see [Troubleshooting Instances Using Instance Console Connections](https://docs.oracle.com/en-us/iaas/Content/Compute/References/serialconsole.htm#Instance_Console_Connections).
From the serial console, you can perform the following administrative tasks: 
  * Interrupt the boot process to [boot into maintenance mode](https://docs.oracle.com/en-us/iaas/Content/Compute/References/serialconsole.htm#instcon_linux_trouble__maintenancemode).
  * In maintenance mode, [add or reset the SSH key for the `opc` user](https://docs.oracle.com/en-us/iaas/Content/Compute/References/serialconsole.htm#instcon_linux_trouble__resetsshkey).


## Observe Instance Health 🔗 
On the instance details page, you can observe metrics related to the instance including the instance's health. The `oci_compute_instance_health` metric lets you monitor whether a VM instance is unresponsive. Compute sends an Address Resolution Protocol (ARP) request to the instance's virtual network interface card (VNIC). If the ARP ping fails, the metric shows that the instance is unresponsive.
To use the metric, select `oci_compute_instance_health` from the **Metric namespace** control on the details page. For more information, see: [Compute Instance Health Metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/compute-health-metrics.htm#compute-health-metrics).
## Other Compute Troubleshooting Sections 🔗 
In addition to SSH, the following troubleshooting topics are also available.
  * [Troubleshooting Oracle Cloud Agent](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#troubleshoot)
  * [Performing a Diagnostic Reboot](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/diagnostic-reboot.htm#diagnostic-reboot)
  * [Sending a Diagnostic Interrupt](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/sendingdiagnosticinterrupt.htm#triggering-diagnostic-interrupt "You can send a diagnostic interrupt to troubleshoot an unresponsive or unreachable Compute virtual machine \(VM\) instance.")
  * [Displaying the Console History for an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole.htm#Displaying_the_Console_for_an_Instance)


Was this article helpful?
YesNo


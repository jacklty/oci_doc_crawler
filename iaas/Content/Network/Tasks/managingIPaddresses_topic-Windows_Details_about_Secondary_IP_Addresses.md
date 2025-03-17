Updated 2025-02-06
# Configuring Windows to Use a Secondary IP Addresses
Configure the Windows OS to use a secondary private IP.
[After assigning a secondary private IP to a VNIC, you must configure the OS to use it](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-create.htm#top "Assign a new secondary private IP address to a VNIC."). Here are instructions for using a PowerShell script or the Network and Sharing Center UI. 
[Using a PowerShell Script](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses_topic-Windows_Details_about_Secondary_IP_Addresses.htm)
You must run PowerShell as an administrator. The script configures two things: static IP addressing on the instance and the secondary private IP. The configuration persists through a reboot of the instance.
  1. In a browser, go to the Console, and note the secondary private IP address that you want to configure on the instance. 
  2. Connect to the instance, and run the following command at a command prompt:
Copy
```
ipconfig /all
```

  3. Note the values for the following items so you can enter them into the script in the next step:
     * Default Gateway
     * DNS Servers
  4. Replace the variables in the following PowerShell script with appropriate values:
Copy
```
$netadapter = Get-Netadapter -Name "Ethernet 2"
$netadapter | Set-NetIPInterface -DHCP Disabled
$netadapter | New-NetIPAddress -AddressFamily IPv4 -IPAddress <secondary_IP_address> -PrefixLength <subnet_prefix_length> -Type Unicast -DefaultGateway <default_gateway>
Set-DnsClientServerAddress -InterfaceAlias "Ethernet 2" -ServerAddresses <DNS_server>

```

For example:
Copy
```
$netadapter = Get-Netadapter -Name "Ethernet 2"
$netadapter | Set-NetIPInterface -DHCP Disabled
$netadapter | New-NetIPAddress -AddressFamily IPv4 -IPAddress 192.168.0.14 -PrefixLength 24 -Type Unicast -DefaultGateway 192.168.0.1
Set-DnsClientServerAddress -InterfaceAlias "Ethernet 2" -ServerAddresses 203.0.113.254

```

  5. Save the script with a name you select and a `.ps1` extension, and run it on the instance.
[![This image shows the PowerShell script for configuring a secondary private IP address.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_windows_config_ip_powershell.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_windows_config_ip_powershell.png)
If you run` ipconfig /all` again, see that DHCP has been disabled and the secondary private IP address is included in the list of IP addresses.


Later, to delete the address, you can use this command:
Copy
```
Remove-NetIPAddress -IPAddress 192.168.11.14 -InterfaceAlias Ethernet
```

Also, ensure that you [delete the secondary IP from the VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-delete.htm#top "Delete a private IP address from a VNIC."). You can do that before or after executing the preceding command to delete the address from the OS configuration.
[Using the Network and Sharing Center UI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses_topic-Windows_Details_about_Secondary_IP_Addresses.htm)
The following instructions configure two things: static IP addressing on the instance and the secondary private IP. The configuration persists through a reboot of the instance.
  1. In a browser, go to the Console, and note the secondary private IP address that you want to configure on the instance. 
  2. Connect to the instance, and run the following command at a command prompt:
Copy
```
ipconfig /all
```

[![This image shows the results of the ipconfig /all command.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_windows_ipconfig.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_windows_ipconfig.png)
  3. Note the values for the following items so you can enter them elsewhere in a later step:
     * IPv4 Address
     * Subnet Mask
     * Default Gateway
     * DNS Servers
  4. In the instance's **Control Panel** , open the **Network and Sharing Center** (see the image that follows for the set of dialog boxes in these steps).
  5. For the active networks, select the connection (**Ethernet**).
  6. Select **Properties**.
  7. Select **Internet Protocol Version 4 (TCP/IPv4)** , and then select **Properties**.
  8. Select the radio button for **Use the following IP address** , and then enter the values you noted earlier for the IP address, subnet mask, default gateway, and DNS servers. 
[![This image shows the series of dialog boxes.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_windows_config_ip_address.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_windows_config_ip_address.png)
  9. Select **Advanced...**.
  10. Under **IP addresses** , select **Add...**.
  11. Enter the secondary private IP address and the subnet mask you used earlier and select **Add**.
[![This image shows the dialog box for adding the secondary private IP address.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_windows_config_ip_address_advanced.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_windows_config_ip_address_advanced.png)
  12. Select **OK** until the Network and Sharing Center is closed.
  13. Verify the changes by returning to the command prompt and running `ipconfig /all`.
You should now see that DHCP is disabled (static IP addressing is enabled), and the secondary private IP address is in the list of addresses displayed. The address is now configured on the instance and available to use.
[![This image shows the results of the ipconfig /all command after adding the secondary private IP address.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_windows_ipconfig_verify.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_windows_ipconfig_verify.png)
**Note**
You might not see the primary private IP address when you again view the properties for Internet Protocol Version 4 (TCP/IPv4) in the Network and Sharing Center UI. The best way to confirm changes is to use `ipconfig /all` at the command line. 


Was this article helpful?
YesNo


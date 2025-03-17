Updated 2025-01-08
# Configuring the Oracle Cloud Infrastructure NTP Service for an Instance
Oracle Cloud Infrastructure offers a fully managed, secure, and highly available NTP service that you can use to set the date and time of compute and database instances from within a virtual cloud network (VCN). The Oracle Cloud Infrastructure NTP service uses redundant Stratum 1 devices in every availability domain. The Stratum 2 devices are synchronized to dedicated Stratum 1 devices that every host synchronizes against. The service is available in every region.
This topic describes how to configure compute instances to use this NTP service.
You can also choose to configure instances to use a public NTP service or use FastConnect to leverage an on-premises NTP service.
**Note** Platform images for Oracle Autonomous Linux 8.x, Oracle Autonomous Linux 7.x, Oracle Linux 9.x, Oracle Linux 8.x, Oracle Linux 7.x, Oracle Linux Cloud Developer 8.x, CentOS 7.x released after February 2018, and CentOS Stream 8 include the Chrony service by default. You do not need to configure the Oracle Cloud Infrastructure NTP service for these instances.
[Oracle Linux 7.x released in February 2018 or earlier](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringntpservice.htm)
Use the following steps to configure Oracle Linux 7.x instances to use the Oracle Cloud Infrastructure NTP service.
  1. Run commands in this section as root with the following command:
Copy
```
sudo su -
```

  2. Install the NTP service with the following command:
Copy
```
yum -y install ntp
```

  3. Change the firewall rules to allow inbound and outbound traffic with the Oracle Cloud Infrastructure NTP server, at 169.254.169.254, on UDP port 123 with the following command:
Copy
```
awk -v n=13 -v s=' <passthrough ipv="ipv4">-A OUTPUT -d 169.254.169.254/32 -p udp -m udp --dport 123 -m comment --comment "Allow access to OCI local NTP service" -j ACCEPT </passthrough>' 'NR == n {print s} {print}' /etc/firewalld/direct.xml > tmp && mv tmp /etc/firewalld/direct.xml
```

At the prompt `mv: overwrite '/etc/firewalld/direct.xml'?`, enter `y`.
  4. Restart the firewall with the following command:
Copy
```
service firewalld restart
```

  5. Set the date of your instance with the following command:
Copy
```
ntpdate 169.254.169.254
```

  6. Configure the instance to use the Oracle Cloud Infrastructure NTP service for iburst. To configure, modify the `/etc/ntp.conf` file as follows:
    1. In the `server` section comment out the lines specifying the RHEL servers: 
Copy
```
#server 0.rhel.pool.ntp.org iburst
#server 1.rhel.pool.ntp.org iburst
#server 2.rhel.pool.ntp.org iburst
#server 3.rhel.pool.ntp.org iburst
```

    2. Add an entry for the Oracle Cloud Infrastructure NTP service: 
Copy
```
server 169.254.169.254 iburst
```

The modified `server` section should now contain the following:
Copy
```
# Please consider joining the pool (http://www.pool.ntp.org/join.html).
#server 0.rhel.pool.ntp.org iburst
#server 1.rhel.pool.ntp.org iburst
#server 2.rhel.pool.ntp.org iburst
#server 3.rhel.pool.ntp.org iburst
server 169.254.169.254 iburst
```

  7. Start and enable the NTP service with the following commands:
Copy
```
systemctl start ntpd
systemctl enable ntpd
```

You also need disable the chrony NTP client to ensure that the NTP service starts automatically after a reboot, using the following commands:
Copy
```
systemctl stop chronyd
systemctl disable chronyd
```

  8. Confirm that the NTP service is configured correctly with the following command:
Copy
```
ntpq -p
```

The output will be similar to the following:
Copy
```
   remote      refid   st t when poll reach  delay  offset jitter
==============================================================================
169.254.169.254 192.168.32.3   2 u  2  64  1  0.338  0.278  0.187
						
```



[Windows Server](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringntpservice.htm)
**Tip** If you encounter a _no time data was available_ error message when setting up the NTP service on Windows Server, review the information in the [Microsoft known issue](https://docs.microsoft.com/troubleshoot/windows-server/identity/error-message-run-w32tm-resync-no-time-data-available) article.
  1. Configure a Windows Server instance to use the Oracle Cloud Infrastructure NTP service by doing one of the following things:
     * To configure the NTP service by using Windows Powershell, run the following commands in Powershell as Administrator:
Copy
```
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Services\W32Time\Parameters' -Name 'Type' -Value NTP -Type String
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Services\W32Time\Config' -Name 'AnnounceFlags' -Value 5 -Type DWord
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Services\W32Time\TimeProviders\NtpServer' -Name 'Enabled' -Value 1 -Type DWord
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Services\W32Time\Parameters' -Name 'NtpServer' -Value '169.254.169.254,0x9' -Type String
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Services\W32Time\TimeProviders\NtpClient' -Name 'SpecialPollInterval' -Value 900 -Type DWord
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Services\W32Time\Config' -Name 'MaxPosPhaseCorrection' -Value 1800 -Type DWord
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Services\W32Time\Config' -Name 'MaxNegPhaseCorrection' -Value 1800 -Type DWord
```

     * To configure the NTP service by manually editing the registry, do the following:
       1. Change the server type to NTP:
         1. From Registry Editor, navigate to:```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Parameters\
```

         2. Click **Type**.
         3. Change the value to `NTP` and click **OK**.
       2. Configure the Windows Time service to enable the `Timeserv_Announce_Yes` and `Reliable_Timeserv_Announce_Auto` flags.
To configure, set the `AnnounceFlags` parameter to 5:
         1. From Registry Editor, navigate to:```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Config\
```

         2. Click **AnnounceFlags**.
         3. Change the value to `5` and click **OK**.
       3. Enable the NTP server:
         1. From Registry Editor, navigate to:```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders\NtpServer\
```

         2. Click **Enabled**.
         3. Change the value to `1` and click **OK**.
       4. Set the time sources:
         1. From Registry Editor, navigate to:```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Parameters\
```

         2. Click **NtpServer**.
         3. Change the value to `169.254.169.254,0x9` and click **OK**.
       5. Set the poll interval:
         1. From Registry Editor, navigate to:```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders\NtpClient\
```

         2. Click **SpecialPollInterval**.
         3. Set the value to the interval that you want the time service to synchronize on. The value is in seconds. To set it for 15 minutes, set the value to `900`, and click **OK**.
       6. Set the phase correction limit settings to restrict the time sample boundaries:
         1. From Registry Editor, navigate to:```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Config\
```

         2. Click **MaxPosPhaseCorrection**.
         3. Set the value to the maximum time offset in the future for time samples. The value is in seconds. To set it for 30 minutes, set the value to `1800` and click **OK**.
         4. Click **MaxNegPhaseCorrection**.
         5. Set the value to the maximum time offset in the past for time samples. The value is in seconds. To set it for 30 minutes, set the value to `1800` and click **OK**.
  2. Restart the time service by running the following command from a command prompt:
Copy
```
net stop w32time && net start w32time
```

  3. Test the connection to the NTP service by running the following command from a command prompt:
Copy
```
w32tm /query /peers
```

The output will be similar to the following:
```
#Peer: 1
 
Peer: 169.254.169.254,0x9
State: Active
Time Remaining: 22.1901786s
Mode: 3 (Client)
Stratum: 0 (unspecified)
PeerPoll Interval: 10 (1024s)
HostPoll Interval: 10 (1024s)
```

After the time specified in the poll interval has elapsed, `State` will change from `Pending` to `Active`.


Was this article helpful?
YesNo


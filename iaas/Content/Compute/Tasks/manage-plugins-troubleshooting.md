Updated 2025-01-08
# Troubleshooting Oracle Cloud Agent
When using [Oracle Cloud Agent](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#manage-plugins), you might encounter the following problems: 
  * On the Oracle Cloud Agent tab of the Instance Details page, the status for all plugins is **Invalid**.
  * In the Metrics section of the Console dashboard, you can't see any CPU, memory, network, or disk metrics for the instance.


If you encounter any of these problems, Oracle Cloud Agent might not be installed or running, or it might not be able to communicate with Oracle services. To diagnose the specific issue, follow these troubleshooting steps.
**Tip** In this topic, the instructions for Oracle Linux also apply to CentOS images.
**Tip** If you can't connect to your instance, see: 
  * [Troubleshooting the SSH Connection](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/troubleshooting-ssh-connection.htm#troubleshooting-ssh-connection "If you're unable to connect to a compute instance using SSH, review the following troubleshooting error messages and suggestions to resolve the issue.")
  * [Troubleshooting Instances Using Instance Console Connections](https://docs.oracle.com/en-us/iaas/Content/Compute/References/serialconsole.htm#Instance_Console_Connections)


## Step 1: Verify that Oracle Cloud Agent is Installed 🔗 
Follow these steps to confirm that Oracle Cloud Agent is installed on your instance.
  1. [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm#top "You can connect to a running compute instance by using a Secure Shell \(SSH\) or Remote Desktop connection.") and run one of the following commands, depending on your operating system.
[Oracle Linux](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm)
Copy
```
rpm -q oracle-cloud-agent && echo "OCA Installed" || echo "OCA not Installed"

```

If Oracle Cloud Agent is installed, a message similar to the following displays:
```
oracle-cloud-agent-<version>.x86_64
OCA Installed

```

[Ubuntu](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm)
Copy
```
snap list oracle-cloud-agent &>/dev/null && echo "OCA Installed" || echo "OCA not Installed"
```

If Oracle Cloud Agent is installed, the following message displays:
```
OCA Installed
```

[Windows Server](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm)
Run the command in [Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows) as an administrator.
Copy
```
Get-WmiObject -Class Win32_Product |where name -eq "Oracle Cloud Agent"
```

If Oracle Cloud Agent is installed, a message similar to the following displays:
```
IdentifyingNumber : {<unique_ID>}
Name       : Oracle Cloud Agent
Vendor      : Oracle Corporation
Version      : <version>
Caption      : Oracle Cloud Agent
    
```

  2. If the message indicating that Oracle Cloud Agent is installed does not display after you run the command, [install Oracle Cloud Agent](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent). If Oracle Cloud Agent is installed, proceed to the next step to verify that it is running.


## Step 2: Verify that Oracle Cloud Agent is Running 🔗 
After you confirm that Oracle Cloud Agent is installed, follow these steps to confirm that it is running.
  1. [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm#top "You can connect to a running compute instance by using a Secure Shell \(SSH\) or Remote Desktop connection.") and run one of the following commands to restart Oracle Cloud Agent. 
[Oracle Linux 7.x and later versions](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm)
Copy
```
systemctl is-enabled oracle-cloud-agent &>/dev/null && echo "OCA is enabled" || echo "OCA is disabled" \
 && systemctl is-active oracle-cloud-agent &> /dev/null && echo "OCA is running" || echo "OCA is not running"
```

Expected response if Oracle Cloud Agent is running:
```
OCA is enabled
OCA is running
```

[Ubuntu](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm)
Copy
```
snap services oracle-cloud-agent
```

Expected response if Oracle Cloud Agent is running:
```
Service                Startup Current Notes
oracle-cloud-agent.oracle-cloud-agent enabled active -
```

[Windows Server](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm)
Run the command in [Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows) as an administrator.
Copy
```
sc.exe query "OCA"|findstr "RUNNING"
```

Expected response if Oracle Cloud Agent is running:
```
STATE : 4 RUNNING
```

  2. If the message indicating that Oracle Cloud Agent is running does not display after you run the command, [run the diagnostic tool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#diagnostic) and then file a [support ticket](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm) with the file that contains debugging information and logs for the plugins. If Oracle Cloud Agent is running, proceed to the next step to verify that it can connect to Oracle services.


## Step 3: Verify that Oracle Cloud Agent Can Connect to Oracle Services 🔗 
If you confirm that Oracle Cloud Agent is installed and running but the status for all plugins on the Instance Details page is **Invalid** or you cannot see any metrics in the Metrics section of the Console dashboard, Oracle Cloud Agent might not be able to connect to Oracle services. The following sections explore possible reasons that Oracle Cloud Agent is unable to connect to Oracle services. To diagnose the issue, follow these steps in order.
  1. [Verify that the instance can access the Instance Metadata Service endpoint.](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#verifyservices__instancemetadataserviceendpoint)
  2. [Check for clock skew errors.](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#verifyservices__clockskew)
  3. [Verify that gateways are configured correctly.](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#verifyservices__gateways)
  4. [Change your proxy server settings.](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#verifyservices__proxyservers)


### Verify that the Instance Can Access the Instance Metadata Service Endpoint 🔗 
These steps verify whether the instance can access the Instance Metadata Service endpoint.
  1. [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm#top "You can connect to a running compute instance by using a Secure Shell \(SSH\) or Remote Desktop connection.") and run one of the following commands, depending on you operating system.
[Oracle Linux and Ubuntu](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm)
Copy
```
curl -v -H 'Authorization: Bearer Oracle' http://169.254.169.254/opc/v2/instance/
```

If Oracle Cloud Agent is running, a message similar to the following displays:
```
* About to connect() to 169.254.169.254 port 80 (#0)
*  Trying 169.254.169.254...
* Connected to 169.254.169.254 (169.254.169.254) port 80 (#0)
> GET /opc/v2/instance/ HTTP/1.1
> User-Agent: curl/7.29.0
> Host: 169.254.169.254
> Accept: */*
> Authorization: Bearer Oracle
>
< HTTP/1.1 200 OK
< Server: server
< Date: Wed, 24 Mar 2021 20:52:38 GMT
< Content-Type: application/json
< Content-Length: 1800
< Last-Modified: Wed, 03 Mar 2021 01:43:50 GMT
< Connection: keep-alive
< ETag: "603ee9d6-708"
< Accept-Ranges: bytes
<
{
 "availabilityDomain" : "uybn:<availability_domain>",
 "faultDomain" : "<fault_domain>",
 "compartmentId" : "ocid1.compartment.oc1..<unique_ID>",
 "displayName" : "<instance_name>",
 "hostname" : "<host_name>",
 "id" : "<unique_ID>",
 "image" : "ocid1.image.oc1.iad.<unique_ID>",
 "metadata" : {
  "ssh_authorized_keys" : ""
 },
 "region" : "<region_key>",
 "canonicalRegionName" : "<region_name>",
 "ociAdName" : "<availability_domain>",
 "regionInfo" : {
  "realmKey" : "<realm>",
  "realmDomainComponent" : "oraclecloud.com",
  "regionKey" : "<region_key>",
  "regionIdentifier" : "<region>"
 },
 "shape" : "<shape>",
 "state" : "Running",
 "timeCreated" : 1614637343723,
 "agentConfig" : {
  "monitoringDisabled" : false,
  "managementDisabled" : false,
  "allPluginsDisabled" : false,
  "pluginsConfig" : [ {
   "name" : "OS Management Service Agent",
   "desiredState" : "ENABLED"
  }, {
   "name" : "Custom Logs Monitoring",
   "desiredState" : "ENABLED"
  }, {
   "name" : "Compute Instance Run Command",
   "desiredState" : "ENABLED"
  }, {
   "name" : "Compute Instance Monitoring",
   "desiredState" : "ENABLED"
  } ]
 },
 "freeformTags" : {
  "keep" : "keep"
 }
* Connection #0 to host 169.254.169.254 left intact

```

[Windows Server](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm)
Run the command in [Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows) as an administrator.
Copy
```
Invoke-WebRequest -Headers @{'Authorization'='Bearer Oracle'} http://169.254.169.254/opc/v2/instance/

```

If Oracle Cloud Agent is running, a message similar to the following displays:
```
StatusCode    : 200
StatusDescription : OK
Content      : {
           "availabilityDomain" : "<availability_domain>",
           "faultDomain" : "<fault_domain>",
           "compartmentId" :
          "ocid1.tenancy.region1..<unique_ID>",
           "displayNam...
RawContent    : HTTP/1.1 200 OK
          Connection: keep-alive
          Accept-Ranges: bytes
          Content-Length: 1197
          Content-Type: application/json
          Date: Wed, 24 Mar 2021 21:07:42 GMT
          ETag: "<unique_ID>"
          Last-Modified: Wed, 24 M...
Forms       : {}
Headers      : {[Connection, keep-alive], [Accept-Ranges, bytes], [Content-Length, 1197], [Content-Type,
          application/json]...}
Images      : {}
InputFields    : {}
Links       : {}
ParsedHtml    : mshtml.HTMLDocumentClass
RawContentLength : 1197

```

  2. If you get a successful response without proxy errors, check for clock skew errors. If proxy server errors occur, [check your proxy server settings](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#verifyservices__proxyservers).


### Check for Clock Skew Errors 🔗 
Sometimes, the clock on an instance is not synchronized with the NTP service. Clock skew can cause TLS negotiations to fail, preventing the instance from connecting to Oracle services. Follow these steps to check for clock skew errors.
  1. [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm#top "You can connect to a running compute instance by using a Secure Shell \(SSH\) or Remote Desktop connection.") and run one of the following commands to generate the `monitoring.log` file.
[Linux](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm)
Copy
```
sudo tail -15 /var/log/oracle-cloud-agent/plugins/gomon/monitoring.log
```

[Windows Server 2019, Windows Server 2022](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm)
Run the command in [Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows) as an administrator.
Copy
```
Get-Content -tail 15 C:\Windows\ServiceProfiles\OCA\AppData\Local\OracleCloudAgent\plugins\gomon\monitoring.log
```

[Windows Server earlier than 2019](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm)
Run the command in [Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows) as an administrator.
Copy
```
Get-Content -tail 15 C:\Users\OCA\AppData\Local\OracleCloudAgent\plugins\gomon\monitoring.log
```

If there is a clock skew error, a message similar to the following displays:
```
failed to call: Service error:NotAuthenticated. Date 'Tue, 09 Mar 2021 06:39:35 UTC' is not within allowed clock skew.
Current 'Tue, 09 Mar 2021 06:45:45 UTC', valid datetime range: ['Tue, 09 Mar 2021 06:40:45 UTC', 'Tue, 09 Mar 2021 06:50:46 UTC'].
http status code: 401. Opc request id: <unique_id>
```

  2. If a clock skew error occurs, [configure the Oracle Cloud Infrastructure NTP service for your instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringntpservice.htm#Configuring_the_Oracle_Cloud_Infrastructure_NTP_Service_for_an_Instance). If no clock skew error occurs, [verify that gateways are configured correctly](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#verifyservices__gateways).
  3. If you configured the NTP service in the previous step, after you complete the configuration, run one of the following commands to restart Oracle Cloud Agent:
[Oracle Linux 7.x and later versions](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm)
Copy
```
sudo systemctl restart oracle-cloud-agent
```

[Ubuntu](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm)
Copy
```
sudo snap restart oracle-cloud-agent
```

[Windows Server](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm)
Run the command in [Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows) as an administrator.
Copy
```
net stop OCA
net start OCA
```

  4. Generate the `monitoring.log` file again.
If Oracle Cloud Agent is running correctly, a successful response is _200 OK_. In the `monitoring.log`, look for a message similar to the following:
```
2021/03/18 03:12:44.391381 t2.go:139: Sent metrics status: 200; took: 387ms; with opc-request-id:<unique_ID>;
2021/03/18 03:13:44.006391 instancemetadata_client.go:64: fetched metadata from http://169.254.169.254/opc/v2/instance/ , status 200 OK
2021/03/18 03:13:44.730102 t2.go:139: Sent metrics status: 200; took: 723ms; with opc-request-id:<unique_ID>;
2021/03/18 03:14:44.324046 t2.go:139: Sent metrics status: 200; took: 320ms; with opc-request-id:<unique_ID>;
```



### Verify Permissions for Windows Domain Joined Instances  🔗 
If you have a Windows instance that is joined to a domain, verify that the virtual account is granted the **Log on as a service** user right in the local Group Policy. To set permissions, follow the steps for enabling service log on through a local group policy in Microsoft's [Enable Service Logon](https://docs.microsoft.com/en-us/system-center/scsm/enable-service-log-on-sm?view=sc-sm-2019#enable-service-log-on-through-a-local-group-policy) guide. For **Log on as a service** , add the user **NT SERVICE\ALL SERVICES** or the specific user.
### Verify that Gateways are Configured Correctly 🔗 
For Oracle Cloud Agent to communicate with Oracle services, gateways in subnets must be configured correctly. Follow these steps to verify and correct your configuration.
  1. [Configure the internet gateway, NAT gateway, or service gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm) for the subnet in your VCN.
  2. After you follow the configuration steps, restart the services using the commands in the [Verify that the Instance Can Access the Instance Metadata Service Endpoint](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#verifyservices__instancemetadataserviceendpoint) section. After you restart the services, check the `monitoring.log` file for successful requests to Oracle services.


### Change Proxy Server Settings 🔗 
Sometimes, local proxy servers prevent Oracle Cloud Agent from communicating with any services. Each proxy server is different.
Often, setting the `http_proxy`, `https_proxy`, and `no_proxy` environment variables for the `oracle-cloud-agent` and `oracle-cloud-agent-updater` services on the proxy client instances resolves proxy issues. After you set these environment variables, in the proxy server `access.log` file (or equivalent, depending on your system), verify that you see requests from the proxy client to services that Oracle Cloud Agent accesses.
[Oracle Linux](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm)
  1. Run the following command.
Copy
```
sudo EDITOR=vi systemctl edit oracle-cloud-agent
```

  2. In the editor window, add the following entries, and then save the file.
Copy
```
[Service]
Environment="http_proxy=<proxy_url>:<proxy_port>"
Environment="https_proxy=<proxy_url>:<proxy_port>"
Environment="no_proxy=localhost,127.0.0.1,169.254.169.254"
```

     * <proxy_url> is the proxy URL.
     * <proxy_port> is the proxy port.
  3. Repeat the previous two steps for the `oracle-cloud-agent-updater` service.
  4. Run the following commands, and then restart the services.
Copy
```
sudo systemctl daemon-reload
sudo systemctl restart oracle-cloud-agent oracle-cloud-agent-updater
```



[Ubuntu](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm)
  1. Run the following command.
Copy
```
sudo EDITOR=vi systemctl edit snap.oracle-cloud-agent.oracle-cloud-agent
```

  2. In the editor window, add the following entries, and then save the file.
Copy
```
[Service]
Environment="http_proxy=<proxy_url>:<proxy_port>"
Environment="https_proxy=<proxy_url>:<proxy_port>"
Environment="no_proxy=localhost,127.0.0.1,169.254.169.254"
```

     * <proxy_url> is the proxy URL.
     * <proxy_port> is the proxy port.
  3. Repeat the previous two steps for the `snap.oracle-cloud-agent.oracle-cloud-agent-updater` service.
  4. Run the following commands, and then restart the services.
Copy
```
sudo systemctl daemon-reload
sudo systemctl restart snap.oracle-cloud-agent.oracle-cloud-agent snap.oracle-cloud-agent.oracle-cloud-agent-updater
```



[Windows Server](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm)
  1. Run the following commands in [Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows) as an administrator. Do not change the casing of the environment variables.
Copy
```
Set System environment variables for HTTP_PROXY, HTTPS_PROXY and NO_PROXY
[System.Environment]::SetEnvironmentVariable("HTTP_PROXY", "<proxy_url>:<proxy_port>", [System.EnvironmentVariableTarget]::Machine)
[System.Environment]::SetEnvironmentVariable("HTTPS_PROXY", "<proxy_url>:<proxy_port>", [System.EnvironmentVariableTarget]::Machine)
[System.Environment]::SetEnvironmentVariable("NO_PROXY", "localhost,127.0.0.1,169.254.169.254", [System.EnvironmentVariableTarget]::Machine)
```

     * <proxy_url> is the proxy URL.
     * <proxy_port> is the proxy port.
  2. Restart the `oracle-cloud-agent` and `oracle-cloud-agent-updater` services.
Copy
```
net stop OCA
net start OCA
net stop OCAU
net start OCAU
```

  3. To verify that the `Custom Logs Monitoring` plugin is able to send metrics, tail the `monitoring.log` file.
**Windows Server 2019, Windows Server 2022**
Copy
```
Get-Content C:\Windows\ServiceProfile\OCA\Appdata\Local\OracleCloudAgent\plugins\gomon\monitoring.log -Wait
```

**Windows Server versions earlier than 2019**
Copy
```
Get-Content C:\Users\OCA\Appdata\Local\OracleCloudAgent\plugins\gomon\monitoring.log -Wait
```



## Step 4: Generate a Diagnostic File for Oracle Cloud Agent 🔗 
To make it easier for [Oracle support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm) to help you troubleshoot issues with the Oracle Cloud Agent software, you can run the Oracle Cloud Agent diagnostic tool on your compute instances. The diagnostic tool generates a file that contains debugging information and logs for the plugins that Oracle Cloud Agent manages.
The diagnostic tool is installed with Oracle Cloud Agent version 1.14.0 and later. To update Oracle Cloud Agent, see [Updating the Oracle Cloud Agent Software](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#update-agent).
After you complete the previous troubleshooting steps, run the diagnostic tool and then file a [support ticket](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm) with the file that contains debugging information and logs for the plugins.
[To generate a diagnostic file on a Linux instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm)
  1. [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm#top "You can connect to a running Linux instance by using a Secure Shell \(SSH\) connection.").
  2. Change directories to the folder where the diagnostic tool is saved:
Copy
```
cd /usr/libexec/oracle-cloud-agent/ocatools
```

  3. Run the diagnostic tool:
Copy
```
sudo ./diagnostic
```

The tool generates a TAR file with a name in the format `oca-diag-<date>.<identifier>.tar.gz`. Provide the file when you open the support request.


[To generate a diagnostic file on a Windows instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm)
  1. [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm#top "You connect to a Windows instance by using a Remote Desktop connection. Most Windows systems include a Remote Desktop client by default.").
  2. Open PowerShell as an administrator.
  3. Change directories to the folder where the diagnostic tool is saved:
Copy
```
cd C:\Program Files\Oracle Cloud Agent\ocatools
```

  4. Run the diagnostic tool:
Copy
```
.\diagnostic.ps1
```

The tool generates a ZIP file and saves it to `C:\Users\opc\Desktop\`. Provide the file when you open the support request.


Was this article helpful?
YesNo


Updated 2025-01-13
# Running Commands on an Instance
You can remotely configure, manage, and troubleshoot compute instances by running scripts within the instance using the run command feature.
For example, the run command feature can help you automate tasks such as configuring [secondary virtual network interface cards (VNICs)](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm), joining instances to an identity provider, troubleshooting [SSH connectivity](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm#top "You can connect to a running compute instance by using a Secure Shell \(SSH\) or Remote Desktop connection."), or responding to cross-region disaster recovery scenarios.
You can run commands on an instance even when the instance does not have SSH access or open inbound ports.
The run command feature uses the Compute Instance Run Command plugin that is [managed by the Oracle Cloud Agent software](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#manage-plugins).
**Caution** Do not use the run command feature to provide or retrieve passwords, secrets, or other confidential information in plain text. To securely provide and retrieve confidential information, use an [Overview of Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm) location to store the script file and response. Use [Oracle Cloud Infrastructure Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm) to manage keys and secret credentials.
For permissions, see [Required IAM Policy for Working with Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#permissions).
## Supported Images 🔗 
The run command feature is supported on compute instances that use the following [platform images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm#OracleProvided_Images):
  * Oracle Autonomous Linux
  * Oracle Linux
  * CentOS
  * Windows Server


[Custom images](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bringyourownimage.htm#Bring_Your_Own_Image_BYOI) that are based on a supported platform image also support the run command feature.
## Supported Regions 🔗 
The run command feature is supported in all regions in the [Oracle Cloud Infrastructure commercial realm](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).
## Limitations and Considerations 🔗 
  * On Linux instances, the script runs in a Bash shell by default. To run the script with a different program, use `#!/<path_to_program>` as the first line of the script.
  * On Windows instances, the script runs in a batch shell by default. To run the script with PowerShell, use `#ps1` as the first line of the script.
[See an example PowerShell script](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/runningcommands.htm)
The following example uses PowerShell to query the instance metadata service and print the instance OCID:
Copy
```
#ps1
$instance = Invoke-RestMethod -Headers @{'Authorization' = 'Bearer Oracle'} -Uri http://169.254.169.254/opc/v2/instance/
Write-Host ('Instance OCID is ' + $($instance.id))
```

  * The maximum size for a script file that you upload directly to an instance in plain text is 4 KB. To provide a larger file, save the file in an Object Storage location.
  * The output of a script when returned as plain text is limited to the last 1 KB. To save a larger response, save the output to an Object Storage location.
  * When you use an Object Storage location to save the script file or response, the instance must have outbound connectivity such as a [Network Access Translation (NAT) gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm), [service gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm), or [internet gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIGs.htm). The instance must also allow egress traffic on port 443 for the Oracle Cloud Agent software, Object Storage, and IAM.
  * Two scripts can run at a time by default. To change the default, update the run command configuration file:
Copy
```
cat /etc/oracle-cloud-agent/plugins/runcommand/config.yml
```

Set the following parameters:
Copy
```
logDir: /var/log/oracle-cloud-agent/plugins/runcommand
commandExecutionMaxWorkers: <number-of-parallel-scripts>
```

  * A maximum of five scripts can be in flight at a time. A script is considered to be in flight if it has been received by the Compute Instance Run Command plugin, but not yet deleted from the queue.
  * To perform long-running tasks, use the run command feature to schedule a cron job on the instance. Command orchestration is not supported.
  * Each script runs once. If you want a script to run multiple times, then use cron to configure a schedule for the script.
  * Scripts that prompt for information are not supported. You can use the [instance metadata service (IMDS)](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/gettingmetadata.htm#Getting_Instance_Metadata), however, to programmatically retrieve information about the instance on which the script runs.
  * When you create an instance from a [custom image](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bringyourownimage.htm#Bring_Your_Own_Image_BYOI) that already has permissions for the Compute Instance Run Command plugin configured, replace `101-oracle-cloud-agent-run-command` with `100-oracle-cloud-agent-run-command` in the configuration file.
  * The exit codes that are returned are standard Linux error codes. An exit code of `0` indicates success.
  * If you apply an optional timeout for a script, then the default is one hour. The maximum is 24 hours.
  * The maximum time that a script can run is one day.
  * To monitor the resources that scripts consume, such as CPU utilization, use [metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Compute_Instance_Metrics).
  * Canceling a script is a best-effort attempt. Commands can't be canceled after they have finished running or if they have expired.
  * Script files and responses that are saved in plain text are retained for seven days. Script files and responses that are saved in an Object Storage location are retained until you delete them.
  * Do not run a script that causes the Oracle Cloud Agent software or the Compute Instance Run Command plugin to stop.


## Running Commands with Administrator Privileges 🔗 
If a command requires administrator permissions, you must grant administrator permissions to the Compute Instance Run Command plugin to be able to run the command. The plugin runs as the `ocarun` user.
You can [use cloud-init (cloudbase-init on Windows) to configure permissions at instance launch](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service."), or [connect to an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm#top "You can connect to a running compute instance by using a Secure Shell \(SSH\) or Remote Desktop connection.") after it has launched and configure permissions manually. The steps to grant administrator permissions depend on the operating system.
### To grant sudo permissions on Linux instances 🔗 
  1. On the instance, create a sudoers configuration file for the Compute Instance Run Command plugin:
Copy
```
vi ./101-oracle-cloud-agent-run-command
```

  2. Allow the `ocarun` user to run all commands as sudo by adding the following line to the configuration file:
Copy
```
ocarun ALL=(ALL) NOPASSWD:ALL
```

You can optionally list specific commands. See the Linux man page for `sudoers` for more information.
  3. Validate that the syntax in the configuration file is correct:
Copy
```
visudo -cf ./101-oracle-cloud-agent-run-command
```

If the syntax is correct, the follow message is returned:
```
./101-oracle-cloud-agent-run-command: parsed OK
```

  4. Add the configuration file to `/etc/sudoers.d`:
Copy
```
sudo cp ./101-oracle-cloud-agent-run-command /etc/sudoers.d/
```



### To grant administrator permissions on Windows instances 🔗 
  1. On the instance, run the following command in PowerShell:
Copy
```
Add-LocalGroupMember -Group "Administrators" -Member "NT SERVICE\OCARUN" | Restart-Service -Name OCARUN -Force
```



## Before You Begin 🔗 
  * The Compute Instance Run Command plugin must be enabled on the instance, and plugins must be running. For more information about how to enable and run plugins, see [Oracle Cloud Agent](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#manage-plugins).
  * You have prepared the script that you want to run. We recommend that you test the command in a non-production environment before deploying it on instances that run production workflows.
  * To provide the script file from an Object Storage location, [Upload the image file to an Object Storage bucket](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects.htm) in the same region as the target instance. Note the bucket and file name, or the Object Storage URL for the file. To use the same command across tenancies, create a [pre-authenticated request URL](https://docs.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm) that points to the file.
  * To save the command output to an Object Storage location, create a bucket to save it in, in the same region as the target instance. Note the bucket name or the Object Storage URL for the bucket. You can optionally save the command output using a pre-authenticated request that points to an Object Storage location.
  * For platform images that were released before October 2020, the [Oracle Cloud Agent software must be updated](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins.htm#update-agent) to a version that supports the Compute Instance Run Command plugin (version 1.5.1 or later).


## Using the Console 🔗 
[To create a command to run on an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/runningcommands.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Under **Resources** , click **Run command**.
  4. Click **Create command**.
  5. Enter a name for the command. Avoid entering confidential information.
  6. In the **Timeout in seconds** box, enter the amount of time to give the Compute Instance Run Command plugin to run the command on the instance before timing out. The timer starts when the plugin starts the command. For no timeout, enter 0.
  7. In the **Add script** section, upload the script that you want the Compute Instance Run Command plugin to run on the instance. Select one of the following options:
     * **Paste script:** Paste the command in the box.
     * **Select a file:** Upload the script as a text (.txt) file. Either browse to the file that you want to upload, or drag and drop the file into the box.
     * **Import from an Object Storage bucket:** Select the bucket that contains the script file. In the **Object name** box, enter the file name.
     * **Import from an Object Storage URL:** Enter the Object Storage URL for the script file.
  8. In the **Output type** section, select the location to save the output of the command:
     * **Output as text:** The output is saved as plain text. You can review the output on the Instance Details page.
     * **Output to an Object Storage bucket:** The output is saved to an Object Storage bucket. Select a bucket. In the **Object name** box, enter a name for the output file. Avoid entering confidential information.
     * **Output to an Object Storage URL:** The output is saved to an Object Storage URL. Enter the URL.
  9. Click **Create command**.


[To view the output of a command](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/runningcommands.htm)
If the command output was saved to an Object Storage location, either [download the response object from the bucket](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects_topic-To_download_an_object_from_a_bucket.htm) where it was saved or navigate to the Object Storage pre-authenticated request URL.
If the command output was saved as a plain text file, do the following:
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Under **Resources** , click **Run command**.
  4. Find the command in the list, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **View command details**.


[To cancel a command](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/runningcommands.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Under **Resources** , click **Run command**.
  4. Find the command in the list, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Cancel command**. Confirm when prompted.


## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use these API operations to work with the run command feature:
  * [CreateInstanceAgentCommand](https://docs.oracle.com/iaas/api/#/en/instanceagent/latest/InstanceAgentCommand/CreateInstanceAgentCommand)
  * [GetInstanceAgentCommand](https://docs.oracle.com/iaas/api/#/en/instanceagent/latest/InstanceAgentCommand/GetInstanceAgentCommand)
  * [GetInstanceAgentCommandExecution](https://docs.oracle.com/iaas/api/#/en/instanceagent/latest/InstanceAgentCommandExecution/GetInstanceAgentCommandExecution)
  * [ListInstanceAgentCommands](https://docs.oracle.com/iaas/api/#/en/instanceagent/latest/InstanceAgentCommandSummary/ListInstanceAgentCommands)
  * [ListInstanceAgentCommandExecutions](https://docs.oracle.com/iaas/api/#/en/instanceagent/latest/InstanceAgentCommandExecutionSummary/ListInstanceAgentCommandExecutions)
  * [CancelInstanceAgentCommand](https://docs.oracle.com/iaas/api/#/en/instanceagent/latest/InstanceAgentCommand/CancelInstanceAgentCommand)


## Troubleshooting the Compute Instance Run Command Plugin 🔗 
To troubleshoot the Compute Instance Run Command plugin, you can view the logs that the plugin generates. [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm#top "You can connect to a running compute instance by using a Secure Shell \(SSH\) or Remote Desktop connection.") and then use the following:
Copy
```
tail -f /var/log/oracle-cloud-agent/plugins/runcommand/runcommand.log
```

For easier visibility into the plugin's operations without having to connect to the instance, you can [create custom logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/custom_logs.htm) using the Oracle Cloud Infrastructure Logging service.
### Log Errors 🔗 
This section describes how to resolve errors that appear in the log file.
#### Failure to Poll
If the Compute Instance Run Command plugin is failing to poll for commands, you might see the following error in the log file:
`poll command err: circuitbreaker:[pollCommand] is open, last err:Service error:NotAuthorizedOrNotFound. Authorization failed or requested resource not found. http status code: 404.`
This error can occur when the dynamic group policy for the run command feature is not enabled or if the instance was recently added to the dynamic group. Instances don't belong to tenancy administrator groups by default, so you need to explicitly [set dynamic group permissions](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances.htm#run-command) for the instance.
When you create an instance and then add it to a dynamic group, it takes up to 30 minutes for the instance to start to poll for commands. If you create the dynamic group first and then create the instance, the instance starts to poll for commands as soon as the instance is created.
To test the dynamic group policy as soon as you add the instance to a dynamic group, restart the service manually using one of the following commands:
**Oracle Linux 7.x and Oracle Linux 8.x**
Copy
```
sudo systemctl restart oracle-cloud-agent
```

**Windows Server**
Copy
```
net restart ocarun
```

Was this article helpful?
YesNo


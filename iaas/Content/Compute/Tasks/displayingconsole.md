Updated 2025-02-13
# Displaying the Console History for an Instance
You can capture and display recent serial console data for an instance. The data includes configuration messages that occur when the instance boots, such as kernel and BIOS messages, and is useful for checking the status of the instance or diagnosing and troubleshooting problems.
The console history captures up to a megabyte of the most recent serial console data for the specified instance. Note that the _raw_ console data, including multi-byte characters, is captured.
The console history is a point-in-time record. To troubleshoot a malfunctioning instance using an interactive console connection, use a [serial console connection or a VNC console connection](https://docs.oracle.com/en-us/iaas/Content/Compute/References/serialconsole.htm#Instance_Console_Connections).
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: The policy in [Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances) includes the ability to manage console history data. If the specified group doesn't need to launch instances or attach volumes, you could simplify that policy to include only `manage instance-family`, and remove the statements involving `volume-family` and `virtual-network-family`.
## Tagging Resources 🔗 
Apply tags to resources to help organize them according to business needs. Apply tags at the time you create a resource, or update the resource later with the wanted tags. For general information about applying tags, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
## Managing Console History Data 🔗 
You can use the Console, CLI, or API to manage console history captures. Console history lets you see serial output from your instance without having to connect to the instance remotely. You can use this information to troubleshoot instance access issues.
### Using the Console 🔗 
On the instance details page in the Console, you can capture and download console histories, view and edit metadata details, and delete console history captures.
[To capture the console history](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Under **Resources** , click **Console history**.
  4. Click **View current history**.
  5. Enter an optional name for the console history. Avoid entering confidential information.
  6. **Show tagging options:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
  7. To download a copy of the console history, click **Download**.
  8. Click **Save and close**.


[To download console history captures](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Under **Resources** , click **Console history**.
  4. In the console history list, for the console history capture that you want to download, click the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), click **Download** , and then save the file.


[To view console history captures](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Under **Resources** , click **Console history**.
  4. In the console history list, for the console history capture that you want to view, click the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **View details**.


[To view and edit the metadata details of a console history capture](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Under **Resources** , click **Console history**.
  4. In the console history list, click the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) next to the console history, and then click **View details**.
  5. Optionally, edit the name for the console history. Avoid entering confidential information.
  6. To view or edit tags, click **Show tagging options**.
  7. To edit or remove tags, click the edit icon next to the tag. To edit a tag, in the **Edit Tag** dialog, make any changes, and then click **Save**. To remove a tag, click **Remove Tag**.
  8. Click **Save and close**.


[To delete console history captures](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Under **Resources** , click **Console history**.
  4. In the console history list, for the console history capture that you want to delete, click the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Delete**.
  5. In the confirmation dialog, click **Delete console history**.


### Using the CLI 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). To manage the serial console logs using the CLI, open a command prompt and run any of the following commands.
**Note** When using the CLI to capture the instance's serial console data history, include the following option to ensure that full history is captured. Without this option, the data might be truncated: `--length 10000000`.
[To capture the console history](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole.htm)
Use the [compute console-history capture](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/console-history/capture.html) command:
```
oci compute console-history capture --instance-id <instance-id>
```

See the CLI online help for a list of options:
```
oci compute console-history capture --help
```

[To get the metadata details of a console history capture](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole.htm)
Use the [compute console-history get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/console-history/get.html) command:
```
oci compute console-history get --instance-console-history-id <instance-console-history-id>
```

See the CLI online help for a list of options:
```
oci compute console-history get --help
```

[To get the details of console history content](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole.htm)
Use the [compute console-history get-content](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/console-history/get-content.html) command:
```
oci compute console-history get-content --file <file_name> --instance-console-history-id <instance-console-history-id>
```

See the CLI online help for a list of options:
```
oci compute console-history get-content --help
```

[To edit console history metadata](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole.htm)
Use the [compute console-history update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/console-history/update.html) command:
```
oci compute console-history update --instance-console-history-id <instance-console-history-id>
```

See the CLI online help for a list of options:
```
oci compute console-history update --help
```

[To list console history captures](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole.htm)
Use the [compute console-history list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/console-history/list.html) command:
```
oci compute console-history list --compartment-id <COMPARTMENT_OCID>
```

See the CLI online help for a list of options:
```
oci compute console-history list --help
```

[To delete console history captures](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole.htm)
Use the [compute console-history](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/console-history/delete.html) delete command:
```
oci compute console-history delete --instance-console-history-id <instance-console-history-id>
```

See the CLI online help for a list of options:
```
oci compute console-history delete --help
```

### Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following API operations to manage the console history data.
  * To capture the console history, use the [CaptureConsoleHistory](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ConsoleHistory/CaptureConsoleHistory) method.
  * To get details of console history metadata, use the [GetConsoleHistory](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ConsoleHistory/GetConsoleHistory) method.
  * To get the details of console history content, use the [GetConsoleHistoryContent](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ConsoleHistory/GetConsoleHistoryContent) method.
  * To edit console history metadata, use the [UpdateConsoleHistory](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ConsoleHistory/UpdateConsoleHistory) method.
  * To list console history captures, use the [ListConsoleHistories](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ConsoleHistory/ListConsoleHistories) method.
  * To delete console history captures, use the [DeleteConsoleHistory](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ConsoleHistory/DeleteConsoleHistory) method.


Was this article helpful?
YesNo


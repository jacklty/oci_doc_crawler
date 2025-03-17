Updated 2024-03-22
# Checking if a Volume Attachment is Multipath-Enabled
When you attach a volume configured for the **Ultra High Performance** level, the volume attachment must be enabled for multipath to optimize the volume's performance. This topic describes how to verify if the volume attachment is multipath-enabled.
If the volume attachment is not multipath-enabled, but the volume's performance level is configured for **Ultra High Performance** , see [Troubleshooting Ultra High Performance Volume Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/troubleshootingmultipathattachments.htm#troubleshootuhp "This topic covers troubleshooting steps you can take as well as prerequisites to verify for volumes configured for the Ultra High Performance level where either the volume fails to attach or the volume attachment is not multipath-enabled.") for steps you can take to address the issue. 
## Using the Console 🔗 
You can check whether a volume attachment is multipath-enabled in the Console from the **Volume Details** page or the **Instance Details** page. 
### From the Volume Details Page
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
  2. Click the block volume that you want to check the volume attachment for.
  3. Click **Attached Instances** in the **Resources** section.
  4. Check the value displayed in the **Multipath** column. 
     * **Yes** : The volume is configured for the **Ultra High Performance** level and the volume attachment is multipath-enabled. No further action is required.
     * **No** : The volume is not configured for the **Ultra High Performance** level, the volume does not need to be multipath-enabled. No further action is required.
     * **No** with a warning icon: The volume is configured for the **Ultra High Performance** level, but the volume attachment is not multipath-enabled. To achieve optimal performance, you need to ensure the volume is attached to a supported instance shape, and that the required prerequisites are configured.


### From the Instance Details Page
  1. Open the navigation menu and click **Compute**. Under **Compute** , click **Instances**.
  2. Click the instance that you want to check the volume attachment for.
  3. Click **Attached Block Volumes** in the **Resources** section.
  4. Check the value displayed in the **Multipath** column. 
     * **Yes** : The volume is configured for the **Ultra High Performance** level and the volume attachment is multipath-enabled. No further action is required.
     * **No** : The volume is not configured for the **Ultra High Performance** level, the volume does not need to be multipath-enabled. No further action is required.
     * **No** with a warning icon: The volume is configured for the **Ultra High Performance** level, but the volume attachment is not multipath-enabled. To achieve optimal performance, you need to ensure the volume is attached to a supported instance shape, and that the required prerequisites are configured.


The following image shows the multipath column in the Console.
[![Multipath column values in the Console.](https://docs.oracle.com/en-us/iaas/Content/Block/Images/multipathcolumn.png)](https://docs.oracle.com/en-us/iaas/Content/Block/Images/multipathcolumn.png)
## Using the CLI 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). Use the `volume-attachment get` operation to check whether the volume attachment is multipath-enabled. 
Open a command prompt and run:
Command
CopyTry It
```
oci compute volume-attachment get --volume-attachment-id <volume-group-ID>
```

For example:
Command
CopyTry It
```
oci compute volume-attachment get --volume-attachment-id ocid1.volumeattachment.oc1.phx.<unique_ID>
```

The `is-multipath` property will be true for multipath-enabled attachments; false for attachments that are not multipath-enabled.
## Using the API 🔗 
To check whether the volume attachment is multipath-enabled, use the following operation:
  * [GetVolumeAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/GetVolumeAttachment)


The attachment is enabled for multipath if the `isMultipath` property is true.
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Was this article helpful?
YesNo


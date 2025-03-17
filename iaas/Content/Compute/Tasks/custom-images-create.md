Updated 2025-02-27
# Creating Custom Images
Create a Compute custom image in an Oracle Cloud Infrastructure compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-create.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-create.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/custom-images-create.htm)


  *     1. If you're creating a custom image from a Windows instance: [Connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm#top "You connect to a Windows instance by using a Remote Desktop connection. Most Windows systems include a Remote Desktop client by default.") by using a Remote Desktop connection and shut down the instance from the operating system.
    2. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    3. Select the instance that you want to use as the basis for the custom image.
    4. Select **More Actions** , and then select **Create custom image**.
    5. In the **Create in compartment** list, select the compartment to create the custom image in.
    6. Enter a **Name** for the image. You can change the name later, if needed. You cannot use the name of a platform image for a custom image. Avoid entering confidential information.
    7. **Show tagging options:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    8. Click **Create custom image**.
To track the progress of the operation and [troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances-monitoring-work-requests.htm#work-requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") that occur during instance creation, use the associated [work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
**Note**
If you see a message indicating that you are at the limit for custom images, you must delete at least one image before you can create another. Or, you can [request a service limit increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti).
  * Use the [image create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/image/create.html) command and required parameters to create a custom image:
Copy
```
oci compute image create --from-json <file://path/to/file.json>
```

<file://path/to/file.json> is the path to a JSON file that defines the instance details. For information about how to generate an example of the JSON file, see [Advanced JSON Options](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON).
For a complete list of flags and variable options for the Compute service CLI commands, see the [command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use this API operation to create an instance:
    * [CreateImage](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Image/CreateImage)


Was this article helpful?
YesNo


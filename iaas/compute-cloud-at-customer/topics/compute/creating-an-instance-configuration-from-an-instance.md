Updated 2024-08-06
# Creating an Instance Configuration from an Instance
On Compute Cloud@Customer you can create an instance configuration by using the configuration information from an existing compute instance.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-configuration-from-an-instance.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-configuration-from-an-instance.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-configuration-from-an-instance.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    2. At the top of the page, select the compartment that contains the instance that you want to use to create the new instance configuration.
    3. Click the name of the instance that you want to use to create the new instance configuration.
    4. On the instance details page, click **Controls** (upper right corner), then click **Create Instance Configuration**.
    5. In the **Create Instance Configuration** dialog box, enter the following information:
       * **Name:** Enter a name for the instance configuration.
       * **Compartment:** Select the compartment where this instance configuration will be created.
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    6. Click **Create Instance Configuration**.
  * Use the [oci compute-management instance-configuration create-from-instance](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-configuration/create-from-instance.html) command and required parameters to create an instance configuration by using the configuration information from an existing compute instance.
Copy
```
oci compute-management instance-configuration create-from-instance --compartment-id <compartment_OCID> --instance-id <instance_OCID> --display-name <IC_name>
```

The specified compartment is where this instance configuration is created.
The specified display name is the name of the instance configuration. If you don't provide a value for the `--display-name` option, the default name of the instance configuration is `instanceconfiguration**_YYYYMMDDhhmmss_**`, where`** _YYYYMMDDhhmmss_**`is the creation date and time.
The output of this command is the same as the output of the `instance-configuration get` command.
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateInstanceConfiguration](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceConfiguration/CreateInstanceConfiguration) operation to create an instance configuration using an instance.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


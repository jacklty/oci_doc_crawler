Updated 2024-01-18
# Using an Instance Configuration to Create an Instance
On Compute Cloud@Customer, you can use an instance configuration to launch a compute instance.
This method of launching a compute instance is an alternative to the method described in [Creating an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance.htm#creating-an-instance "On Compute Cloud@Customer, you can create an instance using the Compute Cloud@Customer Console, CLI, and API.").
The name of the instance is determined as follows:
  * If the instance configuration specifies a value for the `displayName` property, the name of the instance will be `displayName`. If you use the same instance configuration with multiple `launch-compute-instance` commands, all instances will have the same name. Instance names aren't required to be unique.
  * If the instance configuration doesn't specify a value for the `displayName` property, the default name of the instance will be `instance**_YYYYMMDDhhmmss_**`, where`** _YYYYMMDDhhmmss_**`is the creation date and time.


Avoid entering confidential information in names.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/using-an-instance-configuration-to-create-an-instance.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/using-an-instance-configuration-to-create-an-instance.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/using-an-instance-configuration-to-create-an-instance.htm)


  * This task can't be performed using the Console.
  * Use the [oci compute-management instance-configuration launch-compute-instance](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-configuration/launch-compute-instance.html) command and required parameters to change the instance configuration name or tags.
Copy
```
oci compute-management instance-configuration launch-compute-instance [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [GetInstanceConfiguration](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceConfiguration/GetInstanceConfiguration) operation to change the instance configuration name or tags.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


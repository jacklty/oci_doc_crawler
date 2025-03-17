Updated 2024-11-07
# Updating an Instance Configuration
On Compute Cloud@Customer, you can change the instance configuration name, compartment, and tags. 
**Note**
To change other configuration details such as the subnet, or image, create a new instance configuration. See [Creating an Instance Configuration](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-configuration.htm#creating-an-instance-configuration "On Compute Cloud@Customer, you can create an instance configuration from an existing instance \(a template instance\) or by entering the individual configuration settings.").
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-an-instance-configuration.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-an-instance-configuration.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-an-instance-configuration.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instance Configurations**.
    2. At the top of the page, select the compartment that contains the instance configuration that you want to update.
    3. For the instance configuration that you want to update, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), and click **Edit**.
    4. In the **Update Instance Configuration** dialog box, make the changes.
    5. Click **Update Instance Configuration**.
  * Use the [oci compute-management instance-configuration update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-configuration/update.html) command and required parameters to change the instance configuration name or tags.
Copy
```
oci compute-management instance-configuration update --instance-configuration-id <compartment_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateInstanceConfiguration](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceConfiguration/UpdateInstanceConfiguration) operation to change the instance configuration name or tags.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


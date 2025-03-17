Updated 2023-08-28
# Updating Instance Configurations
You can edit the name of instance configurations. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstanceconfig.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstanceconfig.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstanceconfig.htm)


  * #### To update an instance configuration 🔗 
    1. Open the navigation menu and click **Compute**. Under **Compute** , click **Instance Configurations**. 
    2. Click the instance configuration that you're interested in.
    3. Click **Edit**.
    4. For **Name** , enter a new name. Avoid entering confidential information. Then, click **Save changes**.
  * For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
To update an instance configuration using the CLI, open a command prompt and run the [instance-configuration update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-configuration/update.html) command:
Command
CopyTry It
```
oci compute-management instance-configuration update --instance-configuration-id <INSTANCE_CONFIGURATION_OCID> --display-name <text>
```

  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
    * Use the [UpdateInstanceConfiguration](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceConfiguration/UpdateInstanceConfiguration) operation to update an instance configuration.


Was this article helpful?
YesNo


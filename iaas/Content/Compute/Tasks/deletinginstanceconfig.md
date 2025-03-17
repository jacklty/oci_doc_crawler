Updated 2023-08-28
# Deleting Instance Configurations
You can permanently delete instance configurations that you no longer need. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstanceconfig.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstanceconfig.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstanceconfig.htm)


  * #### To delete an instance configuration 🔗 
    1. Open the navigation menu and click **Compute**. Under **Compute** , click **Instance Configurations**. 
    2. Click the instance configuration that you're interested in.
    3. Click **Delete** , and then confirm when prompted.
  * For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
To delete an instance configuration using the CLI, open a command prompt and run the [instance-configuration delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-configuration/delete.html) command:
Command
CopyTry It
```
oci compute-management instance-configuration delete --instance-configuration-id <INSTANCE_CONFIGURATION_OCID>
```

  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
    * Use the [DeleteInstanceConfiguration](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceConfiguration/DeleteInstanceConfiguration) operation to delete an instance configuration.


Was this article helpful?
YesNo


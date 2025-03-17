Updated 2025-02-03
# Editing Custom Instance Display and Instance Host Names
Change custom instance display name and host name for instances you create in an instance pool.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-renaming-custom-display-host-names.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-renaming-custom-display-host-names.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-renaming-custom-display-host-names.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instance Pools**.
    2. In the **List scope** section, select the compartment that contains the instance pool that you want to update.
    3. Click the name of the instance pool that you want to edit to display the details page.
    4. Click **Edit**.
    5. In the **Instance display name formatter** field, enter a new text string that includes lowercase alphanumeric characters, symbols, and dashes. The name must include the `${launchCount}` token. For example: `my-string-${launchCount}`.
    6. In the **Instance host name formatter** field, enter a new text string that includes lowercase alphanumeric characters, symbols, and dashes. The name must include the `${launchCount}` token. For example: `my-string-${launchCount}`.
    7. Click **Save**.
  * Use the [instance-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/update.html) command to change the custom display name for instances you create in an instance pool.
Copy
```
oci compute-management instance-pool update --instance-pool-id <INSTANCE_POOL_OCID> --display-name <INSTANCE_POOL_NAME>
```

For a complete list of flags and variable options for the Compute Service CLI commands, see the [command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [UpdateInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/UpdateInstancePool) operation to change the custom display name for instances you create in an instance pool.


Was this article helpful?
YesNo


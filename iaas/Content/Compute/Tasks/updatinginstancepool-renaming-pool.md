Updated 2025-02-03
# Renaming an Instance Pool
Rename an instance pool without changing its Oracle Cloud Identifier (OCID).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-renaming-pool.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-renaming-pool.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-renaming-pool.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instance Pools**.
    2. In the **List scope** section, select the compartment that contains the instance pool that you want to edit.
    3. Click the name of the instance pool that you want to rename to display the details page.
    4. Click **Edit**.
    5. Enter a new name for the instance pool in the **Name** field. Avoid entering confidential information.
    6. Click **Save**.
  * Use the [instance-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/update.html) command to rename an instance pool.
Copy
```
oci compute-management instance-pool update --instance-pool-id <INSTANCE_POOL_OCID> --display-name <INSTANCE_POOL_NAME>
```

For a complete list of flags and variable options for the Compute Service CLI commands, see the [command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [UpdateInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/UpdateInstancePool) operation to rename an instance pool.


Was this article helpful?
YesNo


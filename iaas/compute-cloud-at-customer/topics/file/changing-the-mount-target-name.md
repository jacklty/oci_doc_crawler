Updated 2024-08-06
# Updating a Mount Target
On Compute Cloud@Customer, when you update a mount target, you can set or change the Network Security Groups and display name. You can't change the backing store pool type assignment (default or high performance).
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/changing-the-mount-target-name.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/changing-the-mount-target-name.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/changing-the-mount-target-name.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **File Storage** , then click **Mount Targets**.
    2. At the top of the page, select the compartment that contains the mount target.
    3. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) for the mount target, and select **Edit**.
    4. Make changes.
    5. Click **Save**.
  * Use the [oci fs mount-target update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/update.html) command and required parameters to change the mount target.
Copy
```
oci fs mount-target update --mount-target-id <mount_target_OCID> <parameters to change> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/UpdateMountTarget) command and required parameters to update a mount target.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


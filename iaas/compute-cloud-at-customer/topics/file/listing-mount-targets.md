Updated 2024-08-06
# Listing Mount Targets and Viewing Details
On Compute Cloud@Customer, you can list File System mount targets.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/listing-mount-targets.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/listing-mount-targets.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/listing-mount-targets.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **File Storage** , then click **Mount Targets**.
    2. At the top of the page, select the compartment that contains the mount target.
The mount targets are displayed.
    3. To see the mount target details, click the mount target name.
  * **Listing Mount Targets**
Use the [oci fs mount-target list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/list.html) command and required parameters to list the mount target resources in the specified compartment.
Copy
```
oci fs mount-target list --availability-domain <availability_domain_name> --compartment-id <compartment_id> [OPTIONS]
```

**Listing Details About a Mount Target**
Use the [oci fs mount-target get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/get.html) command and required parameters to get the specified mount target’s information.
Copy
```
oci fs mount-target get --mount-target-id <mount-target_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListMountTargets](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTargetSummary/ListMountTargets) operation to list the mount target resources in the specified compartment.
Use the [GetMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/GetMountTarget) operation to get the specified mount target’s information.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


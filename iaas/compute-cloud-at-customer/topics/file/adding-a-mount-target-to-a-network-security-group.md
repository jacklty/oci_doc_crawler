Updated 2024-01-18
# Adding a Mount Target to a Network Security Group
On Compute Cloud@Customer, you can add the mount target to one or more Network Security Groups (NSGs). File storage requires specific rules to be configured for NSGs that are associated with mount targets.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/adding-a-mount-target-to-a-network-security-group.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/adding-a-mount-target-to-a-network-security-group.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/adding-a-mount-target-to-a-network-security-group.htm)


  *     1. Ensure that an NSG with ingress and egress rules has been configured. See [Configuring VCN Security Rules for File Storage](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/configuring-vcn-security-rules-for-file-storage.htm#configuring-vcn-security-rules-for-file-storage "On Compute Cloud@Customer, you can add the required rules to a preexisting security list associated with a subnet, such as the default security list that is created along with the VCN.").
    2. Ensure that a mount target is created. See [Creating a Mount Target](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-mount-target.htm#creating-a-mount-target "On Compute Cloud@Customer, A mount target is an NFS endpoint assigned to a subnet of your choice. The mount target provides the IP address or DNS name that's used in the mount command when connecting NFS clients to a file system.").
    3. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **File Storage** , then click **Mount Targets**.
    4. At the top of the page, select the compartment that contains the mount target.
    5. Click the mount target name to see the details page.
    6. Click **Edit**.
    7. Enable Network Security Groups.
    8. Select the NSG from the list.
    9. Click **Save Changes**.
  * Use the [oci fs mount-target update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/update.html) command and required parameters to update the specified mount target’s information.
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
Copy
```
oci fs mount-target update --mount-target-id <mount_target_OCID> --nsg-ids '["<nsg1_OCID>","i"]' [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/UpdateMountTarget) operation to update the specified mount target’s information.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


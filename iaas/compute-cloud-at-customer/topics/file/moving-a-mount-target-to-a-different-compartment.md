Updated 2024-11-07
# Moving a Mount Target to a Different Compartment
On Compute Cloud@Customer, you can move a Mount Target to a different compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/moving-a-mount-target-to-a-different-compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/moving-a-mount-target-to-a-different-compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/moving-a-mount-target-to-a-different-compartment.htm)


  * This task isn't available in the Console.
  * Use the [oci fs mount-target change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/change-compartment.html) command and required parameters to move a mount target to a different compartment.
Copy
```
oci fs mount-target change-compartment --mount-target-id <mount_target_OCID> --compartment-id <destination_compartment_OCID>
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * This task is not available in the API. 
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


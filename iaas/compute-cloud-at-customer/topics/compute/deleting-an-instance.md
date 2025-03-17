Updated 2024-12-16
# Deleting an Instance
On Compute Cloud@Customer, you can delete instances using the Compute Cloud@Customer Console, CLI, and API.
By default, the boot volume of the instance is preserved when you delete (terminate) the instance. You can attach the boot volume to a different instance as a data volume, or use it to create a new instance. 
You have the option to permanently delete the attached boot volume when you delete the instance. If you preserve the attached boot volume and then later decide to permanently delete the volume, see [Deleting a Boot Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/deleting-a-boot-volume.htm#deleting-a-boot-volume "On Oracle Cloud Infrastructure, you can delete a boot volume that's detached from an instance.").
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/deleting-an-instance.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/deleting-an-instance.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/deleting-an-instance.htm)


  *     1. On the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") **Dashboard** , in the **Compute** block, click **Instances**.
    2. At the top of the page, select the compartment that contains the instance you want to delete.
    3. Click the name of the instance you want to delete. 
    4. On the instance details page, click **Controls** (upper right corner), then click **Terminate**.
    5. On confirmation dialog box, do one of the following actions:
       * To keep the boot volume: Leave the slider in the default position.
       * To permanently delete the boot volume: Move the slider to the right.
    6. Click **Confirm**.
    7. Under **Resources** , click **Work Request(s)** to check the status of the termination. 
After the TerminateInstance operation is 100% complete and in state Succeeded, the instance remains visible in the instance list in state Terminated for at least 24 hours, up to 24.5 hours. No further action is needed to terminate the instance.
  * Use the [oci compute instance terminate](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/terminate.html) command and required parameters to delete the specified instance.
Copy
```
oci compute instance terminate --instance-id <instance_OCID> [OPTIONS]
```

To permanently delete the attached boot volume when the instance is terminated, specify `--preserve-boot-volume false` on the command line.
Use the `work-requests work-request get` command to check the status of the instance terminate. After the `TerminateInstance` operation is `percent-complete` `100.0` and `status` `SUCCEEDED`, the instance remains visible in instance `list` or `get` in `lifecycle-state` `TERMINATED` for at least 24 hours, up to 24.5 hours. No further action is needed to terminate the instance.
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [TerminateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/TerminateInstance) operation to delete the specified instance.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


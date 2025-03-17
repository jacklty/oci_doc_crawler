Updated 2025-02-13
# Performing a Diagnostic Reboot
Use a diagnostic reboot to rebuild an unreachable compute virtual machine (VM) instance when other troubleshooting steps aren't successful.
During a diagnostic reboot, the instance is stopped, rebuilt, and restarted. A short downtime occurs during the reboot process. Instance properties such as private and ephemeral public IP addresses, attached block volumes, and virtual network interface cards (VNICs) are preserved.
**Important** Before you send a diagnostic reboot, restart the instance's OS and confirm that the instance is configured correctly. See the [Compute troubleshooting suggestions](https://docs.oracle.com/en-us/iaas/Content/Compute/References/troubleshooting-compute-instances.htm#troubleshooting-compute-instances) and [Networking troubleshooting suggestions](https://docs.oracle.com/iaas/Content/Network/Concepts/troubleshooting.htm). Use diagnostic reboot as a final attempt to troubleshoot an unreachable instance.
## Required IAM policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: The policy in [Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances) includes the ability to perform a diagnostic reboot on an instance. If the specified group doesn't need to launch instances or attach volumes, you could simplify that policy to include only `manage instance-family`, and remove the statements involving `volume-family` and `virtual-network-family`.
If you're new to policies, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for Core Services](https://docs.oracle.com/iaas/Content/Identity/Reference/corepolicyreference.htm). 
## Before You Begin 🔗 
  * Ensure that any block volumes defined in `/etc/fstab` use the [recommended options](https://docs.oracle.com/iaas/Content/Block/References/fstaboptions.htm).
  * Ensure that any File Storage service (NFS) mounts use the `nofail` option.
  * If you use the [Oracle-provided script](https://github.com/oracle/terraform-examples/blob/master/examples/oci/connect_vcns_using_multiple_vnics/scripts/secondary_vnic_all_configure.sh) to configure secondary VNICs, ensure it runs automatically at startup.


## Supported Shapes 🔗 
All VM [shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes) except shapes in the dense I/O series support diagnostic reboots.
## Using the Console 🔗 
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Click **More Actions** , and then click **Send diagnostic reboot**.
  4. Review the confirmation message and then click **Send diagnostic reboot**.


## Using the API 🔗 
Use the [InstanceAction](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/InstanceAction) operation, passing the value `DIAGNOSTICREBOOT` as the action to perform.
## Using the CLI 🔗 
Open a command prompt and run the [instance action](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/action.html) command:
Command
CopyTry It
```
oci compute instance action --action DIAGNOSTICREBOOT --instance-id <INSTANCE_OCID>
```

Was this article helpful?
YesNo


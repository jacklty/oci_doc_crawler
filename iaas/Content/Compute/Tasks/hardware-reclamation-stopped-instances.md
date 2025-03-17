Updated 2023-05-16
# Hardware Reclamation for Stopped Bare Metal Instances
When an Oracle Cloud Infrastructure Compute bare metal instance remains in the stopped state for longer than 48 hours, the instance is taken offline and the physical hardware is reclaimed.
The next time that you [restart the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm#restart-instance), it starts on different physical hardware. There are no changes to the block volumes, boot volumes, and instance metadata, including the ephemeral and public IP addresses.
However, the following properties do change when a bare metal instance restarts on different physical hardware: the MAC addresses and the host serial number. You might also notice changes in the BIOS firmware version, BIOS settings, and CPU microcode.
If you want to keep the same physical hardware, do not [stop the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm#stop-instance) using the Console or the API, SDKs, or CLI. Instead, shut down the instance [using the instance's OS](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm#operatingsystem). When you want to restart the instance, use the Console or the API, SDKs, or CLI.
This behavior applies to Linux instances that use the following [shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes):
  * BM.Standard1.36
  * BM.Standard.B1.44
  * BM.Standard2.52
  * BM.Standard3.64
  * BM.Standard.E2.64
  * BM.Standard.E3.128
  * BM.Standard.E4.128
  * BM.Standard.A1.160


Was this article helpful?
YesNo


Updated 2024-08-06
# Compute Instance Lifecycle
On Compute Cloud@Customer, a compute instance can be in a variety of different lifecycle states.
This list describes the different lifecycle states for compute instances.
  * **Launching:** Occurs when you create a compute instance. The instance is displayed in the Compute Cloud@Customer Console in a provisioning state. Expect provisioning to take several minutes before the state updates to running. After the instance is running, wait another few minutes for the OS to boot before you attempt to connect.
  * **Connecting:** You connect to a running Linux or Oracle Solaris instance using a Secure Shell (SSH) connection. Most Linux and UNIX-like OSs include an SSH client by default. 
  * **Backing up the boot volume:** You can back up the boot volume using the Block Volume backup feature using one of these methods:
    * **Manual backups:** You manually perform create, get, list, rename, and delete backup commands.
    * **Automatic backups:** You create a backup policy and a backup policy assignment that specifies the time and frequency of the volume backups. The system automatically performs the commands that back up the volume.
  * **Stopping:** You can stop an instance using the Compute Cloud@Customer Console, CLI, and API, or by using the commands available in the OS when you are logged in to the instance. 
If the applications that run on the instance take more than 15 minutes to shut down, they could be improperly stopped. To avoid this situation, shut down the instance using the commands available in the OS before you stop the instance.
  * **Starting or restarting:** You can start or restart an instance as needed using the Compute Cloud@Customer Console, CLI, and API.
  * **Rebooting:** You can reboot an instance as needed using the Compute Cloud@Customer Console, CLI, and API. By default, a reboot gracefully restarts the instance by sending a shutdown command to the OS. After waiting 15 minutes for the OS to shut down, the instance is powered off and then powered back on.
  * **Terminating:** You can permanently terminate (delete) instances that you no longer need. Any attached VNICs and volumes are automatically detached when the instance terminates. Eventually, the instance's public and private IP addresses are released and become available for other instances.
By default, the instance's boot volume is preserved when you terminate the instance. You can attach the boot volume to a different instance as a data volume, or use it to launch a new instance. If you no longer need the boot volume, you can permanently delete it.


For more information, see [Working with Instances](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/working-with-instances.htm#working-with-instances "On Compute Cloud@Customer, you can create compute instances as needed to meet your compute and application requirements. After you create an instance, you can access it securely from your computer, restart it, attach and detach volumes, and delete it.").
Was this article helpful?
YesNo


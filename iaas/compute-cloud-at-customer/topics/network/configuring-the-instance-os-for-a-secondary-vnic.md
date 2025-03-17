Updated 2025-02-21
# Configuring the Instance OS for a Secondary VNIC
On Compute Cloud@Customer, after you create a secondary VNIC, log in to the instance OS and configure the OS to use the new VNIC.
For Oracle Linux and Microsoft Windows, you can use utilities and scripts that are provided by Oracle. The scripts use information from the instance metadata. See [Retrieving Instance Metadata from Within the Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/retrieving-instance-metadata-from-within-the-instance.htm#retrieving-instance-metadata-from-within-the-instance "On Compute Cloud@Customer, the Instance Metadata Service \(IMDS\) serves information about a running instance to users who are logged in to that instance. IMDS also provides information to cloud-init that you can use for various system initialization tasks.") for instructions about how to view that data on the instance OS, including how to show the VNIC data.
For other OSs, consult the OS documentation.
## Oracle Linux Instance OS Configuration 🔗 
Use the [ oci-network-config](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm#oci-network-config) utility to perform the OS configuration required for secondary VNICs on instances that run Oracle Linux.
## Microsoft Windows Instance OS Configuration 🔗 
You must configure the secondary VNIC within the OS. You can configure the secondary VNIC manually in the Microsoft Windows OS, or create a PowerShell script.
Ensure that the script includes these actions:
  * Check if the network interface has an IP address and a default route.
  * Enable the OS to recognize the secondary VNIC, the **script must overwrite the IP address and default route with static settings (which effectively disables DHCP).** The script should prompt you with a choice: to overwrite with the static settings, or exit.


**Overall Process to Add a Secondary VNIC**
  1. [Create and attach a secondary VNIC](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-and-attaching-a-secondary-vnic.htm#creating-and-attaching-a-secondary-vnic "On Compute Cloud@Customer, you can add more VNICs to an instance.") to the instance. Keep the VNIC OCID handy so you can provide it later when you run the configuration script. 
  2. [Connect to the instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/accessinginstance.htm) with Remote Desktop.
  3. Run your script as an administrator. 


## Oracle Solaris Instance OS Configuration 🔗 
Use the `ipadm` command to configure network interfaces persistently.
Was this article helpful?
YesNo


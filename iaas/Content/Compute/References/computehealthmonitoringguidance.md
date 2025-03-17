Updated 2024-02-09
# Compute Health Monitoring for Bare Metal Instances
Compute health monitoring for bare metal instances is a feature that provides notifications about hardware issues with your bare metal instances. With the health monitoring feature, you can monitor the health of the hardware for your bare metal instances, including components such as the CPU, motherboard, DIMM, and NVMe drives. You can use the notifications to identify problems, letting you proactively redeploy your instances to improve availability.
Health monitoring notifications are emailed to the tenant administrator within one business day of the error occurring. This warning helps you to take action before any potential hardware failure and redeploy your instances to healthy hardware to minimize the impact on your applications.
You can also use the [infrastructure health metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructurehealthmetrics.htm#Infrastructure_Health_Metrics) available in the Monitoring service to create **alarms** and [notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm) based on hardware issues.
## Error Messages and Troubleshooting 🔗 
This section contains information about the most common health monitoring error messages and provides troubleshooting suggestions for you to try for a bare metal instance.
[An event in the data center environment has been detected, which is impacting this host](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computehealthmonitoringguidance.htm)
**Fault class:** `DC_ENVIRONMENT`
**Details:** DC_ENVIRONMENT is an event which is a data center issue and not a systems issue. Typically the issue is power or temperature related and is also live-repairable. 
Some examples of issues that can cause this type of issue are fan failure on a server, a power supply unit failure, or the air conditioning fails in the data center.
[A fault in the GPU has been detected](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computehealthmonitoringguidance.htm)
**Fault class:** `GPU`
**Details:** This error indicates that at least one failed graphics processing unit (GPU) was detected on the instance while the instance was created or running.
**Troubleshooting steps:**
Try any one of the following troubleshooting options:
  * Install the OCI HPC/GPU diagnostic tool `dr-hpc`, which runs a series of commands that check hardware health.
Copy
```
wget https://objectstorage.eu-frankfurt-1.oraclecloud.com/p/tGXIZ_L6BR-yBp2BPXzGcNXYEhyLveHTLT0n1wg8Fdp4AH3-UjY77RlrXIOBJCSI/n/hpc/b/source/o/oci-dr-hpc-latest.el7.noarch.rpm
```

Copy
```
sudo yum install oci-dr-hpc-latest.el7.noarch.rpm
cd /opt/oci-hpc/oci-dr-hpc/
./oci-dr-hpc run-health-checks
```

  * Run `dcgm` diagnostic tools. (See [NVIDIA GPU Debug Guidelines](https://docs.nvidia.com/deploy/gpu-debug-guidelines/index.html))
Copy
```
dcgmi diag -r [1,2,3]
```

  * Collect the NVIDIA debug logs and grep for errors in the logs.
Copy
```
sudo /usr/bin/nvidia-bug-report.sh # This log can be sent to OCI Support for analysis
```



[A fault in the RDMA has been detected](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computehealthmonitoringguidance.htm)
**Fault class:** `RDMA`
**Details:** This error indicates that at least one RDMA network interface card (NIC) is degraded or faulty.
**Troubleshooting steps:**
Try any one of the following troubleshooting options:
  * Install the OCI HPC/GPU diagnostic tool `dr-hpc`, which runs a series of commands that check hardware health.
Copy
```
wget https://objectstorage.eu-frankfurt-1.oraclecloud.com/p/tGXIZ_L6BR-yBp2BPXzGcNXYEhyLveHTLT0n1wg8Fdp4AH3-UjY77RlrXIOBJCSI/n/hpc/b/source/o/oci-dr-hpc-latest.el7.noarch.rpm
```

Copy
```
sudo yum install oci-dr-hpc-latest.el7.noarch.rpm
cd /opt/oci-hpc/oci-dr-hpc/
./oci-dr-hpc run-health-checks
```

  * Run Mellanox debug commands for the NIC.
Copy
```
sudo su
mlx_devices=$(echo "$ibdev2netdev_output" | awk '/mlx5_[0-9]+.*==>/ && $2 ~ /mlx5_(0?[0-9]|1[0-9]|20)$/ { sub(/\([^\)]+\)$/, "", $NF); print $2 }')   for d in ${mlx_devices[@]}; do echo $d; mlxlink -d $d -c -m -e ; done
```



[A fault has been detected in one or more CPUs](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computehealthmonitoringguidance.htm)
**Fault class:** `CPU`
**Details:** This error indicates that a processor or one or more cores have failed in the instance. The instance might be inaccessible or there might be fewer available cores than expected.
**Troubleshooting steps:**
  * If the instance is inaccessible, you must replace it using the steps in [Live, Reboot, and Manual Migration: Moving a Compute Instance to a New Host](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#Moving_a_Compute_Instance_to_a_New_Host).
  * If the instance is available, check for the expected number of cores:
    * On Linux-based systems, run the following command:
Copy
```
nproc --all
```

    * On Windows-based systems, open Resource Monitor. 
Compare the core count to the expected values documented in [Compute Shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes). If the number of cores is less than expected and this reduction impacts your application, we recommend that you replace the instance using the steps in [Live, Reboot, and Manual Migration: Moving a Compute Instance to a New Host](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#Moving_a_Compute_Instance_to_a_New_Host).


[A fault in the memory subsystem was detected during instance launch or a recent reboot](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computehealthmonitoringguidance.htm)
**Fault class:** `MEM-BOOT`
**Details:** This error indicates that one or more failed DIMMs were detected in the instance while the instance was being launched or rebooted. Any failed DIMMs have been disabled.
**Troubleshooting steps:** The total amount of memory in the instance will be lower than expected. If this impacts your application, we recommend that you replace the instance using the steps in [Live, Reboot, and Manual Migration: Moving a Compute Instance to a New Host](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#Moving_a_Compute_Instance_to_a_New_Host).
To check for the amount of memory in the instance:
  * On Linux-based systems, run the following command:
Copy
```
awk '$3=="kB"{$2=$2/1024**2;$3="GB";} 1' /proc/meminfo | column -t | grep MemTotal
```

  * On Windows-based systems, open Resource Monitor. 


The expected values are documented in [Compute Shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes).
[A fault in the memory subsystem was detected](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computehealthmonitoringguidance.htm)
**Fault class:** `MEM-RUNTIME`
**Details:** This error indicates that one or more non-critical errors were detected on a DIMM in the instance. The instance might have unexpectedly rebooted in the last 72 hours.
**Troubleshooting steps:**
  * If the instance has unexpectedly rebooted in the last 72 hours, one or more DIMMs might have been disabled. To check for the total amount of memory in the instance:
    * On Linux-based systems, run the following command:
Copy
```
awk '$3=="kB"{$2=$2/1024**2;$3="GB";} 1' /proc/meminfo | column -t | grep MemTotal 
```

    * On Windows-based systems, open Resource Monitor. 
If the total memory in the instance is lower than expected, then one or more DIMMs have failed. If this impacts your application, we recommend that you replace the instance using the steps in [Live, Reboot, and Manual Migration: Moving a Compute Instance to a New Host](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#Moving_a_Compute_Instance_to_a_New_Host).
  * If the instance has not unexpectedly rebooted, it is at increased risk of doing so. During the next reboot, one or more DIMMs might be disabled. We recommend that you replace the instance using the steps in [Live, Reboot, and Manual Migration: Moving a Compute Instance to a New Host](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#Moving_a_Compute_Instance_to_a_New_Host).


[A fault in the instance management controller has been detected](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computehealthmonitoringguidance.htm)
**Fault class:** `MGMT-CONTROLLER`
**Details:** This error indicates that a device used to manage the instance might have failed. You might not be able to use the Console, CLI, SDKs, or APIs to stop, start, or reboot the instance. This functionality will still be available from within the instance using the standard operating system commands. You also might not be able to create a console connection to the instance. You will still be able to terminate the instance.
**Troubleshooting steps:** If this loss of control impacts your application, we recommend that you replace the instance using the steps in [Live, Reboot, and Manual Migration: Moving a Compute Instance to a New Host](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#Moving_a_Compute_Instance_to_a_New_Host).
[A fault in the PCI subsystem has been detected](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computehealthmonitoringguidance.htm)
**Fault class:** `PCI`
**Details:** This error indicates that one or more of the PCI devices in the instance have failed or are not operating at peak performance.
**Troubleshooting steps:**
  * If you cannot [connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm#top "You can connect to a running compute instance by using a Secure Shell \(SSH\) or Remote Desktop connection.") over the network, the NIC might have failed. Use the Console or CLI to stop the instance and then start the instance. For steps, see [Stopping, Starting, or Restarting an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm#top "You can stop, start, or restart an instance as needed to update software or resolve error conditions.").
If you're still unable to connect to the instance over the network, you might be able to connect to it using a console connection. Follow the steps in [Making a Local Connection to the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Compute/References/serialconsole.htm#Connecti2) or [Connecting to the VNC Console](https://docs.oracle.com/en-us/iaas/Content/Compute/References/serialconsole.htm#Connecti) to establish a console connection and then reboot the instance. If the instance remains inaccessible, you must replace it using the steps in [Live, Reboot, and Manual Migration: Moving a Compute Instance to a New Host](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#Moving_a_Compute_Instance_to_a_New_Host).
  * An NVMe device may have failed. 
On Linux-based systems, run the command `sudo lsblk` to get a list of the attached NVMe devices. 
On Windows-based systems, open Disk Manager. Check the count of NVMe devices against the expected number of devices in [Compute Shapes](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes).
If you determine that an NVMe device is missing from the list of devices for the instance, we recommend that you replace the instance using the steps in [Live, Reboot, and Manual Migration: Moving a Compute Instance to a New Host](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#Moving_a_Compute_Instance_to_a_New_Host).


[A fault in the instance network interface card (NIC) has been detected](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computehealthmonitoringguidance.htm)
**Fault class:** `PCI-NIC`
**Details:** This error indicates that one or more of the instance network interface card (NIC) devices in the instance have failed or are not operating at peak performance.
**Important** The `PCI-NIC` fault class is [deprecated](https://docs.oracle.com/iaas/Content/servicechanges.htm#compute-pci-nic-fault-class). You should migrate to the `PCI` fault class for similar functionality.
**Troubleshooting steps:** If you cannot [connect to the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm#top "You can connect to a running compute instance by using a Secure Shell \(SSH\) or Remote Desktop connection.") over the network, the NIC might have failed. Use the Console or CLI to stop the instance and then start the instance. For steps, see [Stopping, Starting, or Restarting an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm#top "You can stop, start, or restart an instance as needed to update software or resolve error conditions.").
If you're still unable to connect to the instance over the network, you might be able to connect to it using a console connection. Follow the steps in [Making a Local Connection to the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Compute/References/serialconsole.htm#Connecti2) or [Connecting to the VNC Console](https://docs.oracle.com/en-us/iaas/Content/Compute/References/serialconsole.htm#Connecti) to establish a console connection and then reboot the instance. If the instance remains inaccessible, you must replace it using the steps in [Live, Reboot, and Manual Migration: Moving a Compute Instance to a New Host](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#Moving_a_Compute_Instance_to_a_New_Host).
[A fault in the instance software defined network interface has been detected](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computehealthmonitoringguidance.htm)
**Fault class:** `SDN-INTERFACE`
**Details:** If you cannot connect to the instance or if you're experiencing networking issues, the software-defined network interface device might have a fault.
**Troubleshooting steps:** Although [restarting the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm#top "You can stop, start, or restart an instance as needed to update software or resolve error conditions.") might temporarily resolve the issue, we recommend that you replace the instance using the steps in [Live, Reboot, and Manual Migration: Moving a Compute Instance to a New Host](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#Moving_a_Compute_Instance_to_a_New_Host).
Was this article helpful?
YesNo


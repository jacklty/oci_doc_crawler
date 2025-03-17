Updated 2025-01-13
# Troubleshooting Compute
Use troubleshooting information to identify and address common issues that can occur while working with Compute.
## Diagnosing Issues Using the Console 🔗 
Use the troubleshooting and diagnostic tool in the Console to identify and resolve issues with an instance. The tool observes the instance for some common potential issues and provides suggested troubleshooting steps.
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Click **More Actions** , and then click **Troubleshoot instance**.
The **Troubleshoot instance** panel displays the status of the indicators that are being observed. If an issue is detected, then the panel displays recommended troubleshooting steps that you can follow to resolve the issue.
  4. (Optional) To download a PDF of the troubleshooting suggestions, click **Download results**.


## Resources for Troubleshooting 🔗 
For detailed information about how to troubleshoot issues with compute instances, see the following topics:
  * [Troubleshooting the SSH Connection](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/troubleshooting-ssh-connection.htm#troubleshooting-ssh-connection "If you're unable to connect to a compute instance using SSH, review the following troubleshooting error messages and suggestions to resolve the issue."). If you're unable to connect to a Linux instance using a Secure Shell (SSH) connection, follow the troubleshooting steps to identify common problems.
  * [Compute Instance Health Metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/compute-health-metrics.htm#compute-health-metrics). To determine whether an instance is responsive, use the instance accessibility status metric. Compute sends an Address Resolution Protocol (ARP) request to the instance's virtual network interface card (VNIC). If the ARP ping fails, the metric shows that the instance is unresponsive.
  * [Troubleshooting Instances Using Instance Console Connections](https://docs.oracle.com/en-us/iaas/Content/Compute/References/serialconsole.htm#Instance_Console_Connections). To interactively debug issues that happen during instance launch or during the OS boot sequence, use a serial console connection or a VNC console connection.
  * [Troubleshooting Oracle Cloud Agent](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm#troubleshoot). If the status for all Oracle Cloud Agent plugins on the Instance Details page is **Invalid** or you can't see any metrics in the Metrics section of the Console, confirm that Oracle Cloud Agent is installed, running, and able to communicate with Oracle services.
  * [Performing a Diagnostic Reboot](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/diagnostic-reboot.htm#diagnostic-reboot). To troubleshoot an unreachable virtual machine (VM) instance when other troubleshooting steps aren't successful, you can rebuild the instance by performing a diagnostic reboot.
  * [Sending a Diagnostic Interrupt](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/sendingdiagnosticinterrupt.htm#triggering-diagnostic-interrupt "You can send a diagnostic interrupt to troubleshoot an unresponsive or unreachable Compute virtual machine \(VM\) instance."). To debug a running VM instance that becomes unresponsive, you can generate a copy of the system memory (also called a crash dump) by sending a diagnostic interrupt to the instance.
  * [Displaying the Console History for an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/displayingconsole.htm#Displaying_the_Console_for_an_Instance). To analyze the most recent OS-level error messages and other serial console data for an instance, you can capture and download the serial console history.


Was this article helpful?
YesNo


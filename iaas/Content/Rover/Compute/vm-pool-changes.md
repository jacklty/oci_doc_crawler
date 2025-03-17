Updated 2025-02-21
# Updating a Roving Edge Infrastructure Device VM when the IP Pool Range Changes
Describes how to update your VM's public IP when you change your instance's public IP address pool range without having to recreate the instances.
You can change your VM's public IP range without having to recreate your VMs. Updating your VMs when the IP address pool changes requires you to perform the following tasks:
  * Configuring the attached VNIC for no public IP. You can do this through the Device Console.
  * Use the serial console to specify the updated pool range of public IP addresses available for use.
  * Use the Device Console to reconfigure the attached VNIC back to using an ephemeral or reserved public IP.


  1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
  2. Select a **State** from the list to limit the instances displayed to that state.
  3. Click the instance whose public IP address you want to change. The instance's **Details** page appears.
  4. Click **Attached VNICs** under **Resources**. The **Attached VNICs** page appears.
  5. Click the attached VNIC whose IP address you want to update. The attached VNIC's **Details** page appears.
  6. Click **IP Addresses** under **Resources**. The IP Addresses page appears. The IP addresses are displayed in tabular form.
  7. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)) next to the IP address you need to make private and click **Edit**. The **Edit Private IP Address** dialog box appears.
  8. Select **No public IP** and click **Update**.
  9. Open the Roving Edge Infrastructure device's serial console. See [Operating the Serial Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/setting_up_devices.htm#OperatingSerialConsole).
  10. Select **Configure Networking**. The **Network Configuration** menu appears.
  11. Select **Display Public IP Pool Status**. The serial console displays the public IP address pool ranges. Press `ENTER` to exit.
  12. Select **Set IP Pool Range for Compute Instances**. Enter a list of IP address ranges separated by `ENTER`. Use the following format: `x.x.x.x-y.y.y.y` to specify the beginning and end of the range. If the range is a single address, just enter that address by itself. Press `ENTER` to exit.
  13. Reopen the **Edit Private IP Address** dialog box and select the **Ephemeral public IP** or **Reserved public IP** option.
  14. (optional) Enter the name of the ephemeral or reserved public IP address in the associated **Name** box.


Was this article helpful?
YesNo


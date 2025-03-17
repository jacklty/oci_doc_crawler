Updated 2025-01-14
# Install App Gateway Using Oracle VM Virtual Box
To install App Gateway using Oracle VM Virtual Box, import the App Gateway `Open Virtual Appliance` (`OVA`) file in an **Oracle VM Virtual Box** , and then configure the App Gateway virtual machine to receive HTTP request.
## Importing the Open Virtual Appliance Image File in VM Software 🔗 
To run App Gateway in a virtual machine, import the App Gateway `Open Virtual Appliance` (`OVA`) image file in virtual machine software such as Oracle VM Virtual Box.
The following procedure requires access to a Windows server as administrator. This server must have **Oracle VM Virtual Box** software installed.
  1. Log in to the Windows server, and upload the App Gateway `OVA` file from your desktop to a working folder in the server. For example, `c:\temp`.
  2. Start the **Oracle VM Virtual Box Manager** software, and then select **Import Appliance** from the **File** menu.
  3. Locate the `OVA` file on the Windows server, and then select **Next**.
  4. In the **Import Virtual Appliance** window, update the **Name** field with the value `App Gateway             Server`.
  5. To define a new MAC address to the App Gateway server network component, select **Reinitialize the MAC address of all network cards**.
  6. Select **Import**.
  7. Verify `App Gateway server` is listed in the **Oracle VM Virtual Box Manager**.


After you import App Gateway, a virtual disk image file (`VMDK`) will be created in the Windows server.
To locate this file, select `App Gateway Server` in **Oracle VM Virtual Box Manager** , select **Settings** , select **Storage** , and then select the name that appears under **Controller: SATA** in the **Storage Devices** section. The location of the `VMDK` file appears in the **Location** field under **Information**.
## Configuring Port Forwarding Rules 🔗 
Create a port forwarding rule to allow the requests received by the Windows server hosting the App Gateway virtual machine to be forwarded to the App Gateway server.
  1. In the **Oracle VM Virtual Box Manager** software, select the App Gateway server, and then select **Settings**.
  2. Select **Network** on the left menu, expand **Advanced** , and then select **Port Forwarding**.
  3. In the **Port Forwarding Rules** window, select ![Adds new port forwarding rule icon](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-oracle-vm-virtual-box-adds-new-port-forwarding-rule-icon.png), configure a rule to forward the requests from the host port to the guest port, and then select **OK**.
For example, if your App Gateway is configured to use port `4443`, then enter `4443` in both **Host Port** and **Guest Port** columns.
The port number must be the same as the port value that you provided during App Gateway registration.
  4. In the **Port Forwarding Rules** window, select ![Adds new port forwarding rule icon](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-oracle-vm-virtual-box-adds-new-port-forwarding-rule-icon.png), configure a rule to forward the requests from the host port `22` to the guest port `22`, and then select **OK**.
This enables you to use a `SSH` client such as `PuTTY` to sign in to the App Gateway server later.
  5. In the **Port Forwarding Rules** dialog box, select **OK**.
  6. In the **App Gateway Settings** dialog box, select **OK**.
  7. Select the App Gateway server, and then select **Start**.


Was this article helpful?
YesNo


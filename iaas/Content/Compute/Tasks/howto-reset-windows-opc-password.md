Updated 2025-02-19
# How-to: Reset the Windows OPC Password
To reset the Oracle Public Cloud (OPC) password on Windows, you can use the OS Safe Mode feature and complete the steps on this page.
**Note** Before you complete the steps on this page, you must create a VNC (Virtual Network Computing) Console connection so that you can boot the OS in Safe Mode. For information, see [Connecting to the VNC Console](https://docs.oracle.com/en-us/iaas/Content/Compute/References/serialconsole.htm#Connecti) for instructions.
After you set up the VNC Console connection, you can boot the OS in Safe Mode by following these steps:
  1. From the Console sign-in page, select the **Restart** button.
  2. While the OS is restarts, hold F5 to bring up Windows Boot Manager.
  3. Press F8 to specify an advanced option.
  4. Select **Safe Mode**.
  5. When the OS boots up in Safe Mode, select the Administrator account.
  6. Create a new password for the Administrator user.
  7. Sign in to the Administrator account with the new password.
  8. Navigate to **Computer Management** , select **Local Users and Groups** , and then select **Users.**
  9. Select **OPC user** and then **Set a new password**.


After you regain access to the OPC user account, disable the administrator account for security purposes.
For more details, see [How to Reset a Forgotten Password for a Windows Instance](https://learnoci.cloud/how-to-reset-your-forgotten-windows-password-in-oci-596b4e99f4ca) tutorial.
Was this article helpful?
YesNo


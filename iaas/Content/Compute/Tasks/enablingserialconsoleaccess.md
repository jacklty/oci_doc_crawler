Updated 2024-07-26
# Enabling Serial Console Access for Imported Linux Images
You can configure your custom Linux image to support connections using the serial console feature in the Compute service.
For more information about serial console connections, and steps to troubleshoot if your image has network connectivity issues after it is launched, see [Troubleshooting Instances Using Instance Console Connections](https://docs.oracle.com/en-us/iaas/Content/Compute/References/serialconsole.htm#Instance_Console_Connections).
The serial console connection in Oracle Cloud Infrastructure uses the first serial port, ttyS0, on the VM. The boot loader and the operating system should be configured to use ttyS0 as a console terminal for both input and output.
**Important** For Arm, the first serial port is ttyAMA0.
## Configuring the Boot Loader 🔗 
The steps to configure the boot loader to use ttyS0 as a console terminal for both input and output depend on the GRUB version. Run the following command on the operating system to determine the GRUB version:
Copy
```
grub-install --version

```

If you receive an error stating `'grub' not found`, then run the following command:
Copy
```
grub2-install --version
```

If the version number returned is 2.x, then use the steps to configure GRUB 2. For earlier versions, use the steps to configure GRUB.
[To configure GRUB2](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingserialconsoleaccess.htm)
  1. Run the following command to modify the GRUB configuration file:
Copy
```
sudo vi /etc/default/grub
```

  2. Confirm that the configuration file contains the following:
Copy
```
GRUB_SERIAL_COMMAND="serial --unit=0 --speed=115200"
							GRUB_TERMINAL="serial console"
```

  3. Append the following to the end of the `GRUB_CMDLINE_LINUX` line:
Copy
```
console=tty1 console=ttyS0,115200
```

If `GRUB_CMDLINE_LINUX` does not exist, create this line, using `GRUB_CMDLINE_OUTPUT` as a template.
  4. Regenerate the GRUB2 configuration using the following command:
Copy
```
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

If you have a beta version of GRUB 2, use this command instead:
Copy
```
sudo grub-mkconfig -o /boot/grub/grub.cfg
```



[To configure GRUB](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingserialconsoleaccess.htm)
  1. Run the following command to modify the GRUB configuration file:
Copy
```
sudo vi /boot/grub/grub.conf
```

  2. Add following after the line containing `timeout`:
Copy
```
serial --unit=0 --speed=115200
terminal --timeout=5 serial console
```

  3. Append the following to each `kernel` line:
Copy
```
console=tty1 console=ttyS0,115200
```



## Configuring the Operating System 🔗 
The operating system may already be configured to use ttyS0 as a console terminal for both input and output. To verify, run the following command:
Copy
```
sudo vi /etc/securetty
```

Check the file for `ttyS0`. If you don't see it, append `ttyS0` to the end of the file.
## Validating Serial Console Access 🔗 
After completing the steps to enable serial console access to the image, you should validate that serial console access is working by testing the image with serial console in your virtualization environment. Consult the documentation for your virtualization environment for steps to do this. Verify that the boot output displays in the serial console output and that there is interactive input after the image has booted.
### Troubleshooting the Serial Console 🔗 
If no output is displayed on the serial console, verify in the configuration for your virtualization environment that the serial console device is attached to the first serial port.
If the serial console displays output, but there is no interactive input available, check that there is a terminal process listening on the ttyS0 port (or ttyAMA0 for Arm). To do this, run the following command:
Copy
```
ps aux | grep ttyS0
```

This command should output a terminal process that is listening on the ttyS0 port. For example, if your system is using getty, you will see the following output:
```
/sbin/getty ttyS0
```

If you don't see this output, it is likely that a login process is not configured for the serial console connection. To resolve this, enable the init settings, so that a terminal process is listening on the ttyS0 at startup. 
For example, if your system is using getty, add the following command to the init settings to run on system startup:
Copy
```
getty -L 9600 ttyS0 vt102
```

The steps to do this will vary depending on the operating system, so consult the documentation for the image's operating system.
## Modifying GRUB Entries Using Keystrokes 🔗 
You can modify GRUB entries by using only keystrokes. 
Keystrokes to modify GRUB entries Keystroke | Description  
---|---  
Ctrl+f | Move to the right one character.  
Ctrl+b | Move to the left one character.  
Ctrl+a | Move to start of the line.  
Ctrl+e | Move to end of the line.  
Ctrl+p | Move up one character.  
Ctrl+n | Move down one character.  
Ctrl+d | Delete the character under the cursor.   
Ctrl+h | Delete the character to the left of the cursor.   
Ctrl+k | Delete the characters from the cursor to the end of the line.   
Ctrl+u | Delete the characters from the cursor to the beginning of the line.   
Ctrl+y | Bring deleted text back at the cursor.   
Was this article helpful?
YesNo


Updated 2023-01-04
# OS Kernel Updates for Legacy Linux Instances
**Note**
This topic applies only to Linux instances that were launched before February 15, 2017. Linux instances launched on or after February 15, 2017 boot directly from the image and do not require further action for kernel updates.
Oracle Cloud Infrastructure boots each instance from a network drive. This configuration requires additional actions when you update the OS kernel.
Oracle Cloud Infrastructure uses Unified Extensible Firmware Interface (UEFI) firmware and a Preboot eXecution Environment (PXE) interface on the host server to load iPXE from a Trivial File Transfer Protocol (TFTP) server. The iPXE implementation runs a script to boot Oracle Linux. During the boot process, the system downloads the kernel, the `initrd` file, and the kernel boot parameters from the network. The instance does not use the host's GRUB boot loader.
Normally, the `yum update kernel-uek` command edits the GRUB configuration file, either `grub.cfg` or `grub.conf`, to configure the next boot. Since bare metal instances do not use the GRUB boot loader, changes to the GRUB configuration file are not implemented. When you update the kernel on your instance, you also must upload the update to the network to ensure a successful boot process. The following approaches address this need:
  * Instances launched from platform images include an Oracle yum plugin that seamlessly handles the upload when you run the `yum update kernel-uek` command.
  * If you use a custom image based on a platform image, the included yum plugin will continue to work, barring extraordinary changes.
  * If you install your own package manager, you must either write your own plugin or upload the kernel, initrd, and kernel boot parameters manually.


## Oracle Yum Plugin 🔗 
On instances launched with a [platform image](https://docs.oracle.com/en-us/iaas/Content/Compute/References/images.htm#OracleProvided_Images), you can find the Oracle yum plugin at:
`/usr/share/yum-plugins/kernel-update-handler.py`
The plugin configuration is at:
`/etc/yum/pluginconf.d`
The plugin looks for two variables in the `/etc/sysconfig/kernel` file, `UPDATEDEFAULT` and `DEFAULTKERNEL`. It picks up the updates only when the first variable is set to "yes" and the `DEFAULTKERNEL` value matches the kernel being updated. For example:
```
# UPDATEDEFAULT specifies if new-kernel-pkg should make
# new kernels the default
UPDATEDEFAULT=yes
# DEFAULTKERNEL specifies the default kernel package type
DEFAULTKERNEL=kernel-uek
```

Platform images incorporate the Unbreakable Enterprise Kernel (UEK). If you want to switch to a non-UEK kernel, you must update the `DEFAULTKERNEL` value to "kernel" before you run `yum update kernel`.
## Manual Updates 🔗 
**Tip** Oracle recommends using the Oracle yum plugin to update the kernel.
If you manually upload the updates, there are four relevant URLs:
Copy
```
http://169.254.0.3/kernel
http://169.254.0.3/initrd
http://169.254.0.3/cmdline
http://169.254.0.3/activate
```

The first three URLs are for uploading files (HTTP request type PUT). The fourth URL is for activating the uploaded files (HTTP request type POST). The system discards the uploaded files if they are not activated before the host restarts.
The kernel and initrd are simple file uploads. The cmdline upload must contain the kernel boot parameters found in the `grub.cfg` or `grub.conf` file, depending on the Linux version. The following example is an entry from the `/boot/efi/EFI/redhat/grub.cfg` file in Red Hat Linux 7. The highlighted text represents the parameters to upload.
Copy
```
kernel /boot/vmlinuz-4.1.12-37.5.1.el6uek.x86_64 
ro root=UUID=8079e287-53d7-4b3d-b708-c519cf6829c8 rd_NO_LUKS KEYBOARDTYPE=pc KEYTABLE=us netroot=iscsi:@169.254.0.2::3260:iface1:eth0::iqn.2015-02.oracle.boot:uefi rd_NO_MD SYSFONT=latarcyrheb-sun16 ifname=eth0:90:e2:ba:a2:e3:80 crashkernel=auto iscsi_initiator=iqn.2015-02. rd_NO_LVM ip=eth0:dhcp rd_NO_DM LANG=en_US.UTF-8 console=tty0 console=ttyS0,9600 iommu=on

```

The following command returns what is being uploaded to the cmdline file.
Copy
```
cat /tmp/cmdline
```

A typical response resembles the following.
Copy
```
ro root=UUID=8079e287-53d7-4b3d-b708-c519cf6829c8 rd_NO_LUKS KEYBOARDTYPE=pc KEYTABLE=us netroot=iscsi:@169.254.0.2::3260:iface1:eth0::iqn.2015-02.oracle.boot:uefi rd_NO_MD SYSFONT=latarcyrheb-sun16 ifname=eth0:90:e2:ba:a2:e3:80 crashkernel=auto iscsi_initiator=iqn.2015-02. rd_NO_LVM ip=eth0:dhcp rd_NO_DM LANG=en_US.UTF-8 console=tty0 console=ttyS0,9600 iommu=on
```

The following commands update the `cmdline` and `initrd` files, and then activate the changes.
Copy
```
CKSUM=`md5sum /tmp/cmdline | cut -d ' ' -f 1`
```

Copy
```
sudo curl -X PUT --data-binary @/tmp/cmdline -H "Content-MD5: $CKSUM" http://169.254.0.3/cmdline
```

Copy
```
CKSUM=`md5sum /boot/initramfs-3.8.13-118.8.1.el7uek.x86_64.img | cut -d ' ' -f 1`
```

Copy
```
sudo curl -X PUT --data-binary @/boot/initramfs-3.8.13-118.8.1.el7uek.x86_64.img -H "Content-MD5: $CKSUM" http://169.254.0.3/initrd
```

Copy
```
sudo curl -X POST http://169.254.0.3/activate
```

Was this article helpful?
YesNo


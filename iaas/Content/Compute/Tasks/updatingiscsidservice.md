Updated 2025-01-08
# Updating the Linux iSCSI Service to Restart Automatically
Oracle Cloud Infrastructure supports iSCSI attached remote boot and block volumes to compute instances. These iSCSI attached volumes are managed by the Linux iSCSI initiator service, `iscsid` . In scenarios where this service is stopped for any reason, such as the service crashes or a system administrator inadvertently stops the service, it's important that this service is automatically restarted immediately. 
The following platform images distributed by Oracle Cloud Infrastructure are configured so that the `iscsid` service restarts automatically:
  * Oracle Autonomous Linux 8 images
  * Oracle Autonomous Linux 7 images
  * Oracle Linux 9 images
  * Oracle Linux 8 images
  * Oracle Linux Cloud Developer 8 images
  * Oracle Linux 7 images released February 26, 2019 and later. Refer to the release notes for [Oracle-Linux-7.6-Gen2-GPU-2019.02.20-0](https://docs.oracle.com/iaas/images/image/3463f922-b66d-4556-9e22-2f0bc403951a/) and [Oracle-Linux-7.6-2019.02.20-0](https://docs.oracle.com/iaas/images/image/66379f54-edd0-4294-895f-47291a3eb4ed/).
  * CentOS 7 images released February 25, 2019 and later. Refer to the release notes for [CentOS-7-2019.02.23-0](https://docs.oracle.com/iaas/images/image/4ed32af7-e4c0-4612-803b-d67c9d112e70/).


Instances created from earlier versions of CentOS 7.x, CentOS Stream 8, and Oracle Linux platform images, or any versions of Ubuntu platform images, do not have this configuration. You should update these existing instances and custom images created from these images so that the `iscsid` service restarts automatically. You should also check this configuration on your imported paravirtualized custom images and any instances launched from these images and update the configuration as needed.
This topic describes how to update the `iscsid` service on an instance so that it will restart automatically.
**Note** Configuring an instance to automatically restart the `iscsid` service does not require a reboot and will increase the stability of your infrastructure.
## Oracle Linux 7 🔗 
To update the `iscsid` service on Oracle 7 Linux instances, run the following command:
Copy
```
sudo yum update -y iscsi-initiator-utils
```

After running this command, the version of the `iscsid` service should be 6.2.0.874 or later.
To check the version, run the following command:
Copy
```
yum info iscsi-initiator-utils
```

This update does not require a system reboot and will not make any changes to the instances beyond configuring `iscsid` to restart automatically. 
## CentOS 7.x 🔗 
**Important** Do not directly edit the `systemd` **iscsid.service** file. You should instead create an override to ensure that the `restart` option isn't overwritten the next time the `iscsid` service is updated.
To create an override file on CentOS 7 instances, run the following command:
Copy
```
sudo systemctl edit iscsid.service
```

Paste and save the following into the file:
Copy
```
[Service]
Restart=always
```

To reload `systemd` and restart the `iscsid` service, run the following commands:
Copy
```
sudo systemctl daemon-reload
sudo systemctl restart iscsid
```

## CentOS Stream 8 🔗 
**Important** Do not directly edit the `systemd` **iscsid.service** file. You should instead create an override to ensure that the `restart` option isn't overwritten the next time the `iscsid` service is updated.
To create an override file on CentOS Stream 8 instances, run the following command:
Copy
```
sudo systemctl edit iscsid.service
```

Paste and save the following into the file:
Copy
```
[Service]
Restart=always
```

To reload `systemd` and restart the `iscsid` service, run the following commands:
Copy
```
sudo systemctl daemon-reload
sudo systemctl restart iscsid
```

## Ubuntu 18.04, Ubuntu 20.04, Ubuntu 22.04 🔗 
**Important** Do not directly edit the `systemd` **iscsid.service** file. You should instead create an override to ensure that the `restart` option isn't overwritten the next time the `iscsid` service is updated.
To create an override file on Ubuntu 18.04 and Ubuntu 20.04 instances, run the following command:
Copy
```
sudo systemctl edit iscsid.service
```

Paste and save the following into the file:
Copy
```
[Service]
Restart=
Restart=always
```

To reload `systemd` and restart the `iscsid` service, run the following commands:
Copy
```
sudo systemctl daemon-reload
sudo systemctl restart iscsid
```

## Testing the iscsid Service Update 🔗 
Perform these steps to verify that the `iscsid` service has been updated successfully, and that it restarts automatically.
**Caution** Do not perform these steps on a production instance. If the `iscsid` service fails to restart, the instance might become unresponsive. 
  1. To confirm that the `iscsid` service is running, run the following command:
Copy
```
ps -ef | grep iscsid
```

  2. To stop the `iscsid` service, run the following command:
Copy
```
sudo pkill -9 iscsid
```

  3. Wait 60 seconds. Then, run the following command to verify that the `iscsid` service has restarted:
Copy
```
ps -ef | grep iscsid
```



Was this article helpful?
YesNo


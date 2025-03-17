Updated 2025-02-13
# How-to: Change an Instance Host Name
You can change the host name of Compute VM instances.
**Note** Changes made in the `/etc/hosts` and `resolv.conf` files revert to their original values when the instance restarts, unless you complete the steps outlined here.
To change the host name, use the following commands:
  1. Update the `/etc/hostname` file.```
hostnamectl set-hostname <new name>
```

  2. Edit the OCI configuration file and update the needed value to 2.```
sudo vi /etc/oci-hostname.conf
PRESERVE_HOSTINFO=2
```

  3. Edit the Fully Qualified Domain Name (FQDN) from the OCI Console.
    1. Go to Compute instances.
    2. Select the instance.
    3. Under resources, select **attached VNIC**.
    4. From the Action Menu, select **Edit**.
    5. Change the host name to update the FQDN.
    6. Select **Save changes**.
  4. Reboot the instance.
  5. Check the host name with `hostname` command.
  6. Check if FQDN is resolving.```
host <ip address>
```

or```
nslookup <ip address>
```



Was this article helpful?
YesNo


Updated 2025-02-06
# Configuring Linux to Use a Secondary Private IP Address
Configure Linux to use a secondary private IP address.
[After assigning a secondary private IP to a VNIC, you must configure the OS to use it](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-create.htm#top "Assign a new secondary private IP address to a VNIC.").
## Basic Commands (Not Persistent Through a Reboot)
On the instance, run the following command. It works on all variants of Linux, for both bare metal and VM instances:
Copy
```
ip addr add <address>/<subnet_prefix_len> dev <phys_dev> label <phys_dev>:<addr_seq_num>
```

where:
  * `<address>`: The secondary private IP address.
  * `<subnet_prefix_len>`: The subnet's prefix length. For example, if the subnet is 192.168.20.0/24, the subnet prefix length is 24.
  * `<phys_dev>`: The interface to add the address to (for example, ens2f0).
  * `<addr_seq_num>`: The sequential number in the stack of addresses on the device (for example, 0).

For example:
Copy
```
ip addr add 192.168.20.50/24 dev ens2f0 label ens2f0:0
```

To delete the address, you can use:
Copy
```
ip addr del 192.168.20.50/24 dev ens2f0:0 
```

Also, [delete the secondary IP from the VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-delete.htm#top "Delete a private IP address from a VNIC."). You can do that before or after executing the preceding command to delete the address from the OS configuration.
**Note**
If you assigned a secondary IP to a [secondary VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Virtual_Network_Interface_Cards_VNICs), and you're using policy-based routing for the secondary VNIC, configure the route rules for the instance to look up the same route table for the secondary IP address, using the `ip rule add from <source address> lookup <table name>` command.
## Configuration File (Persistent Through a Reboot)
You can make the configuration persistent through a reboot by adding the information to a configuration file.
[For Oracle Linux and CentOS](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses_topic-Linux_Details_about_Secondary_IP_Addresses.htm)
For Oracle Linux 7, create an `ifcfg` file named `/etc/sysconfig/network-scripts/ifcfg-<phys_dev>:<addr_seq_num>`. To continue with the preceding example, the file name would be `/etc/sysconfig/network-scripts/ifcfg-ens2f0:0`, and the contents would be:
Copy
```
DEVICE="ens2f0:0"
BOOTPROTO=static
IPADDR=192.168.0.50
NETMASK=255.255.255.0
ONBOOT=yes

```

For [Oracle Linux 8](https://docs.oracle.com/en/operating-systems/oracle-linux/8/network/) or Oracle Linux 9, the preferred method would be to use nmcli to configure the interface for NetworkManager. 
If Network Manager overwrites the connections after reboot, the preferred solution is to run the `ip addr add <address>/<subnet_prefix_len> dev <phys_dev> label <phys_dev>:<addr_seq_num>` command at boot time. This can be done with a cron job, or using /etc/rc.d/rc.local etc. Or, you can change the kernel command line parameters so that dracut doesn't overwrite NetworkManager connection profiles.
**Note**
If you assigned a secondary IP to a [secondary VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Virtual_Network_Interface_Cards_VNICs), and you're using policy-based routing for the secondary VNIC, configure the route rules for the instance to look up the same route table for the secondary IP address, using the `ip rule add from <source address> lookup <table name>` command.
[For Ubuntu](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses_topic-Linux_Details_about_Secondary_IP_Addresses.htm)
Create or change a netplan configuration stored at `/etc/netplan/<filename>.yaml`. To continue with the preceding example, the file name would be `/etc/netplan/50-cloud-init.yaml`, and it would be changed to disable DHCP (for all addresses) and replace it with manual configuration as shown:
Copy
```

network:
 ethernets:
  ens3: 
   dhcp4: no
  addresses: [192.168.64.223/24, 192.168.64.75/24]
  gateway4: 192.168.64.1
  nameservers:
   addresses: [169.254.169.254] 
  match:
   macaddress: 02:00:17:0e:66:7b
  set-name: ens3 
  version: 2
```

In this example, 192.168.64.223 is the primary IP address assigned to the VNIC and 192.168.64.75 is the secondary IP address. `macaddress` refers to the VNIC, and this can be found in the Console or by using `oci-utils`. More complex netplan configuration examples can be found at the [netplan reference pages](https://netplan.io/reference). See [Attaching VLANs to network interfaces](https://netplan.io/examples#attaching-vlans-to-network-interfaces) for an upstream example.
**Note**
If you assigned a secondary IP to a [secondary VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Virtual_Network_Interface_Cards_VNICs), and you're using policy-based routing for the secondary VNIC, configure the route rules for the instance to look up the same route table for the secondary IP address, using the `ip rule add from <source address> lookup <table name>` command.
Was this article helpful?
YesNo


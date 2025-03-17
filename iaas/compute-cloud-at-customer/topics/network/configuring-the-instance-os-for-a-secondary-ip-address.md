Updated 2025-02-21
# Configuring the Instance OS for a Secondary IP Address
On Compute Cloud@Customer, after you create a secondary private IP address on a VNIC, sign in to the instance to configure the instance OS to use the new IP address.
## Linux Instance OS Configuration 🔗 
This configuration permits use of an IP address subnet, netmask, gateway, and DNS service that are entirely independent from the existing NIC. This configuration is persistent across reboots.
Create a new network interface configuration file to create a subinterface on the existing NIC. In this example, `ens03` is the name of the existing NIC and `ifcfg-ens3:0` is the name of the new configuration file.
  1. Create the network configuration file `ifcfg-ens3:0` in the `/etc/sysconfig/network-scripts/` directory to create the first sub-interface (`:0`) on the existing `ens3` NIC.
Include the following entries in `ifcfg-ens3:0`:
```
TYPE=Ethernet
BOOTPROTO=none
IPADDR=a.b.c.d
PREFIX=24
GATEWAY=
DNS=
NAME=ens3:0
DEVICE=ens3:0
```

  2. Include the appropriate `IPADDR`, `PREFIX`, `GATEWAY`, and `DNS` entries for this new sub-interface.
  3. Run the following command to start the new interface:
```
# ifup ens3:0
```

  4. Run the following command to confirm that the new interface is operational:
```
# ifconfig -a
```



See also [Linux: Details about Secondary IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIPaddresses.htm#Linux).
## Oracle Solaris Instance OS Configuration 🔗 
Use the `ipadm` command to configure network interfaces persistently.
## Microsoft Windows Instance OS Configuration 🔗 
See [Windows: Details about Secondary IP Addresses](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIPaddresses.htm#Windows) for information about how to either:
  * Create a PowerShell script.
  * Use the Network and Sharing Center user interface.


Was this article helpful?
YesNo


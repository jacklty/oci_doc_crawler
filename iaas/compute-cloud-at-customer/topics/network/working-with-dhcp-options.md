Updated 2024-04-02
# Working with DHCP Options
On Compute Cloud@Customer, when you create a subnet, you can specify the set of DHCP options for the subnet. A set of DHCP options is a resource with an OCID. If you don't specify a set of DHCP options, the default set for the VCN is used.
A subnet can only be assigned one set of DHCP options. You can edit a set of DHCP options, create a new set, and change which set is assigned to a subnet. The assigned DHCP option set applies to all the instances in that subnet.
Each subnet in a VCN can have a single set of DHCP options associated with it. That set of options applies to all instances in the subnet. Each VCN comes with a default set of DHCP options with initial values that you can change. Unless you create and assign a different set of DHCP options, every subnet uses the VCN default set.
These are the available DHCP options you can configure:
  * **Domain Name Server**
The default setting is DNS Type = Internet and VCN Resolver.
If instead you set DNS Type = Custom Resolver, you can specify up to three DNS servers of your choice.
  * **Search Domain**
If you set up your VCN with a DNS label, the default value for the Search Domain option is the VCN domain name: `**_<VCN_DNS_label>_**.oraclevcn.com`. Otherwise, the Search Domain option isn't present in the default set of DHCP options.
In general, when any set of DHCP options is initially created – the default set or a custom set –, the Networking service automatically adds the Search Domain option and sets it to the VCN domain name (`**_<VCN_DNS_label>_**.oraclevcn.com`) if all of these are true:
    * The VCN has a DNS label.
    * DNS Type = Internet and VCN Resolver.
    * You did NOT specify a search domain of your choice during creation of the set of DHCP options.
After the set of DHCP options is created, you can always remove the Search Domain option or set it to a different value. You can specify only a single search domain in a set of DHCP options.


Important notes about your instances and DHCP options:
  * Whenever you change the value of one of the DHCP options, you must either restart the DHCP client on the instance, or reboot the instance for the changes to take effect. This applies to all existing instances in the subnets associated with that set of DHCP options.
  * Keep the DHCP client running so you can always access the instance. If you stop the DHCP client manually or disable NetworkManager, the instance can't renew its DHCP lease and will become inaccessible when the lease expires; typically within 24 hours. Do not disable NetworkManager unless you use another method to ensure renewal of the lease.
  * Stopping the DHCP client might remove the host route table when the lease expires. Also, loss of network connectivity to your iSCSI connections might result in loss of the boot drive.
  * Any changes you make to the `/etc/resolv.conf` file are overwritten whenever the DHCP lease is renewed or the instance is rebooted. 
  * Changes you make to the `/etc/hosts` file are overwritten whenever the DHCP lease is renewed or the instance is rebooted. To persist your changes to the `/etc/hosts` file in Linux or CentOS instances, add the following line to `/etc/oci-hostname.conf`: `PRESERVE_HOSTINFO=2`. If the `/etc/oci-hostname.conf` file doesn't exist, create it.


Was this article helpful?
YesNo


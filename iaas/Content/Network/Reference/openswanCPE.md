Updated 2024-05-29
# Openswan
If you want to use Openswan to create Site-to-Site VPN to Oracle Cloud Infrastructure, see [Libreswan](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/libreswanCPE.htm#Libreswan).
## How Openswan and Libreswan Are Related 🔗 
[Openswan](https://www.openswan.org/) is a well-known IPSec implementation for Linux. It began as a fork of the now-defunct [FreeS/WAN project](https://www.freeswan.org/) in 2003. Unlike the FreeS/WAN project, it didn't exclusively target the GNU/Linux operation system, but expanded its use to other operating systems. In 2012, FreeS/WAN renamed itself to the [Libreswan](https://libreswan.org/) Project because of a lawsuit over a trademark of the name _openswan_.
As a result, when you try to install or query the Openswan package on Oracle Linux, by default the Libreswan package is installed or shown instead. The following yum search query command illustrates this behavior:
```
$ sudo yum search openswan
Loaded plugins: langpacks, ulninfo
Matched: openswan ============================================
NetworkManager­-libreswan.x86_64 : NetworkManager VPN plug­in for libreswan
NetworkManager­-libreswan-gnome.x86_64 : NetworkManager VPN plugin for libreswan-GNOME files
libreswan.x86_64 : IPsec implementation with IKEv1 and IKEv2 keying protocols
```

Libreswan is maintained by The Libreswan Project and has been under active development for over 15 years, going back to the FreeS/WAN Project. For more information, see the [project's history](https://libreswan.org/wiki/History).
Was this article helpful?
YesNo


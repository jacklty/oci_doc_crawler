Updated 2024-10-16
# Hanging Connection
This topic covers one of the most common issues seen with communications between your cloud network and on-premises network: a hanging connection, even though you can ping hosts across the connection. 
## Summary of Problem and Solutions 🔗 
**Symptom:** Your Virtual Cloud Network (VCN) connects to your existing on-premises network using Site-to-Site VPN, or Oracle Cloud Infrastructure FastConnect. Hosts on one side of the connection can ping hosts on the other side, but normal traffic using the connection hangs. For example:
  * You can SSH to a host across the connection, but after you log in to the host, the connection hangs.
  * You can start a Virtual Networking Computing (VNC) connection, but the session hangs.
  * You can start an SFTP download, but the download hangs.


**General problem:** _Path Maximum Transmission Unit Discovery (PMTUD)_ is probably not working on one or both sides of the connection. It must be working on both sides of the connection so that both sides can know if they're trying to send packets that are too large for the connection and adjust accordingly. For a brief overview of Maximum Transmission Unit (MTU) and PMTUD, see [Overview of MTU](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/connectionhang.htm#Overview) and [Overview of PMTUD](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/connectionhang.htm#Path). 
**Solutions for fixing PMTUD:**
The following diagram shows an example scenario with your on-premises network connected to your VCN over Site-to-Site VPN and has callouts representing each part of the solution. 
[![This image shows the various parts of the solution for fixing the hanging connection](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_mtu_overall_fixes.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_mtu_overall_fixes.svg)
  1. **Ensure that your hosts use PMTUD:** If the hosts in your on-premises network don't use PMTUD (that is, if they don't set the Don't Fragment flag in the packets), they have no way to discover if they're sending packets that are too large for the connection. Your instances on the Oracle side of the connection use PMTUD by default. Don't change that configuration on the instances. Also, ensure that the servers have a firewall rule to allow ICMP type 3 code 4.
  2. **Ensure that both the VCN security lists and the instance firewalls allow ICMP type 3 code 4 messages:** When PMTUD is in use, the sending hosts receive a special ICMP message if they send packets that are too large for the connection. Upon receipt of the message, the host can dynamically update the size of the packets to fit the connection. However, for your instances to receive these important ICMP messages you must configure both the security lists for the subnet in the VCN and the instance firewalls to accept them.
**Tip** If you're using [stateful security list rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful) (for TCP, UDP, or ICMP traffic), you don't need to ensure that your security list has an explicit rule to allow ICMP type 3 code 4 messages because the Networking service tracks the connections and automatically allows those messages. Stateless rules require an explicit rule in the ingress security list for ICMP type 3 code 4 messages. Confirm that the instance firewalls are set up correctly. 
To check to see if a host is receiving the messages, see [Finding Where PMTUD Is Broken](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/connectionhang.htm#Finding).
  3. **Ensure that your on-premises router honors the _Don't Fragment_ flag:** If the router doesn't honor the flag and thus ignores the use of PMTUD, it sends fragmented packets to the instances in the VCN. That's not what you want to see (refer to [Why Avoid Fragmentation?](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/connectionhang.htm#Why)). The VCN's security lists are most likely configured in such a way that they recognize only the initial fragment, and drop the remaining ones, causing the connection to hang. Instead, your router should use PMTUD and honor the Don't Fragment flag to determine the correct size of unfragmented packets to send through the connection.


Keep reading for a brief overview of MTU and PMTUD, and [how to check if PMTUD is working](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/connectionhang.htm#Finding) on both sides of the network connection.
## Why Avoid Fragmentation? 🔗 
You might be wondering why you want to avoid fragmentation. First, it adversely affects the performance of your application. Fragmentation requires reassembly of the fragments and retransmission of lost fragments. Reassembly and retransmission require time and CPU resources. 
Second, only the first fragment contains the source and destination port information. This means that either firewalls or your VCN's [security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists) drop the other packets, because they're typically configured to evaluate the port information. For fragmentation to work with your firewalls and security lists, you would have to configure them to be more permissive than usual, which isn't desirable.
## Overview of MTU 🔗 
The communications between any two hosts across an Internet Protocol (IP) network use packets. Each packet has a source and destination IP address and a payload of data. Every network segment between the two hosts has a _Maximum Transmission Unit (MTU)_ that represents the number of bytes that a single packet can carry.
The standard internet MTU size is 1500 bytes. This is also true for most home networks and many corporate networks (and their Wi-Fi networks). Some data centers, including those for Oracle Cloud Infrastructure, can have a larger MTU. All OCI compute instances use an MTU of 9000 by default. On an Oracle Linux 8 host, you can use the `ip address show` command to display the MTU of that host's network connection (or use `ip link` on Red Hat Linux). As an example, here's the output from an Oracle Linux 8 instance (the MTU is highlighted in red italics):
Copy
```
ip address show <interface-x>
<interface-x>: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9000 qdisc pfifo_fast state UP group default qlen 1000
  link/ether 01:00:5E:90:10:10 brd ff:ff:ff:ff:ff:ff
  ... 
```

For comparison, here's the output from an Oracle Linux 8 host connected to a corporate network:
Copy
```
ip address show <interface-y>
<interface-y>: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
  link/ether 01:00:5E:90:10:20 brd ff:ff:ff:ff:ff:ff
  ...
```

Notice that its MTU is the more typical 1500 bytes.
If the host connects through a corporate VPN, the MTU is even smaller, because the VPN tunnel must encapsulate the traffic inside an IPSec packet and send it across the local network. For example:
Copy
```
ip address show <interface-z>
<interface-z>: flags=81d1<UP,POINTOPOINT,RUNNING,NOARP,PROMISC,MULTICAST> mtu 1300 
... 
```

How do the two hosts figure out how large of a packet they can send to each other? For many types of network traffic, such as HTTP, SSH, and FTP, the hosts use TCP to establish new connections. During the initial three-way handshake between two hosts, they each send the _Maximum Segment Size (MSS)_ for how large their payload can be. This is smaller than the MTU. (TCP runs inside the Internet Protocol (IP), which is why it's referred to as TCP/IP. Segments are to TCP what packets are to IP.)
Using the [tcpdump](https://www.tcpdump.org/) application, you can see the MSS value shared during the handshake. Here's an example from tcpdump (with the MSS highlighted in red italics):
Copy
```
12:11:58.846890 IP 192.168.0.25.22 > 10.197.176.19.58824: Flags [S.], seq
2799552952, ack 2580095593, win 26844, options [mss 1260,sackOK,TS val
44858491 ecr 1321638674,nop,wscale 7], length 0
```

The preceding packet is from an SSH connection to an instance from a laptop connected to a corporate VPN. The local network that the laptop uses for its internet connection has an MTU of 1500 bytes. The VPN tunnel enforces an MTU of 1300 bytes. Then when attempting the SSH connection, TCP (running inside the IP connection) tells the Oracle Cloud Infrastructure instance that it supports TCP segments that are less than or equal to 1260 bytes. With a corporate VPN connection, the laptop connected to the VPN typically has the smallest MTU and MSS compared to anything it's communicating with across the internet. 
A more complex case is when the two hosts have a larger MTU than some intermediary network link between them _not directly connected to either of them_. The following diagram illustrates an example.
[![This image shows the different MTU levels at different points in the overall network connection](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_mtu_byte_levels.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_mtu_byte_levels.svg)
The example shows two servers, each directly connected to its own routed network that supports a 9000-byte MTU. The servers are in different data centers. Each data center connects to the internet, which supports a 1500-byte MTU. A Site-to-Site VPN IPSec tunnel connects the two data centers. That tunnel crosses the internet, so the inside of the tunnel has a smaller MTU than the internet. In this diagram, the MTU is 1380 bytes.
If the two servers try to communicate (with SSH, for example), during the three-way handshake, they agree on an MSS around 8960. The initial SSH connection might succeed, because the maximum packet sizes during the initial SSH connection setup are usually less than 1380 bytes. When one side tries to send a packet larger than the smallest link between the two endpoints, Path MTU Discovery (PMTUD) becomes critical.
## Overview of PMTUD 🔗 
Path MTU Discovery is defined in [RFC 1191](https://datatracker.ietf.org/doc/html/rfc1191) and [RFC 8899](https://datatracker.ietf.org/doc/html/rfc8899) . It works by requiring the two communicating hosts to set a _Don't Fragment_ flag in the packets they each send. If a packet from one of these hosts reaches a router where the egress (or outbound) interface has an MTU smaller than the packet length, the router drops that packet. The router also returns an ICMP type 3 code 4 message to the host. This message specifically says "Destination Unreachable, Fragmentation Needed and Don't Fragment Was Set" (defined in [RFC 792](https://datatracker.ietf.org/doc/rfc792/)). Effectively the router tells the host: "You told me not to fragment packets that are too large, and this one's too large. I'm not sending it." The router also tells the host the maximum size packets allowed through that egress interface. The sending host then adjusts the size of its outbound packets so they're smaller than the value the router provided in the message.
This example shows the result when an instance tries to ping a host (203.0.113.2) over the internet with an 8000-byte packet and the Don't Fragment flag set (that is, with PMTUD in use). The returned ICMP message is highlighted in red italics:
Copy
```
ping 203.0.113.2 -M do -s 8000
PING 203.0.113.2 (203.0.113.2) 8000(8028) bytes of data.
From 10.0.0.2 icmp_seq=1 
Frag needed and DF set (mtu = 1500)

```

The response is exactly what you should expect. The destination host is across the internet, which has an MTU of 1500 bytes. Even though the sending host's local network connection has an MTU of 9000 bytes, the host can't reach the destination host with the 8000-byte packet and gets an ICMP message accordingly. PMTUD is working correctly. 
For comparison, here's the same ping, but the destination host is across a Site-to-Site VPN IPSec tunnel:
Copy
```
ping 192.168.6.130 -M do -s 8000
PING 192.168.0.130 (192.168.0.130) 8000(8028) bytes of data.
From 192.0.2.2 icmp_seq=1 Frag needed and DF set 
(mtu = 1358)

```

Here the VPN router sees that to send this packet to its destination, the outbound interface is a VPN tunnel. That tunnel goes across the internet, so the tunnel must fit inside the internet's 1500-byte MTU link. As a result, the inside of the tunnel only allows packets up to 1360 bytes (which the router then lowered to 1358, which can make things more confusing).
## Finding Where PMTUD Is Broken 🔗 
If PMTUD isn't working somewhere along the connection, you need to figure out why and where it's broken. Typically it's because the ICMP type 3 code 4 packet (from the router with the constrained link that can't fit the packet) never gets back to the sending host. This can happen if something blocks that kind of traffic between the host and the router, and on either side of the VPN tunnel (or other constrained MTU link). 
### Try Pinging from Each Side of the Connection
To troubleshoot the broken PMTUD, you must determine if PMTUD is working on each side of the connection. In this scenario, let's assume the connection uses Site-to-Site VPN. 
**How to ping:** Like in [Overview of PMTUD](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/connectionhang.htm#Path), ping a host on the other side of the connection with a packet that you know is too large to fit through the VPN tunnel (for example, 1500 bytes or larger). Depending on which operating system the sending host uses, you might need to format the ping command slightly different to determine that the Don't Fragment flag is set. For both Ubuntu and Oracle Linux, you use the `-M` flag with the ping command.
Here's the embedded help information about the `-M` flag:
Copy
```
-M pmtudisc_opt
Select Path MTU Discovery strategy. pmtudisc_option may be either do
(prohibit fragmentation, even local one), want (do PMTU discovery, fragment
locally when packet size is large), or dont (do not set DF flag).
```

Here's an example ping (with the -M flag and the resulting ICMP message highlighted in red italics)
Copy
```
ping -M do
 -s 1500 192.168.6.130
PING 192.168.0.130 (192.168.0.130) 1500(1528) bytes of data.
From 10.0.0.2 icmp_seq=1 
Frag needed and DF set (mtu = 1358)

```

### Good: PMTUD Works 🔗 
If the result includes the line "From x.x.x.x icmp_seq=1 Frag needed and DF set (mtu = xxxx)", then PMTUD is working on that side of the tunnel. Note that the source address of the ICMP message is the public IP address of the tunnel the traffic is trying to go out (for example 203.0.113.13 in the preceding Ubuntu example).
Also, ping from the other side of the connection to confirm that PMTUD is working from that side. Both sides of the connection must recognize when a tunnel between them can't fit the large packets.
### Bad: If you're testing your side of the connection and the ping succeeds 🔗 
If you're sending the ping from a host in your on-premises network, and the ping succeeds, that probably means your edge router isn't honoring the Don't Fragment flag. Instead, the router is fragmenting the large packet. The first fragment reaches the destination host, so the ping succeeds, which is misleading. If you try to do more than just ping, the fragments after the first drop, and the connection hangs.
**Verify that your router configuration honors the Don't Fragment flag.** The router's default configuration is to honor it, but someone might have changed the default.
### Bad: If you're testing the VCN side of the connection and you don't see the ICMP message 🔗 
When testing from the VCN side of the connection, if you don't see the ICMP message in the response, there is probably something dropping the ICMP packet before it reaches your instance. 
There could be two issues:
  * **Security list:** The Networking [security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists) could be missing an ingress rule that allows ICMP type 3 code 4 messages to reach the instance. This is an issue only if you're using [stateless security list rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful). If you're using stateful rules, your connections are tracked, and the ICMP message is automatically allowed without needing a specific security list rule to allow it. **If you're using stateless rules, ensure that the instance's subnet has a security list with an ingress rule allowing ICMP traffic type 3 code 4 from source 0.0.0.0/0 and any source port.** For more information, see [Security Lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists), and specifically [Updating Rules in a Security List](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/update-securitylist.htm#update-securitylist "Update the rules used in a security list in a Virtual Cloud Network \(VCN\).").
  * **Instance firewall:** The instance's firewall rules (set in the OS) could be missing a rule that allows ICMP type 3 code 4 messages to reach the instance. Specifically for a Linux instance, configure iptables or firewalld to allow the ICMP type 3 code 4 messages. 


## Avoiding the Need for PMTUD 🔗 
Oracle recommends using PMTUD. However, in some situations it's possible to configure servers so they don't need to rely on it. Consider the case of the instances in your VCN communicating across Site-to-Site VPN to hosts in your on-premises network. You know the range of IP addresses for your on-premises network. You can add a special route to your instances that specifies the maximum MTU to use when communicating with hosts in that address range. The instance-to-instance communication within the VCN still uses an MTU of 9000 bytes. 
The following information shows how to set that route on a Linux instance.
The default route table on the instance typically has two routes: the default route (for the default gateway), and a local route (for the local subnet). For example:
Copy
```
ip route show
default via 10.0.6.1 dev ens3
10.0.6.0/27 dev ens3 proto kernel scope link src 10.0.6.9
```

You can add another route pointing to the same default gateway, with the address range of the on-premises network and a smaller MTU. For example, in the following command, the on-premises network is 1.0.0.0/8, the default gateway is 10.0.6.1, and the maximum MTU size is 1300 for packets sent to the on-premises network. 
Copy
```
ip route add 1.0.0.0/8 via 10.0.6.1 mtu 1300
```

The updated route table looks like this:
Copy
```
ip route show
default via 10.0.6.1 dev ens3
1.0.0.0/8 via 10.0.6.1 dev ens3 mtu 1300
10.0.6.0/27 dev ens3 proto kernel scope link src 10.0.6.9
```

Within the VCN, the instance-to-instance communication continues to use 9000 MTU. However, communication to the on-premises network uses a maximum of 1300. This example assumes no part of the connection between the on-premises network and VCN uses an MTU smaller than 1300. 
**Important** The preceding commands don't persist if you reboot the instance. You can make the route permanent by adding it to a configuration file in the OS. Oracle Linux, for example, uses an interface-specific file called `/etc/sysconfig/network-scripts/route-<interface>`. For more information, see the documentation for your variant of Linux.
Was this article helpful?
YesNo


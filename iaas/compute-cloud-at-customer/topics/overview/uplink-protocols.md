Updated 2024-10-07
# Uplink Protocols
On Compute Cloud@Customer, the uplinks to the data center run various protocols to provide redundancy and reduce link failure detection and recovery times on these links. These protocols work with the triangle, square, or mesh topologies.
The suite of uplink protocols include:
  * Bidirectional Forwarding Detection (BFD)
  * Virtual Router Redundancy Protocol (VRRP)
  * Hot Spare Router Protocol (HSRP)
  * Equal Cost Multipath (ECMP)


Each is briefly described in the following sections of this topic.
## BFD 🔗 
In most router networks, connection failures are detected by loss of the “hello” packets sent by routing protocols. However, detection by this method often takes more than one second, routing a lot of packets on high-speed links to a destination that they can't reach, which burdens link buffers. Increasing the “hello” packet rate burdens the router CPU.
Bidirectional Forwarding Detection (BFD) is a built-in mechanism that alerts routers at the end of a failed link that there's a problem more quickly than any other mechanism, reducing the load on buffers and CPUs. BFD works even in situations where there are switches or hubs between the routers.
BFD requires no configuration and has no user-settable parameters.
## VRRPv3 🔗 
The Virtual Router Redundancy Protocol version 3 (VRRPv3) is a networking protocol that uses the concept of a virtual router to group physical routers together and make them appear as one to participating hosts. This increases the availability and reliability of routing paths through automatic default gateway selections on an IP subnetwork.
With VRRPv3, the primary/active and secondary/standby routers act as one virtual router. This virtual router becomes the default gateway for any host on the subnet participating in VRRPv3. One physical router in the group becomes the primary/active router for packet forwarding. However, if this router fails, another physical router in the group takes over the forwarding role, adding redundancy to the router configuration. The VRRPv3 “network” is limited to the local subnet and doesn't advertise routes beyond the local subnet. 
## HSRP 🔗 
Cisco routers often use a redundancy protocol called the Hot Spare Router Protocol (HSRP) to improve router availability. Similar to the methods of VRRP, HSRP groups physical routers into a single virtual router. The failure of a physical default router results in another router using HSRP to take over the default forwarding of packets without stressing the host device. 
## ECMP 🔗 
Equal Cost Multipath (ECMP) is a way to make better use of network bandwidth, especially in more complex router networks with many redundant links. 
Normally, router networks with multiple router paths to another destination network choose one active route to a gateway router as the “best” path and use the other paths as a standby in case of failure. The decision about which path to a network gateway router to use is usually determined by its “cost” from the routing protocol perspective. In cases where the cost over several links to reach network gateways are equal, the router chooses one based on some criteria. This makes routing decisions easy but wastes network bandwidth as network links on paths not chosen sit idle.
ECMP is a way to send traffic on multiple path links with equal cost, making more efficient use of network bandwidth. 
Was this article helpful?
YesNo


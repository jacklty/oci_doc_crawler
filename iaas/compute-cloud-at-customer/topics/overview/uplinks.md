Updated 2024-12-11
# Uplinks
The connections between the Compute Cloud@Customer and the customer data center are called _uplinks_. They're physical cable connections between the spine switches in the rack and one or, preferably, two next-level network devices in the data center.
Besides the physical aspect, there's also a logical aspect to the uplinks: how traffic is routed between the rack and the external network it's connected to.
## Physical Connection 🔗 
On each spine switch, ports 1-4 can be used for uplinks to the data center network. For speeds of 10-Gbps or 25-Gbps, the spine switch port must be split using an MPO-to-4xLC breakout cable. For speeds of 40-Gbps or 100-Gbps each switch port uses a single MPO-to-MPO cable connection. The correct connection speed must be specified during initial setup so that the switch ports are configured with the appropriate breakout mode and transfer speed.
The uplinks are configured during system initialization, based on information you provide as part of the installation checklist. Unused spine switch uplink ports, including unused breakout ports, are disabled for security reasons. The table shows the supported uplink configurations by port count and speed, and the resulting total bandwidth.
Uplink Speed |  Number of Uplinks per Spine Switch  |  Total Bandwidth  
---|---|---  
10 Gbps |  1, 2, 4, 8, or 16 |  20, 40, 80, 160, or 320 Gbps  
25 Gbps |  1, 2, 4, 8, or 16 |  50, 100, 200, 400, or 800 Gbps  
40 Gbps |  1, 2, or 4 |  80, 160, or 320 Gbps  
100 Gbps |  1, 2, or 4 |  200, 400, or 800 Gbps  
Regardless of the number of ports and port speeds configured, you also select a topology for the uplinks between the spine switches and the data center network. This information is critical for the network administrator to configure link aggregation (port channels) on the data center switches. The table shows the available options.
Topology |  Description   
---|---  
Triangle |  In a triangle topology, all cables from both spine switches are connected to a single data center switch.  
Square |  In a square topology, two data center switches are used. All outbound cables from a given spine switch are connected to the same data center switch.  
Mesh |  In a mesh topology, two data center switches are used as well. The difference with the square topology is that uplinks are created in a cross pattern. Outbound cables from each spine switch are connected in pairs: one cable to each data center switch.  
## Topology 🔗 
The physical topology for the uplinks from the rack to the data center network is dependent on bandwidth requirements and available data center switches and ports. Connecting to a single data center switch implies that you select a triangle topology. To increase redundancy you distribute the uplinks across a pair of data center switches, selecting either a square or mesh topology. Each topology allows you to start with a minimum bandwidth, which you can scale up with increasing need. The maximum bandwidth is 800 Gbps, assuming the data center switches, transceivers and cables allow it.
The following diagrams provide a simplified view of supported topologies, and can be used as initial guidance to integrate the rack into the data center network. Use the diagrams and the notes to determine the appropriate cabling and switch configuration for your installation. For more detailed uplink configuration examples, which have been tested by Oracle, see [Reference Topologies](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/uplinks-reference-topologies.htm#uplinks-reference-topologies "These detailed topologies are examples of uplink configurations that have been tested and are known to work as expected. Each example includes a diagram for illustration, and configuration guidelines.").
[![Figure showing six examples of supported uplink topologies. The examples are explained in the diagram notes below.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/uplinks_reference_examples.png)](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/uplinks_reference_examples.png)
**Diagram Notes**
On the rack side there are two spine switches that must be connected to the data center network. Both spine switches must have identical port and cable configurations. In each example, the spine switches are shown at the bottom, with all uplink ports identified by their port number. The lines represent outgoing cable connection to the data center switches, which are shown at the top of each example without port numbers.
**Cabling Pattern and Port Speed**
There are six examples in total, organized in two rows by three columns.
  * The top row shows cabling options based on full-port 100-Gbps or 40-Gbps connections. The bottom row shows cabling options using breakout ports at 25-Gbps or 10-Gbps speeds; the smaller boxes numbered 1-4 represent the breakout connections for each of the four main uplink ports per spine switch.
  * The third column shows a triangle topology with full-port connections and breakout connections. The difference with column two is that all uplinks are connected to a single data center switch. The total bandwidth is the same, but the triangle topology lacks data center switch redundancy.
  * There are no diagrams for the square topology. The square cabling configuration is similar to the mesh examples, but without the crossing patterns. Visually, all connectors in the diagrams would be parallel. In a square topology, all outgoing cables from one spine switch are connected port for port to the same data center switch. Unlike mesh, square implies that each spine switch is peered with only one data center switch.


**Link Count**
When connecting the uplinks, you are required to follow the spine switch port numbering. Remember that both spine switches are cabled identically, so each uplink or connection corresponds with a pair of cables.
  * With one cable per spine port, using 100 or 40 Gbps transceivers, the first uplink pair uses spine switch ports numbered 1, the second uses port 2, and so on. In this configuration, the maximum number of uplinks is four per spine switch.
  * When breakout cables are used, with 25 or 10-Gbps port speeds, the first uplink pair uses port 1/1. With two or four uplinks per spine switch there's still only one full port in use. When you increase the uplink count to 8 per spine switch, ports 1/1-2/4 are in use. At 16 uplinks per spine switch, all breakout connections of all four reserved ports will be in use.
  * In a mesh topology, a particular cabling pattern must be followed: connect the first half of all uplinks to one data center switch, and the second half to the other data center switch. For example: if you have four uplinks then the first two go to the same switch; if you have eight uplinks (not shown in the diagrams) then the first four go to the same switch; if you have 16 uplinks then the first eight go to the same switch.


**Mesh Topology Implications**
  * In a mesh topology, the spine switch configuration expects that the first half of all uplinks is connected to one data center switch, and the second half to the other data center switch. When you initially connect the rack to your data center network, it is straightforward to follow this pattern.
  * However, if you increase the number of uplinks at a later time, the mesh cabling pattern has a significant implication for the existing uplinks. Compare the diagrams in the first two columns: when you double the uplink count, half of the existing connections must be moved to the other data center switch. For 100/40-Gbit uplinks, recabling is only required when you increase the link count from 2 to 4. Because of the larger number of cables, 25/10-Gbit uplinks require more re-cabling: when increasing uplink count from 2 to 4, from 4 to 8, and from 8 to 16.


## Logical Connection 🔗 
The logical connection between the rack and the data center is implemented entirely in layer 3. In the OSI model (Open Systems Interconnection model), layer 3 is known as the network layer, which uses the source and destination IP address fields in its header to route traffic between connected devices.
Compute Cloud@Customer supports two logical connection options: you must choose between static routing and dynamic routing. Both routing options are supported by all three physical topologies.
Connection Type |  Description   
---|---  
Static Routing |  When static routing is selected, all egress traffic goes through a single default gateway IP address configured on data center network devices. This gateway IP address must be in the same subnet as the rack uplink IP addresses, so it is reachable from the spine switches. The data center network devices can use SVIs (Switch Virtual Interfaces) with VLAN IDs in the range of 2-3899. All gateways configured within a virtual cloud network (VCN) will automatically have a route rule to direct all traffic intended for external destination to the IP address of the default gateway.  
Dynamic Routing |  When dynamic routing is selected, BGP (Border Gateway Protocol) is used to establish a TCP connection between two Autonomous Systems: the rack network and the data center network. This configuration requires a registered or private ASN (Autonomous System Number) on each side of the connection. Compute Cloud@Customer BGP configuration uses ASN 136025 by default, this can be changed during initial configuration. For BGP routing, two routing devices in the data center must be connected to the two spine switches in the rack. Corresponding interfaces (port channels) between the spine switches and the data center network devices must be in the same subnet. It is considered good practice to use a dedicated /30 subnet for each point-to-point circuit, which is also known as a route hand-off network. This setup provides redundancy and multipathing. Dynamic routing is also supported in a triangle topology, where both spine switches are physically connected to the same data center network device. In this configuration, two BGP sessions are still established: one from each spine switch. However, this approach reduces the level of redundancy.  
**Supported Routing Designs**
The following table shows which routing designs are supported depending on the physical topology in your data center and the logical connection you choose to implement.
Note that link aggregation across multiple devices (vPC or MLAG) is only supported with static routing. When dynamic routing is selected, link aggregation is restricted to ports of the same switch.
When the uplinks are cabled in a mesh topology, a minimum of 2 physical connections per spine switch applies. To establish BGP peering, 2 subnets are required. If the uplink count changes, the port channels are reconfigured but the dedicated subnets remain the same.
Logical Connection |  Physical Topology |  Routing Design  
---|---|---  
Single Subnet |  Dual Subnet |  vPC/MLAG  
Static Routing |  Square |  Yes |  Yes |  Yes  
Mesh |  Yes |  Yes |  Yes  
Triangle |  Yes |  Yes |  Yes  
Dynamic Routing |  Square |  Yes |  – |  –  
Mesh |  – |  Yes |  –  
Triangle |  Yes |  – |  –  
Was this article helpful?
YesNo


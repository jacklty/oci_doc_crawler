Updated 2024-11-07
# Network Infrastructure
For network connectivity, Compute Cloud@Customer relies on a physical layer that provides the necessary high-availability, bandwidth and speed. On top of this, a distributed network fabric composed of software-defined switches, routers, gateways, and tunnels enables secure and segregated data traffic – both internally between cloud resources, and externally to and from resources outside of Compute Cloud@Customer. 
This section provides a network overview. For more details, see [Customer Site Network Requirements](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/network-requirements.htm#customer-network-requirements "Review the topics in this section to prepare your network environment before the arrival of the Oracle Compute Cloud@Customer rack.").
## Data Network 🔗 
On Compute Cloud@Customer, data connectivity is built on redundant 100Gbit switches in two-layer design similar to a leaf-spine topology.
The leaf switches interconnect the rack hardware components, while the spine switches form the backbone of the network and provide a path for external traffic. Each leaf switch is connected to all the spine switches, which are also interconnected. The main benefits of this topology are extensibility and path optimization. A Compute Cloud@Customer rack contains two leaf and two spine switches.
For external connectivity, 5 ports are reserved on each spine switch. Four ports are available to establish the uplinks between the rack and the data center network; one port is reserved to segregate the administration network from the data traffic.
## Administration Network 🔗 
On Compute Cloud@Customer, the administration network physically separates configuration and management traffic from the operational activity on the data network by providing dedicated secured network paths for administration operations. This network includes all component management interfaces.
This network is only accessed by authorized Oracle operators.
Was this article helpful?
YesNo


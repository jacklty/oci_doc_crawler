Updated 2024-10-07
# NLB Frontend Configuration
On Compute Cloud@Customer, in the context of network load balancers (NLB), the term _frontend_ refers to the components that a client can see and send requests to. The entry point of client requests is the outward-facing floating IP address of the NLB.
Three main configuration tasks are needed for the NLB frontend: 
  * Type (public or private)
  * Policy (the number of tuples used for the hash value)
  * Listeners (Port number and other parameters that the NLB uses when waiting for traffic) 


See [Managing NLBs](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/managing-nlbs.htm#managing-nlb "On Compute Cloud@Customer, you can create, view, edit and delete Network Load Balancers \(NLBs\).").
## NLB Types 🔗 
On Compute Cloud@Customer, there are two types of network load balancers (NLBs): _public_ and _private_.
Private NLBs use a private IP address to serve as the entry point for incoming traffic. The load balancing service requires only one subnet to host both the primary and secondary load balancers. However, the NLB is only accessible from within the VCN that contains the host subnet, or as further restricted by security rules.
Public NLBs use a public IP address and accept traffic from a network location outside of Compute Cloud@Customer. However, the public NLB must be deployed in a public subnet of a VCN that has an internet gateway (IGW) correctly configured.
## NLB Policies 🔗 
On Compute Cloud@Customer, a network load balancer (NLB) policy acts on an _n-tuple_ mapped to an IP hash instead of directly on the packet header. A tuple is an ordered and finite list of elements. For an NLB, these elements to be hashed are drawn from the fields in a packet header. The _n_ indicates how many fields the tuple contains.
Allowed NLB policies include:
  * A default policy based on a hash on 5 fields in the TCP/IP header (called "5-Tuple Hash") 
    * Source IP address
    * Source port
    * Destination IP address
    * Destination port
    * Protocol 
  * A policy based on a hash on 3 fields in the TCP/IP header (called "3-Tuple Hash") 
    * Source IP address
    * Destination IP address
    * Protocol 
  * A policy based on a hash on 2 fields in the TCP/IP header (called "2-Tuple Hash" 
    * Source IP address
    * Destination IP address


Hashing generates a smaller number of bits than used in the concatenated fields before the hashing algorithms is applied. Packets that have the same hash value are treated the same way by the NLB.
The more tuples that are used for the load balancing policy, the more processing required for each load balanced packet, but the wider the range of values that can be used by the NLB to distribute traffic. 
The IP hash is the "policy in action." The NLB uses an incoming request’s tuple information as a hashing key to consistently route traffic to the same backend server. This ensures that requests from a particular client are always directed to the same backend server if that backend server remains available.
## NLB Listeners 🔗 
On Compute Cloud@Customer, a listener is a logical entity at the ingress side of the network load balancer (NLB) setup. This key component detects incoming traffic on the NLB IP address. It listens for requests from clients using a particular protocol and port. Requests are then routed to the appropriate backend servers based on the rules defined in the NLB configuration. You must configure a listener. 
When you create a listener, ensure that the VCN security rules let the listener accept traffic.
**Note**
To accommodate high-volume traffic, we recommend that you use _stateless_ security rules for NLB subnets. For more information, see [Virtual Firewall](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/virtual-firewall.htm#virtual-firewall "On Compute Cloud@Customer, the Networking service offers two virtual firewall features that both use security rules to control traffic at the packet level – security lists and network security groups \(NSGs\). They offer different ways to apply security rules to a set of virtual network interface cards \(VNICs\).").
See [Managing NLB Listeners](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/managing-nlb-listeners.htm#managing-nlb-listeners "On Compute Cloud@Customer, use listeners to check for incoming traffic on the network load balancer IP address.").
Was this article helpful?
YesNo


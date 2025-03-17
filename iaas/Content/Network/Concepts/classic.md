Updated 2024-10-16
# Access to Oracle Cloud Infrastructure Classic
There are two ways to set up a connection between an Oracle Cloud Infrastructure Classic IP network and an Oracle Cloud Infrastructure Virtual Cloud Network (VCN):
  * [Option 1: Connection over the Oracle network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithoraclenetwork.htm#Connection_Over_Oracle_Network)
    * You file a ticket with My Oracle Support and Oracle provisions a connection between the IP network's private gateway and the VCN's attached Dynamic Routing Gateway (DRG). The connection runs over Oracle's network and not the internet.
    * The two environments must be in the same geographical area, and the connection is available only between the specific regions listed in [Overview](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithoraclenetwork.htm#overview). 
    * The two environments must belong to the same company. Oracle validates ownership when setting up the connection.
  * [Option 2: Connection over Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/classicwithvpn.htm#Connection_Over_IPSec_VPN)
    * You set up Site-to-Site VPN between the IP network's VPN as a Service (VPNaaS) gateway and the VCN's attached DRG. The connection runs over the internet.
    * The two environments do not have to be in the same geographical area or regions.
    * The two environments do not have to belong to the same company.


Was this article helpful?
YesNo


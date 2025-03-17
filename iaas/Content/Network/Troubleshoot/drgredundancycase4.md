Updated 2023-01-04
# Redundancy Remedy: Case 4
This topic describes one of several redundancy issues that you might be alerted to in the Console. 
## Summary of the Issue 🔗 
You use FastConnect to connect your on-premises network to a VCN. Although you might have multiple virtual circuits in this connection, _only one_ of them is up (the BGP status is UP). Your connection to Oracle is at risk when routine maintenance is performed on the Oracle router.
You can fix the problem in one of two possible ways.
## Option A: Use a Second Virtual Circuit 🔗 
The details of the fix depend on your situation.
### If You Are Using an Oracle FastConnect Partner
The following diagram illustrates the issue.
**Before the fix:**
[![This image shows a single virtual circuit.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case4_before.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case4_before.svg)
In this case, you have only a single FastConnect virtual circuit that is up. 
**After the fix:**
[![This image shows two virtual circuits that run on the same provider but use different physical connections.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case4_after.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case4_after.svg)
After the fix, you have two FastConnect virtual circuits that are up, each to a different Oracle router. Some partners give you an option to specify which physical location to use for each virtual circuit. Other partners automatically use a different physical connection for the secondary virtual circuit.
### If You Are Using a Third-Party Provider or Colocated with Oracle
The following diagram illustrates the issue.
**Before the fix:**
[![This image shows a single virtual circuit.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case4_direct_before.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case4_direct_before.svg)
In this case, you have only a single FastConnect virtual circuit that is up.
**After the fix:**
[![This image shows two virtual circuits that run on different physical connections.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case4_direct_after.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case4_direct_after.svg)
To fix the problem, set up a secondary physical connection to Oracle. It must go to a different router (B in the diagram). To do that, set up a new physical connect (cross-connect group) in the Oracle Console. During setup, specify the proximity of that connection to other FastConnect connections in that location. For example, the following image shows how to request that your secondary cross-connect group is created on a different router than your primary connection in that FastConnect location (called MyConnection-1). 
[![This image shows the router proximity information in the Console.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_colo_router_proximity.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_colo_router_proximity.png)
After you've worked with the data center to have the cabling set up, and the new secondary cross-connect group is up and running, you can create a new virtual circuit on that cross-connect group. Confirm that failover works between the primary and new secondary cross-connect group. 
## Option B: Use Site-to-Site VPN with Both Tunnels Up/Active 🔗 
This option is recommended if your CPE supports having two IPSec tunnels up/active to the same destination. 
The details of the fix depend on your situation.
### If You Are Using an Oracle Partner
The following diagram illustrates the issue.
**Before the fix:**
[![This image shows a single virtual circuit.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case4_before.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case4_before.svg)
In this case, you have only a single FastConnect virtual circuit that is up.
**After the fix:**
[![This image shows a virtual circuit and two IPSec tunnels that are up.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case4_direct_after_vpn.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case4_direct_after_vpn.svg)
Here you set up Site-to-Site VPN as backup. You must configure your CPE so that both IPSec tunnels are up/active. Oracle automatically provisions each tunnel on a different Oracle router. Therefore, the secondary tunnel (to router B in the diagram) will be available when Oracle performs maintenance on the virtual circuit's router (router A in the diagram). Oracle recommends configuring both tunnels to use BGP dynamic routing.
### If You Are Using a Third-Party Provider or Colocated with Oracle
The following diagram illustrates the issue.
**Before the fix:**
[![This image shows a single virtual circuit.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case4_direct_before.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case4_direct_before.svg)
In this case, you have only a single FastConnect virtual circuit that is up.
**After the fix:**
[![This image shows a virtual circuit and two IPSec tunnels that are up.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case4_direct_after_vpn.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case4_direct_after_vpn.svg)
Here you set up Site-to-Site VPN as backup. You must configure your CPE so that both IPSec tunnels are up/active. Oracle automatically provisions each tunnel on a different Oracle router. Therefore, the secondary tunnel (to router B in the diagram) will be available when Oracle performs maintenance on the virtual circuit's router (router A in the diagram). Oracle recommends configuring both tunnels to use BGP dynamic routing.
Was this article helpful?
YesNo


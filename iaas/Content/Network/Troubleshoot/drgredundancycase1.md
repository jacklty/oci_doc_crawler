Updated 2023-01-04
# Redundancy Remedy: Case 1
This topic describes one of several redundancy issues that you might be alerted to in the Console. 
## Summary of the Issue 🔗 
You have redundant FastConnect virtual circuits that connect your on-premises network to a VCN. However, both of those virtual circuits terminate on the _same_ Oracle edge router. Your connection to Oracle is at risk when routine maintenance is performed on that router.
Depending on your situation, there are two possible ways to fix the problem.
## If You Are Using an Oracle Partner 🔗 
The following diagram illustrates the issue.
**Before the fix:**
[![This image shows multiple virtual circuits that run on different providers but terminate on the same Oracle router.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case1_before.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case1_before.svg)
In this case, you have multiple FastConnect virtual circuits, each using a different Oracle partner (called X and Y in the diagram). Each partner has two physical connections to Oracle, and each goes to a different Oracle router (called A and B in the diagram). 
The problem is that both virtual circuits happen to terminate on the same Oracle router (router A in the diagram). 
**After the fix:**
[![This image shows multiple virtual circuits that run on different providers and terminate on different Oracle routers.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case1_after.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case1_after.svg)
To fix the problem, work with one of the partners to establish a new virtual circuit that goes to the _other_ Oracle router (router B in the diagram). When that new secondary virtual circuit is up and running, delete the old secondary virtual circuit (in the diagram, the one on physical connection Y-A).
## If You Are Using a Third-Party Provider or Colocated with Oracle 🔗 
The following diagram illustrates the issue.
**Before the fix:**
[![This image shows multiple physical connections to the same Oracle router.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case1_direct_before.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case1_direct_before.svg)
In this case, you have two physical connections (**cross-connect groups**), and both go to the same Oracle router (router A in the diagram). 
**After the fix:**
[![This image shows the physical connections each going to a different Oracle router.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case1_direct_after.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case1_direct_after.svg)
To fix the problem, one of your physical connections must go to a different router (B in the diagram). To do that, set up a new physical connect (cross-connect group) in the Oracle Console. During setup, specify the proximity of that connection to other FastConnect connections in that location. For example, the following image shows how to request that your secondary cross-connect group is created on a different router than your primary connection in that FastConnect location (called MyConnection-1). 
[![This image shows the router proximity information in the Console.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_colo_router_proximity.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_colo_router_proximity.png)
After you've worked to set up the cabling in the data center, and the new secondary cross-connect group is up and running, you can create a new virtual circuit on that cross-connect group. When the virtual circuit is up and running, confirm that failover works between the primary and new secondary cross-connect group. Then you can terminate the old virtual circuit and old cross-connect group.
Was this article helpful?
YesNo


Updated 2023-01-04
# Redundancy Remedy: Case 5
This topic describes one of several redundancy issues that you might be alerted to in the Console. 
## Summary of the Issue 🔗 
You use Site-to-Site VPN to connect your on-premises network to a VCN. Although Oracle provisions two IPSec tunnels for the connection, _only one_ of them is up/active. Your connection to Oracle is at risk when routine maintenance is performed on the Oracle router.
## How to Fix the Issue 🔗 
The following diagram illustrates the issue.
**Before the fix:**
[![This image shows redundant IPSec tunnels, but only one is up.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case5_before.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case5_before.svg)
Notice that a Site-to-Site VPN consists of two IPSec tunnels, and Oracle automatically provisions each on a different Oracle router. 
**After the fix:**
[![This image shows both IPSec tunnels up.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case5_after.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case5_after.svg)
If your CPE supports having two active IPSec tunnels, you need to bring up the second tunnel. This avoids having the single tunnel as a point of failure. Oracle recommends configuring both tunnels to use BGP dynamic routing.
**Note** How to bring up the tunnel depends on which CPE device you use. See the instructions for your CPE device. Devices are listed at [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm#CPE_Configuration). 
Was this article helpful?
YesNo


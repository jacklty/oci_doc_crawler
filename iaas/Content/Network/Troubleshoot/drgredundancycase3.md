Updated 2023-01-04
# Redundancy Remedy: Case 3
This topic describes one of several redundancy issues that you might be alerted to in the Console. 
## Summary of the Issue 🔗 
You have redundant Site-to-Site VPN connections that connect your on-premises network to a VCN. Although each connection consists of two IPSec tunnels, only one tunnel per connection is up/active, and both of those tunnels terminate on the _same_ Oracle edge router. Your connection to Oracle is at risk when routine maintenance is performed on that router.
## How to Fix the Issue 🔗 
The following diagram illustrates the issue.
**Before the fix:**
[![This image shows redundant IPSec tunnels that terminate on the same Oracle router.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case3_before.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case3_before.svg)
In this case, you have a primary connection and a secondary connection as backup. Notice that each Site-to-Site VPN consists of two IPSec tunnels, and Oracle provisions each on a different Oracle router. However, you must configure your CPE so that both tunnels are up/active. 
The problem has two parts:
  * In each connection, only one of the two IPSec tunnels is up/active. 
  * Both of the tunnels that are up/active terminate on the same Oracle router.


Some CPEs only support one IPSec tunnel being up/active to a given destination. 
**After the fix:**
[![This image shows four IPSec tunnels that are up.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case3_after.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case3_after.svg)
If your CPE supports having two IPSec tunnels up/active to the same destination, configure the second tunnel to also be up/active. Oracle recommends configuring all tunnels to use BGP dynamic routing.
If your CPE supports only a single active IPSec tunnel to a given destination, then for _one of the connections only_ , switch which of the two IPSec tunnels is configured to be up. The following diagram illustrates that setup. Oracle recommends configuring both tunnels to use BGP dynamic routing.
[![This image shows one tunnel in each connection up, and each terminating on different Oracle routers.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case3_after2.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case3_after2.svg)
Was this article helpful?
YesNo


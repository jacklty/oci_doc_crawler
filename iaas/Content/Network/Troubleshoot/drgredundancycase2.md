Updated 2023-01-04
# Redundancy Remedy: Case 2
This topic describes one of several redundancy issues that you might be alerted to in the Console. 
## Summary of the Issue 🔗 
You have a FastConnect virtual circuit that connects your on-premises network to a VCN. For redundancy you use Site-to-Site VPN, but with only a single active IPSec tunnel. Both the FastConnect virtual circuit and the IPSec tunnel terminate on the _same_ Oracle edge router. Your connection to Oracle is at risk when routine maintenance is performed on that router.
## How to Fix the Issue 🔗 
The following diagram illustrates the issue.
**Before the fix:**
[![This image shows a virtual circuit and a single active IPSec tunnel that both terminate on the same Oracle router.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case2_before.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case2_before.svg)
In this case, you have a FastConnect virtual circuit and Site-to-Site VPN as backup. Notice that each VPN Connect consists of two IPSec tunnels, and Oracle automatically provisions each tunnel on a different Oracle router. However, you must configure your CPE so that both tunnels are up/active. 
The problem is that:
  * Only one of the two IPSec tunnels is up/active. 
  * The one IPSec tunnel that is up terminates on the same Oracle router as the virtual circuit.


Notice that some CPEs only support one IPSec tunnel being up/active to a given destination. 
**After the fix:**
[![This image shows a virtual circuit and two IPSec tunnels that are up.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case2_after.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case2_after.svg)
If your CPE supports having two IPSec tunnels up/active to the same destination, configure the second tunnel to also be up/active. Oracle recommends configuring them both to use BGP dynamic routing for the IPSec tunnels.
If your CPE supports only a single active IPSec tunnel to a given destination, configure the _other_ IPSec tunnel to be up. Then switch the original IPSec tunnel to be down/inactive. The following diagram illustrates that setup. Also, if your CPE supports BGP dynamic routing, configure the tunnel to use it instead of static routing. 
[![This image shows a virtual circuit and a single IPSec tunnel that is up, each terminating on a different Oracle router.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case2_after2.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_redundancy_case2_after2.svg)
Was this article helpful?
YesNo


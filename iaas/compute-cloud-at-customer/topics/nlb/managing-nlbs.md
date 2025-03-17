Updated 2024-01-18
# Managing NLBs
On Compute Cloud@Customer, you can create, view, edit and delete Network Load Balancers (NLBs).
For conceptual information about NLBs, see [Network Load Balancing](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/network-load-balancing.htm#network-load-balancing "On Compute Cloud@Customer, you can configure the Network Load Balancing \(NLB\) feature to automatically distribute network traffic.").
When you create an NLB, you can either configure all the resources at the same time or create a minimal NLB and supply other configuration details later. More than the basic NLB is needed to establish the NLB service. You add more components by editing the NLB resources. 
After you create the NLB, perform the following tasks:
  * Cipher Suites and SSL Certificates
  * Backend Sets and Backend Servers
  * Virtual Hostnames
  * Path Route Sets
  * Listeners


Many configuration steps are processed as work requests. Work requests are tasks that can take some time to complete and therefore are tracked as they're processed. For example, the act of creating an NLB or cipher suite is a work request that records and displays start and finish times, state (succeeded, failed, and so on), and other relevant details. Work requests are part of the NLB resource list. 
The status of a work request, such as succeeded, isn't the same as completion of the provisioning of the resource. NLB creation can succeed while provisioning is still in progress.
Was this article helpful?
YesNo


Updated 2024-10-16
# Cisco ASA Configuration Options
Choose the configuration based on the ASA software version: 
  * **9.7.1 or newer:** [Route-based configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEroutebased.htm#Cisco_ASA_RouteBased)
  * **8.5 to 9.7.0:** [Policy-based configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEpolicybased.htm#Cisco_ASA_PolicyBased)
  * **Older than 8.5:** Not supported by the Oracle configuration instructions. Consider upgrading to a newer version.


**Important**
Oracle recommends using a [route-based configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEroutebased.htm#Cisco_ASA_RouteBased) to avoid interoperability issues and to achieve tunnel redundancy with a single Cisco ASA device. 
The Cisco ASA does not support route-based configuration for software versions older than 9.7.1. For the best results, if your device allows it, Oracle recommends that you upgrade to a software version that supports route-based configuration.
With policy-based configuration, you can configure only a single tunnel between your Cisco ASA and your Dynamic Routing Gateway (DRG).
Was this article helpful?
YesNo


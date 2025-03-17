Updated 2024-02-13
# Enable HA for an Existing AD Bridge Deployment
Enabling high availability for a new AD bridge deployment in an IAM identity domain.
  * Ensure that you have upgraded the existing AD bridge to version 20.1.3 and greater for every domain that you have configured. 
  * AD bridge HA must be enabled for you. After all AD bridges in all domains have been upgraded to version 20.1.3 or greater, enter an SR with Oracle Support to enable HA. After HA is enabled, it's enabled for all configured domains.


## Limitations 🔗 
Note the following limitiations for AD bridge HA.
  * Only one AD bridge can be configured in one Windows machine. To configure multiple AD bridges you have to use multiple Windows machines in the same domain. Note that without AD bridge HA enabled by Oracle Support, installation of second AD bridge for the domain fails.
  * Maximum of 5 AD bridges per domain can be configured by an administrator for HA and load sharing.
  * AD bridge HA won't work if any one of the AD bridges installed for a domain is version 19.3.3 and below. To check the version of an AD bridge, open the AD bridge user interface and note the version in the bottom right corner of the window.


**Note** If additional bridges won't install for a domain, ensure that all prerequisites are met and that none of the constraints apply to your environment.
Was this article helpful?
YesNo


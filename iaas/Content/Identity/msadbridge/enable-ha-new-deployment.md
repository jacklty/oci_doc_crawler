Updated 2024-02-13
# Enable HA for a New Deployment
Enabling high availability for an existing AD bridge deployment in an IAM identity domain.
AD Bridge High Availability must be enabled for you. Enter an SR with Oracle Support to enable the feature.
## Limitations 🔗 
Note the following limitations for AD bridge HA.
  * AD bridge HA will not work if any one of the AD bridges installed for a domain is version 19.3.3 and below.
  * Only one AD bridge can be configured in one Windows machine. To configure multiple AD bridges you have to use multiple Windows machines in the same domain. Note that without AD bridge HA enabled by Oracle Support, installation of second AD bridge for the domain fails.
  * Maximum of 5 AD bridges per domain can be configured by an administrator for HA and load sharing.


**Note** If additional bridges won't install for a domain, ensure that all prerequisites are met and that none of the constraints apply to your environment.
Was this article helpful?
YesNo


Updated 2025-03-10
# Secondary DNS
Set up secondary domain name system (DNS) zones using the Oracle Cloud Infrastructure DNS service. 
Secondary DNS provides redundancy for primary DNS **servers**. The Oracle Cloud Infrastructure DNS service supports the following secondary DNS configurations:
  * **Egress:** Oracle Cloud Infrastructure DNS is the primary provider, and an external DNS provider is the secondary provider.
  * **Ingress:** An external DNS provider is the primary provider, and Oracle Cloud Infrastructure is the secondary provider.


## How Secondary DNS works 🔗 
The secondary DNS service contains a copy of **zone** and **record** data that exists on the primary DNS provider. You can configure the primary provider to send a notification to the secondary provider when zone records change. After a notification is received, secondary providers then request the updated zone contents from the configured primary provider. This process is called a zone transfer.
DNS resolvers query providers' nameservers in a "round-robin" fashion over the domains following the delegation path. If you delegate to both providers ("dual delegation"), then DNS resolvers can use either provider when resolving a name, providing redundancy in case a provider fails. If you delegate to the secondary provider solely, the primary nameserver is treated as a "hidden" primary. The primary nameserver maintains the source of truth for the zone records, which the secondary zone uses to answer queries.
To set up dual delegation where both sets of nameservers are specified for a zone, first update the registrar or parent zone to add the downstream nameservers to the [NS](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/supporteddnsresource.htm#types) `**rrset **`for the zone. You don't need to take any further action. DNS resolvers decide which provider to use when resolving a name.
## Egress from Oracle Cloud Infrastructure DNS to an External DNS Provider 🔗 
When you create a primary DNS zone in OCI DNS, you can specify one or more external downstream servers. The downstream servers are notified of changes and then request zone transfers. The specified nameservers can also issue transfer requests to the Oracle primary nameservers. You can specify nameservers managed by different vendors.
## Ingress from an External DNS Provider to Oracle Cloud Infrastructure DNS 🔗 
After you create a secondary DNS zone in an external DNS provider, you can specify one or more OCI DNS downstream servers. The OCI downstream servers are notified of changes by the primary external provider and then request zone transfers. The specified nameservers can also issue transfer requests to the external primary nameservers. You can specify downstream servers for external zones managed by different vendors.
Secondary zones in OCI DNS are _active-active_. This means that the secondary zone is "always on" and serves answers to queries like a regular zone. Although the primary provider serves as the source of truth for the secondary zone's records, the secondary provider is still authoritative for the zone.
## Using TSIG Keys 🔗 
Optionally, you can configure OCI secondary DNS to use TSIG keys. TSIG (Transaction Signature), also referred to as Secret Key Transaction Authentication, ensures that DNS packets originate from an authorized sender by using shared secret keys and one-way hashing to add a cryptographic signature to the DNS packets. TSIG keys are used to enable DNS to authenticate updates to secondary zones. You can configure TSIG keys for both secondary ingress and secondary egress DNS. 
Create TSIG keys _before_ you create or update a zone with external masters or external downstream servers that use them. See [Managing TSIG Keys](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig.htm#manage-tsig "Transaction signature \(TSIG\), also referred to as Secret Key Transaction Authentication, ensures that domain name service \(DNS\) packets originate from an authorized sender by using shared secret keys and one-way hashing to add a cryptographic signature to the DNS packets.") for more information.
## Monitoring Secondary DNS 🔗 
The OCI DNS service emits the following metrics to help you monitor zone transfers for both secondary ingress and secondary egress:
  * `ZoneTransferFailureCount`
  * `ZoneTransferSuccessCount`
  * `ZoneExpirationInHours`


These metrics can be used to configure [notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm) that let you know if secondary DNS zones are working. 
For example, you can configure an [alarm](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#alarms) based on the number of times the Zone Transfer fails for a zone (`ZoneTransferFailureCount`). Then, you can configure a [notification](https://docs.oracle.com/iaas/Content/Notification/home.htm) that sends subscribers a message when the alarm is triggered. You can send messages by different protocols, including email, Slack, or SMS.
Here's how this notification is set up:
  1. [Create an alarm that is triggered by exceeding a specified Zone Transfer Failure Count](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/create-alarm-basic.htm#top) Specify the **Namespace** as `oci_dns`, and the **Metric** name as `ZoneTransferFailureCount`.
Set the **Trigger rule operator** to `greater than`, and specify the failure count that exceeds tolerance during the interval.
**Note** When you're configuring an alarm for `Zone Transfer Failure Count`, be sure to carefully consider the refresh rate value in the SOA of the secondary zone. The refresh rate varies from 1200 do 43200 seconds. For example, if the refresh rate value is short, but the alarm interval is high, you could receive a lot of duplicate alarm notifications.
To get a notification for the alarm, specify a **Topic** to send the alarm to. You can create a new topic in this workflow if you need to.
  2. [Create a subscription to the topic](https://docs.oracle.com/iaas/Content/Notification/Tasks/create-subscription.htm#top)
To receive a notification for an alarm, subscribe to the **Topic** that you sent the alarm to in step 1. You can configure the subscription to send to different protocols such as email, Slack, or SMS. You can specify an email list, or you can create individual subscriptions with a single address.
**Note** If you expect more than 60 alarm messages in a minute, you can send the alarm to the [Streaming](https://docs.oracle.com/iaas/Content/Streaming/Concepts/streamingoverview.htm) service and receive a stream.


See [DNS Metrics](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/dnsmetrics.htm#dns_metrics "Learn about the metrics emitted by the metric namespace oci_dns \(the DNS service\).") for a detailed description on the metric types emitted by DNS.
## Limitations and Considerations 🔗 
  * Ensure that secondary nameservers can connect to primary providers, and that they support zone transfers to the secondary nameserver's IP addresses. For cases where OCI is the secondary DNS provider (ingress), we provide you with a list of host server IPs that the primary nameservers can transfer zone files to. For cases where the secondary DNS provider is external (egress), you can obtain the IP addresses from the provider.
  * If an external primary provider signs zones with **DNSSEC** , the signatures are transferred with the zone records. OCI doesn't issue DNSSEC signed zones, but supports externally signed DNS zones. For DNSSEC records to be transferred to OCI DNS as the secondary, the external primary would need to transfer a signed zone. If the external primary only does inline signing, then DNSSEC records aren't included in the transfer.
  * Advanced features provided by a primary DNS provider aren't supported in secondary DNS. This statement applies to both secondary ingress to OCI DNS and secondary egress to an external provider. Examples of advanced features include OCI Traffic Management Steering Policies, round-robin balancing, or [ALIAS](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/supporteddnsresource.htm#types).


## Setting Up Secondary Egress 🔗 
Set up egress from Oracle Cloud Infrastructure DNS to an external DNS provider.
Prerequisites:
  * IP addresses of the external downstream servers.
  * (Optional) Create TSIG keys to assign to each downstream server.
  * Connectivity to OCI egress nameserver IP addresses on externally managed master DNS servers. Connectivity to OCI IP addresses is a requirement to successfully configuring secondary DNS because it lets the service perform the required zone transfer to secondary to keep the zone in sync.


You can obtain the OCI IP addresses that perform the zone transfers using the Oracle Cloud Infrastructure API before you begin setup. [ ListZoneTransferServers](https://docs.oracle.com/iaas/api/#/en/dns/latest/ZoneTransferServer/ListZoneTransferServers) returns a list of IP addresses provided for a specified root compartment. The provided transfer name server IP addresses vary by region.
### Secondary Egress Setup Tasks 🔗 
  1. (Optional) [Listing Zone Transfer Servers](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-transfer-server-list.htm#top "You can use the CLI or API to obtain a list of IP addresses of OCI domain name service \(DNS\) nameservers for inbound and outbound transfer of zones.")
  2. (Optional) [Creating a TSIG Key](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-create.htm#top "Create a TSIG key to enable the domain name service \(DNS\) to authenticate updates to secondary zones.")
  3. [Creating a Public DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/gettingstarted_topic-Creating_a_Zone.htm#top "Create a public domain name service \(DNS\) zone to hold the trusted DNS records that reside on Oracle Cloud Infrastructure's nameservers.")
  4. [Adding Downstream Servers to a Primary DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/add-downstream-servers-primary-zone.htm#top "Set up secondary egress from OCI DNS to an external DNS provider.")


## Setting Up Secondary Ingress 🔗 
Set up ingress from an external DNS provider to Oracle Cloud Infrastructure DNS.
Prerequisites:
  * IP addresses of the primary upstream server.
  * (Optional) Create TSIG keys to assign to each upstream server.
  * Connectivity to OCI ingress nameserver IP addresses on an externally managed master DNS servers. Connectivity to OCI IP addresses is a requirement to successfully configuring secondary DNS because it lets the service perform the required zone transfer process from the primary to keep the secondary zone in sync.


You can obtain the OCI IP addresses that perform the zone transfers using the Oracle Cloud Infrastructure API before you begin setup. [ ListZoneTransferServers](https://docs.oracle.com/iaas/api/#/en/dns/latest/ZoneTransferServer/ListZoneTransferServers) returns a list of IP addresses provided for the specified root compartment. The provided transfer name server IP addresses vary by region.
### Secondary Ingress Setup Tasks 🔗 
  1. (Optional) [Listing Zone Transfer Servers](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-transfer-server-list.htm#top "You can use the CLI or API to obtain a list of IP addresses of OCI domain name service \(DNS\) nameservers for inbound and outbound transfer of zones.")
  2. (Optional) [Creating a TSIG Key](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-create.htm#top "Create a TSIG key to enable the domain name service \(DNS\) to authenticate updates to secondary zones.")
  3. [Creating a Secondary DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/create-secondary-zone.htm#top "Create a secondary domain name service \(DNS\) zone to set up ingress from an external DNS provider to Oracle Cloud Infrastructure \(OCI\) DNS.")


Was this article helpful?
YesNo


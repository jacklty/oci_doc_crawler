Updated 2025-03-10
# Dynamic Routing Gateways
This topic describes how to manage a **dynamic routing gateway (DRG)**. This topic uses the terms _dynamic routing gateway_ and _DRG_ interchangeably. The Console uses the term _Dynamic Routing Gateway_ , whereas for brevity the API uses _DRG_.
A DRG is a virtual router to which you can attach the following resources:
  * [VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNs.htm#VCNs_temp "A Virtual Cloud Network \(VCN\) is a customizable and private network set up in Oracle Cloud Infrastructure.")
  * [Remote Peering Connections](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Remote_VCN_Peering_Across_Regions)
  * Site-to-Site VPN [IPSec tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\).")
  * Oracle Cloud Infrastructure FastConnect [virtual circuits ](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.")


A DRG can have [many network attachments](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#DRG_limits) of each of the following types:
  * **VCN attachments** : you can attach many VCNs to a single DRG. Each VCN can be in the same tenancy as the DRG, or in a different tenancy (provided appropriate policies are set). A VCN can attach to one and only one DRG. 
  * **RPC attachments** : you can peer a DRG to other DRGs using remote peering connections. The other DRG can be in other regions or tenancies, or in the same region.
  * **IPSEC_TUNNEL attachments** : you can use Site-to-Site VPN to attach two or more IPSec tunnels to your DRG to connect to on-premises networks. This is also allowed across tenancies.
  * **VIRTUAL_CIRCUIT attachments** : you can attach one or more FastConnect virtual circuits to your DRG to connect to on-premises networks. 
  * **LOOPBACK attachments** : you can use Site-to-Site VPN to encrypt FastConnect virtual circuits. See [Loopback Attachments](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm#fastconnectsecurity_topic-loopback) for details. 


Creating DRG route tables and DRG route distributions lets you define routing policies that route traffic between attachments. Routes can be dynamically imported and exported through these attachments. A route table must be associated with an attachment for that table's configuration to be applied, but an unassociated routing table can exist. DRG route distributions are of an explicit type (either import or export) and don't inherit an action that depends on where they're associated.
## Overview of Dynamic Routing Gateways 🔗 
A DRG acts as a virtual router, providing a path for traffic between on-premises networks and VCNs, and can also be used to route traffic between VCNs. Using different types of attachments, custom network topologies can be constructed using components in different regions and tenancies. Each DRG attachment has an associated route table which is used to route packets entering the DRG to their next hop. In addition to static routes, routes from the attached networks are dynamically imported into DRG route tables using optional import route distributions.
### Working with DRGs and DRG Attachments 🔗 
**Note** A DRG created before April 2021 can't perform transit routing between on-premises networks and VCNs, or provide peering between VCNs. If you require that functionality and you see an **Upgrade DRG** button in the console, click it. Upgrading the DRG resets all existing BGP sessions and temporarily interrupts traffic from the on-premises network. After the upgrade starts, you can't roll it back. See [Upgrading a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-upgrade.htm#drg-upgrade "Upgrade a Dynamic Routing Gateway \(DRG\) in Oracle Cloud Infrastructure.").
When creating a DRG, you must specify the compartment where you want the DRG to reside. Placing the DRG in a compartment helps to limit access control. If you're not sure which compartment to use, put the DRG in the same compartment as a VCN you use regularly. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
You might optionally assign a friendly name to the DRG. It doesn't have to be unique, and you can change it later. Oracle automatically assigns the DRG a unique identifier called an Oracle Cloud ID (OCID). For more information, see [Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
To use a DRG, it must be attached to other network resources. In the API, the process of attaching creates a `DrgAttachment` object with its own OCID. The `DrgAttachment` has a type field which denotes the type of object being attached to the DRG. The type field can be set to one of the following values:
  * VCN
  * VIRTUAL_CIRCUIT
  * IPSEC_TUNNEL
  * REMOTE_PEERING_CONNECTION
  * LOOPBACK (See [Loopback Attachments](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm#fastconnectsecurity_topic-loopback) for more details.) 


To attach a VCN to a DRG, use the `CreateDrgAttachment` operation or the Console to explicitly create the DRG attachment object. Attachments for virtual circuits, IPSec tunnels, and remote peering connections are created (and deleted) automatically for you when you create (or delete) the network object.
### Working with DRG Route Tables and Route Distributions  🔗 
A packet enters a DRG through an attachment and is routed using rules in the DRG route table assigned to that attachment. You can assign the same route table to many DRG attachments or create a dedicated route table for each attachment depending on the routing policies you want. 
When you create a DRG, two default route tables are created for you: one for VCN attachments and one for all other attachments. When a route table is set as the default route table for an attachment type, the table is assigned to newly created attachments of that type unless an alternate table is explicitly specified. Route tables specified as the default for any type can't be deleted. Ensure that a route table isn't set as a default route table for an attachment type before trying to delete it. 
A VCN attachment has two route tables: One DRG routing table for traffic entering the DRG, and one VCN routing table for traffic entering the VCN. The DRG route table exists in the DRG and is used to route packets entering the DRG through the attachment. The VCN route table is used to route packets entering the VCN through the attachment. If a VCN routing table isn't defined, a hidden implicit table always provides connectivity to all subnets in the VCN.
### Dynamic Import/Export Route Distributions 🔗 
DRG route tables contain both static and dynamic routes. Static routes are inserted into tables using the API, while dynamic routes are imported from attachments and inserted using a route distribution, a list of declarative statements that contain a match criteria (such as an OCID or an attachment type) and an action. You can use route distributions to specify how routes get imported from or exported to a DRG attachment. Two auto generated import route distributions are created for each DRG: one for VCN routes only and one for all routes. You can create other import route distributions.
When a route distribution's match criteria includes an attachment type, routes associated with the attachment are dynamically imported into the DRG route table used by the attachment. When a statement is removed from the route distribution, the matching routes are removed from the DRG route tables. Statements in a route distribution are evaluated in priority order: the lowest number has the highest priority. The order in which statements are evaluated doesn't affect the preference set for the routes they import.
When building route distribution statements in the Console, you can create a statement whose match type is "Match All". In the API, encode a "match all" statement by setting the match criteria to an empty list. 
**How do dynamic routes arrive at an attachment?**
Routes to your on-premises networks are advertised from the CPE to IPSec tunnel and virtual circuit attachments using BGP. Routes are dynamically propagated from an RPC attachment on one DRG to an RPC attachment on another DRG through connected RPCs. Dynamic routes in a VCN include either all subnet CIDRs or all VCN CIDRs _and_ all static route CIDRs configured on the VCN route table associated with the DRG attachment. The vcnRouteType property of the VCN attachment determines whether the subnet CIDRs or VCN CIDRs are propagated into the VCN attachment. The default behavior is to import the subnet CIDRs, but this behavior can be changed when creating or updating the VCN attachment. Refer to [Route Aggregation](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#managingDRGs_topic_drg_routing__rt_agg) for other details. 
### Dynamic Export Route Distributions 🔗 
When an attachment is assigned to a DRG route table, the contents of that table can be dynamically exported to the attachment. If the default export route distribution is assigned to an attachment, the entire contents of the attachment's assigned DRG route table are dynamically exported to the attachment. To disable dynamic route exports to an attachment, use the API operation `removeExportDrgRouteDistribution` to set the attachment's `exportDrgRouteDistributionId` field to NULL. Dynamic route export to VCN attachments isn't supported.
One auto generated export route distribution is created for each DRG. You can create and attach other export route distributions using the CLI and API.
### Route Propagation Restrictions
Routes imported from an **IPSec tunnel** or **virtual circuit** are never exported to other **IPSec tunnel** or **virtual circuit** attachments, regardless of how the export route distribution is configured. In a similar vein, packets which enter a DRG through an IPSec tunnel or virtual circuit attachment can never leave through an IPSec tunnel or virtual circuit attachment. Packets are dropped if routing is configured such that packets originating from IPSec tunnel or virtual circuit attachments are sent to IPSec tunnel or virtual circuit attachments.
### ECMP 🔗 
Equal-cost multi-path routing (ECMP) lets flow-based load balancing of network traffic over FastConnect virtual circuits or IPSec tunnels (but not a mix of circuit types) using BGP. ECMP allows active-active load balancing and failover of network traffic between a maximum of eight circuits. 
Oracle uses the protocol, destination IP, source IP, destination port, and source port to distinguish flows for load balancing purposes using a consistent and deterministic algorithm. Therefore, several flows are necessary to use all available bandwidth. 
ECMP is off by default and can be enabled on a per-route table basis. Oracle only considers routes with identical route preference as eligible for ECMP forwarding. See [Route Conflicts](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#managingDRGs_topic_drg_routing__conflicts) for more.
### Route Source
DRG routes _originate_ as either static routes or as dynamic routes from VCN, IPSec tunnel, FastConnect virtual circuit, or RPC attachments. This origin defines their **source** , which is an immutable characteristic of the route. In the API, the source is referred to as the `routeProvenance` of a DrgRouteRule. 
Routes are _propagated_ between DRGs using RPC attachments. 
Routes with a source of IPSEC_TUNNEL or VIRTUAL_CIRCUIT aren't exported to IPSec tunnel or virtual circuit attachments, regardless of the attachment's export distribution.
### Routing a Subnet's Traffic to a DRG
The basic routing scenario sends traffic from a subnet in the VCN to the DRG. For example, if you're sending traffic from the subnet to an on-premises network, you [set up a rule in the subnet's route table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables_topic-working.htm#add_route_rule). The rule's destination CIDR is the CIDR for the on-premises network (or a subnet within), and the rule's target is the DRG. For more information, see [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2).
### Required IAM Policy 🔗 
Peering VCNs using a DRG requires specific IAM permissions. See [IAM Policies for Routing Between VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m "Learn about IAM policies used with peering and dynamic routing gateways.") for details on the permissions needed. 
### DRG Versions 🔗 
DRGs created before May 17, 2021 use the legacy software, and can be upgraded to the most recent version. DRGs created after that have the upgraded features by default. 
The following summarizes the difference between an upgraded and legacy DRG: 
A legacy DRG:
  * Has no programmable route tables. It has a default routing behavior where all traffic is forwarded from on-premises to an associated VCN and from the VCN to on-premises.
  * Can attach to a single VCN. The DRG can attach to another DRG for remote VCN peering using an RPC.
  * Can attach FastConnect or Site-to-Site VPN, or both. You can only reach resources in the local region using these connections.
  * Can support an RPC connection with a remote DRG-VCN pair in the same tenancy. See [Remote VCN Peering using a Legacy DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Remote_VCN_Peering_Across_Regions) to learn about remote peering using a legacy DRG.


An upgraded DRG: 
  * Has two route tables by default, and more can be added later.
  * Can have many VCNs attached to it within the same region. Local VCN to VCN traffic can pass through a mutually connected DRG instead of an LPG. See [Local VCN Peering Through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenariod "This scenario describes using a mutual connection to an upgraded DRG to enable traffic between two or more VCNs.") for details. 
  * Can attach to on-premises using FastConnect orSite-to-Site VPN, or both. You can reach resources in both local and remote regions using these connections.
  * Supports an RPC connection with a DRG/VCN pair in the same tenancy or another tenancy. See [Remote VCN Peering through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_e.htm#scenario_e "This topic is about remote VCN peering.") to learn about remote peering using an upgraded DRG.


The rest of this article has recently been updated to reflect the capabilities of an upgraded DRG, as have the common [networking scenarios](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarios.htm#networking_scenarios). [Remote VCN Peering using a Legacy DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Remote_VCN_Peering_Across_Regions) is the only routing or peering scenario specific to a legacy DRG.
### Before you Upgrade a DRG 🔗 
**Note** We recommend upgrading a DRG during a maintenance window. 
To take advantage of enhanced DRG features, upgrade the DRG. The DRG upgrade process is automated, but you must have the required permissions to start an upgrade. Upgrading a DRG is a one-way process with no option to roll back to a legacy DRG after the upgrade process has been started. 
Expect each of the DRG's attachments to update in turn, forcing each upgrading attachment into a provisioning state. Virtual circuit and VPN tunnel attachments can no longer forward traffic when in a provisioning state. If you only have one virtual circuit, it could go down for about 20 minutes. Any existing BGP sessions for on-premises connections are also reset while the attachment and connections are also brought offline.
If you have redundant connections, expect traffic to failover to other circuits while one connection undergoes upgrade. Using a [redundant configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectresiliency.htm#FastConnect_Redundancy_Best_Practices "This topic covers best practices for redundancy when implementing FastConnect."), the overall connection between on-premises and OCI is maintained during the DRG upgrade. For example, if a DRG has two FastConnect virtual circuit attachments to an on premises network with one configured as primary, while the primary virtual circuit is upgraded it drops connectivity but traffic can still pass over the secondary virtual circuit. After that first update has finished and traffic over the primary virtual circuit is restored, the process upgrades the secondary virtual circuit attachment and eventually both virtual circuits are back online. Expect the upgrade process to last up to 30 minutes per on-premises attachment. Likewise, if the upgrade process upgrades the secondary virtual circuit's attachment first, traffic stops on that circuit but can still pass over the primary virtual circuit until the secondary circuit connection is reestablished.
Remote peering connections and VCN attachments don't need to have a BGP reset the way virtual circuit or IPSec tunnel connections do, and the upgrade is faster. VCN connections to an LPG or other gateways are unaffected, as they're attachments on the VCN and not the DRG.
After the DRG upgrade process has completed, any Site-to-Site VPN IPSec tunnels are brought back online and all BGP sessions for FastConnect and Site-to-Site VPN are re-established. By default, the upgraded DRG has two auto generated DRG route tables and import route distributions enabled for the attachments. These resources are designed for backward compatibility with a legacy DRG and allow all previous communication to resume in the same manner as before the upgrade without further user intervention.
For step-by-step instructions on how to upgrade a DRG, see [Upgrading a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-upgrade.htm#drg-upgrade "Upgrade a Dynamic Routing Gateway \(DRG\) in Oracle Cloud Infrastructure.").
**Note** If the DRG upgrade process gets stuck for any reason, create a service request at [My Oracle Support](http://support.oracle.com/), and mark the ticket as high severity.
### Scenarios
We have provided some detailed networking [scenarios](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarios.htm#networking_scenarios) to help you understand the role of a DRG in the Networking service and how the components work together in general.
## DRG Routing 🔗 
See the [Learn routing in OCI Networking with examples (PDF)](https://docs.oracle.com/iaas/Content/Resources/Assets/whitepapers/learn-routing-in-oci-networking-with-examples.pdf) technical brief to learn more about DRG routing.
### Route Conflicts 🔗 
If two routes with identical CIDRs are observed the same DRG route table, the DRG resolves the conflict using the following criteria:
  1. Static routes always have higher preference than dynamic routes.
**Note** You can't manually specify two static routes with the same CIDR in the same DRG route table, but it's possible for more than one route with the same CIDR to be imported dynamically.
  2. Conflicts between dynamic routes are resolved by first analyzing the route's AS Path:
     * Routes with a route source of VCN or STATIC always have an empty AS Path. 
     * Routes with a route source of IPSEC_TUNNEL or VIRTUAL_CIRCUIT have populated AS Path data (see [Routing Details for Connections to the On-premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem2.htm#Routing_Details_for_Connections_to_Your_OnPremises_Network) for more details).
  3. Otherwise, the attachment type that imported the route is evaluated according to the following priority based on the attachment type: 
    1. **VCN:** the DRG makes an arbitrary but stable selection.
    2. **VIRTUAL_CIRCUIT:** If ECMP is _disabled_ , the DRG makes an arbitrary but stable selection. If ECMP is _enabled_ , all routes are added to the route table and the DRG makes routing choices using ECMP. The maximum supported ECMP width inside a DRG is 8.
    3. **IPSEC_TUNNEL:** If ECMP is _disabled_ , the DRG makes an arbitrary but stable selection.If ECMP is _enabled_ , all routes are added to the route table and the DRG makes routing choices using ECMP. The maximum supported ECMP width inside a DRG is 8.
    4. **REMOTE_PEERING_CONNECTION:** The DRG chooses the route with the lowest network distance. 
If two routes have identical network distances, the DRG selects the route with the highest priority route source (STATIC > VCN > VIRTUAL_CIRCUIT> IPSEC_TUNNEL > RPC). 
If two routes have the same route source, the DRG makes an arbitrary but stable selection.
  4. If conflicting routes are imported from attachments of the same type, the conflict is resolved differently depending on the attachment type:
    1. **VCN attachments** : If identical CIDRs are imported from two VCN attachments, only one is selected using an arbitrary but stable decision procedure. 
    2. **VIRTUAL_CIRCUIT and IPSEC_TUNNEL attachments** : If several routes with the same CIDR and different AS_PATH lengths are imported into a DRG route table, the route with the lowest AS_PATH length is selected. Otherwise, one route is chosen using an arbitrary but stable decision procedure. 
    3. **RPC attachments** : If identical CIDRs are imported from two RPC attachments, one of them is chosen using an arbitrary stable decision procedure.


You can observe the results of conflict resolution by listing the contents of the route table. Deprecated routes are marked with the "conflict" status.
### Route Aggregation 🔗 
As described in [RFC-1338](https://www.rfc-editor.org/rfc/rfc1338) route aggregation lets you "advertise a single, aggregate, route which describes all of the destinations contained within it" instead of advertising a separate route for each client. The primary example of this in OCI Networking happens when you configure a DRG's VCN attachment to [import VCN CIDRs instead of subnet CIDRs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-attachment.htm#drg-create_attachment "Create a VCN attachment on a Dynamic Routing Gateway \(DRG\) in Oracle Cloud Infrastructure."), thus simplifying what routes are advertised by BGP. Depending on the network architecture, you might also choose to:
  * Use static routes instead of import distributions on the DRG to summarize even more narrowly (the scope for this is limited to that specific attachment)
  * Aggregate across several attachments by introducing a second DRG and making the aggregated attachments only available through an RPC to another DRG


Other forms of route aggregation aren't available.
### Limitations 🔗 
Some functions might appear to be possible, but the following routing functions aren't allowed: 
  * Explicit creation or deletion of RPC, IPSec tunnel, or virtual circuit attachments
  * Static routes in DRG route tables with next-hop of IPSec tunnel or virtual circuit attachments
  * Use of non-default export route distributions
  * Dynamic route export to VCN attachments
  * Routes propagating through RPC through more than 4 DRGs 


### Using BGP to prefer routes from Oracle to your on-premises network 🔗 
This section describes in greater detail how the BGP AS_PATH attribute can be used to influence route selection in the context of a single DRG route table.
If the routes for the different paths are the same, **Oracle uses the shortest AS path** when sending traffic to an on-premises network, regardless of which path was used to start the connection to Oracle.**Therefore asymmetric routing is allowed.** _Asymmetric routing_ here means that Oracle's response to a request can follow a different path than the request. For example, depending on how an edge device (also called the _customer-premises equipment_ , or CPE) is configured, you could send a request over Site-to-Site VPN, but the Oracle response could come back over FastConnect. To force symmetric routing, we recommend using BGP and AS path prepended with the routes to influence which path Oracle uses when responding to and starting connections. 
Oracle implements AS path prepending to establish preference on which path to use if an edge device advertises the same route and routing attributes over different connection types between an on-premises network and a VCN. The details are summarized in the following table. Unless you're influencing routing in some other way, when the same route is advertised over multiple paths to the DRG at the Oracle end of the connections, Oracle prefers the paths in the following order:
Oracle preference | Path | Details of how Oracle prefers the path | Resulting AS path for the route  
---|---|---|---  
**1** |  FastConnect | Oracle prepends no ASNs to the routes that the edge device advertises, for a total AS path length of 1. | Your ASN  
**2** | Site-to-Site VPN with BGP routing | Oracle prepends a single private ASN on all the routes that your edge device advertises over Site-to-Site VPN with BGP, for a total AS path length of 2. | Private ASN, Your ASN  
**3** | Site-to-Site VPN with static routing | Oracle prepends 3 private ASNs on the static routes that you've provided (Oracle advertises those routes to the **dynamic routing gateway (DRG)** at the Oracle end of Site-to-Site VPN). This results in a total AS path length of 3. | Private ASN, Private ASN, Private ASN  
The preceding table assumes you're sending a single autonomous system number in your AS path. Oracle honors the complete AS path you send. If you use static routing, and also send an AS path that has "Your ASN" plus two or more other ASNs, it can cause unexpected behavior because Oracle's routing preference might change.
While policy-based VPN static routing behavior is documented earlier, Oracle also recommends that if you use FastConnect connections with VPN backup, you use BGP on the IPSec route-based VPN. This strategy lets you have full control of failover behavior.
#### Other relevant links
  * [DRG Route Advertisements to the On-Premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem2.htm#DRG_Route_Advertisements_to_Your_OnPremises_Network)
  * [Using AS_PATH to Prefer Routes from Oracle to the On-premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem2.htm#oracle-to-on-prem)
  * [Routing Preferences for Traffic from An On-premises Network to Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem2.htm#on-prem-to-oracle)


Was this article helpful?
YesNo


Updated 2024-11-06
# Details for the Core Services
This topic covers details for writing policies to control access to the Core Services (Networking, Compute, and Block Volume).
## Resource-Types 🔗 
[Networking](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
#### Aggregate Resource-Type
`virtual-network-family`
`drgs` (covers drg-object, drg-route-table, drg-route-distribution, drg-attachment)
#### Individual Resource-Types
`byoiprange`
`capture-filters`
`cpes`
`cross-connect-groups`
`cross-connects`
`dhcp-options`
`drg-attachments`
`drg-object`
`drg-route-distributions`
`drg-route-tables`
`internet-gateways`
`ipsec-connections`
`ipv6s`
`ipam`
`local-peering-gateways` (which includes `local-peering-from`, and `local-peering-to`) 
`nat-gateways`
`network-security-groups`
`private-ips`
`publicippool`
`public-ips`
`remote-peering-connections` (which includes `remote-peering-from`, and `remote-peering-to`) 
`route-tables`
`security-lists`
`service-gateways`
`subnets`
`vcns`
`virtual-circuits`
`vlans`
`vnic-attachments`
`vnics`
`vtaps`
#### Comments
A policy that uses `<verb> virtual-network-family` is equivalent to writing one with a separate `<verb> <individual resource-type>` statement for each of the individual resource-types.
See the table in [Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm#Core) for details of the API operations covered by each verb, for each individual resource-type included in `virtual-network-family`.
[Compute](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
#### instance-family Aggregate Resource-Type
The `instance-family` aggregate resource-type covers these individual resource-types:
`app-catalog-listing`
`console-histories`
`instances`
`instance-console-connection`
`instance-images`
`volume-attachments` (includes only the permissions required for attaching volumes to instances)
#### compute-management-family Aggregate Resource-Type
The `compute-management-family` aggregate resource-type covers these individual resource-types:
`instance-configurations`
`instance-pools`
`cluster-networks`
#### instance-agent-family Aggregate Resource-Type
The `instance-agent-family` aggregate resource-type covers this individual resource-type:
`instance-agent-plugins`
#### instance-agent-command-family Aggregate Resource-Type
The `instance-agent-command-family` aggregate resource-type covers this individual resource-type:
`instance-agent-commands`
#### Additional Individual Resource-Types
`auto-scaling-configurations`
`compute-capacity-reports`
`compute-capacity-reservations`
`compute-clusters`
`compute-global-image-capability-schema`
`compute-image-capability-schema`
`dedicated-vm-hosts`
`instance-agent-commands`
`work-requests`
#### Comments
A policy that uses `<verb> instance-family` or `<verb> compute-management-family` is equivalent to writing one with a separate `<verb> <individual resource-type>` statement for each of the individual resource-types in the family.
See the table in [Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm#Core) for details of the API operations covered by each verb, for each individual resource-type.
[Block Volume](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
#### Aggregate Resource-Type 🔗 
`volume-family`
#### Individual Resource-Types 🔗 
`volumes`
`volume-attachments`
`volume-backups`
`boot-volume-backups`
`backup-policies`
`backup-policy-assignments`
`volume-groups`
`volume-group-backups`
#### Comments 🔗 
A policy that uses `<verb> volume-family` is equivalent to writing one with a separate `<verb> <individual             resource-type>` statement for each of the individual resource-types.
See the table in [Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm#Core) for details of the API operations covered by each verb, for each individual resource-type included in `volume-family`.
## Supported Variables 🔗 
The Core Services support all the general variables, plus the ones listed here. For more information about general variables supported by Oracle Cloud Infrastructure services, see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General).
Variable | Variable Type | Comments  
---|---|---  
`target.boot-volume.kms-key.id` | String | Use this variable to control whether Compute instances can be launched with boot volumes that were created without a Vault service master encryption key.  
`target.image.id` | String | The specific image OCID allowed by the policy.  
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
For example, the `read` and `use` verbs for the `vcns` resource-type cover no extra permissions or API operations compared to the `inspect` verb. However, the `manage` verb includes several extra permissions and API operations.
### For virtual-network-family Resource Types 🔗 
The following tables list the permissions and API operations covered by each of the individual resource-types included in `virtual-network-family`.
[byoiprange](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  BYOIP_RANGE_INSPECT |  `ListByoipRanges` |  none  
read |  INSPECT+ BYOIP_RANGE_READ |  `GetByoipRange` `ListByoipAllocatedRanges` |  none  
use |  READ + BYOIP_RANGE_ADD_CAPACITY_FROM | `AddPublicIpPoolCapacity` |  none  
manage |  USE + BYOIP_RANGE_CREATE BYOIP_RANGE_DELETE BYOIP_RANGE_UPDATE BYOIP_RANGE_VALIDATE BYOIP_RANGE_ADVERTISE BYOIP_RANGE_WITHDRAW BYOIP_RANGE_MOVE |  `CreateByoipRange` `DeleteByoipRange` `UpdateByoipRange` `ValidateByoipRange` `AdvertiseByoipRange` `WithdrawByoipRange` `ChangeByoipRangeCompartment` |  none  
[capture-filters](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  CAPTURE_FILTER_LIST |  `ListCaptureFilters` |  none  
read |  INSPECT+ CAPTURE_FILTER_READ |  `GetCaptureFilter` |  none  
use |  READ + CAPTURE_FILTER_UPDATE CAPTURE_FILTER_ATTACH CAPTURE_FILTER_DETACH | `UpdateCaptureFilter` |  none  
manage |  USE + CAPTURE_FILTER_CREATE CAPTURE_FILTER_DELETE CAPTURE_FILTER_MOVE |  `ChangeCaptureFilterCompartment` | `CreateCaptureFilter` requires CAPTURE_FILTER_CREATE and VCN_ATTACH`DeleteCaptureFilter` requires CAPTURE_FILTER_DELETE and VCN_DETACH**Note:** The above operations in this cell are totally covered with just `manage         virtual-network-family`.  
[cpes](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | CPE_READ | `ListCpes` `GetCpe` | none  
read | no extra | no extra | none  
use | no extra | no extra | none  
manage | USE + CPE_ATTACH CPE_DETACH CPE_UPDATE CPE_CREATE CPE_DELETE CPE_RESOURCE_MOVE | USE + `CreateCpe` `UpdateCpe` `DeleteCpe` `ChangeCpeCompartment` | `CreateIPSecConnection, DeleteIPSecConnection` (both also need `manage ipsec-connections` and `manage drgs`) **Note:** All of the above operations in this cell are totally covered with just `manage virtual-network-family`.  
[cross-connect-groups](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | CROSS_CONNECT_GROUP_READ | `ListCrossConnectGroups` `GetCrossConnectGroup` | none  
read | no extra | no extra | none  
use | no extra | no extra | no extra  
manage | USE + CROSS_CONNECT_GROUP_UPDATE CROSS_CONNECT_GROUP_CREATE CROSS_CONNECT_GROUP_DELETE CROSS_CONNECT_GROUP_RESOURCE_MOVE | `UpdateCrossConnectGroup` `CreateCrossConnectGroup` `DeleteCrossConnectGroup` `ChangeCrossConnectGroupCompartment` | no extra  
[cross-connects](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | CROSS_CONNECT_READ | `ListCrossConnects` `GetCrossConnect` | none  
read | no extra | no extra | none  
use | no extra | no extra | no extra  
manage | USE + CROSS_CONNECT_UPDATE CROSS_CONNECT_CREATE CROSS_CONNECT_DELETE CROSS_CONNECT_RESOURCE_MOVE CROSS_CONNECT_ATTACH CROSS_CONNECT_DETACH | `UpdateCrossConnect` `CreateCrossConnect` `DeleteCrossConnect` `ChangeCrossConnectCompartment` | `UpdateVirtualCircuit` (also need `use virtual-circuits`) `CreateVirtualCircuit, DeleteVirtualCircuit` (also need `manage virtual-circuits`)  
[dhcp-options](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | DHCP_READ | `ListDhcpOptions` `GetDhcpOptions` | none  
read | no extra | no extra | none  
use | no extra | no extra | none  
manage | USE + DHCP_ATTACH  DHCP_DETACH DHCP_UPDATE DHCP_CREATE DHCP_DELETE DHCP_MOVE | USE + `UpdateDhcpOptions` **Note:** Ability to update a set of DHCP options is available only with the `manage` verb, not the `use` verb. `ChangeDhcpOptionsCompartment` | USE + `CreateDhcpOptions, DeleteDhcpOptions` (both also need `manage vcns`) `CreateSubnet, DeleteSubnet` (also need `manage vcns, manage subnets, manage route-tables, manage security-lists`) `UpdateSubnet` (if changing which set of DHCP options is associated with the subnet, also need `manage subnets`) **Note:** All of the above operations in this cell are totally covered with just `manage virtual-network-family`.  
[drgs](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
#### drg-object
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  DRG_READ  |  `GetDrg ` `ListDrgs` `GetAllDrgAttachments` |  none  
read |  no extra |  no extra |  none  
use |  DRG_ATTACH DRG_DETACH |  no extra |  `CreateDrgAttachment` (also need `manage                     vcns`, and need `manage route-tables` if you associate a VCN route table during creation) (also need` manage drg-route-tables` if you want to assign a DRG route table during creation) `DeleteDrgAttachment` (also need `manage                     vcns`)  
manage |  USE + DRG_UPDATE DRG_CREATE DRG_DELETE DRG_MOVE |  USE + `CreateDrg` `DeleteDrg` `UpdateDrg` `UpgradeDrg` `ChangeDrgCompartment` |  none  
#### drg-attachment
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  DRG_ATTACHMENT_READ |  `ListDrgAttachments` `GetDrgAttachment` |  none  
read |  no extra |  no extra |  none  
use |  no extra |  no extra |  none  
manage |  USE + DRG_ATTACHMENT_UPDATE |  USE + |  `RemoveExportDrgRouteDistribution` (also need `manage drg-route-distribution` to remove the distribution from the attachment) `UpdateDrgAttachment` (also need `manage                     route-tables` if you associate a VCN route table during the update) (also need `manage                     drg-route-tables` if you want to assign a DRG route table during the update) **Note:** All of the above operations in this cell are totally covered with just `manage                   virtual-network-family`.  
#### drg-route-table
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  DRG_ROUTE_TABLE_READ DRG_ROUTE_RULE_READ |  `GetDrgRouteTable` `ListDrgRouteRules` |  none  
read |  no extra |  no extra |  none  
use |  DRG_ROUTE_TABLE_ATTACH |  no extra |  For assigning the DRG route tables to DRG attachments, use `CreateDrgAttachment` (also need `manage drg-attachment`) `UpdateDrgAttachment` (also need `manage                     drg-attachment`)  
manage |  USE + DRG_ROUTE_TABLE_CREATE DRG_ROUTE_TABLE_DELETE DRG_ROUTE_TABLE_UPDATE DRG_ROUTE_RULE_UPDATE |  USE + `CreateDrgRouteTable` `DeleteDrgRouteTable` `UpdateDrgRouteTable` `UpdateDrgRouteRules` `RemoveDrgRouteRules` `AddDrgRouteRules` |  `RemoveImportDrgRouteDistribution` (also need `manage drg-route-table` to remove the distribution from the DRG route table)  
#### drg-route-distribution
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  DRG_ROUTE_DISTRIBUTION_READ DRG_ROUTE_DISTRIBUTION_STATEMENT_READ |  `GetDrgRouteDistribution` `ListDrgRouteDistributions` `ListDrgRouteDistributionStatements` |  none  
read |  no extra |  no extra |  none  
use |  DRG_ROUTE_DISTRIBUTION_ASSIGN |  no extra |  `UpdateDrgRouteTable` or `CreateDrgRouteTable` (also need `manage drg-route-table` to assign the distribution to a table) `RemoveExportDrgRouteDistribution` (also need `manage drg-attachment` to remove the distribution from the attachment) `RemoveImportDrgRouteDistribution` (also need `manage drg-route-table` to remove the distribution from the table)  
manage |  USE + DRG_ROUTE_DISTRIBUTION_UPDATE DRG_ROUTE_DISTRIBUTION_CREATE DRG_ROUTE_DISTRIBUTION_DELETE DRG_ROUTE_DISTRIBUTION_STATEMENT_UPDATE |  USE + `UpdateDrgRouteDistribution` `CreateDrgRouteDistribution` `DeleteDrgRouteDistribution` `UpdateDrgRouteDistributionStatements` `RemoveDrgRouteDistributionStatements` `AddDrgRouteDistributionStatements` |  none  
[ipsec](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | IPSEC_CONNECTION_READ | `ListIPSecConnections` `GetIPSecConnection` `GetIPSecConnectionStatus` `ListIPSecConnectionTunnels` `GetIPSecConnectionTunnel` `GetTunnelCpeDeviceConfig` `GetTunnelCpeDeviceTemplateContent` `GetCpeDeviceTemplateContent` `GetIpsecCpeDeviceTemplateContent` | none  
read | INSPECT + IPSEC_CONNECTION_DEVICE_CONFIG_READ | INSPECT + `GetIPSecConnectionDeviceConfig` `GetIPSecConnectionTunnelSharedSecret` | none  
use | no extra | no extra | none  
manage | USE + IPSEC_CONNECTION_CREATE IPSEC_CONNECTION_UPDATE IPSEC_CONNECTION_DELETE IPSEC_CONNECTION_DEVICE_CONFIG_UPDATE | USE + `UpdateIPSecConnection` `UpdateTunnelCpeDeviceConfig` `UpdateIPSecConnectionTunnel` | `CreateIPSecConnection, DeleteIPSecConnection` (both also need `manage cpes` and `manage drgs`) **Note:** All of the above operations in this cell are totally covered with just `manage virtual-network-family`.  
[internet-gateways](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | INTERNET_GATEWAY_READ | `ListInternetGateways` `GetInternetGateway` | none  
read | no extra | no extra | none  
use | no extra | no extra | none  
manage | USE + INTERNET_GATEWAY_ATTACH  INTERNET_GATEWAY_DETACH INTERNET_GATEWAY_UPDATE INTERNET_GATEWAY_CREATE INTERNET_GATEWAY_DELETE INTERNET_GATEWAY_MOVE | USE + `UpdateInternetGateway` **Note:** Ability to update a an internet gateway is available only with the `manage` verb, not the `use` verb. `ChangeInternetGatewayCompartment` | `CreateInternetGateway, DeleteInternetGateway` (both also need `manage vcns`) `CreateRouteTable, DeleteRouteTable` (both also need` manage route-tables, manage vcns, manage drgs, manage private-ips, manage local-peering-gateways, use nat-gateways, use nat-gateways, use service-gateways`) `UpdateRouteTable` (also need` manage route-tables, manage drgs, manage private-ips, manage local-peering-gateways, use nat-gateways, use service-gateways`) **Note:** All of the above operations in this cell are totally covered with just `manage virtual-network-family`.  
[ipv6s](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | none | none | none  
read | IPV6_READ | `GetIpv6` | `ListIpv6s` (also need `inspect vnics` and `inspect subnets` to list IPv6s by VNIC and subnets) **Note:** The above operation in this cell is totally covered with just `use virtual-network-family`.  
use | no extra | no extra | no extra  
manage | USE + IPV6_UPDATE IPV6_CREATE IPV6_DELETE | no extra | USE + `UpdateIpv6` (also need `use vnics`) `CreateIpv6, ``DeleteIpv6` (both also need `use vnics` and `use subnets`) **Note:** The above operations in this cell are totally covered with just `manage virtual-network-family`.  
[local-peering-gateways](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | LOCAL_PEERING_GATEWAY_READ | `ListLocalPeeringGateways` `GetLocalPeeringGateway` | none  
read | no extra | no extra | none  
use | no extra | no extra | none  
manage | USE + LOCAL_PEERING_GATEWAY_UPDATE LOCAL_PEERING_GATEWAY_ATTACH  LOCAL_PEERING_GATEWAY_DETACH LOCAL_PEERING_GATEWAY_CREATE LOCAL_PEERING_GATEWAY_DELETE LOCAL_PEERING_GATEWAY_MOVE | no extra | `CreateLocalPeeringGateway` (also need `manage vcns`, and need `manage route-tables` if you associate a route table during creation) `UpdateLocalPeeringGateway` (also need `manage route-tables` if you associate a route table during the update) `DeleteLocalPeeringGateway` (also need `manage vcns`) `CreateRouteTable, DeleteRouteTable` (both also need` manage route-tables, manage vcns, manage internet-gateways, manage drgs, manage private-ips, use nat-gateways, use service-gateways`) `UpdateRouteTable` (also need `manage route-tables, manage internet-gateways, manage drgs, manage private-ips, use nat-gateways, use service-gateways`) `ChangeLocalPeeringGatewayCompartment` **Note:** The above operations in this cell are totally covered with just `manage virtual-network-family`.  
[local-peering-from](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | LOCAL_PEERING_GATEWAY_READ | none | none  
read | no extra | none | none  
use | no extra | none | none  
manage | USE + LOCAL_PEERING_GATEWAY_CONNECT_FROM | no extra | `ConnectLocalPeeringGateways` (acceptor in the peering relationship must also grant the requestor `manage local-peering-to` in the compartment where the acceptor's LPG resides. See [Local VCN Peering using Local Peering Gateways](https://docs.oracle.com/iaas/Content/Network/Tasks/localVCNpeering.htm).) **Note:** The above operation in this cell is totally covered with just `manage virtual-network-family`.  
[local-peering-to](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | LOCAL_PEERING_GATEWAY_READ | none | none  
read | no extra | none | none  
use | no extra | none | none  
manage | USE + LOCAL_PEERING_GATEWAY_CONNECT_TO | no extra | `ConnectLocalPeeringGateways` (requestor in the peering relationship must also have `manage local-peering-from` in the compartment where the requestor's LPG resides. See [Local VCN Peering using Local Peering Gateways](https://docs.oracle.com/iaas/Content/Network/Tasks/localVCNpeering.htm).) **Note:** The above operation in this cell is totally covered with just `manage virtual-network-family`.  
[nat-gateways](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | none | none | none  
read | NAT_GATEWAY_READ | `ListNatGateways` `GetNatGateway` | none  
use | READ + NAT_GATEWAY_ATTACH NAT_GATEWAY_DETACH | no extra | READ + `CreateRouteTable, DeleteRouteTable` (both also need` manage route-tables, manage vcns, manage drgs, manage private-ips, manage internet-gateways, manage local-peering-gateways, use service-gateways`) `UpdateRouteTable` (also need` manage route-tables, manage drgs, manage private-ips, manage internet-gateways, manage local-peering-gateways, use service-gateways`) **Note:** All of the above operations in this cell are totally covered with just `manage virtual-network-family`.  
manage | USE + NAT_GATEWAY_UPDATE NAT_GATEWAY_CREATE NAT_GATEWAY_DELETE NAT_GATEWAY_MOVE | USE + `UpdateNatGateway` `ChangeNatGatewayCompartment` **Note:** Ability to update a NAT gateway is available only with the `manage` verb, not the `use` verb. | `CreateNatGateway, DeleteNatGateway` (both also need `manage vcns`) **Note:** All of the above operations in this cell are totally covered with just `manage virtual-network-family`.  
[network-security-groups](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | NETWORK_SECURITY_GROUP_INSPECT | none | `AddNetworkSecurityGroupSecurityRules` and `UpdateNetworkSecurityGroupSecurityRules` (both also need `manage network-security-groups`)   
read | INSPECT + NETWORK_SECURITY_GROUP_READ | INSPECT + `GetNetworkSecurityGroup` `ListNetworkSecurityGroups` | no extra  
use | READ + NETWORK_SECURITY_GROUP_LIST_SECURITY_RULES NETWORK_SECURITY_GROUP_LIST_MEMBERS NETWORK_SECURITY_GROUP_UPDATE_MEMBERS | READ + `ListNetworkSecurityGroupSecurityRules` `ListNetworkSecurityGroupVnics` | READ + `LaunchInstance` (also need `manage instances`, `read instance-images`, `use vnics`, `use subnets`, and `read app-catalog-listing`) `AttachVnic` (also need `manage instances`, and `use subnets`) `UpdateVnic` (also need `use vnics`)   
manage | USE + NETWORK_SECURITY_GROUP_UPDATE NETWORK_SECURITY_GROUP_CREATE NETWORK_SECURITY_GROUP_DELETE NETWORK_SECURITY_GROUP_MOVE NETWORK_SECURITY_GROUP_UPDATE_SECURITY_RULES | USE + `UpdateNetworkSecurityGroup` `ChangeNetworkSecurityGroupCompartment` `AddNetworkSecurityGroupSecurityRules` `UpdateNetworkSecurityGroupSecurityRules` `RemoveNetworkSecurityGroupSecurityRules` | USE + `CreateNetworkSecurityGroup, DeleteNetworkSecurityGroup` (both also need `manage vcns`) **Note:** Both of the above operations in this cell are totally covered with just `manage virtual-network-family`.  
[private-ips](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | PRIVATE_IP_READ | `ListPrivateIps` `GetPrivateIp` For ephemeral public IPs only: `ListPublicIps,``GetPublicIpByPrivateIpId`, `GetPublicIpByIpAddress` | none  
read | no extra | no extra | none  
use | READ + PRIVATE_IP_UPDATE PRIVATE_IP_ASSIGN PRIVATE_IP_UNASSIGN  PRIVATE_IP_CREATE PRIVATE_IP_DELETE PRIVATE_IP_ASSIGN_PUBLIC_IP PRIVATE_IP_UNASSIGN_PUBLIC_IP | READ + For ephemeral public IPs: ` UpdatePublicIp, CreatePublicIp, DeletePublicIp` | `CreatePrivateIp, DeletePrivateIp` (both also need `use subnets` and `use vnics`) `UpdatePrivateIp` (also needs `use vnics`) For reserved public IPs: `UpdatePublicIp, CreatePublicIp, DeletePublicIp` (all also need `manage public-ips`) **Note:** The above operations in this cell are totally covered with just `use virtual-network-family`.  
manage | USE + PRIVATE_IP_ROUTE_TABLE_ATTACH PRIVATE_IP_ROUTE_TABLE_DETACH | no extra | USE + `CreateRouteTable, DeleteRouteTable` (both also need `manage vcns, manage internet-gateways, manage drgs, and manage route-tables, manage local-peering-gateways, use nat-gateways, use service-gateways`) `UpdateRouteTable` (also need `manage internet-gateways, manage drgs, manage route-tables, manage local-peering-gateways, use nat-gateways, use service-gateways`) **Note:** The above operations in this cell are totally covered with just `manage virtual-network-family`.  
[publicippool](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  PUBLIC_IP_POOL_INSPECT | `ListPublicIpPool` |  none  
read |  INSPECT + PUBLIC_IP_POOL_READ |  `ReadPublicIpPool` |  none  
use |  READ + PUBLIC_IP_POOL_CREATE_PUBLIC_IP_FROM | `CreatePublicIpPool` |  none  
manage |  USE + PUBLIC_IP_POOL_CREATE PUBLIC_IP_POOL_DELETE PUBLIC_IP_POOL_UPDATE PUBLIC_IP_POOL_ADD_CAPACITY PUBLIC_IP_POOL_REMOVE_CAPACITY PUBLIC_IP_POOL_MOVE |  `CreatePublicIp` `DeletePublicIpPool` `UpdatePublicIpPool` `AddPublicIpPoolCapacity` `RemovePublicIpPoolCapacity` `ChangePublicIpPoolCompartment` |  none  
[public-ips](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | none | none | none  
read | PUBLIC_IP_READ | For reserved public IPs only: `ListPublicIps,``GetPublicIpByPrivateIpId,`` GetPublicIpByIpAddress` Permissions for listing/getting ephemeral public IPs are part of the [private-ip](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm#private-) permissions. | none  
use | READ + PUBLIC_IP_ASSIGN_PRIVATE_IP PUBLIC_IP_UNASSIGN_PRIVATE_IP  | no extra | For reserved public IPs: `UpdatePublicIp, CreatePublicIp, DeletePublicIp` (all of these also need `use private-ips` and `manage public-ips`). **Note:** The above operations in this cell are totally covered with just `manage virtual-network-family`.  
manage | USE + PUBLIC_IP_UPDATE PUBLIC_IP_CREATE PUBLIC_IP_DELETE | no extra | USE + For reserved public IPs: `UpdatePublicIp, CreatePublicIp, DeletePublicIp` (all of these also need `use private-ips`). **Note:** The above operations in this cell are totally covered with just `manage virtual-network-family`.  
[ipam](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | IPAM_READ | `ListIpInventory` `GetVcnOverlap` `GetSubnetIpInventory` `GetSubnetCidrUtilization` | none  
[remote-peering-connections](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | REMOTE_PEERING_CONNECTION_READ | `ListRemotePeeringConnections` `GetRemotePeeringConnection` | none  
read | no extra | no extra | none  
use | no extra | no extra | none  
manage | USE + REMOTE_PEERING_CONNECTION_UPDATE REMOTE_PEERING_CONNECTION_CREATE REMOTE_PEERING_CONNECTION_DELETE REMOTE_PEERING_CONNECTION_RESOURCE_MOVE | `UpdateRemotePeeringConnection` | `CreateRemotePeeringConnection, DeleteRemotePeeringConnection` (both also need `manage drgs`) `ChangeRemotePeeringConnectionCompartment` **Note:** The above operations in this cell are totally covered with just `manage virtual-network-family`.  
[remote-peering-to](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | REMOTE_PEERING_CONNECTION_READ | none | none  
read | no extra | none | none  
use | no extra | none | none  
manage | USE + REMOTE_PEERING_CONNECTION_CONNECT_TO | no extra | `ConnectRemotePeeringConnections` (requestor in the peering relationship must also have `manage remote-peering-from` in the compartment where the requestor's RPC resides. See [Remote VCN Peering using a Legacy DRG](https://docs.oracle.com/iaas/Content/Network/Tasks/remoteVCNpeering.htm).) **Note:** The above operation in this cell is totally covered with just `manage virtual-network-family`.  
[remote-peering-from](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | REMOTE_PEERING_CONNECTION_READ | none | none  
read | no extra | none | none  
use | no extra | none | none  
manage | USE + REMOTE_PEERING_CONNECTION_CONNECT_FROM | no extra | `ConnectRemotePeeringConnections` (acceptor in the peering relationship must also grant the requestor `manage remote-peering-to` in the compartment where the acceptor's RPC resides. See [Remote VCN Peering using a Legacy DRG](https://docs.oracle.com/iaas/Content/Network/Tasks/remoteVCNpeering.htm).) **Note:** The above operation in this cell is totally covered with just `manage virtual-network-family`.  
[route-tables](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | ROUTE_TABLE_READ | `ListRouteTables` `GetRouteTable` | none  
read | no extra | no extra | none  
use | no extra | no extra | none  
manage | USE + ROUTE_TABLE_ATTACH ROUTE_TABLE_DETACH ROUTE_TABLE_UPDATE ROUTE_TABLE_CREATE ROUTE_TABLE_DELETE ROUTE_TABLE_MOVE | no extra `ChangeRouteTableCompartment` | `CreateRouteTable, DeleteRouteTable` (both also need `manage vcns, manage internet-gateways, manage drgs, manage private-ips, manage local-peering-gateways, use nat-gateways, use service-gateways`) `UpdateRouteTable` (also need `manage internet-gateways, manage drgs, manage private-ips, manage local-peering-gateways, use nat-gateways, use service-gateways`) `CreateSubnet, DeleteSubnet` (both also need `manage vcns, manage subnets, manage security-lists, manage dhcp-options)` `UpdateSubnet` (if changing which route table is associated with the subnet, also need `manage subnets`) **Note:** All of the above operations in this cell are totally covered with just `manage virtual-network-family`.  
[security-lists](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | SECURITY_LIST_READ | `ListSecurityLists` `GetSecurityList` | none  
read | no extra | no extra | none  
use | no extra | no extra | none  
manage | USE + SECURITY_LIST_ATTACH SECURITY_LIST_DETACH SECURITY_LIST_UPDATE SECURITY_LIST_CREATE SECURITY_LIST_DELETE SECURITY_LIST_MOVE | USE + `UpdateSecurityList` **Note:** Ability to update a security list is available only with the `manage` verb, not the `use` verb. `ChangeSecurityListCompartment` | `CreateSecurityList, DeleteSecurityList` (both also need `manage vcns`) `CreateSubnet, DeleteSubnet` (both also need `manage vcns, manage subnets, manage route-tables, manage dhcp-options)` `UpdateSubnet` (if changing which security lists are associated with the subnet, also need `manage subnets`) **Note:** All of the above operations in this cell are totally covered with just `manage virtual-network-family`.  
[service-gateways](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | SERVICE_GATEWAY_READ | `ListServiceGateways` `GetServiceGateway` | none  
read | no extra | no extra | no extra  
use | READ + SERVICE_GATEWAY_ATTACH  SERVICE_GATEWAY_DETACH | no extra | READ + `CreateRouteTable, DeleteRouteTable` (both also need` manage route-tables, manage vcns, manage internet-gateways, manage drgs, manage private-ips, manage local-peering-gateways`) `UpdateRouteTable` (also need` manage route-tables, manage drgs, manage internet-gateways, manage private-ips, manage local-peering-gateways`)  
manage | USE + SERVICE_GATEWAY_UPDATE SERVICE_GATEWAY_CREATE SERVICE_GATEWAY_DELETE SERVICE_GATEWAY_ADD_SERVICE SERVICE_GATEWAY_DELETE_SERVICE SERVICE_GATEWAY_MOVE | USE + `ChangeServiceGatewayCompartment` `AttachServiceId` `DetachServiceId` **Note:** Ability to update a service gateway is available only with the `manage` verb, not the `use` verb. | `CreateServiceGateway` (also need `manage vcns`, and need `manage route-tables` if you associate a route table during creation) `UpdateServiceGateway` (also need `manage route-tables` if you associate a route table during the update) `DeleteServiceGateway` (also need `manage vcns`) **Note:** All of the above operations in this cell are totally covered with just `manage virtual-network-family`.  
[subnets](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | SUBNET_READ | `ListSubnets` `GetSubnet` | none  
read | no extra | no extra | none  
use | READ + SUBNET_ATTACH SUBNET_DETACH | no extra | `LaunchInstance` (also need `use vnics`, `use network-security-groups`, and `manage instance-family`)  `TerminateInstance` (also need `manage instance-family`, and `use volumes` if a volume is attached) `AttachVnic` (also need `manage instances`, `use network-security-groups`, and either `use vnics` or `use instance-family`) `DetachVnic` (also need `manage instances` and either `use vnics` or `use instance-family`) `CreatePrivateIp, DeletePrivateIp` (both also need `use private-ips` and `use vnics`)  
manage | USE + SUBNET_CREATE SUBNET_UPDATE SUBNET_DELETE SUBNET_MOVE | no extra `ChangeSubnetCompartment` | USE + `CreateSubnet, DeleteSubnet` (both also need `manage vcns, manage route-tables, manage security-lists, manage dhcp-options)` `UpdateSubnet` (also need `manage route-tables` if changing which route table is associated with the subnet, `manage security-lists` if changing which security lists are associated with the subnet, and `manage dhcp-options` if changing which set of DHCP options is associated with the subnet) **Note:** The above operations in this cell are covered with just `manage virtual-network-family`.  
[vcns](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | VCN_READ | `ListVcns` `GetVcn` | `CreateNatGateway, DeleteNatGateway` (both also need `manage nat-gateways` and `manage vcns`) **Note:** The above operations in this cell are totally covered with just `manage virtual-network-family`.  
read | no extra | no extra | no extra  
use | no extra | no extra | no extra  
manage | USE + VCN_ATTACH VCN_DETACH VCN_UPDATE VCN_CREATE VCN_DELETE VCN_MOVE | USE + `CreateVcn` `UpdateVcn` `DeleteVcn, AddVcnCidr, ModifyVcnCidr, RemoveVcnCidr` `ChangeVcnCompartment` | USE + `CreateSubnet, DeleteSubnet` (both also need `manage route-tables and manage-security-lists and manage-dhcp-options`) `CreateInternetGateway, DeleteInternetGateway` (also need `manage internet-gateways`) `CreateLocalPeeringGateway` (also need `manage local-peering-gateways`, and need `manage route-tables` if you associate a route table during creation) `DeleteLocalPeeringGateway` (also need `manage local-peering-gateways`) `CreateNatGateway, DeleteNatGateway` (also need `manage nat-gateways`) `CreateNetworkSecurityGroup, DeleteNetworkSecurityGroup` (also need `manage network-security-groups`) `CreateRouteTable, DeleteRouteTable` (also need `manage route-tables, ``manage internet-gateways, manage drgs, manage private-ips, manage local-peering-gateways, use nat-gateways, use service-gateways`) `CreateServiceGateway, DeleteServiceGateway` (also need `manage service-gateways`)  `CreateSecurityList, DeleteSecurityList` (also need `manage security-lists`) `CreateDhcpOptions, DeleteDhcpOptions` (also need `manage dhcp-options`) `CreateDrgAttachment` (also need `manage drgs`, and need `manage route-tables` if you associate a route table during creation) `DeleteDrgAttachment` (also need `manage drgs`) **Note:** The operations above are totally covered with just `manage virtual-network-family`.  
[virtual-circuits](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  VIRTUAL_CIRCUIT_READ |  `ListVirtualCircuits` `GetVirtualCircuit` |  none  
read |  no extra |  no extra |  none  
use |  READ + VIRTUAL_CIRCUIT_UPDATE |  no extra | `UpdateVirtualCircuit` (also need `manage                 drgs`,and if you're also changing which cross-connect or cross-connect group the virtual circuit uses, also need `manage                 cross-connects`)   
manage |  USE + VIRTUAL_CIRCUIT_CREATE VIRTUAL_CIRCUIT_DELETE VIRTUAL_CIRCUIT_RESOURCE_MOVE | `ChangeVirtualCircuitCompartment` |  USE + `CreateVirtualCircuit, DeleteVirtualCircuit` (both also need `manage drgs`, and if you're also creating/deleting the virtual circuit with a mapping to a specific cross-connect or cross-connect group, also need `manage                   cross-connects`) **Note:** All of the above operations in this cell are totally covered with just `manage                 virtual-network-family`.  
[vlans](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | VLAN_READ | `ListVlans` `GetVlan` | none  
read | no extra | no extra | none  
use | READ + no extra | `UpdateVlan` | none  
manage | USE + VLAN_CREATE VLAN_DELETE VLAN_ASSOCIATE_NETWORK_SECURITY_GROUP VLAN_DISASSOCIATE_NETWORK_SECURITY_GROUP VLAN_MOVE | no extra `ChangeVlanCompartment` | USE + `CreateVlan, DeleteVlan` (both also need `manage vcns, manage route-tables, manage security-lists)` **Note:** The above operations in this cell are covered with just `manage virtual-network-family`.  
[vnic-attachments](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | VNIC_ATTACHMENT_READ | `GetVnicAttachment` | `ListVnicAttachments` (also need `inspect instances`) `CreateInstanceConfiguration` (if using the `CreateInstanceConfigurationFromInstanceDetails` subtype. Also need `read instances`, `inspect vnics`, `inspect volumes`, and `inspect volume-attachments`.)  
read | no extra | none | no extra  
use | no extra | none | no extra  
manage | no extra | none | no extra  
[vnics](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | VNIC_READ | `GetVnic` | `CreateInstanceConfiguration` (if using the `CreateInstanceConfigurationFromInstanceDetails` subtype. Also need `read instances`, `inspect vnic-attachments`, `inspect volumes`, and `inspect volume-attachments`.)   
read | no extra | no extra | none  
use | READ + VNIC_ATTACH VNIC_DETACH VNIC_CREATE VNIC_DELETE VNIC_UPDATE VNIC_ASSOCIATE_NETWORK_SECURITY_GROUP VNIC_DISASSOCIATE_NETWORK_SECURITY_GROUP | no extra  |  READ + `LaunchInstance` (also need `use subnets`, `use network-security-groups`, and `manage instance-family`) `AttachVnic` (also need `manage instances`, `use subnets`, and `use network-security-groups`) `UpdateVnic` (also need `use network-security-groups`) `DetachVnic` (also need `manage instances` and `use subnets`) `CreatePrivateIp, DeletePrivateIp` (both also need `use subnets` and `use private-ips`)  
manage | no extra | no extra | no extra  
[vtaps](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  VTAP_LIST |  `ListVtaps` |  none  
read |  INSPECT+ VTAP_READ |  `GetVtap` |  none  
use |  READ + VTAP_UPDATE | none |  `UpdateVtap` requires VTAP_UPDATE and CAPTURE_FILTER_ATTACH (for a new capture filter) and CAPTURE_FILTER_DETACH (on the old capture filter), NLB_VTAP_TARGET_ATTACH and NLB_VTAP_TARGET_DETACH (when an NLB is the target), VNIC_ATTACH and VNIC_DETACH (for both a source and target) , or LB_VTAP_ENABLE and LB_VTAP_DISABLE (when a Load Balancer is the source) or DB_SYSTEM_VTAP_ENABLE and DB_SYSTEM_VTAP_DISABLE (when a DB system is the source), or EXADATA_VM_CLUSTER_VTAP_ENABLE and EXADATA_VM_CLUSTER_VTAP_DISABLE (when an EXA-CS is the source) or ADW_VTAP_ENABLE and ADW_VTAP_DISABLE (when an ADW is the source).  **Note:** The above operations in this cell are totally covered with just `manage virtual-network-family`.  
manage |  USE + VTAP_CREATE VTAP_DELETE VTAP_MOVE |  `ChangeVtapCompartment` |  `CreateVtap` requires VTAP_CREATE and CAPTURE_FILTER_ATTACH (in capture filter compartment)and VCN_ATTACH (in VCN compartment).  `DeleteVtap` requires VTAP_DELETE and CAPTURE_FILTER_DETACH, NLB_VTAP_TARGET_DETACH (when nlb is the target), and VCN_DETACH, VNIC_DETACH (both source and target) or SUBNET_DETACH (when subnet is the source) or LB_VTAP_DISABLE (when loadbalancer is the source) or DB_SYSTEM_VTAP_DISABLE (when db systen is the source) or EXADATA_VM_CLUSTER_VTAP_DISABLE (when EXA-CS is the source) or ADW_VTAP_DISABLE (when ADW is the source) **Note:** The above operations in this cell are totally covered with just `manage virtual-network-family`.  
### For instance-family Resource Types 🔗 
The `instance-family` aggregate resource-type includes extra permissions beyond the sum of the permissions for the individual resource-types included in `instance-family`. For example: It includes a few permissions for `vnics` and `volumes`, even though those resource-types aren't generally considered part of the `instance-family`. Why are there extras included? So you can write fewer policy statements to cover general use cases, like working with an instance that has an attached block volume. You can write one statement for `instance-family` instead of multiple statements covering `instances`, `vnics`, and `volumes`. 
Here's a list of the extra permissions:
For `inspect instance-family`:
  * VNIC_READ
  * VNIC_ATTACHMENT_READ
  * VOLUME_ATTACHMENT_INSPECT


For `read instance-family`:
  * VOLUME_ATTACHMENT_READ


For `use instance-family`:
  * VNIC_ATTACH
  * VNIC_DETACH
  * VOLUME_ATTACHMENT_UPDATE


For `manage instance-family`:
  * VOLUME_ATTACHMENT_CREATE
  * VOLUME_ATTACHMENT_DELETE


The following tables list the permissions and API operations covered by each of the individual resource-types included in `instance-family`.
[instances](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | INSTANCE_INSPECT | none | `GetConsoleHistory, ListConsoleHistories` (both also need `inspect console-histories`) `ListVnicAttachments` (also need `inspect vnic-attachments`) `ListVolumeAttachments` (also need `inspect volumes` and `inspect volume-attachments`) `GetVolumeAttachments` (also need `inspect volumes` and `inspect volume-attachments`)  
read | INSPECT + INSTANCE_READ |  `ListInstances` **Note:** When using `ListInstances` to list instances in a compute cluster, also need `read compute-clusters`. `ListInstanceDevices` `GetInstance` `GetInstanceMaintenanceReboot` **Note:**` ListInstances` and `GetInstance` include any user-provided metadata added to the instance. | INSPECT + `CaptureConsoleHistory` (also need `manage console-histories` and `read instance-images`) `ShowConsoleHistoryData` (also need `read console-histories` and `read instance-images`) `CreateInstanceConfiguration` (if using the `CreateInstanceConfigurationFromInstanceDetails` subtype. Also need `inspect vnics`, `inspect vnic-attachments`, `inspect volumes`, and `inspect volume-attachments`.)  
use | READ + INSTANCE_UPDATE INSTANCE_CREATE_IMAGE INSTANCE_POWER_ACTIONS INSTANCE_ATTACH_VOLUME INSTANCE_DETACH_VOLUME | READ + `UpdateInstance` `InstanceAction` | READ + `CreateImage` (also need `manage instance-images`) `AttachVolume` (also need `manage volume-attachments` and `use volumes`) `DetachVolume` (also need `manage volume-attachments` and `use volumes`)  
manage | USE + INSTANCE_CREATE INSTANCE_DELETE INSTANCE_ATTACH_SECONDARY_VNIC INSTANCE_DETACH_SECONDARY_VNIC INSTANCE_MOVE | `ChangeInstanceCompartment` | USE + `LaunchInstance` (also need `read instance-images`, `use vnics`, `use subnets`, `use network-security-groups`, and `read app-catalog-listing`. To launch instances using the Console, also need `inspect vcns`. To create instances in a compute cluster, also need `use compute-clusters`.) `TerminateInstance` (also need `use vnics` and `use subnets`; also need `manage volume-attachments` and `use volumes` if a volume is attached) `AttachVnic` (also need `use subnets`, `use network-security-groups`, and either `use vnics` or use `instance-family`) `DetachVnic` (also need `use subnets` and either `use vnics` or use `instance-family`) `GetWorkRequest`, `ListWorkRequestErrors`, and `ListWorkRequestLogs` (for work requests related to `instances` resource types. All also need the permissions for `LaunchInstance`)  
[console-histories](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | CONSOLE_HISTORY_INSPECT | none | `ListConsoleHistories, GetConsoleHistory` (both also need `inspect instances`)   
read | INSPECT + CONSOLE_HISTORY_READ | none | INSPECT + `ShowConsoleHistoryData` (also need `read instances` and `read instance-images`)  
use | no extra | none | no extra  
manage | USE + CONSOLE_HISTORY_CREATE CONSOLE_HISTORY_DELETE | `DeleteConsoleHistory` | USE + `CaptureConsoleHistory` (also need `read instances` and `read instance-images`)  
[instance-console-connection](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | INSTANCE_CONSOLE_CONNECTION_INSPECT | none | `ListInstanceConsoleConnections` (also need `inspect instances` and `read                 instances`)   
read | INSPECT + INSTANCE_CONSOLE_CONNECTION_READ | none | INSPECT + `GetInstanceConsoleConnection` (also need `read                   instances`)  
use | READ + | none | no extra  
manage | USE + INSTANCE_CONSOLE_CONNECTION_CREATE INSTANCE_CONSOLE_CONNECTION_DELETE | `DeleteInstanceConsoleConnection` `UpdateInstanceConsoleConnection` | `CreateInstanceConsoleConnection` (also need `read instances`)   
[instance-images](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | INSTANCE_IMAGE_INSPECT | `ListImages` `GetImage` | none  
read | INSPECT + INSTANCE_IMAGE_READ | no extra | INSPECT + `LaunchInstance` (also need `manage instances, use vnics,` `use subnets`, and `use network-security-groups`) `CaptureConsoleHistory` (also need `read instances` and `manage console-histories`) `ShowConsoleHistoryData` (also need `read instances` and `read console-histories`)  
use | READ + INSTANCE_IMAGE_UPDATE | `UpdateImage` | no extra  
manage | USE + INSTANCE_IMAGE_CREATE INSTANCE_IMAGE_DELETE INSTANCE_IMAGE_MOVE | `DeleteImage` `ChangeImageCompartment` | USE + `CreateImage` (also need `use instances`) `GetWorkRequest`, `ListWorkRequestErrors`, and `ListWorkRequestLogs` (for work requests related to `instance-images` resource types. All also need the permissions for `CreateImage`)  
[app-catalog-listing](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | APP_CATALOG_LISTING_INSPECT | `ListAppCatalogSubscriptions` | none  
read | INSPECT + APP_CATALOG_LISTING_READ | no extra | INSPECT + `LaunchInstance` (Also need `use instances`, `read instance-images`, `use vnics`, `use subnets`, and `use network-security-groups`)   
manage | READ + APP_CATALOG_LISTING_SUBSCRIBE | READ + `CreateAppCatalogSubscription` `DeleteAppCatalogSubscription` | none  
### For compute-management-family Resource Types 🔗 
The following tables list the permissions and API operations covered by each of the individual resource-types included in `compute-management-family`.
[instance-configurations](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | INSTANCE_CONFIGURATION_INSPECT | `ListInstanceConfigurations` | none  
read | INSPECT + INSTANCE_CONFIGURATION_READ | INSPECT + `GetInstanceConfiguration` | none  
use | no extra | no extra | none  
manage | USE + INSTANCE_CONFIGURATION_CREATE INSTANCE_CONFIGURATION_UPDATE INSTANCE_CONFIGURATION_LAUNCH INSTANCE_CONFIGURATION_DELETE INSTANCE_CONFIGURATION_MOVE | USE + `CreateInstanceConfiguration` (if using the `CreateInstanceConfigurationDetails` subtype) `UpdateInstanceConfiguration` `LaunchInstanceConfiguration` `DeleteInstanceConfiguration` `ChangeInstanceConfigurationCompartment` | none  
[instance-pools](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | INSTANCE_POOL_INSPECT | `ListInstancePools` | none  
read | INSPECT + INSTANCE_POOL_READ | INSPECT + `GetInstancePool` `ListInstancePoolInstances` | none  
use | READ + INSTANCE_POOL_POWER_ACTIONS | no extra | `ResetInstancePool` `SoftresetInstancePool` `StartInstancePool` `StopInstancePool` All also need `use instances`.  
manage | USE + INSTANCE_POOL_CREATE INSTANCE_POOL_UPDATE INSTANCE_POOL_DELETE INSTANCE_POOL_MOVE INSTANCE_POOL_INSTANCE_ATTACH INSTANCE_POOL_INSTANCE_DETACH | USE + `UpdateInstancePool` `ChangeInstancePoolCompartment` `AttachInstancePoolInstance` `DetachInstancePoolInstance` | USE + `CreateInstancePool` (also need `manage instances`, `read instance-images`, `use vnics`, and `use subnets`) `TerminateInstancePool` (also need `manage instances`, `use vnics`, `use subnets`, `manage volume-attachments`, and `use volumes`) `GetWorkRequest`, `ListWorkRequestErrors`, and `ListWorkRequestLogs` (for work requests related to `instance-pools` resource types. All also need the permissions for `CreateInstancePool` or `TerminateInstancePool`, depending on the operation that spawns the work request)  
[cluster-networks](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | CLUSTER_NETWORK_INSPECT | `ListClusterNetworks` | none  
read | INSPECT + CLUSTER_NETWORK_READ | INSPECT + `GetClusterNetwork` | `ListClusterNetworkInstances` (also need `read instance-pools`)   
use | no extra | no extra | no extra  
manage | USE + CLUSTER_NETWORK_CREATE CLUSTER_NETWORK_UPDATE CLUSTER_NETWORK_DELETE CLUSTER_NETWORK_MOVE | USE + `UpdateClusterNetwork` `ChangeClusterNetworkCompartment` | USE + `CreateClusterNetwork` (also need `manage instances`, `manage instance-pools`, `read instance-images`, `use vnics`, and `use subnets`) `TerminateClusterNetwork` (also need `manage instances`, `manage instance-pools`, `use vnics`, `use subnets`, `manage volume-attachments`, and `use volumes`) `GetWorkRequest`, `ListWorkRequestErrors`, and `ListWorkRequestLogs` (for work requests related to `cluster-networks` resource types. All also need the permissions for `CreateClusterNetwork` or `TerminateClusterNetwork`, depending on the operation that spawns the work request)  
### For instance-agent-command-family Resource Types 🔗 
The following table lists the permissions and API operations covered by each of the individual resource-types included in `instance-agent-command-family`.
[instance-agent-commands](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  INSTANCE_AGENT_COMMAND_INSPECT | `ListInstanceAgentCommands` (to view commands in the Console, also need `read instances`) |  none  
read |  INSPECT + INSTANCE_AGENT_COMMAND_READ INSTANCE_AGENT_COMMAND_EXECUTION_INSPECT |  INSPECT + `GetInstanceAgentCommand` `GetInstanceAgentCommandExecution` `ListInstanceAgentCommandExecutions` |  none  
use |  READ + INSTANCE_AGENT_COMMAND_CREATE INSTANCE_AGENT_COMMAND_DELETE |  READ + `CreateInstanceAgentCommand` `CancelInstanceAgentCommand` |  none  
manage |  no extra |  no extra |  none  
### For instance-agent-family Resource Types 🔗 
The following table lists the permissions and API operations covered by each of the individual resource-types included in `instance-agent-family`.
[instance-agent-plugins](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  INSTANCE_AGENT_PLUGIN_INSPECT |  `ListInstanceAgentPlugins` `ListInstanceagentAvailablePlugins` |  none  
read |  INSPECT + INSTANCE_AGENT_PLUGIN_READ |  INSPECT + `GetInstanceAgentPlugin` (to view plugins in the Console, also need `read instances`) |  none  
use |  no extra |  no extra |  none  
manage |  no extra |  no extra |  none  
### For Additional Compute Individual Resource Types 🔗 
The following tables list the permissions and API operations covered by other Compute resource-types that aren't included in any aggregate resource-types.
[auto-scaling-configurations](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | AUTO_SCALING_CONFIGURATION_INSPECT | `ListAutoScalingConfigurations` `ListAutoScalingPolicies` | none  
read | INSPECT + AUTO_SCALING_CONFIGURATION_READ | INSPECT + `GetAutoScalingConfiguration` `GetAutoScalingPolicy` | none  
use | no extra | no extra | none  
manage | USE + AUTO_SCALING_CONFIGURATION_CREATE AUTO_SCALING_CONFIGURATION_UPDATE AUTO_SCALING_CONFIGURATION_DELETE AUTO_SCALING_CONFIGURATION_MOVE | USE + `ChangeAutoScalingConfigurationCompartment` | USE + `CreateAutoScalingConfiguration` `UpdateAutoScalingConfiguration` `DeleteAutoScalingConfiguration` `CreateAutoScalingPolicy` `UpdateAutoScalingPolicy` `DeleteAutoScalingPolicy` All also need `manage instance-pools`.  
[compute-capacity-reports](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  none |  none |  none  
read |  none |  none |  none  
use |  none |  none |  none  
manage |  COMPUTE_CAPACITY_REPORT_CREATE |  `CreateComputeCapacityReport` |  none  
[compute-capacity-reservations](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | CAPACITY_RESERVATION_INSPECT | `ListComputeCapacityReservations` `ListComputeCapacityReservationInstanceShapes` | none  
read | INSPECT + CAPACITY_RESERVATION_READ | INSPECT + `GetComputeCapacityReservation` `ListComputeCapacityReservationInstances` | none  
use |  READ + CAPACITY_RESERVATION_LAUNCH_INSTANCE CAPACITY_RESERVATION_UPDATE |  none |  READ + `LaunchInstance` (also need `use                   subnets`, `use network-security-groups`, and `manage instance-family`)  
manage | USE + CAPACITY_RESERVATION_CREATE CAPACITY_RESERVATION_UPDATE CAPACITY_RESERVATION_DELETE CAPACITY_RESERVATION_MOVE | USE + `CreateComputeCapacityReservation` `UpdateComputeCapacityReservation` `DeleteComputeCapacityReservation` `ChangeComputeCapacityReservationCompartment` |  none  
[compute-clusters](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  COMPUTE_CLUSTER_INSPECT |  `ListComputeClusters` |  none  
read |  INSPECT + COMPUTE_CLUSTER_READ |  INSPECT + `GetComputeCluster` |  none  
use |  READ + COMPUTE_CLUSTER_UPDATE COMPUTE_CLUSTER_LAUNCH_INSTANCE |  READ + `UpdateComputeCluster` |  READ + `LaunchInstance` (also need `read instance-images`, `use vnics`, `use subnets`, `use network-security-groups`, and `read app-catalog-listing`. To launch instances using the Console, also need `inspect vcns`.)  
manage |  USE + COMPUTE_CLUSTER_CREATE COMPUTE_CLUSTER_MOVE COMPUTE_CLUSTER_DELETE |  USE + `CreateComputeCluster` `ChangeComputeClusterCompartment` `DeleteComputeCluster` |  no extra  
[compute-global-image-capability-schema](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMA_INSPECT | `ListComputeGlobalImageCapabilitySchemas` `ListComputeGlobalImageCapabilitySchemaVersions` | none  
read | INSPECT + COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMA_READ | INSPECT + `GetComputeGlobalImageCapabilitySchema` `GetComputeGlobalImageCapabilitySchemaVersion` | none  
use |  no extra |  no extra |  none  
manage |  no extra |  no extra |  none  
[compute-image-capability-schema](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  COMPUTE_IMAGE_CAPABILITY_SCHEMA_INSPECT | `ListComputeImageCapabilitySchemas` | none  
read | INSPECT + COMPUTE_IMAGE_CAPABILITY_SCHEMA_READ | INSPECT + `GetComputeImageCapabilitySchema` | none  
use |  READ + COMPUTE_IMAGE_CAPABILITY_SCHEMA_UPDATE |  READ + `UpdateComputeImageCapabilitySchema` |  none  
manage | USE + COMPUTE_IMAGE_CAPABILITY_SCHEMA_CREATE COMPUTE_IMAGE_CAPABILITY_SCHEMA_MOVE COMPUTE_IMAGE_CAPABILITY_SCHEMA_DELETE | USE + `CreateComputeImageCapabilitySchema` `ChangeComputeImageCapabilitySchemaCompartment` `DeleteComputeImageCapabilitySchema` |  none  
[dedicated-vm-hosts](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | DEDICATED_VM_HOST_INSPECT | `ListDedicatedVmHosts` | none  
read | INSPECT + DEDICATED_VM_HOST_READ | INSPECT + `GetDedicatedVmHost` `ListDedicatedVmHostInstances` | none  
use | INSPECT + DEDICATED_VM_HOST_LAUNCH_INSTANCE DEDICATED_VM_HOST_UPDATE | INSPECT + `UpdateDedicatedVmHost` | INSPECT + `LaunchInstance` All also need `create instance` in the compartment to launch the instance in and `dedicated vm host launch instance` in the comparment for the dedicated virtual machine host.  
manage | USE + DEDICATED_VM_HOST_CREATE DEDICATED_VM_HOST_MOVE DEDICATED_VM_HOST_DELETE | USE + `CreateDedicatedVmHost` `DeleteDedicatedVmHost` `ChangeDedicatedVmHostCompartment` | USE + none  
[work-requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | WORKREQUEST_INSPECT | `ListWorkRequests` | none  
read | no extra | no extra | none  
use | no extra | no extra | none  
manage | no extra | no extra | none  
### For volume-family Resource Types 🔗 
The following tables list the permissions and API operations covered by each of the individual resource-types included in `volume-family`.
[volumes](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | VOLUME_INSPECT | `ListVolumes` `GetVolume` | `ListVolumeBackups, GetVolumeBackup ` (these also need `inspect volume-backups`)  `UpdateVolumeBackup `(also need `read volume-backups`)  `DeleteVolumeBackup` (also need `manage volume-backups`)  `CreateInstanceConfiguration` (if using the `CreateInstanceConfigurationFromInstanceDetails` subtype. Also need `read instances`, `inspect vnics`, `inspect vnic-attachments`, and `inspect volume-attachments`.)  
read | no extra | no extra | no extra  
use | READ + VOLUME_UPDATE VOLUME_WRITE | no extra | READ + `AttachVolume` and `DetachVolume` (both also need `manage volume-attachments, use instances`)  `CreateVolumeBackup` (also need `manage volume-backups`)  
manage | USE + VOLUME_CREATE VOLUME_DELETE VOLUME_MOVE | USE + `CreateVolume` `DeleteVolume` `ChangeVolumeCompartment` When moving volumes between compartments, the `move volume` permission is needed for both source and destination compartments. | USE + If creating a volume _from a backup_ , also need `read volume-backups`. If creating a volume _encrypted with a Vault service master encryption key_ , also need `use key-delegate` (for the caller) and `read keys` (for the service principal). For more information, see [Details for the Vault Service](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/keypolicyreference.htm#Details_for_the_Vault_Service).  
[volume-attachments](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | VOLUME_ATTACHMENT_INSPECT | `ListVolumeAttachments` | `GetVolumeAttachment` (also need `inspect volumes` and `inspect instances`)  **Note:** The CHAP secret (if it exists) is NOT included with `inspect volume-attachments`. `CreateInstanceConfiguration` (if using the `CreateInstanceConfigurationFromInstanceDetails` subtype. Also need `read instances`, `inspect vnics`, `inspect vnic-attachments`, and `inspect volumes`.)  
read | INSPECT + VOLUME_ATTACHMENT_READ | no extra | Same as for` inspect volume-attachments`, except that `GetVolumeAttachment` also includes the CHAP secret, if it exists.  
use | READ + VOLUME_ATTACHMENT_UPDATE | no extra | no extra  
manage | USE + VOLUME_ATTACHMENT_CREATE VOLUME_ATTACHMENT_DELETE | no extra | USE + `AttachVolume, ``DetachVolume` (both also need `use volumes` and `use instances`)   
[volume-backups](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | VOLUME_BACKUP_INSPECT | none | `ListVolumeBackups, GetVolumeBackup` (both also need `inspect volumes`)   
read | INSPECT + VOLUME_BACKUP_READ | none | INSPECT + `CreateVolume` when creating volume from an backup (also need `manage volumes`)  
use | READ + VOLUME_BACKUP_COPY VOLUME_BACKUP_UPDATE | none | READ + `UpdateVolumeBackup` (also need `inspect volumes`) `CopyVolumeBackup` (also need `create volume backups` in destination region)  
manage | USE + VOLUME_BACKUP_CREATE VOLUME_BACKUP_DELETE VOLUME_BACKUP_MOVE | `ChangeVolumeBackupCompartment` When moving volume backups between compartments, the `move volume backup` permission is needed for both source and destination compartments. | USE + `CreateVolumeBackup` (also need `use volumes`) `DeleteVolumeBackup` (also need `inspect volumes`)  
[boot-volume-backups](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | BOOT_VOLUME_BACKUP_INSPECT | none | `ListBootVolumeBackups, GetBootVolumeBackup` (both also need `inspect volumes`)   
read | INSPECT + BOOT_VOLUME_BACKUP_READ | none | INSPECT + `CreateBootVolume` when creating volume from an backup (also need `manage volumes`)  
use | READ + BOOT_VOLUME_BACKUP_UPDATE BOOT_VOLUME_BACKUP_COPY  | none | READ + `UpdateBootVolumeBackup` (also need `inspect volumes`) `CopyBootVolumeBackup` (also need `create boot volume backups` in destination region)  
manage | USE + BOOT_VOLUME_BACKUP_CREATE BOOT_VOLUME_BACKUP_DELETE BOOT_VOLUME_BACKUP_MOVE | `ChangeVolumeBackupCompartment` When moving boot volume backups between compartments, the `move boot volume backup` permission is needed for both source and destination compartments. | USE + `CreateBootVolumeBackup` (also need `use volumes`) `DeleteBootVolumeBackup` (also need `inspect volumes`)  
[backup-policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | BACKUP_POLICY_INSPECT | `ListVolumeBackupPolicies` `GetVolumeBackupPolicy` | none  
read | no extra | no extra | no extra  
use | READ + BACKUP_POLICIES_UPDATE | READ + `UpdateVolumeBackupPolicy` | none  
manage | USE + BACKUP_POLICIES_CREATE BACKUP_POLICIES_DELETE | USE + `CreateVolumeBackupPolicy` `DeleteVolumeBackupPolicy` | none  
[backup-policy-assignments](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | BACKUP_POLICY_ASSIGNMENT_INSPECT | `GetVolumeBackupPolicyAssignment` | `GetVolumeBackupPolicyAssetAssignment` (also need `inspect volumes`)   
read | no extra | no extra | no extra  
use | no extra | no extra | no extra  
manage | USE + BACKUP_POLICY_ASSIGNMENT_CREATE BACKUP_POLICY_ASSIGNMENT_DELETE | USE + `CreateVolumeBackupPolicyAssignment` `DeleteVolumeBackupPolicyAssignment` | none  
[volume-groups](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | VOLUME_GROUP_INSPECT | `ListVolumeGroups` `GetVolumeGroup` | no extra  
read | no extra | no extra | no extra  
use | no extra | no extra | no extra  
manage | USE + VOLUME_GROUP_UPDATE VOLUME_GROUP_CREATE VOLUME_GROUP_DELETE VOLUME_GROUP_MOVE | USE + `DeleteVolumeGroup` | USE + `UpdateVolumeGroup` (also need `inspect volume ` for the volumes in the request)  `CreateVolumeGroup` If creating a volume group from a _list of volumes_ , also need `inspect volume` for the volumes to include in the group If creating a volume group from another _volume group_ , also need the following: 
  * `inspect volume group` for the source volume group
  * `create volume group` for the destination volume group
  * `write volume ` for the source volumes
  * `create volume ` for the destination volumes
  * `write volume ` for the destination volumes

If creating a volume group from a _volume group backup_ , also need the following: 
  * `inspect volume group backup` for the source volume group
  * `create volume group` for the destination volume group
  * `read volume backup` or `read boot volume backup` for the source volumes
  * `create volume ` for the destination volumes
  * `write volume ` for the destination volumes

`ChangeVolumeGroupCompartment` (also need `move volume ` or `move boot volume` for the volumes in the request)  When moving volume groups between compartments, the `move volume group` and `move volume` permissions are needed for both source and destination compartments.  
[volume-group-backups](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/corepolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | VOLUME_GROUP_BACKUP_INSPECT  | `ListVolumeGroupBackups` `GetVolumeGroupBackup` | no extra  
read | no extra | no extra | no extra  
use | no extra | no extra | no extra  
manage | USE + VOLUME_GROUP_BACKUP_UPDATE VOLUME_GROUP_BACKUP_CREATE VOLUME_GROUP_BACKUP_DELETE VOLUME_GROUP_BACKUP_MOVE | USE + `UpdateVolumeGroupBackup` | USE + `CreateVolumeGroupBackup` also need the following: `DeleteVolumeGroupBackup` also need `delete volume backup` or `delete boot volume backup` `ChangeVolumeGroupBackupCompartment` (also need `move volume backup` or `move boot volume backup` for the volumes in the request)  When moving volume group backups between compartments, the `move volume group backup` and `move volume backup` permissions are needed for both source and destination compartments.  
## Permissions Required for Each API Operation 🔗 
The following tables list the API operations grouped by resource type. The resource types are listed in alphabetical order.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).
### Core Services API Operations
API Operation | Permissions Required to Use the Operation  
---|---  
`CreateVolumeBackupPolicy` | BACKUP_POLICIES_CREATE  
`DeleteVolumeBackupPolicy` | BACKUP_POLICIES_DELETE  
`GetVolumeBackupPolicy` | BACKUP_POLICIES_INSPECT  
`ListVolumeBackupPolicies` | BACKUP_POLICIES_INSPECT  
`CreateVolumeBackupPolicyAssignment` | BACKUP_POLICY_ASSIGNMENT_CREATE  
`DeleteVolumeBackupPolicyAssignment` | BACKUP_POLICY_ASSIGNMENT_DELETE  
`GetVolumeBackupPolicyAssetAssignment` | BACKUP_POLICY_ASSIGNMENT_INSPECT and VOLUME_INSPECT  
`GetVolumeBackupPolicyAssignment` |  BACKUP_POLICY_ASSIGNMENT_INSPECT  
`CreateComputeCapacityReport` | COMPUTE_CAPACITY_REPORT_CREATE  
`ListClusterNetworks` | CLUSTER_NETWORK_INSPECT and INSTANCE_POOL_INSPECT  
`ListClusterNetworkInstances` | CLUSTER_NETWORK_READ and INSTANCE_POOL_READ  
`GetClusterNetwork` | CLUSTER_NETWORK_READ and INSTANCE_POOL_READ  
`UpdateClusterNetwork` | CLUSTER_NETWORK_UPDATE  
`CreateClusterNetwork` |  CLUSTER_NETWORK_CREATE and INSTANCE_POOL_CREATE  
`ChangeClusterNetworkCompartment` | CLUSTER_NETWORK_MOVE  
`TerminateClusterNetwork` |  CLUSTER_NETWORK_DELETE and INSTANCE_POOL_DELETE  
`ListConsoleHistories` | CONSOLE_HISTORY_READ and INSTANCE_INSPECT  
`CreateComputeCluster` | COMPUTE_CLUSTER_CREATE  
`ListComputeClusters` | COMPUTE_CLUSTER_INSPECT  
`GetComputeCluster` | COMPUTE_CLUSTER_READ  
`UpdateComputeCluster` | COMPUTE_CLUSTER_UPDATE  
`ChangeComputeClusterCompartment` | COMPUTE_CLUSTER_MOVE  
`DeleteComputeCluster` | COMPUTE_CLUSTER_DELETE  
`ListConsoleHistories` | CONSOLE_HISTORY_READ and INSTANCE_INSPECT  
`GetConsoleHistory` | CONSOLE_HISTORY_READ and INSTANCE_INSPECT  
`ShowConsoleHistoryData` | CONSOLE_HISTORY_READ and INSTANCE_READ and INSTANCE_IMAGE_READ  
`CaptureConsoleHistory` | CONSOLE_HISTORY_CREATE and INSTANCE_READ and INSTANCE_IMAGE_READ  
`DeleteConsoleHistory` | CONSOLE_HISTORY_DELETE  
`ListCpes` | CPE_READ  
`GetCpe` | CPE_READ  
`UpdateCpe` | CPE_UPDATE  
`CreateCpe` | CPE_CREATE  
`DeleteCpe` | CPE_DELETE  
`ChangeCpeCompartment` | CPE_RESOURCE_MOVE  
`UpdateTunnelCpeDeviceConfig` |  IPSEC_CONNECTION_UPDATE  
`GetTunnelCpeDeviceConfig` |  IPSEC_CONNECTION_READ  
`GetTunnelCpeDeviceTemplateContent` |  IPSEC_CONNECTION_READ  
`GetCpeDeviceTemplateContent` |  IPSEC_CONNECTION_READ  
`GetIpsecCpeDeviceTemplateContent` |  IPSEC_CONNECTION_READ  
`ListCrossConnects` | CROSS_CONNECT_READ  
`GetCrossConnect` | CROSS_CONNECT_READ  
`UpdateCrossConnect` |  CROSS_CONNECT_UPDATE  
`CreateCrossConnect` |  CROSS_CONNECT_CREATE if not creating cross-connect in a cross-connect group. If creating the cross-connect in a cross-connect group, also need CROSS_CONNECT_CREATE and CROSS_CONNECT_ATTACH  
`DeleteCrossConnect` |  CROSS_CONNECT_DELETE if cross-connect is not in a cross-connect group. If the cross-connect is in a cross-connect group, also need CROSS_CONNECT_DELETE and CROSS_CONNECT_DETACH  
`ChangeCrossConnectCompartment` | CROSS_CONNECT_RESOURCE_MOVE  
`ListCrossConnectGroups` | CROSS_CONNECT_GROUP_READ  
`GetCrossConnectGroup` | CROSS_CONNECT_GROUP_READ  
`UpdateCrossConnectGroup` | CROSS_CONNECT_GROUP_UPDATE  
`CreateCrossConnectGroup` | CROSS_CONNECT_GROUP_CREATE  
`DeleteCrossConnectGroup` | CROSS_CONNECT_GROUP_DELETE   
`ChangeCrossConnectGroupCompartment` | CROSS_CONNECT_GROUP_RESOURCE_MOVE  
`ListDhcpOptions` | DHCP_READ  
`GetDhcpOptions` | DHCP_READ  
`UpdateDhcpOptions` | DHCP_UPDATE  
`CreateDhcpOptions` | DHCP_CREATE and VCN_ATTACH  
`DeleteDhcpOptions` | DHCP_DELETE and VCN_DETACH  
`ChangeDhcpOptionsCompartment` | DHCP_MOVE  
`ListDrgs` | DRG_READ  
`GetDrg` | DRG_READ  
`UpdateDrg` | DRG_UPDATE  
`CreateDrg` | DRG_CREATE  
`DeleteDrg` | DRG_DELETE  
`ChangeDrgCompartment` | DRG_MOVE  
`ListDrgAttachments` | DRG_ATTACHMENT_READ  
`GetDrgAttachment` | DRG_ATTACHMENT_READ  
`UpdateDrgAttachment` |  DRG_ATTACHMENT_UPDATE ROUTE_TABLE_ATTACH is necessary to associate a route table with the DRG attachment during the update.  
`CreateDrgAttachment` |  DRG_ATTACH and VCN_ATTACH ROUTE_TABLE_ATTACH is necessary to associate a route table with the DRG attachment during creation.  
`DeleteDrgAttachment` | DRG_DETACH or VCN_DETACH  
`GetAllDrgAttachments` | DRG_READ  
`UpgradeDrg` | DRG_UPDATE  
`ListAttachmentsToDrg` | DRG_READ  
`ListDrgAttachments` | DRG_ATTACHMENT_READ  
`CreateDrgRouteTable` | DRG_ROUTE_TABLE_CREATE  
`DeleteDrgRouteTable` | DRG_ROUTE_TABLE_DELETE  
`GetDrgRouteTable` | DRG_ROUTE_TABLE_READ  
`ListDrgRouteTables` | DRG_ROUTE_TABLE_READ  
`UpdateDrgRouteTable` | DRG_ROUTE_TABLE_UPDATE  
`UpdateDrgRouteRules` | DRG_ROUTE_RULE_UPDATE  
`RemoveDrgRouteRules` | DRG_ROUTE_RULE_UPDATE  
`AddDrgRouteRules` | DRG_ROUTE_RULE_UPDATE  
`ListDrgRouteRules` | DRG_ROUTE_RULE_READ  
`GetDrgRouteDistribution` | DRG_ROUTE_DISTRIBUTION_READ  
`ListDrgRouteDistributions` | DRG_ROUTE_DISTRIBUTION_READ  
`CreateDrgRouteDistribution` | DRG_ROUTE_DISTRIBUTION_CREATE  
`DeleteDrgRouteDistribution` | DRG_ROUTE_DISTRIBUTION_DELETE  
`UpdateDrgRouteDistribution` | DRG_ROUTE_DISTRIBUTION_UPDATE  
`UpdateDrgRouteDistributionStatements` | DRG_ROUTE_DISTRIBUTION_STATEMENT_UPDATE  
`RemoveDrgRouteDistributionStatements` | DRG_ROUTE_DISTRIBUTION_STATEMENT_UPDATE  
`AddDrgRouteDistributionStatements` | DRG_ROUTE_DISTRIBUTION_STATEMENT_UPDATE  
`ListDrgRouteDistributionStatements` | DRG_ROUTE_DISTRIBUTION_STATEMENT_READ  
`RemoveExportDrgRouteDistribution` | DRG_ROUTE_DISTRIBUTION_ASSIGN  
`RemoveImportDrgRouteDistribution` | DRG_ROUTE_DISTRIBUTION_ASSIGN  
`CreateInstanceConsoleConnection` | INSTANCE_CONSOLE_CONNECTION_CREATE and INSTANCE_READ  
`DeleteInstanceConsoleConnection` | INSTANCE_CONSOLE_CONNECTION_DELETE  
`GetInstanceConsoleConnection` | INSTANCE_CONSOLE_CONNECTION_READ and INSTANCE_READ  
`UpdateInstanceConsoleConnection` | INSTANCE_CONSOLE_CONNECTION_CREATE and INSTANCE_CONSOLE_CONNECTION_DELETE  
`ListInstanceConsoleConnections` | INSTANCE_CONSOLE_CONNECTION_INSPECT and INSTANCE_INSPECT and INSTANCE_READ  
`ListImages` | INSTANCE_IMAGE_INSPECT  
`GetImage` | INSTANCE_IMAGE_INSPECT  
`UpdateImage` | INSTANCE_IMAGE_UPDATE  
`CreateImage` |  INSTANCE_IMAGE_CREATE and INSTANCE_CREATE_IMAGE The first permission is related to the `instance-image`; the second is related to the `instance`.  
`ChangeImageCompartment` | INSTANCE_IMAGE_MOVE  
`DeleteImage` | INSTANCE_IMAGE_DELETE  
`GetComputeGlobalImageCapabilitySchema` | COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMA_READ  
`GetComputeGlobalImageCapabilitySchemaVersion` | COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMA_READ  
`ListComputeGlobalImageCapabilitySchemas` | COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMA_INSPECT  
`ListComputeGlobalImageCapabilitySchemaVersions` | COMPUTE_GLOBAL_IMAGE_CAPABILITY_SCHEMA_INSPECT  
`CreateComputeImageCapabilitySchema` | COMPUTE_IMAGE_CAPABILITY_SCHEMA_CREATE  
`ListComputeImageCapabilitySchemas` | COMPUTE_IMAGE_CAPABILITY_SCHEMA_INSPECT  
`GetComputeImageCapabilitySchema` | COMPUTE_IMAGE_CAPABILITY_SCHEMA_READ  
`UpdateComputeImageCapabilitySchema` | COMPUTE_IMAGE_CAPABILITY_SCHEMA_UPDATE  
`ChangeComputeImageCapabilitySchemaCompartment` | COMPUTE_IMAGE_CAPABILITY_SCHEMA_MOVE  
`DeleteComputeImageCapabilitySchema` | COMPUTE_IMAGE_CAPABILITY_SCHEMA_DELETE  
`LaunchInstance` |  INSTANCE_CREATE and INSTANCE_IMAGE_READ and VNIC_CREATE and VNIC_ATTACH and SUBNET_ATTACH If putting the instance in a network security group during instance creation, also need NETWORK_SECURITY_GROUP_UPDATE_MEMBERS and VNIC_ASSOCIATE_NETWORK_SECURITY_GROUP If creating an instance in a compute cluster, also need COMPUTE_CLUSTER_LAUNCH_INSTANCE  
`ListInstances` |  INSTANCE_READ If listing instances in a compute cluster, also need COMPUTE_CLUSTER_READ  
`ListInstanceDevices` | INSTANCE_READ  
`GetInstance` | INSTANCE_READ  
`GetInstanceMaintenanceReboot` | INSTANCE_READ  
`UpdateInstance` | INSTANCE_UPDATE  
`InstanceAction` | INSTANCE_POWER_ACTIONS  
`ChangeInstanceCompartment` | INSTANCE_MOVE  
`TerminateInstance` |  INSTANCE_DELETE and VNIC_DELETE and SUBNET_DETACH If volumes are attached, also need VOLUME_ATTACHMENT_DELETE and VOLUME_WRITE and INSTANCE_DETACH_VOLUME  
`ListInstanceConfigurations` | INSTANCE_CONFIGURATION_INSPECT  
`GetInstanceConfiguration` | INSTANCE_CONFIGURATION_READ  
`LaunchInstanceConfiguration` | INSTANCE_CONFIGURATION_LAUNCH  
`UpdateInstanceConfiguration` | INSTANCE_CONFIGURATION_UPDATE  
`CreateInstanceConfiguration` |  INSTANCE_CONFIGURATION_CREATE (if using the `CreateInstanceConfigurationDetails` subtype) INSTANCE_READ and VNIC_READ and VNIC_ATTACHMENT_READ and VOLUME_INSPECT and VOLUME_ATTACHMENT_INSPECT (if using the `CreateInstanceConfigurationFromInstanceDetails` subtype)  
`ChangeInstanceConfigurationCompartment` | INSTANCE_CONFIGURATION_MOVE  
`DeleteInstanceConfiguration` | INSTANCE_CONFIGURATION_DELETE  
`ListInstanceMaintenanceEvent` | INSTANCE_MAINTENANCE_EVENT_INSPECT  
`GetInstanceMaintenanceEvent` | INSTANCE_MAINTENANCE_EVENT_READ  
`UpdateInstanceMaintenanceEvent` | INSTANCE_MAINTENANCE_EVENT_UPDATE  
`CreateInstancePool` | INSTANCE_POOL_CREATE and INSTANCE_CREATE and IMAGE_READ and VNIC_CREATE and SUBNET_ATTACH  
`ListInstancePools` | INSTANCE_POOL_INSPECT  
`ListInstancePoolInstances` | INSTANCE_POOL_READ  
`GetInstancePool` | INSTANCE_POOL_READ  
`UpdateInstancePool` | INSTANCE_POOL_UPDATE  
`AttachInstancePoolInstance` | INSTANCE_POOL_INSTANCE_ATTACH  
`DetachInstancePoolInstance` | INSTANCE_POOL_INSTANCE_DETACH  
`StartInstancePool` | INSTANCE_POOL_POWER_ACTIONS  
`StopInstancePool` | INSTANCE_POOL_POWER_ACTIONS  
`ResetInstancePool` | INSTANCE_POOL_POWER_ACTIONS  
`SoftresetInstancePool` | INSTANCE_POOL_POWER_ACTIONS  
`ChangeInstancePoolCompartment` | INSTANCE_POOL_MOVE  
`TerminateInstancePool` |  INSTANCE_POOL_DELETE and INSTANCE_DELETE and VNIC_DELETE and SUBNET_DETACH and VOLUME_ATTACHMENT_DELETE and VOLUME_WRITE  
`ListInternetGateways` | INTERNET_GATEWAY_READ  
`GetInternetGateway` | INTERNET_GATEWAY_READ  
`UpdateInternetGateway` | INTERNET_GATEWAY_UPDATE  
`CreateInternetGateway` | INTERNET_GATEWAY_CREATE and VCN_ATTACH  
`DeleteInternetGateway` | INTERNET_GATEWAY_DELETE and VCN_DETACH  
`ChangeInternetGatewayCompartment` | INTERNET_GATEWAY_MOVE  
`ListIPSecConnections` | IPSEC_CONNECTION_READ  
`GetIPSecConnection` | IPSEC_CONNECTION_READ  
`UpdateIpSecConnection` | IPSEC_CONNECTION_UPDATE  
`CreateIPSecConnection` | DRG_ATTACH and CPE_ATTACH and IPSEC_CONNECTION_CREATERequired to create IPSec over FastConnect: DRG_ROUTE_TABLE_ATTACH, DRG_ROUTE_TABLE_CREATE DRG_ROUTE_TABLE_UPDATE, DRG_ROUTE_DISTRIBUTION_CREATE, DRG_ROUTE_DISTRIBUTION_UPDATE, DRG_ROUTE_DISTRIBUTION_ASSIGN, DRG_ROUTE_DISTRIBUTION_STATEMENT_UPDATE  
`DeleteIPSecConnection` | DRG_DETACH and CPE_DETACH and IPSEC_CONNECTION_DELETERequired to create IPSec over FastConnect: DRG_ROUTE_TABLE_DELETE DRG_ROUTE_TABLE_UPDATE, DRG_ROUTE_DISTRIBUTION_DELETE, DRG_ROUTE_DISTRIBUTION_UPDATE, DRG_ROUTE_DISTRIBUTION_STATEMENT_UPDATE  
`GetIPSecConnectionDeviceConfig` | IPSEC_CONNECTION_DEVICE_CONFIG_READ  
`GetIPSecConnectionDeviceStatus` | IPSEC_CONNECTION_READ  
`ListIPSecConnectionTunnels` | IPSEC_CONNECTION_READ  
`GetIPSecConnectionTunnel` | IPSEC_CONNECTION_READ  
`UpdateIPSecConnectionTunnel` | IPSEC_CONNECTION_UPDATE  
`GetIPSecConnectionTunnelSharedSecret` | IPSEC_CONNECTION_DEVICE_CONFIG_READ  
`UpdateIPSecConnectionTunnelSharedSecret` | IPSEC_CONNECTION_DEVICE_CONFIG_UPDATE  
`ListIpv6s` |  IPV6_READ and SUBNET_READ (if listing by subnet) and VNIC_READ (if listing by VNIC)  
`GetIpv6` | IPV6_READ  
`UpdateIpv6` |  IPV6_UPDATE and  VNIC_UNASSIGN and VNIC_ASSIGN (if moving IPv6 to a different VNIC)  
`CreateIpv6` | IPV6_CREATE and SUBNET_ATTACH and VNIC_ASSIGN  
`DeleteIpv6` | IPV6_DELETE and SUBNET_DETACH and VNIC_UNASSIGN  
`ListLocalPeeringGateways` | LOCAL_PEERING_GATEWAY_READ  
`GetLocalPeeringGateway` | LOCAL_PEERING_GATEWAY_READ  
`UpdateLocalPeeringGateway` |  LOCAL_PEERING_GATEWAY_UPDATE ROUTE_TABLE_ATTACH is necessary to associate a route table with the LPG during the update.  
`CreateLocalPeeringGateway` |  LOCAL_PEERING_GATEWAY_CREATE and VCN_ATTACH ROUTE_TABLE_ATTACH is necessary to associate a route table with the LPG during creation.  
`DeleteLocalPeeringGateway` | LOCAL_PEERING_GATEWAY_DELETE and VCN_DETACH  
`ConnectLocalPeeringGateway` |  LOCAL_PEERING_GATEWAY_CONNECT_FROM and  LOCAL_PEERING_GATEWAY_CONNECT_TO  
`ChangeLocalPeeringGatewayCompartment` | LOCAL_PEERING_GATEWAY_MOVE  
`ListNatGateways` | NAT_GATEWAY_READ  
`GetNatGateway` | NAT_GATEWAY_READ  
`UpdateNatGateway` | NAT_GATEWAY_UPDATE  
`CreateNatGateway` | NAT_GATEWAY_CREATE and VCN_READ and VCN_ATTACH  
`DeleteNatGateway` | NAT_GATEWAY_DELETE and VCN_READ and VCN_DETACH  
`ChangeNatGatewayCompartment` | NAT_GATEWAY_MOVE  
`ListNetworkSecurityGroups` | NETWORK_SECURITY_GROUP_READ  
`GetNetworkSecurityGroup` | NETWORK_SECURITY_GROUP_READ  
`UpdateNetworkSecurityGroup` | NETWORK_SECURITY_GROUP_UPDATE  
`CreateNetworkSecurityGroup` |  NETWORK_SECURITY_GROUP_CREATE and VCN_ATTACH  
`DeleteNetworkSecurityGroup` | NETWORK_SECURITY_GROUP_DELETE and VCN_DETACH  
`ChangeNetworkSecurityGroupCompartment` | NETWORK_SECURITY_GROUP_MOVE  
`ListNetworkSecurityGroupSecurityRules` | NETWORK_SECURITY_GROUP_LIST_SECURITY_RULES  
`UpdateNetworkSecurityGroupSecurityRules` |  NETWORK_SECURITY_GROUP_UPDATE_SECURITY_RULES and  NETWORK_SECURITY_GROUP_INSPECT if writing a rule that specifies a network security group as the source (for ingress rules) or destination (for egress rules)  
`AddNetworkSecurityGroupSecurityRules` |  NETWORK_SECURITY_GROUP_UPDATE_SECURITY_RULES and  NETWORK_SECURITY_GROUP_INSPECT if writing a rule that specifies a network security group as the source (for ingress rules) or destination (for egress rules)  
`RemoveNetworkSecurityGroupSecurityRules` | NETWORK_SECURITY_GROUP_UPDATE_SECURITY_RULES  
`ListPrivateIps` | PRIVATE_IP_READ  
`GetPrivateIp` | PRIVATE_IP_READ  
`UpdatePrivateIp` | PRIVATE_IP_UPDATE and VNIC_ASSIGN and VNIC_UNASSIGN  
`CreatePrivateIp` |  PRIVATE_IP_CREATE and PRIVATE_IP_ASSIGN and VNIC_ASSIGN and SUBNET_ATTACH  
`DeletePrivateIp` | PRIVATE_IP_DELETE and PRIVATE_IP_UNASSIGN and VNIC_UNASSIGN and SUBNET_DETACH  
`ListRemotePeeringConnections` | REMOTE_PEERING_CONNECTION_READ   
`GetRemotePeeringConnection` | REMOTE_PEERING_CONNECTION_READ  
`UpdateRemotePeeringConnection` | REMOTE_PEERING_CONNECTION_UPDATE   
`CreateRemotePeeringConnection` | REMOTE_PEERING_CONNECTION_CREATE and DRG_ATTACH  
`DeleteRemotePeeringConnection` | REMOTE_PEERING_CONNECTION_DELETE and DRG_DETACH  
`ChangeRemotePeeringConnectionCompartment` | REMOTE_PEERING_CONNECTION_RESOURCE_MOVE  
`ConnectRemotePeeringConnections` |  REMOTE_PEERING_CONNECTION_CONNECT_FROM and REMOTE_PEERING_CONNECTION_CONNECT_TO  
`ListPublicIps` |  For ephemeral public IPs: PRIVATE_IP_READ  For reserved public IPs: PUBLIC_IP_READ  
`GetPublicIp` |  For ephemeral public IPs: PRIVATE_IP_READ For reserved public IPs: PUBLIC_IP_READ  
`GetPublicIpByPrivateIpId` |  For ephemeral public IPs: PRIVATE_IP_READ For reserved public IPs: PUBLIC_IP_READ  
`GetPublicIpByIpAddress` |  For ephemeral public IPs: PRIVATE_IP_READ For reserved public IPs: PUBLIC_IP_READ  
`UpdatePublicIP` |  For ephemeral public IPs: PRIVATE_IP_UPDATE  For reserved public IPs: PUBLIC_IP_UPDATE and PRIVATE_IP_ASSIGN_PUBLIC_IP and PUBLIC_IP_ASSIGN_PRIVATE_IP and PRIVATE_IP_UNASSIGN_PUBLIC_IP and PUBLIC_IP_UNASSIGN_PRIVATE_IP  
`CreatePublicIp` |  For ephemeral public IPs: PRIVATE_IP_ASSIGN_PUBLIC_IP For reserved public IPs: PUBLIC_IP_CREATE and PUBLIC_IP_ASSIGN_PRIVATE_IP and PRIVATE_IP_ASSIGN_PUBLIC_IP  
`DeletePublicIp` |  For ephemeral public IPs: PRIVATE_IP_UNASSIGN_PUBLIC_IP For reserved public IPs: PUBLIC_IP_DELETE and PUBLIC_IP_UNASSIGN_PRIVATE_IP and PRIVATE_IP_UNASSIGN_PUBLIC_IP  
`ChangePublicIpCompartment` |  PUBLIC_IP_MOVE Note: This operation applies only to reserved public IPs.   
`ListRouteTables` | ROUTE_TABLE_READ  
`GetRouteTable` | ROUTE_TABLE_READ  
`UpdateRouteTable` |  ROUTE_TABLE_UPDATE and INTERNET_GATEWAY_ATTACH (if creating a route rule that uses an internet gateway as a target) and INTERNET_GATEWAY_DETACH (if deleting a route rule that uses an internet gateway as a target) and DRG_ATTACH (if creating a route rule that uses a DRG as a target) and DRG_DETACH (if deleting a route rule that uses a DRG as a target) and PRIVATE_IP_ROUTE_TABLE_ATTACH (if creating a route rule that uses a private IP as a target) and PRIVATE_IP_ROUTE_TABLE_DETACH (if deleting a route rule that uses a private IP as a target) and LOCAL_PEERING_GATEWAY_ATTACH (if creating a route rule that uses an LPG as a target) and LOCAL_PEERING_GATEWAY_DETACH (if deleting a route rule that uses an LPG as a target) and NAT_GATEWAY_ATTACH (if creating a route rule that uses a NAT gateway as a target) and NAT_GATEWAY_DETACH (if deleting a route rule that uses a NAT gateway as a target) and SERVICE_GATEWAY_ATTACH (if creating a route rule that uses a service gateway as a target) and SERVICE_GATEWAY_DETACH (if deleting a route rule that uses a service gateway as a target)  
`CreateRouteTable` |  ROUTE_TABLE_CREATE and VCN_ATTACH and INTERNET_GATEWAY_ATTACH (if creating a route rule that uses an internet gateway as a target) and DRG_ATTACH (if creating a route rule that uses a DRG as a target) and PRIVATE_IP_ROUTE_TABLE_ATTACH (if creating a route rule that uses a private IP as a target) and LOCAL_PEERING_GATEWAY_ATTACH (if creating a route rule that uses an LPG as a target) and NAT_GATEWAY_ATTACH (if creating a route rule that uses a NAT gateway as a target) and  SERVICE_GATEWAY_ATTACH (if creating a route rule that uses a service gateway as a target)   
`DeleteRouteTable` |  ROUTE_TABLE_DELETE and VCN_DETACH and INTERNET_GATEWAY_DETACH (if deleting a route rule that uses an internet gateway as a target) and DRG_DETACH (if deleting a route rule that uses a DRG as a target) and PRIVATE_IP_ROUTE_TABLE_DETACH (if deleting a route rule that uses a private IP as a target) and LOCAL_PEERING_GATEWAY_DETACH (if deleting a route rule that uses an LPG as a target) and NAT_GATEWAY_DETACH (if deleting a route rule that uses a NAT gateway as a target) and SERVICE_GATEWAY_DETACH (if deleting a route rule that uses a service gateway as a target)   
`ChangeRouteTableCompartment` | ROUTE_TABLE_MOVE  
`ListSecurityLists` | SECURITY_LIST_READ  
`GetSecurityList` | SECURITY_LIST_READ  
`UpdateSecurityList` | SECURITY_LIST_UPDATE  
`ChangeSecurityListCompartment` | SECURITY_LIST_MOVE  
`CreateSecurityList` | SECURITY_LIST_CREATE and VCN_ATTACH  
`DeleteSecurityList` | SECURITY_LIST_DELETE and VCN_DETACH  
`ListServiceGateways` | SERVICE_GATEWAY_READ  
`GetServiceGateway` | SERVICE_GATEWAY_READ  
`UpdateServiceGateway` |  SERVICE_GATEWAY_UPDATE ROUTE_TABLE_ATTACH is necessary to associate a route table with the service gateway during the update.  
`ChangeServiceGatewayCompartment` | SERVICE_GATEWAY_MOVE  
`CreateServiceGateway` |  SERVICE_GATEWAY_CREATE and VCN_READ and VCN_ATTACH ROUTE_TABLE_ATTACH is necessary to associate a route table with the service gateway during creation.  
`DeleteServiceGateway` | SERVICE_GATEWAY_DELETE and VCN_READ and VCN_DETACH  
`AttachServiceId` | SERVICE_GATEWAY_ADD_SERVICE  
`DetachServiceId` | SERVICE_GATEWAY_DELETE_SERVICE  
`ListShapes` | INSTANCE_INSPECT  
`ListSubnets` | SUBNET_READ  
`GetSubnet` | SUBNET_READ  
`UpdateSubnet` |  SUBNET_UPDATE If changing which route table is associated with the subnet, also need ROUTE_TABLE_ATTACH and ROUTE_TABLE_DETACH If changing which security lists are associated with the subnet, also need SECURITY_LIST_ATTACH and SECURITY_LIST_DETACH If changing which set of DHCP options are associated with the subnet, also need DHCP_ATTACH and DHCP_DETACH  
`CreateSubnet` | SUBNET_CREATE and VCN_ATTACH and ROUTE_TABLE_ATTACH and SECURITY_LIST_ATTACH and DHCP_ATTACH  
`DeleteSubnet` | SUBNET_DELETE and VCN_DETACH and ROUTE_TABLE_DETACH and SECURITY_LIST_DETACH and DHCP_DETACH  
`ChangeSubnetCompartment` | SUBNET_MOVE  
`ListVcns` | VCN_READ  
`GetVcn` | VCN_READ  
`UpdateVcn` | VCN_UPDATE  
`CreateVcn` | VCN_CREATE  
`DeleteVcn` | VCN_DELETE  
`AddVcnCidr` | VCN_UPDATE  
`ModifyVcnCidr` | VCN_UPDATE  
`RemoveVcnCidr` | VCN_UPDATE  
`ChangeVcnCompartment` | VCN_MOVE  
`ListVirtualCircuits` | VIRTUAL_CIRCUIT_READ  
`GetVirtualCircuit` | VIRTUAL_CIRCUIT_READ  
`UpdateVirtualCircuit` |  VIRTUAL_CIRCUIT_UPDATE and DRG_ATTACH and DRG_DETACH If updating which cross-connect or cross-connect group the virtual circuit is using, also need CROSS_CONNECT_DETACH and CROSS_CONNECT_ATTACH   
`CreateVirtualCircuit` |  VIRTUAL_CIRCUIT_CREATE and DRG_ATTACH  If creating the virtual circuit with a mapping to a specific cross-connect or cross-connect group, also need CROSS_CONNECT_ATTACH  
`DeleteVirtualCircuit` |  VIRTUAL_CIRCUIT_DELETE and DRG_DETACH If deleting a virtual circuit that's currently using a cross-connect or cross-connect group, also need CROSS_CONNECT_DETACH   
`changeVirtualCircuitCompartment` | VIRTUAL_CIRCUIT_RESOURCE_MOVE  
`ListVlans` | VLAN_READ  
`GetVlan` | VLAN_READ  
`CreateVlan` |  VLAN_CREATE and VCN_ATTACH and ROUTE_TABLE_ATTACH and SECURITY_LIST_ATTACH and VLAN_ASSOCIATE_NETWORK_SECURITY_GROUP  
`UpdateVlan` | VLAN_UPDATE  
`DeleteVlan` |  VLAN_DELETE and VCN_DETACH and ROUTE_TABLE_DETACH and SECURITY_LIST_DETACH and VLAN_DISASSOCIATE_NETWORK_SECURITY_GROUP  
`ChangeVlanCompartment` | VLAN_MOVE  
`GetVnic` | VNIC_READ  
`AttachVnic` |  INSTANCE_ATTACH_SECONDARY_VNIC and VNIC_ATTACH and VNIC_CREATE and SUBNET_ATTACH If putting the secondary VNIC in a network security group during VNIC creation, also need NETWORK_SECURITY_GROUP_UPDATE_MEMBERS and VNIC_ASSOCIATE_NETWORK_SECURITY_GROUP  
`DetachVnic` | INSTANCE_DETACH_SECONDARY_VNIC and VNIC_DETACH and VNIC_DELETE and SUBNET_DETACH  
`UpdateVnic` |  VNIC_UPDATE  If adding or removing the VNIC from a network security group, also need NETWORK_SECURITY_GROUP_UPDATE_MEMBERS and VNIC_ASSOCIATE_NETWORK_SECURITY_GROUP  
`ListVnicAttachments` | VNIC_ATTACHMENT_READ and INSTANCE_INSPECT  
`GetVnicAttachment` | VNIC_ATTACHMENT_READ  
`ChangeVtapCompartment` | VTAP_MOVE  
`CreateVtap` | VTAP_CREATE and CAPTURE_FILTER_ATTACH (in capture filter compartment) and VNIC_ATTACH (both source and target in source & target compartment) || SUBNET_ATTACH(when subnet as source) and VCN_ATTACH (in VCN compartment)  
`DeleteVtap` | VTAP_DELETE and CAPTURE_FILTER_DETACH and NLB_VTAP_TARGET_DETACH (when NLB as target) and VNIC_DETACH (both source and target) or SUBNET_DETACH (when subnet as source) or LB_VTAP_DISABLE (when load balancer as source) or DB_SYSTEM_VTAP_DISABLE (when DB as source) or EXADATA_VM_CLUSTER_VTAP_DISABLE (when Exadata cluster as source) or ADW_VTAP_DISABLE (when ADW as source) and VCN_DETACH  
`GetVtap` | VTAP_READ  
`ListVtaps` | VTAP_LIST  
`UpdateVtap` |  VTAP_UPDATE and CAPTURE_FILTER_ATTACH (new) and NLB_VTAP_TARGET_ATTACH (when NLB as target) and VNIC_ATTACH (both new source and target) or SUBNET_ATTACH (when subnet as source) or LB_VTAP_ENABLE (when load balancer as source) or DB_SYSTEM_VTAP_ENABLE (when DB system as source) or EXADATA_VM_CLUSTER_VTAP_ENABLE (when Exadata cluster as source) or ADW_VTAP_ENABLE (when ADW as source) and NLB_VTAP_TARGET_DETACH (when NLB as target) and CAPTURE_FILTER_DETACH (old) and VNIC_DETACH (both old source and target) or SUBNET_DETACH (when subnet as source) or LB_VTAP_DISABLE (when load balancer as source) or DB_SYSTEM_VTAP_DISABLE (when DB system as source) or EXADATA_VM_CLUSTER_VTAP_DISABLE (when Exadata cluster as source) or ADW_VTAP_DISABLE (when ADW as source)  
`ChangeCaptureFilterCompartment` | CAPTURE_FILTER_MOVE  
`CreateCaptureFilter` | CAPTURE_FILTER_CREATE and VCN_ATTACH  
`DeleteCaptureFilter` | CAPTURE_FILTER_DELETE and VCN_DETACH  
`GetCaptureFilter` | CAPTURE_FILTER_READ  
`ListCaptureFilters` | CAPTURE_FILTER_LIST  
`UpdateCaptureFilter` | CAPTURE_FILTER_UPDATE  
`GetVolume` | VOLUME_INSPECT  
`ListVolumes` | VOLUME_INSPECT  
`UpdateVolume` | VOLUME_UPDATE  
`CreateVolume` | VOLUME_CREATE (and VOLUME_BACKUP_READ if creating volume from a backup)  
`DeleteVolume` | VOLUME_DELETE  
`ChangeVolumeCompartment` | VOLUME_MOVE  
`ListVolumeAttachments` | VOLUME_ATTACHMENT_INSPECT and VOLUME_INSPECT and INSTANCE_INSPECT  
`GetVolumeAttachment` |  VOLUME_ATTACHMENT_INSPECT and INSTANCE_INSPECT **Note:** To also get the CHAP secret for the volume, then VOLUME_ATTACHMENT_READ is required instead of VOLUME_ATTACHMENT_INSPECT  
`AttachVolume` | VOLUME_ATTACHMENT_CREATE and VOLUME_WRITE and INSTANCE_ATTACH_VOLUME  
`DetachVolume` | VOLUME_ATTACHMENT_DELETE and VOLUME_WRITE and INSTANCE_DETACH_VOLUME  
`ListVolumeBackups` | VOLUME_BACKUP_INSPECT and VOLUME_INSPECT  
`GetVolumeBackup` | VOLUME_BACKUP_INSPECT and VOLUME_INSPECT  
`UpdateVolumeBackup` | VOLUME_BACKUP_UPDATE and VOLUME_INSPECT  
`CreateVolumeBackup` | VOLUME_BACKUP_CREATE and VOLUME_WRITE  
`DeleteVolumeBackup` | VOLUME_BACKUP_DELETE and VOLUME_INSPECT  
`ChangeVolumeBackupCompartment` | VOLUME_BACKUP_MOVE  
`GetBootVolume` | VOLUME_INSPECT  
`ListBootVolumes` | VOLUME_INSPECT  
`UpdateBootVolume` | VOLUME_UPDATE  
`DeleteBootVolume` | VOLUME_DELETE  
`ChangeBootVolumeCompartment` | BOOT_VOLUME_MOVE  
`CreateBootVolumeBackup` | BOOT_VOLUME_BACKUP_CREATE, VOLUME_WRITE  
`ListBootVolumeBackups` | BOOT_VOLUME_BACKUP_INSPECT, VOLUME_INSPECT   
`GetBootVolumeBackup` | BOOT_VOLUME_BACKUP_INSPECT, VOLUME_INSPECT   
`UpdateBootVolumeBackup` | BOOT_VOLUME_BACKUP_UPDATE, VOLUME_INSPECT  
`DeleteBootVolumeBackup` | BOOT_VOLUME_BACKUP_DELETE, VOLUME_INSPECT  
`ChangeBootVolumeBackupCompartment` | BOOT_VOLUME_BACKUP_MOVE  
`CreateVolumeGroup` |  VOLUME_GROUP_CREATE, VOLUME_INSPECT if creating the volume group from a list of volumes. VOLUME_GROUP_CREATE, VOLUME_GROUP_INSPECT, VOLUME_CREATE, VOLUME_WRITE if cloning a volume group. VOLUME_GROUP_CREATE, VOLUME_GROUP_BACKUP_INSPECT, VOLUME_BACKUP_READ/BOOT_VOLUME_BACKUP_READ, VOLUME_CREATE, VOLUME_WRITE if restoring from a volume group backup.   
`DeleteVolumeGroup` | VOLUME_GROUP_DELETE  
`GetVolumeGroup` | VOLUME_GROUP_INSPECT  
`ListVolumeGroups` | VOLUME_GROUP_INSPECT  
`UpdateVolumeGroup` | VOLUME_GROUP_UPDATE, VOLUME_INSPECT  
`ChangeVolumegGroupCompartment` | VOLUME_GROUP_MOVE, VOLUME_MOVE/BOOT_VOLUME_MOVE  
`CreateVolumeGroupBackup` |  VOLUME_GROUP_BACKUP_CREATE, VOLUME_GROUP_INSPECT, VOLUME_WRITE, VOLUME_BACKUP_CREATE/BOOT_VOLUME_BACKUP_CREATE  
`DeleteVolumeGroupBackup` | VOLUME_GROUP_BACKUP_DELETE, VOLUME_BACKUP_DELETE/BOOT_VOLUME_BACKUP_DELETE  
`GetVolumeGroupBackup` | VOLUME_GROUP_BACKUP_INSPECT  
`ListVolumeGroupBackups` | VOLUME_GROUP_BACKUP_INSPECT  
`UpdateVolumeGroupBackup` | VOLUME_GROUP_BACKUP_UPDATE  
`ChangeVolumegGroupBackupCompartment` | VOLUME_GROUP_BACKUP_MOVE, VOLUME_BACKUP_MOVE/BOOT_VOLUME_BACKUP_MOVE  
`ListIpInventory` | IPAM_READ  
`GetVcnOverlap` | IPAM_READ  
`GetSubnetIpInventory` | IPAM_READ  
`GetSubnetCidrUtilization` | IPAM_READ  
### Dedicated Virtual Machine Host API Operations 🔗 
API Operation | Permissions Required to Use the Operation  
---|---  
`CreateDedicatedVmHost` | DEDICATED_VM_HOST_CREATE  
`ChangeDedicatedVmHostCompartment` | DEDICATED_VM_HOST_MOVE  
`DeleteDedicatedVmHost` | DEDICATED_VM_HOST_DELETE  
`GetDedicatedVmHost` | DEDICATED_VM_HOST_READ  
`ListDedicatedVmHosts` | DEDICATED_VM_HOST_INSPECT  
`ListDedicatedVmHostInstances` | DEDICATED_VM_HOST_READ  
`ListDedicatedVmHostInstanceShapes` | None  
`ListDedicatedVmHostShapes` | None  
`LaunchInstance` |  DEDICATED_VM_HOST_LAUNCH_INSTANCE in dedicated virtual machine host compartment INSTANCE_CREATE in compartment for the instance launched on the dedicated virtual machine host  
`UpdateDedicatedVmHost` | AUTO_SCALING_CONFIGURATION_CREATE and INSTANCE_POOL_UPDATE  
### Autoscaling API Operations
API Operation | Permissions Required to Use the Operation  
---|---  
`ListAutoScalingConfigurations` | AUTO_SCALING_CONFIGURATION_INSPECT  
`GetAutoScalingConfiguration` | AUTO_SCALING_CONFIGURATION_READ  
`UpdateAutoScalingConfiguration` | AUTO_SCALING_CONFIGURATION_UPDATE and INSTANCE_POOL_UPDATE  
`CreateAutoScalingConfiguration` | AUTO_SCALING_CONFIGURATION_CREATE and INSTANCE_POOL_UPDATE  
`ChangeAutoScalingConfigurationCompartment` | AUTO_SCALING_CONFIGURATION_MOVE  
`DeleteAutoScalingConfiguration` | AUTO_SCALING_CONFIGURATION_DELETE and INSTANCE_POOL_UPDATE  
`ListAutoScalingPolicies` | AUTO_SCALING_CONFIGURATION_READ  
`GetAutoScalingPolicy` | AUTO_SCALING_CONFIGURATION_READ  
`UpdateAutoScalingPolicy` | AUTO_SCALING_CONFIGURATION_UPDATE and INSTANCE_POOL_UPDATE  
`CreateAutoScalingPolicy` | AUTO_SCALING_CONFIGURATION_CREATE and INSTANCE_POOL_UPDATE  
`DeleteAutoScalingPolicy` | AUTO_SCALING_CONFIGURATION_DELETE and INSTANCE_POOL_UPDATE  
### Compute Capacity Reservation API Operations
API Operation | Permissions Required to Use the Operation  
---|---  
`ListComputeCapacityReservations` | CAPACITY_RESERVATION_INSPECT  
`GetComputeCapacityReservation` | CAPACITY_RESERVATION_READ  
`UpdateComputeCapacityReservation` | CAPACITY_RESERVATION_UPDATE  
`CreateComputeCapacityReservation` | CAPACITY_RESERVATION_CREATE  
`ChangeComputeCapacityReservationCompartment` | CAPACITY_RESERVATION_MOVE  
`DeleteComputeCapacityReservation` | CAPACITY_RESERVATION_DELETE  
`ListComputeCapacityReservationInstances` | CAPACITY_RESERVATION_READ  
`ListComputeCapacityReservationInstanceShapes` | CAPACITY_RESERVATION_INSPECT  
### Oracle Cloud Agent API Operations
API Operation | Permissions Required to Use the Operation  
---|---  
`CreateInstanceAgentCommand` | INSTANCE_AGENT_COMMAND_CREATE  
`GetInstanceAgentCommand` | INSTANCE_AGENT_COMMAND_READ  
`GetInstanceAgentCommandExecution` | INSTANCE_AGENT_COMMAND_EXECUTION_INSPECT  
`ListInstanceAgentCommands` | INSTANCE_AGENT_COMMAND_INSPECT  
`ListInstanceAgentCommandExecutions` | INSTANCE_AGENT_COMMAND_EXECUTION_INSPECT  
`CancelInstanceAgentCommand` | INSTANCE_AGENT_COMMAND_DELETE  
`GetInstanceAgentPlugin` | INSTANCE_AGENT_PLUGIN_READ  
`ListInstanceAgentPlugins` | INSTANCE_AGENT_PLUGIN_INSPECT  
`ListInstanceagentAvailablePlugins` | INSTANCE_AGENT_PLUGIN_INSPECT  
### Work Requests API Operations
API Operation | Permissions Required to Use the Operation  
---|---  
`ListWorkRequests` |  WORKREQUEST_INSPECT  
`GetWorkRequests` | Work requests inherit the permissions of the operation that spawns the work request. Generally, <RESOURCE>_CREATE permissions for the associated resource are required.  
`ListWorkRequestLogs` |  Work requests inherit the permissions of the operation that spawns the work request. Generally, <RESOURCE>_CREATE permissions for the associated resource are required.  
`ListWorkRequestErrors` |  Work requests inherit the permissions of the operation that spawns the work request. Generally, <RESOURCE>_CREATE permissions for the associated resource are required.  
Was this article helpful?
YesNo


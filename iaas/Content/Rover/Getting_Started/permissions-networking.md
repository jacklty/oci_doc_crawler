Updated 2023-09-25
# Networking Permissions for Roving Edge Infrastructure
Describes the details for writing user IAM policies that control access to rules for the Networking service for a Roving Edge Infrastructure device.
## Resource-Types 🔗 
`subnets`
`vnic-attachments`
`vcns`
`route-tables`
`public-ips`
`network-security-group`
`security-lists`
`private-ips`
`dhcp-options`
`vnics`
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the permissions and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`.
### subnets
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  SUBNET_READ |  ListSubnets GetSubnet |  None  
read |  SUBNET_READ |  ListSubnets GetSubnet |  None  
use |  SUBNET_READ SUBNET_ATTACH SUBNET_DETACH |  ListSubnets GetSubnet |  LaunchInstance (also need use vnics, use network-security-groups, and manage instance-family) TerminateInstance (also need manage instance-family, and use volumes if a volume is attached) AttachVnic (also need manage instances, use network-security-groups, and either use vnics or use instance-family) DetachVnic (also need manage instances and either use vnics or use instance-family) CreatePrivateIp, DeletePrivateIp (both also need use private-ips and use vnics)  
manage |  SUBNET_READ SUBNET_ATTACH SUBNET_DETACH SUBNET_CREATE SUBNET_DELETE SUBNET_MOVE SUBNET_UPDATE |  ListSubnets GetSubnet |  LaunchInstance (also need use vnics, use network-security-groups, and manage instance-family) TerminateInstance (also need manage instance-family, and use volumes if a volume is attached) AttachVnic (also need manage instances, use network-security-groups, and either use vnics or use instance-family) DetachVnic (also need manage instances and either use vnics or use instance-family) CreatePrivateIp, DeletePrivateIp (both also need use private-ips and use vnics) CreateSubnet, DeleteSubnet (both also need manage vcns, manage route-tables, manage security-lists, manage dhcp-options) UpdateSubnet  **Note** : The above operations in this cell are covered with just manage virtual-network-family.  
### vnic-attachments
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  VNIC_ATTACHMENT_READ |  GetVnicAttachment |  ListVnicAttachments CreateInstanceConfiguration (if using the CreateInstanceConfigurationFromInstanceDetails subtype. Also need read instances, inspect vnics, inspect volumes, and inspect volume-attachments.)  
read |  VNIC_ATTACHMENT_READ |  None |  ListVnicAttachments CreateInstanceConfiguration (if using the CreateInstanceConfigurationFromInstanceDetails subtype. Also need read instances, inspect vnics, inspect volumes, and inspect volume-attachments.)  
use |  VNIC_ATTACHMENT_READ |  None |  ListVnicAttachments CreateInstanceConfiguration (if using the CreateInstanceConfigurationFromInstanceDetails subtype. Also need read instances, inspect vnics, inspect volumes, and inspect volume-attachments.)  
manage |  VNIC_ATTACHMENT_READ |  None |  ListVnicAttachments CreateInstanceConfiguration (if using the CreateInstanceConfigurationFromInstanceDetails subtype. Also need read instances, inspect vnics, inspect volumes, and inspect volume-attachments.)  
### vcns
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  VCN_READ |  ListVcns GetVcn |  None  
read |  VCN_READ |  ListVcns GetVcn |  None  
use |  VCN_READ |  ListVcns GetVcn |  None  
manage |  VCN_READ VCN_ATTACH VCN_DETACH VCN_UPDATE VCN_CREATE VCN_DELETE VCN_MOVE |  ListVcns CreateVcn UpdateVcn DeleteVcn, AddVcnCidr ModifyVcnCidr RemoveVcnCidr |  CreateSubnet, DeleteSubnet (both also need manage route-tables and manage-security-lists and manage-dhcp-options)  
### route-tables
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  ROUTE_TABLE_READ |  ListRouteTables GetRouteTable |  None  
read |  ROUTE_TABLE_READ |  ListRouteTables GetRouteTable |  None  
use |  ROUTE_TABLE_READ |  ListRouteTables GetRouteTable |  None  
manage |  ROUTE_TABLE_READ ROUTE_TABLE_UPDATE ROUTE_TABLE_ATTACH ROUTE_TABLE_DETACH ROUTE_TABLE_MOVE ROUTE_TABLE_CREATE ROUTE_TABLE_DELETE |  ListRouteTables GetRouteTable |  CreateSubnet, DeleteSubnet (both also need manage vcns, manage subnets, manage security-lists, manage dhcp-options) UpdateSubnet (if changing which route table is associated with the subnet, also need manage subnets) **Note** : All of the above operations in this cell are totally covered with just manage virtual-network-family.  
### public-ips
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
read |  PUBLIC_IP_READ |  ListPublicIps GetPublicIpByPrivateIpId GetPublicIpByIpAddress |  None  
use |  PUBLIC_IP_READ PUBLIC_IP_ASSIGN_PRIVATE_IP PUBLIC_IP_UNASSIGN_PRIVATE_IP |  ListPublicIps GetPublicIpByPrivateIpId GetPublicIpByIpAddress |  For reserved public IPs: UpdatePublicIp, CreatePublicIp, DeletePublicIp (all of these also need use private-ips and manage public-ips).  
manage |  PUBLIC_IP_READ PUBLIC_IP_ASSIGN_PRIVATE_IP PUBLIC_IP_UNASSIGN_PRIVATE_IP PUBLIC_IP_UPDATE PUBLIC_IP_MOVE PUBLIC_IP_CREATE PUBLIC_IP_DELETE |  ListPublicIps GetPublicIpByPrivateIpId GetPublicIpByIpAddress |  For reserved public IPs: UpdatePublicIp, CreatePublicIp, DeletePublicIp (all of these also need use private-ips and manage public-ips).  
### network-security-group
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  NETWORK_SECURITY_GROUP_INSPECT NETWORK_SECURITY_GROUP_READ |  None |  AddNetworkSecurityGroupSecurityRules and UpdateNetworkSecurityGroupSecurityRules (both also need manage network-security-groups)  
read |  NETWORK_SECURITY_GROUP_INSPECT NETWORK_SECURITY_GROUP_READ NETWORK_SECURITY_GROUP_LIST_MEMBERS NETWORK_SECURITY_GROUP_LIST_SECURITY_RULES |  GetNetworkSecurityGroup ListNetworkSecurityGroups |  None  
use |  NETWORK_SECURITY_GROUP_INSPECT NETWORK_SECURITY_GROUP_READ NETWORK_SECURITY_GROUP_LIST_MEMBERS NETWORK_SECURITY_GROUP_LIST_SECURITY_RULES NETWORK_SECURITY_GROUP_UPDATE_MEMBERS |  GetNetworkSecurityGroup ListNetworkSecurityGroups ListNetworkSecurityGroupSecurityRules ListNetworkSecurityGroupVnics |  LaunchInstance (also need manage instances, read instance-images, use vnics, use subnets, and read app-catalog-listing) AttachVnic (also need manage instances, and use subnets) UpdateVnic (also need use vnics)  
manage |  NETWORK_SECURITY_GROUP_INSPECT NETWORK_SECURITY_GROUP_READ NETWORK_SECURITY_GROUP_LIST_MEMBERS NETWORK_SECURITY_GROUP_LIST_SECURITY_RULES NETWORK_SECURITY_GROUP_UPDATE_MEMBERS NETWORK_SECURITY_GROUP_CREATE NETWORK_SECURITY_GROUP_DELETE NETWORK_SECURITY_GROUP_MOVE NETWORK_SECURITY_GROUP_UPDATE NETWORK_SECURITY_GROUP_UPDATE_SECURITY_RULES |  GetNetworkSecurityGroup ListNetworkSecurityGroups ListNetworkSecurityGroupSecurityRules ListNetworkSecurityGroupVnics UpdateNetworkSecurityGroup ChangeNetworkSecurityGroupCompartment AddNetworkSecurityGroupSecurityRules |  LaunchInstance (also need manage instances, read instance-images, use vnics, use subnets, and read app-catalog-listing) AttachVnic (also need manage instances, and use subnets) UpdateVnic (also need use vnics) CreateNetworkSecurityGroup, DeleteNetworkSecurityGroup (both also need manage vcns) **Note** : Both of the above operations in this cell are totally covered with just manage virtual-network-family.  
### security-lists
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  SECURITY_LIST_READ |  ListSecurityLists GetSecurityList |  None  
read |  SECURITY_LIST_READ |  ListSecurityLists GetSecurityList |  None  
use |  SECURITY_LIST_READ |  ListSecurityLists GetSecurityList |  None  
manage |  SECURITY_LIST_READ SECURITY_LIST_UPDATE SECURITY_LIST_MOVE SECURITY_LIST_ATTACH SECURITY_LIST_DETACH SECURITY_LIST_CREATE SECURITY_LIST_DELETE |  ListSecurityLists GetSecurityList UpdateSecurityList |  CreateSecurityList, DeleteSecurityList (both also need manage vcns) CreateSubnet, DeleteSubnet (both also need manage vcns, manage subnets, manage route-tables, manage dhcp-options) UpdateSubnet (if changing which security lists are associated with the subnet, also need manage subnets) Note: All of the above operations in this cell are totally covered with just manage virtual-network-family.  
### private-ips
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  PUBLIC_IP_READ |  ListPublicIps GetPublicIpByPrivateIpId GetPublicIpByIpAddress |  None  
read |  PUBLIC_IP_READ |  ListPublicIps GetPublicIpByPrivateIpId GetPublicIpByIpAddress |  None  
use |  PRIVATE_IP_READ PRIVATE_IP_UNASSIGN PRIVATE_IP_UNASSIGN_PUBLIC_IP PRIVATE_IP_UPDATE PRIVATE_IP_ASSIGN PRIVATE_IP_ASSIGN_PUBLIC_IP PRIVATE_IP_CREATE PRIVATE_IP_DELETE |  ListPublicIps GetPublicIpByPrivateIpId GetPublicIpByIpAddress For ephemeral public IPs: UpdatePublicIp, CreatePublicIp, DeletePublicIp |  CreatePrivateIp, DeletePrivateIp (both also need use subnets and use vnics) UpdatePrivateIp (also needs use vnics) For reserved public IPs: UpdatePublicIp, CreatePublicIp, DeletePublicIp (all also need manage public-ips) **Note** : The above operations in this cell are totally covered with just use virtual-network-family.  
manage |  PRIVATE_IP_READ PRIVATE_IP_UNASSIGN PRIVATE_IP_UNASSIGN_PUBLIC_IP PRIVATE_IP_UPDATE PRIVATE_IP_ASSIGN PRIVATE_IP_ASSIGN_PUBLIC_IP PRIVATE_IP_CREATE PRIVATE_IP_DELETE PRIVATE_IP_ROUTE_TABLE_ATTACH PRIVATE_IP_ROUTE_TABLE_DETACH |  For ephemeral public IPs: UpdatePublicIp, CreatePublicIp, DeletePublicIp |  CreatePrivateIp, DeletePrivateIp (both also need use subnets and use vnics) UpdatePrivateIp (also needs use vnics) For reserved public IPs: UpdatePublicIp, CreatePublicIp, DeletePublicIp (all also need manage public-ips) **Note** : The above operations in this cell are totally covered with just use virtual-network-family.  
### dhcp-options
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  DHCP_READ |  ListDhcpOptions GetDhcpOptions |  None  
read |  DHCP_READ |  ListDhcpOptions GetDhcpOptions |  None  
use |  DHCP_READ |  ListDhcpOptions GetDhcpOptions |  None  
manage |  DHCP_READ DHCP_UPDATE DHCP_MOVE DHCP_ATTACH DHCP_DETACH DHCP_CREATE DHCP_DELETE |  ListDhcpOptions GetDhcpOptions UpdateDhcpOptions **Note** : Ability to update a set of DHCP options is available only with the manage verb, not the use verb. |  CreateDhcpOptions, DeleteDhcpOptions (both also need manage vcns) CreateSubnet, DeleteSubnet (also need manage vcns, manage subnets, manage route-tables, manage security-lists) UpdateSubnet (if changing which set of DHCP options is associated with the subnet, also need manage subnets) **Note** : All of the above operations in this cell are totally covered with just manage virtual-network-family.  
### vnics
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  VNIC_READ |  GetVnic |  CreateInstanceConfiguration (if using the CreateInstanceConfigurationFromInstanceDetails subtype. Also need read instances, inspect vnic-attachments, inspect volumes, and inspect volume-attachments.)  
read |  VNIC_READ |  GetVnic |  None  
use |  VNIC_READ VNIC_UNASSIGN VNIC_ASSIGN VNIC_UPDATE VNIC_ASSOCIATE_NETWORK_SECURITY_GROUP VNIC_DISASSOCIATE_NETWORK_SECURITY_GROUP VNIC_ATTACH VNIC_DETACH VNIC_CREATE VNIC_DELETE |  GetVnic |  LaunchInstance (also need use subnets, use network-security-groups, and manage instance-family) AttachVnic (also need manage instances, use subnets, and use network-security-groups) UpdateVnic (also need use network-security-groups) DetachVnic (also need manage instances and use subnets) CreatePrivateIp, DeletePrivateIp (both also need use subnets and use private-ips)  
manage |  VNIC_READ VNIC_UNASSIGN VNIC_ASSIGN VNIC_UPDATE VNIC_ASSOCIATE_NETWORK_SECURITY_GROUP VNIC_DISASSOCIATE_NETWORK_SECURITY_GROUP VNIC_ATTACH VNIC_DETACH VNIC_CREATE VNIC_DELETE |  GetVnic |  LaunchInstance (also need use subnets, use network-security-groups, and manage instance-family) AttachVnic (also need manage instances, use subnets, and use network-security-groups) UpdateVnic (also need use network-security-groups) DetachVnic (also need manage instances and use subnets) CreatePrivateIp, DeletePrivateIp (both also need use subnets and use private-ips)  
Was this article helpful?
YesNo


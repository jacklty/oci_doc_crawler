Updated 2024-11-06
# Permissions Required for Each API Operation
Core services permissions required for API operations.
The following tables list the API operations grouped by resource type. The resource types are listed in alphabetical order.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/permissions.htm#permissions "Permissions are the atomic units of authorization that control a user's ability to perform operations on resources. Oracle defines all the permissions in the policy language.").
## Core Services API Operations
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
`CreateVtap` | VTAP_CREATE and CAPTURE_FILTER_ATTACH (in capture filter compartment) and VNIC_ATTACH (both source and target in source & target compartment) or SUBNET_ATTACH (when subnet as source) and VCN_ATTACH (in VCN compartment)  
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
`ListVolumes` | VOLUME_INSPECT  
`GetVolume` | VOLUME_INSPECT  
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
## Dedicated Virtual Machine Host API Operations 🔗 
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
## Autoscaling API Operations
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
## Compute Capacity Reservation API Operations
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
## Oracle Cloud Agent API Operations
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
## Work Requests API Operations
API Operation | Permissions Required to Use the Operation  
---|---  
`ListWorkRequests` |  WORKREQUEST_INSPECT  
`GetWorkRequests` | Work requests inherit the permissions of the operation that spawns the work request. Generally, <RESOURCE>_CREATE permissions for the associated resource are required.  
`ListWorkRequestLogs` |  Work requests inherit the permissions of the operation that spawns the work request. Generally, <RESOURCE>_CREATE permissions for the associated resource are required.  
`ListWorkRequestErrors` |  Work requests inherit the permissions of the operation that spawns the work request. Generally, <RESOURCE>_CREATE permissions for the associated resource are required.  
Was this article helpful?
YesNo


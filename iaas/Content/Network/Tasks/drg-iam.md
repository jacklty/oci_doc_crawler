Updated 2024-09-17
# IAM Policies for Routing Between VCNs
Learn about IAM policies used with peering and dynamic routing gateways.
For more general IAM policies used in networking, see [IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Policies).
For IAM policies specific to local or remote peering using DRGs, see:
  * [Remote Peering with a Legacy DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__remote-peer-policy)
  * [Remote Peering with an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__IAM_cross-tenancy)


For IAM policies specific to local peering using LPGs, see:
  * [Local Peering using an LPG (VCNs in the Same Tenancy)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__local-LPG)
  * [Local Peering using an LPG (VCNs in Different Tenancies)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__local-LPG-xten)


For IAM policies specific to attaching DRGs and VCNs, see:
  * [Attaching to VCNs in the Same Tenancy](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__VCN-attachments)
  * [Attaching to VCNs in Other Tenancies](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__xtenancy-VCN)


## Controlling the Establishment of Peerings
With IAM policies, you can control:
  * Who can [subscribe your tenancy to another region](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm) (required for remote VCN peering).
  * Who in your organization has the authority to establish VCN peerings (for example, see the IAM policies in [Setting Up a Local Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Setting) and [Setting Up a Remote Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Setting)). Deletion of these IAM policies does not affect any existing peerings, only the ability for future peerings to be created.
  * For local VCN peering through a mutually attached DRG in the same tenancy and region, no special IAM policies are needed. Whether peering can occur with VCNs in a different tenancy (which might belong to your organization, Oracle, or a third party) would require special policy statements to enable cross-tenancy peering. In the statements, you can specify which particular tenancy. For local VCN peering through a mutually attached DRG in a different tenancy but the same region, see [Attaching to VCNs in Other Tenancies](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__xtenancy-VCN). For remote VCN peering (possibly to a different tenancy), see [Remote Peering with a Legacy DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__remote-peer-policy).
  * Who can [manage route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2) and [security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists). 


## Explicit Agreement Required from Both Sides
Peering and transit routing involve two VCNs owned by the same party or two different ones. The two parties might both be in your company but in different departments. Or the two parties might be in entirely different companies (for example, in a service-provider model). See [Accessing Object Storage Resources Across Tenancies](https://docs.oracle.com/iaas/Content/Object/Concepts/accessingresourcesacrosstenancies.htm) for further examples of cross-tenant policies.
The agreement is in the form of Oracle Cloud Infrastructure Identity and Access Management policies that each party implements for their own VCN's **compartment** or tenancy. If the VCNs are in different tenancies, each administrator must provide their tenancy [OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm) and put in place special policy statements to enable the peering. For details on the IAM policies required to connect to a VCN in another tenancy, see [Remote Peering with an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__IAM_cross-tenancy). 
## `Endorse`, `Admit`, and `Define` Statements 🔗 
Here's an overview of the verbs used in these statements:
  * **`Endorse`**: States the general set of abilities that a group _in your own tenancy_ can perform in other tenancies. The `_Endorse_`statement always belongs in the tenancy that contains the group of users crossing the boundaries into the other tenancy to work with that tenancy's resources. In the examples, we refer to this tenancy as the source tenancy.
  * **`Admit`**: States the kind of ability in _your own tenancy_ that you want to grant a group from the other tenancy. The `_Admit_`statement belongs in the tenancy who is granting "admittance" to the tenancy. The` _Admit_`statement identifies the group of users that requires resource access from the source tenancy and is identified with a corresponding` _Endorse_`statement. In the examples, we refer to this tenancy as the destination tenancy.
  * **`Define`**: Assigns a local alias to a tenancy OCID for` _Endorse_`and` _Admit_`policy statements. A` _Define_`statement is also required in the destination tenancy to assign an alias to the source IAM group OCID for` _Admit_`statements.
Include a `_Define_`statement in the same policy entity as the` _Endorse_`or` _Admit_`statement.


The `_Endorse_`and` _Admit_`statements work together. An` _Endorse_`statement resides in the source tenancy while an` _Admit_`statement resides in the destination tenancy. Without a corresponding statement that specifies access, a particular` _Endorse_`or` _Admit_`statement grants no access._Both tenancies must agree on access._
**Important** In addition to policy statements, you must also subscribe to a region to share resources across regions.
## Remote Peering with a Legacy DRG 🔗 
A DRG can connect to another DRG (and any attached VCN) in another region provided the compartments containing the requestor and the acceptor have the right policies in place. These consist of:
  * **Policy R (implemented by the requestor):**
Copy
```
Define group RequestorGrp as <requestorGroupOcid>
Define compartment RequestorComp as <RequestorCompartmentOcid>
Allow group RequestorGrp to manage remote-peering-from in compartment RequestorComp
```

The requestor is in an IAM group called RequestorGrp. This policy lets anyone in the group initiate a connection from any DRG in the requestor's compartment (RequestorComp). Policy R can be attached to either the tenancy (root compartment) or to RequestorComp. For information about why you would attach it to one versus the other, see [Policy Basics](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm#Policy).
  * **Policy A (implemented by the acceptor):**
Copy
```
Define group RequestorGrp as <requestorGroupOcid>
Define compartment AcceptorComp as <AcceptorCompartmentOcid>
Allow group RequestorGrp to manage remote-peering-to in compartment AcceptorComp

```

This policy lets the requestor connect to any RPC in the acceptor's compartment (AcceptorComp). This statement reflects the required agreement from the acceptor for the peering to be established. Policy A can be attached to either the tenancy (root compartment) or to AcceptorComp.


[![This image shows the two policies for VCNs in different regions but in the same tenancy.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_remote_peering_policy_same_tenancy.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_remote_peering_policy_same_tenancy.svg)
Both Policy R and Policy A give RequestorGrp access. However, Policy R has a resource-type called remote-peering-_from_ , and Policy A has a resource-type called remote-peering-_to_. Together, these policies let someone in RequestorGrp establish the connection _from_ an RPC in the requestor's compartment _to_ an RPC in the acceptor's compartment. The API call to actually create the connection specifies which two RPCs.
**Tip** The permission granted by Policy R might already be in place if the requestor has permission in another policy to manage all of the Networking components in RequestorComp. For example, there might be a general Network Admin policy like this: `Allow group NetworkAdmin to           manage virtual-network-family in compartment           RequestorComp`. If the requestor is in the NetworkAdmin group, then they already have the required permissions covered in Policy R (the virtual-network-family includes RPCs). And further, if the policy is instead written to cover the _entire tenancy_ (`Allow group             NetworkAdmin to manage virtual-network-family in           tenancy`), then the requestor already has all the required permissions in both compartments to establish the connection. In that case, policy A is not required.
## Remote Peering with an Upgraded DRG 🔗 
Both the requestor and acceptor must ensure that the right policies are in place. This example shows the minimal identity policies needed to create a cross-tenancy remote peering connection:
  * **Policy R (implemented by the requestor):**
Copy
```
Define group requestorGroup as <requestorGroupOcid>
Define compartment requestorCompartment as id <requestorCompartmentOcid>
Define tenancy Acceptor as <AcceptorTenancyOcid>
Allow group requestorGroup to manage remote-peering-from in compartment requestorCompartment
Endorse group requestorGroup to manage remote-peering-to in tenancy Acceptor
```

  * **Policy A (implemented by the acceptor):**
Copy
```
Define group requestorGroup as <requestor-group-ocid>
Define tenancy Requestor as <requestorTenancyOcid>
Define compartment acceptorCompartment as id <acceptorCompartmentOcid>
Admit group requestorGroup of tenancy Requestor to manage remote-peering-to in compartment <acceptorCompartment>
```



## Local Peering using an LPG (VCNs in the Same Tenancy) 🔗 
In this use case, both VCNs are in the same tenancy. If they're in different tenancies, instead see [Local Peering using an LPG (VCNs in Different Tenancies)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__local-LPG-xten).
Admins for the requestor and acceptor VCNs must ensure that the right policies are in place:
  * **Policy R (implemented by the requestor):**
Copy
```
Define group requestorGrp as <requestorGroupOcid>
Define compartment requestorComp as <requestorCompartmentOcid>
Allow group requestorGrp to manage local-peering-from in compartment requestorComp
```

The requestor is in an IAM group called requestorGrp. This policy lets anyone in the group initiate a connection from any LPG in the requestor's compartment (requestorComp). Policy R can be attached to either the tenancy (root compartment) or to requestorComp. For information about why you would attach it to one versus the other, see [Policy Basics](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm#Policy).
  * **Policy A (implemented by the acceptor):**
Copy
```
Define group requestorGrp as <requestorGroupOcid>
Define compartment acceptorComp as id <acceptorCompartmentOcid>
Allow group requestorGrp to manage local-peering-to in compartment acceptorComp
Allow group requestorGrp to inspect vcns in compartment acceptorComp
Allow group requestorGrp to inspect local-peering-gateways in compartment acceptorComp

```

The statements in the policy lets the requestor connect to any LPG in the acceptor's compartment (acceptorComp). This statement reflects the required agreement from the acceptor for the peering to be established. Policy A can be attached to either the tenancy (root compartment) or to acceptorComp. 
**Tip** The statements in Policy A let the requestor list the VCNs and LPGs in acceptorComp. The statements are required for the requestor to use the Console UI to select from a list of VCNs and LPGs in acceptorComp and establish the connection. The following diagram focuses only on the first statement, which is the critical one that permits the connection. 


[![This image shows the two policies for VCNs in the same tenancy.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_local_peering_policy_same_tenancy.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_local_peering_policy_same_tenancy.svg)
Both Policy R and Policy A give requestorGrp access. However, Policy R has a resource-type called local-peering-_from_ , and Policy A has a resource-type called local-peering-_to_. Together, these policies let someone in requestorGrp establish the connection _from_ an LPG in the requestor's compartment _to_ an LPG in the acceptor's compartment. The API call to create the connection specifies which two LPGs.
**Tip**
The permission granted by Policy R might already be in place if the requestor has permission in another policy to manage all Networking components in RequestorComp. For example, there might be a general Network Admin policy like this:
Copy
```
 Allow group NetworkAdmin to manage virtual-network-family in compartment requestorComp
```

If the requestor is in the NetworkAdmin group, then they already have the required permissions covered in Policy R (the virtual-network-family includes LPGs). And further, if the policy is instead written to cover the _entire tenancy_ instead of only compartment requestorComp, then the requestor already has all the required permissions in both compartments to establish the connection. In that case, policy A is not required.
## Local Peering using an LPG (VCNs in Different Tenancies) 🔗 
In this use case, the VCNs are in different tenancies (in other words, it's a _cross-tenancy_ peering). If the VCNs are in the same tenancy, instead see [Local Peering using an LPG (VCNs in the Same Tenancy)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__local-LPG).
Both the requestor and acceptor must ensure that the right policies are in place:
  * **Policy R (implemented by the requestor):**
Copy
```
Define tenancy Acceptor as <acceptorTenancyOcid>
Define group requestorGrp as <requestorGroupOcid>
Define compartment requestorComp as id <requestorCompartmentOcid>
Allow group requestorGrp to manage local-peering-from in compartment requestorComp
Endorse group requestorGrp to manage local-peering-to in tenancy Acceptor
Endorse group requestorGrp to associate local-peering-gateways in compartment requestorComp
  with local-peering-gateways in tenancy Acceptor
```

The requestor is in an IAM group with an assigned OCID you provide. This policy lets anyone in that group initiate a connection from any LPG in the requestor's compartment (requestorComp). 
The first statement is a `Define` statement that assigns a friendly label to the acceptor's tenancy OCID. The statement happens to use "Acceptor" as the label, but it could be a value of the requestor's choice. **All`Define` statements in a policy must be the first ones (at the top).**
The second statement lets the requestorGrp establish a connection from an LPG in the requestor's compartment. 
The `Allow` and `Endorse` statements are special ones required because the LPGs are in different tenancies. They let the requestorGrp connect an LPG in the requestor's tenancy to an LPG in the acceptor's tenancy. 
If the intent is to give the requestorGrp permission to connect to an LPG _in any tenancy_ , the policy would instead look like this:
Copy
```

Allow group requestorGrp to manage local-peering-from in compartment requestorComp
Endorse group requestorGrp to manage local-peering-to in any-tenancy
Endorse group requestorGrp to associate local-peering-gateways in compartment requestorComp with local-peering-gateways in any-tenancy

```

Regardless, Policy R must be attached to the requestor's tenancy (root compartment), and not the requestor's compartment. Policies that enable cross-tenancy access must be attached to the tenancy. For more information about attachment of policies, see [Policy Basics](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm#Policy).
  * **Policy A (implemented by the acceptor):**
Copy
```
Define tenancy Requestor as <requestorTenancyOcid>
Define group requestorGrp as <requestorGroupOcid>
Define compartment acceptorComp as id <acceptorCompartmentOcid>
Admit group requestorGrp of tenancy Requestor to manage local-peering-to in compartment acceptorComp
Admit group requestorGrp of tenancy Requestor to associate local-peering-gateways in tenancy Requestor with local-peering-gateways in compartment acceptorComp

```

Similar to the requestor's policy, this policy first uses `Define` statements to assign friendly labels to the requestor's tenancy OCID and the requestor admin group's OCID. As mentioned earlier, the acceptor could use other values for those labels if wanted.
The fourth and fifth statements let the requestorGrp connect to an LPG in the acceptor's compartment (acceptorComp). **These statements reflect the critical agreement required for the peering to be established.** The word `Admit` indicates that the access applies to a group _outside the tenancy_ where the policy resides.
Policy A must be attached to the acceptor's tenancy (root compartment), and not the acceptor's compartment.


[![This image shows the location of the two policies for VCNs in different tenancies.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_local_peering_policy_cross_tenancy.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_local_peering_policy_cross_tenancy.svg)
## Attaching to VCNs in the Same Tenancy 🔗 
If you want the VCN administrators group to create and manage VCN attachments and assign DRG route tables to the attachments, implement the following policy: 
Copy
```
define group VcnAdmin as <vcnAdminGroupOcid>
Allow group VcnAdmin to manage vcns in tenancy
Allow group VcnAdmin to manage drgs in tenancy
```

**Note** To associate a VCN route table with the attachment, add this additional line: 
Copy
```
Allow group VCN-Admin to manage route-tables in tenancy
```

## Attaching to VCNs in Other Tenancies  🔗 
"Cross-tenancy attachments" are special VCN attachments used to connect a DRG directly to a VCN in another tenancy but homed in the same region. The VCN will not be attached to a DRG in its own tenancy. The example policy below details the minimum IAM policy requirements for both tenancies to allow for this type of connection.
This example of a set of policies allows the following set of actions: 
  * DRG administrators in the DRG tenant can create a DRG attachment in the VCN tenant.
  * VCN administrators in the VCN tenant can associate a VCN route table to the attachment (used when the VCN attached is a transit VCN). If the VCN administrator has a policy to manage all-resources in the VCN tenant, they already have this ability, because the VCN attachment resides in the VCN tenancy.
  * VCN administrators do not have the ability to change the DRG route table association for the DRG attachment.


  * **Policy R (DRG in this tenancy)**
Copy
```
define group vcnAdmin as <vcnAdminGroupOcid>
define group drgAdmin as <drgAdminGroupOcid>
define tenancy acceptorVCN as <acceptorTenancyOcid>
endorse group drgAdmin to manage drg-attachment in tenancy acceptorVCN
admit group vcnAdmin of tenancy acceptorVCN to manage drg in tenancy 
```

vcnAdminGroupOcid is the OCID of the vcnAdmin group that is in the Acceptor tenancy and endorsed in the Acceptor policy.
  * **Policy A (VCN in this tenancy)**
Copy
```
define tenancy requestorDRG as <requestorTenancyOcid>
define group drgAdmin as <drgAdminGroupOcid>
define group vcnAdmin as <vcnAdminGroupOcid>
admit group drgAdmin of tenancy requestorDRG to manage drg-attachment in tenancy
endorse group vcnAdmin to manage drg in tenancy requestorDRG
```

drgAdminGroupOcid is the OCID of the drgAdmin group that is in the Requestor tenancy and endorsed in the Requestor policy.


Was this article helpful?
YesNo


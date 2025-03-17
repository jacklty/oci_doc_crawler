Updated 2024-10-07
# Compute Cloud@Customer Policy Reference
Use policies to control access to Compute Cloud@Customer infrastructure and upgrade schedule operations.
Information in these sections provide policy information specifically for Compute Cloud@Customer infrastructures and upgrade schedules. For detailed information about Oracle Cloud Infrastructure IAM and policies, see the following topics:
  * [Overview of IAM](https://docs.oracle.com/iaas/Content/Identity/getstarted/identity-domains.htm)
  * [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)
  * [Oracle Cloud Infrastructure Policy Reference](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference.htm)


**Note** Creating a policy requires proper privileges. Work with your tenancy administrator to either obtain the privileges or have the policies created for you.
## Resource-Types 🔗 
Compute Cloud@Customer introduces additional resource-types that enable you to manage the Compute Cloud@Customer infrastructures and upgrade schedules.
### Aggregate Resource-Type 🔗 
An aggregate resource-type covers the list of individual resource-types that directly follow. For example, writing one policy to allow a group to have access to the `ccc-family` is equivalent to writing separate policies for the group that would grant access to the `ccc-infrastructure`, and `ccc-upgrade-schedule`. For more information, see
Family Name | Member Resources  
---|---  
ccc-family |  ccc-infrastructure ccc-upgrade-schedule  
### Individual Resource-Types 🔗 
Resource Types |  Permissions  
---|---  
ccc-infrastructure |  CCC_INFRASTRUCTURE_INSPECT (list with summaries) CCC_INFRASTRUCTURE_READ (view resource) CCC_INFRASTRUCTURE_UPDATE (modify settings) CCC_INFRASTRUCTURE_CREATE (provision new CCC infrastructure) CCC_INFRASTRUCTURE_DELETE (delete CCC infrastructure) CCC_INFRASTRUCTURE_MOVE (move the infrastructure)  
ccc-upgrade-schedule |  CCC_UPGRADE_SCHEDULE_INSPECT CCC_UPGRADE_SCHEDULE_READ CCC_UPGRADE_SCHEDULE_UPDATE CCC_UPGRADE_SCHEDULE_CREATE CCC_UPGRADE_SCHEDULE_DELETE CCC_UPGRADE_SCHEDULE_MOVE  
## Supported Variables 🔗 
Compute Cloud@Customer, supports the Oracle Cloud Infrastructure general variables. 
See [General Variables for All Requests](https://docs.oracle.com/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm)
## Details for Verb+Resource-Type Combinations 🔗 
You use permissions and verbs to write policies to give a group access to a particular resource-type. Compute Cloud@Customer provides resource-types and permissions that are unique to Compute Cloud@Customer, but use the Oracle Cloud Infrastructure verbs. 
The following tables show the [Permissions](https://docs.oracle.com/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi) and API operations covered by each verb, using the following notations: 
  * The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`.
  * A plus sign (+) indicates incremental access compared to the cell directly above it.
  * "no extra" indicates no incremental access.


[ccc-infrastructure](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/iam/policy-reference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  CCC_INFRASTRUCTURE_INSPECT |  ListCccInfrastructures | none  
read |  INSPECT + CCC_INFRASTRUCTURE_READ |  GetCccInfrastructure | none  
use |  READ + CCC_INFRASTRUCTURE_UPDATE |  UpdateCccInfrastructure | none  
manage |  USE + CCC_INFRASTRUCTURE_CREATE CCC_INFRASTRUCTURE_DELETE CCC_INFRASTRUCTURE_MOVE | no extra | CreateCccInfrastructure (also needs use subnets)DeleteCccInfrastructure (also needs use subnets)ChangeCccInfrastructureCompartment  
[ccc-upgrade-schedule](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/iam/policy-reference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  CCC_UPGRADE_SCHEDULE_INSPECT |  ListCccUpgradeSchedules | none  
read |  INSPECT + CCC_UPGRADE_SCHEDULE_READ |  GetCccUpgradeSchedule | none  
use |  READ + CCC_UPGRADE_SCHEDULE_UPDATE |  UpdateCccUpgradeSchedule | none  
manage |  USE + CCC_UPGRADE_SCHEDULE_CREATE CCC_UPGRADE_SCHEDULE_DELETE CCC_UPGRADE_SCHEDULE_MOVE |  CreateCccUpgradeSchedule DeleteCccUpgradeSchedule ChangeCccUpgradeScheduleCompartment | none  
## Permissions Required for Each API Operation 🔗 
The following tables list the API operations and which permissions are required to use the operation.
### Compute Cloud@Customer Infrastructure Operations 🔗 
API Operation |  Permissions Required to Use the Operation  
---|---  
ListCccInfrastructures | CCC_INFRASTRUCTURE_INSPECT  
CreateCccInfrastructure | CCC_INFRASTRUCTURE_CREATE and CLIENT_SUBNET_UPDATE  
GetCccInfrastructure | CCC_INFRASTRUCTURE_READ  
UpdateCccInfrastructure | CCC_INFRASTRUCTURE_UPDATE  
DeleteCccInfrastructure | CCC_INFRASTRUCTURE_DELETE and CLIENT_SUBNET_UPDATE  
ChangeCccInfrastructureCompartment | CCC_INFRASTRUCTURE_MOVE  
### Upgrade Schedule Operations 🔗 
API Operation |  Permissions Required to Use the Operation  
---|---  
ListCccUpgradeSchedules | CCC_UPGRADE_SCHEDULE_INSPECT  
CreateCccUpgradeSchedule | CCC_UPGRADE_SCHEDULE_CREATE  
GetCccUpgradeSchedule | CCC_UPGRADE_SCHEDULE_READ  
UpdateCccUpgradeSchedule | CCC_UPGRADE_SCHEDULE_UPDATE   
DeleteCccUpgradeSchedule | CCC_UPGRADE_SCHEDULE_DELETE   
ChangeCccUpgradeScheduleCompartment | CCC_UPGRADE_SCHEDULE_MOVE  
## Sample Policies 🔗 
**Allow Full Administration Anywhere in a Tenancy**
```
Allow group CCCAdministrators to manage ccc-infrastructure in tenancy
Allow group CCCAdministrators to manage ccc-upgrade-schedule in tenancy
```

**Allow a Compartment Administrator to View Infrastructures in a Compartment**
```
Allow group CCCMonitors to read ccc-infrastructure in compartment SampleCompartment
```

**Allow a Compute Cloud@Customer Administrator Access to Manage the Upgrade Schedules in a Compartment**
```
Allow group CCCEngineeringAdministrators to manage ccc-upgrade-schedule in compartment Engineering
```

Was this article helpful?
YesNo


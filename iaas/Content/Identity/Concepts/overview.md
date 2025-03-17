Updated 2025-02-13
# Overview of Identity and Access Management
Oracle Cloud Infrastructure Identity and Access Management (IAM) lets you control who has access to your cloud resources. You can control what type of access a group of users have and to which specific resources. This section gives you an overview of IAM components and an example scenario to help you understand how they work together.
**Note** This document uses the term "you" broadly to mean any administrator in your company who has access to work with IAM. 
## IAM Components 🔗 
IAM uses the components described in this section. To better understand how the components fit together, see [Example Scenario](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/overview.htm#Example). 

RESOURCE
    The cloud objects that your company's employees create and use when interacting with Oracle Cloud Infrastructure. For example: compute instances, block storage volumes, virtual cloud networks (VCNs), subnets, route tables, etc. 

USER
    An individual employee or system that needs to manage or use your company's Oracle Cloud Infrastructure resources. Users might need to launch instances, manage remote disks, work with your virtual cloud network, etc. End users of your application are not typically IAM users. Users have one or more IAM credentials (see [User Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/usercredentials.htm#User_Credentials)).  

GROUP
    A collection of users who all need the same type of access to a particular set of resources or compartment. 

DYNAMIC GROUP
    A special type of group that contains resources (such as compute instances) that match rules that you define (thus the membership can change dynamically as matching resources are created or deleted). These instances act as "principal" actors and can make API calls to services according to policies that you write for the dynamic group. 

NETWORK SOURCE
    A group of IP addresses that are allowed to access resources in your tenancy. The IP addresses can be public IP addresses or IP addresses from a VCN within your tenancy. After you create the network source, you use policy to restrict access to only requests that originate from the IPs in the network source.  

COMPARTMENT
    A collection of related resources. Compartments are a fundamental component of Oracle Cloud Infrastructure for organizing and isolating your cloud resources. You use them to clearly separate resources for the purposes of measuring usage and billing, access (through the use of policies), and isolation (separating the resources for one project or business unit from another). A common approach is to create a compartment for each major part of your organization. For more information, see [Learn Best Practices for Setting Up Your Tenancy](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm). 

TENANCY
    The root compartment that contains _all_ of your organization's Oracle Cloud Infrastructure resources. Oracle automatically creates your company's tenancy for you. Directly within the tenancy are your IAM entities (users, groups, compartments, and some policies; you can also put policies into compartments inside the tenancy). You place the other types of cloud resources (e.g., instances, virtual networks, block storage volumes, etc.) inside the compartments that you create.  

POLICY
    A document that specifies who can access which resources, and how. Access is granted at the group and compartment level, which means you can write a policy that gives a group a specific type of access within a specific compartment, or to the tenancy itself. If you give a group access to the tenancy, the group automatically gets the same type of access to all the compartments inside the tenancy. For more information, see [Example Scenario](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/overview.htm#Example) and [How Policies Work](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#How_Policies_Work). The word "policy" is used by people in different ways: to mean an individual statement written in the policy language; to mean a collection of statements in a single, named "policy" document (which has an Oracle Cloud ID (OCID) assigned to it); and to mean the overall body of policies your organization uses to control access to resources.      When you apply a policy, there might be a slight delay before the policy is effective. 

HOME REGION
    The region where your IAM resources reside. All IAM resources are global and available across all regions, but the master set of definitions reside in a single region, the home region. You must make changes to your IAM resources in your home region. The changes will be automatically propagated to all regions. For more information, see [Managing Regions](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingregions.htm#Managing_Regions). 

FEDERATION
    A relationship that an administrator configures between an identity provider and a service provider. When you federate Oracle Cloud Infrastructure with an identity provider, you manage users and groups in the identity provider. You manage authorization in Oracle Cloud Infrastructure's IAM service. Oracle Cloud Infrastructure tenancies are federated with Oracle Identity Cloud Service by default.
## Services You Can Control Access To 🔗 
You can write policies to control access to all of the [services](https://docs.oracle.com/en-us/iaas/Content/services.htm "Oracle Cloud Infrastructure \(OCI\) is a set of complementary cloud services that enable you to build and run a range of applications and services in a highly available hosted environment.") within Oracle Cloud Infrastructure. 
## The Administrators Group and Policy 🔗 
When your company signs up for an Oracle account and Identity Domain, Oracle sets up a _default administrator_ for the account. This person will be the first IAM user for your company and will be responsible for initially setting up additional administrators. Your tenancy comes with a group called _Administrators_ , and the default administrator automatically belongs in this group. You can't delete this group, and there must always be at least one user in it.
Your tenancy also automatically has a policy that gives the Administrators group access to all of the Oracle Cloud Infrastructure API operations and all of the cloud resources in your tenancy. You can neither change nor delete this policy. Any other users you put into the Administrators group will have full access to all of the services. This means they can create and manage IAM resources such as, groups, policies, and compartments. And they can create and manage the cloud resources such as virtual cloud networks (VCNs), instances, block storage volumes, and any other new types of Oracle Cloud Infrastructure resources that become available in the future.
## Example Scenario 🔗 
The goal of this scenario is to show how the different IAM components work together, and basic features of policies.
In this scenario, Acme Company has two teams that will be using Oracle Cloud Infrastructure resources for infrastructure: Project A and Project B. In reality, your company may have many more.
Acme Company plans to use a single virtual cloud network (VCN) for both teams, and wants a network administrator to manage the VCN.
Acme Company also wants the Project A team and Project B team to _each_ have their own set of instances and block storage volumes. The Project A team and Project B teams shouldn't be able to use each other's instances. These two teams also shouldn't be allowed to change anything about the VCN set up by the network administrator. Acme Company wants each team to have administrators for that team's resources. The administrators for the Project A team can decide who can use the Project A cloud resources, and how. Same for the Project B team.
### Acme Company Gets Started with Oracle Cloud Infrastructure
Acme Company signs up to use Oracle Cloud Infrastructure and tells Oracle that an employee named Wenpei will be the default administrator. In response, Oracle:
  * Creates a tenancy for Acme Company (see the following diagram).
  * Creates an IAM user account for Wenpei in the tenancy.
  * Creates the Administrators group in the tenancy and places Wenpei in that group.
  * Creates a policy in Acme Company's tenancy that gives the Administrators group access to manage all of the resources in the tenancy. Here's that policy:

```
Allow group Administrators to manage all-resources in tenancy
```

[![This image shows the tenancy with the initial group, user, and policy.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/identity_scenario_step1.jpg)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/identity_scenario_step1.jpg)
### The Default Administrator Creates Some Groups and Another Administrator
Wenpei next creates several groups and users (see the following diagram). She:
  * Creates groups called _NetworkAdmins_ , _A-Admins_ , and _B-Admins_ (these last two are for Project A and Project B within the company)
  * Creates a user called Alex and puts him in the Administrators group.
  * Leaves the new groups empty.


To learn how to create groups, see [Working with Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managinggroups.htm#Working). To learn how to create users and put them in groups, see [Working with Users](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusers.htm#Working).
[![This image builds on the previous one by adding more users and groups.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/identity_scenario_step2.jpg)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/identity_scenario_step2.jpg)
### The Default Administrator Creates Some Compartments and Policies
Wenpei next creates compartments to group resources together (see the following diagram). She:
  * Creates a compartment called _Networks_ to control access to the Acme Company's VCN, subnets, Site-to-Site VPN, and other components from Networking. 
  * Creates a compartment called _Project-A_ to organize Project A team's cloud resources and control access to them.
  * Creates a compartment called _Project-B_ to organize Project B team's cloud resources and control access to them.


To learn how to manage compartments, see [Working with Compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm#Working). 
Wenpei then creates a policy to give the administrators for each compartment their required level of access. She attaches the policy to the tenancy, which means that only users with access to manage policies in the tenancy can later update or delete the policy. In this scenario, that is only the Administrators group. The policy includes multiple statements that:
  * Give the NetworkAdmins group access to manage networks and instances (for the purposes of easily testing the network) in the Networks compartment 
  * Give both the A-Admins and B-Admins groups access to use the networks in the Networks compartment (so they can create instances into the network). 
  * Give the A-Admins group access to manage all resources in the Project-A compartment.
  * Give the B-Admins group access to manage all resources in the Project-B compartment.


Here's what that policy looks like (notice it has multiple statements in it):
```
Allow group NetworkAdmins to manage virtual-network-family in compartment Networks
Allow group NetworkAdmins to manage instance-family in compartment Networks
Allow group A-Admins,B-Admins to use virtual-network-family in compartment Networks
Allow group A-Admins to manage all-resources in compartment Project-A
Allow group B-Admins to manage all-resources in compartment Project-B

```

Notice the difference in the verbs (`manage, use`), as well as the resources (`virtual-network-family, instance-family, all-resources`). For more information about them, see [Verbs](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Verbs) and [Resource-Types](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Resource-Types).To learn how to create policies, see [To create a policy](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy).
**Important** A-Admins and B-Admins can _use_ the virtual-network-family in the compartment Networks. However, they can't create instances in that compartment. They can only create instances in the Project-A or Project-B compartment. Remember, a compartment is a logical grouping, not a physical one, so resources that make up or reside on the same VCN can belong to different compartments.
Acme Company wants to let the administrators of the Project-A and Project-B compartments decide which users can use the resources in those compartments. So Wenpei creates two more groups: A-Users and B-Users. She then adds six more statements that give the compartment admins the required access they need in order to add and remove users from those groups:
```
Allow group A-Admins to use users in tenancy where target.group.name='A-Users'
Allow group A-Admins to use groups in tenancy where target.group.name='A-Users'
Allow group B-Admins to use users in tenancy where target.group.name='B-Users'
Allow group B-Admins to use groups in tenancy where target.group.name='B-Users'
Allow group A-Admins,B-Admins to inspect users in tenancy
Allow group A-Admins,B-Admins to inspect groups in tenancy
```

Notice that this policy doesn't let the project admins _create_ new users or manage credentials for the users. It lets them decide which existing users can be in the A-Users and B-Users groups. The last two statements are necessary for A-Admins and B-Admins to list all the users and groups, and confirm which users are in which groups.
[![This image builds on the previous one by adding compartments and policy statements.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/identity_scenario_step3.jpg)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/identity_scenario_step3.jpg)
Item | Description  
---|---  
![Callout 1](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable1.png) |  Policies attached to the tenancy: 
  * `Allow group Administrators to manage all-resources in tenancy`
  * `Allow group NetworkAdmins to manage virtual-network-family in compartment Networks`
  * `Allow group NetworkAdmins to manage instance-family in compartment Networks`
  * `Allow group A-Admins, B-Admins to use virtual-network-family in compartment Networks`
  * `Allow group A-Admins to manage all-resources in compartment Project-A`
  * `Allow group B-Admins to manage all-resources in compartment Project-B`
  * `Allow group A-Admins to use users in tenancy where target.group.name='A-Users'`
  * `Allow group A-Admins to use groups in tenancy where target.group.name='A-Users'`
  * `Allow group B-Admins to use users in tenancy where target.group.name='B-Users'`
  * `Allow group B-Admins to use groups in tenancy where target.group.name='B-Users'`
  * `Allow group A-Admins, B-Admins to inspect users in tenancy`
  * `Allow group A-Admins, B-Admins to inspect groups in tenancy`

  
### An Administrator Creates New Users
At this point, Alex is in the Administrators group and now has access to create new users. So he provisions users named Leslie, Jorge, and Cheri and places them in the NetworkAdmins, A-Admins, and B-Admins groups, respectively. Alex also creates other users who will eventually be put in the A-Users and B-Users groups by the admins for Project A and Project B.
[![This image builds on the previous one by adding new users and putting them in groups.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/identity_scenario_step4.jpg)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/identity_scenario_step4.jpg)
Item | Description  
---|---  
![Callout 1](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable1.png) |  Policies attached to the tenancy: 
  * `Allow group Administrators to manage all-resources in tenancy`
  * `Allow group NetworkAdmins to manage virtual-network-family in compartment Networks`
  * `Allow group NetworkAdmins to manage instance-family in compartment Networks`
  * `Allow group A-Admins, B-Admins to use virtual-network-family in compartment Networks`
  * `Allow group A-Admins to manage all-resources in compartment Project-A`
  * `Allow group B-Admins to manage all-resources in compartment Project-B`
  * `Allow group A-Admins to use users in tenancy where target.group.name='A-Users'`
  * `Allow group A-Admins to use groups in tenancy where target.group.name='A-Users'`
  * `Allow group B-Admins to use users in tenancy where target.group.name='B-Users'`
  * `Allow group B-Admins to use groups in tenancy where target.group.name='B-Users'`
  * `Allow group A-Admins, B-Admins to inspect users in tenancy`
  * `Allow group A-Admins, B-Admins to inspect groups in tenancy`

  
### The Network Admin Sets Up the Network
Leslie (in the NetworkAdmins group) has access to manage `virtual-network-family` and `instance-family` in the Networks compartment. She creates a virtual cloud network (VCN) with a single subnet in that compartment. She also sets up an Internet gateway for the VCN, and updates the VCN's route table to allow traffic via that gateway. To test the VCN's connectivity to the on-premises network, she launches an instance in the subnet in the VCN. As part of the launch request, she must specify which compartment the instance should reside in. She specifies the Networks compartment, which is the only one she has access to. She then confirms connectivity from the on-premises network to the VCN by logging in to the instance via SSH from the on-premises network.
Leslie terminates her test instance and lets Jorge and Cheri know that the VCN is up and running and ready to try out. She lets them know that their compartments are named Project-A and Project-B respectively. For more information about setting up a cloud network, see [Networking](https://docs.oracle.com/iaas/Content/Network/Concepts/landing.htm). For information about launching instances into the network, see [Compute](https://docs.oracle.com/iaas/Content/Compute/home.htm).
### Compartment Admins Set Up Their Compartments
Jorge and Cheri now need to set up their respective compartments. Each admin needs to do the following:
  * Launch instances in their own compartment
  * Put users in their "users" group (e.g., A-Users)
  * Decide the type of access to give those users, and accordingly attach a policy to their compartment


Jorge and Cheri both launch instances into the subnet in the VCN, into their respective team's compartments. They create and attach block volumes to the instances. Only the compartment admins can launch/terminate instances or attach/detach block volumes in their respective team's compartments.
**Important**
Network Topology and Compartment Access Are Different Concepts
It's important to understand the difference between the network topology of the VCN and the access control that the compartments provide. The instances Jorge launched reside in the VCN from a network topology standpoint. But from an access standpoint, they're in the Project-A compartment, not the Networks compartment where the VCN is. Leslie (the Networks admin) can't terminate or reboot Jorge's instances, or launch new ones into the Project-A compartment. But Leslie controls the instances' network, so she controls what traffic will be routed to them. If Jorge had specified the Networks compartment instead of the Project-A compartment when launching his instances, his request would have been denied. The story is similar for Cheri and the Project-B compartment. 
But it's also important to note that Wenpei and Alex in the Administrators group do have access to the resources inside the compartments, because they have access to manage all kinds of resources in the tenancy. Compartments inherit any policies attached to their parent compartment (the tenancy), so the Administrators access also applies to all compartments _within_ the tenancy.
Next, Jorge puts several of the users that Alex created into the A-Users group. Cheri does the same for B-Users. 
Then Jorge writes a policy that gives users the level of access they need in the Project-A compartment. 
```
Allow group A-Users to use instance-family in compartment Project-A
Allow group A-Users to use volume-family in compartment Project-A
Allow group A-Users to inspect virtual-network-family in compartment Networks

```

This lets them use existing instances (with attached block volumes) that the compartment admins already launched in the compartment, and stop/start/reboot them. It does not let A-Users create/delete or attach/detach any volumes. To give that ability, the policy would need to include `manage volume-family`.
Jorge attaches this policy to the Project-A compartment. Anyone with the ability to manage policies _in the compartment_ can now modify or delete this policy. Right now, that is only the A-Admins group (and the Administrators group, which can do anything throughout the tenancy). 
Cheri creates and attaches her own policy to the Project-B compartment, similar to Jorge's policy:
```
Allow group B-Users to use instance-family in compartment Project-B
Allow group B-Users to use volume-family in compartment Project-B
Allow group B-Users to inspect virtual-network-family in compartment Networks

```

Now the A-Users and B-Users can work with the existing instances and attached volumes in the Project-A and Project-B compartments, respectively. Here's what the layout looks like:
[![This image builds on the previous one by adding policy statements for some of the compartments.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/identity_scenario_step5.jpg)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/identity_scenario_step5.jpg)
Item | Description  
---|---  
![Callout 1](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable1.png) |  Policies attached to the tenancy: 
  * `Allow group Administrators to manage all-resources in tenancy`
  * `Allow group NetworkAdmins to manage virtual-network-family in compartment Networks`
  * `Allow group NetworkAdmins to manage instance-family in compartment Networks`
  * `Allow group A-Admins, B-Admins to use virtual-network-family in compartment Networks`
  * `Allow group A-Admins to manage all-resources in compartment Project-A`
  * `Allow group B-Admins to manage all-resources in compartment Project-B`
  * `Allow group A-Admins to use users in tenancy where target.group.name='A-Users'`
  * `Allow group A-Admins to use groups in tenancy where target.group.name='A-Users'`
  * `Allow group B-Admins to use users in tenancy where target.group.name='B-Users'`
  * `Allow group B-Admins to use groups in tenancy where target.group.name='B-Users'`
  * `Allow group A-Admins, B-Admins to inspect users in tenancy`
  * `Allow group A-Admins, B-Admins to inspect groups in tenancy`

  
![Callout 2](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable2.png) |  Policy attached and managed by Jorge:
  * `Allow group A-Users to use instance-family in compartment Project-A`
  * `Allow group A-Users to use volume-family in compartment Project-A`
  * `Allow group A-Users to use virtual-network-family in compartment Project-A`

  
![Callout 3](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable3.png) |  Policy attached and managed by Cheri:
  * `Allow group B-Users to use instance-family in compartment Project-B`
  * `Allow group B-Users to use volume-family in compartment Project-B`
  * `Allow group B-Users to use virtual-network-family in compartment Project-B`

  
For more information about basic and advanced features of policies, see [How Policies Work](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#How_Policies_Work). For examples of other typical policies your organization might use, see [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top).
## Viewing Resources by Compartment in the Console 🔗 
In the Console, you view your cloud resources _by compartment_. This means that after you sign in to the Console, you'll choose which compartment to work in (there's a list of the compartments you have access to on the left side of the page). Notice that compartments can be nested inside other compartments. The page will update to show that compartment's resources that are within the current region. If there are none, or if you don't have access to the resource in that compartment, you'll see a message.
This experience is different when you're viewing the lists of users, groups, dynamic groups, and federation providers. Those reside in the tenancy itself (the root compartment), not in an individual compartment. 
As for policies, they can reside in either the tenancy or a compartment, depending on where the policy _is attached._ Where it's attached controls who has access to modify or delete it. For more information, see [Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy3).
## The Scope of IAM Resources 🔗 
Oracle Cloud Infrastructure uses the concepts of regions and availability domains (see [Regions and Availability Domains](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm#top)). Some resources are available regionally, whereas others are available only within a certain availability domain. IAM resources (users, groups, dynamic groups, compartments, tag namespaces, federation providers, and policies) are global and available across all regions. See [Managing Regions](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingregions.htm#Managing_Regions).
## Creating Automation with Events 🔗 
You can create automation based on state changes for Oracle Cloud Infrastructure resources by using event types, rules, and actions. For more information, see [Overview of Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm).
The following IAM resources emit events: 
  * Authentication policies
  * Credentials 
  * Dynamic groups
  * Groups
  * Identity Providers
  * Multifactor Authentication TOTP Devices
  * Policies
  * Users


## Resource Identifiers 🔗 
Most types of Oracle Cloud Infrastructure resources have a unique, Oracle-assigned identifier called an Oracle Cloud ID (OCID). For information about the OCID format and other ways to identify your resources, see [Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
## Ways to Access Oracle Cloud Infrastructure 🔗 
You can access Oracle Cloud Infrastructure (OCI) by using the [Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm) (a browser-based interface), [REST API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm), or [OCI CLI](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). Instructions for using the Console, API, and CLI are included in topics throughout this documentation. For a list of available SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
To access the [Console](https://cloud.oracle.com/), you must use a [supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#supported-browsers). To go to the Console sign-in page, open the navigation menu at the top of this page and select **Infrastructure Console**. You are prompted to enter your cloud tenant, your user name, and your password.
For general information about using the API, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm).
## Limits on IAM Resources 🔗 
For a list of applicable limits and [instructions for requesting a limit increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti), see [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm). To set compartment-specific limits on a resource or resource family, administrators can use [compartment quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm).
Was this article helpful?
YesNo


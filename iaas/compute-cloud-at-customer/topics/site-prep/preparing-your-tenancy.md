Updated 2025-02-05
# Preparing Your Tenancy
Before the Compute Cloud@Customer infrastructure is connected to Oracle Cloud Infrastructure, the tenancy administrator must set up compartments, create policies, and configure a virtual cloud network. This setup is used to connect the Compute Cloud@Customer infrastructure to Oracle Cloud Infrastructure.
You can prepare your tenancy before the Compute Cloud@Customer rack is delivered to your site.
If working in the Oracle Cloud Infrastructure environment is new to you, consider reviewing [Learn Best Practices for Setting Up Your Tenancy](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm).
Prepare your tenancy by completing these activities:
  * [Establish a Federated Identity Provider](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/preparing-your-tenancy.htm#establish-a-federating-identity-provider "Before Compute Cloud@Customer is installed, your tenancy must be set up to use a federated identity provider to manage authentication.")
  * [Create Users and Groups](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/preparing-your-tenancy.htm#create-users-and-groups "To prepare your Oracle Cloud Infrastructure tenancy, identify users and create groups for the people in your organization who administer the Compute Cloud@Customer infrastructure.")
  * [Create or Identify Compartments](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/preparing-your-tenancy.htm#create-or-identify-compartments "When Compute Cloud@Customer is connected to Oracle Cloud Infrastructure, one or more compartments are needed.")
  * [Add Required Policies](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/preparing-your-tenancy.htm#add-required-policies "Certain IAM policies must be configured before Compute Cloud@Customer is connected to your tenancy.")
  * [Create a VCN and Subnet](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/preparing-your-tenancy.htm#create-a-vcn-and-subnet "Before Compute Cloud@Customer is connected to your tenancy, create a VCN with a subnet in the tenancy.")


You can also watch this [Video: Prepare your Oracle Cloud Infrastructure Tenancy for Compute Cloud@Customer](https://youtu.be/HWn0zGJw7Ng).
**Note**
The tasks you perform in this section are required to establish the connection between OCI and the Compute Cloud@Customer infrastructure. You need to perform similar administrative tasks, beyond what is described here, before you can create resources such as instances on Compute Cloud@Customer infrastructure. Most of the additional administrative tasks can be performed after you prepare your tenancy, or after the installation. See [Postinstallation Administration](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/starting-to-manage-resources.htm#starting-to-manage-resources "After the Compute Cloud@Customer infrastructure is installed and connected to Oracle Cloud Infrastructure \(OCI\), you need to perform additional administrative tasks before you can create resources such as virtual cloud networks, instances, and storage on the Compute Cloud@Customer infrastructure.").
## Establish a Federated Identity Provider 🔗 
Before Compute Cloud@Customer is installed, your tenancy must be set up to use a federated identity provider to manage authentication.
When Oracle installs Compute Cloud@Customer, Oracle configures the Compute Cloud@Customer infrastructure to use the same federated identity provider. This enables you to use the same credentials to access Oracle Cloud Infrastructure and Compute Cloud@Customer.
If your tenancy is already configured to use a federated identity provider, including Oracle's Identity Cloud Service, you're all set. Share your federated identity information with your Oracle representative. Otherwise, work with your Oracle representative to establish a federated identity provider.
You can use an external identity provider or Oracle Identity Cloud Service. The type of identity provider you can use depends on the type of tenancy you have (a tenancy with IAM identity domains or without IAM identity domains).
For more information, see these resources:
  * [Determining the Tenancy Type](https://docs.oracle.com/iaas/Content/Security/Reference/determining_the_tenancy_type.htm)
  * Tenancies with Identity Domains – [Federating with Identity Providers](https://docs.oracle.com/iaas/Content/Identity/federating/federating_section.htm)
  * Tenancies without Identity Domains – [Federating with Identity Providers](https://docs.oracle.com/iaas/Content/Identity/Concepts/federation.htm)


**Important**
If you change your identity provider configuration in Oracle Cloud Infrastructure, Oracle must make the same administrative changes on Compute Cloud@Customer. In this situation, open an Oracle Support Request to request help. See [Creating a Support Request](https://docs.oracle.com/iaas/Content/GSG/support/create-incident.htm).
For information about securing IAM Federation, see [IAM Federation](https://docs.oracle.com/iaas/Content/Security/Reference/iam_security_topic-IAM_Federation.htm).
## Create Users and Groups 🔗 
To prepare your Oracle Cloud Infrastructure tenancy, identify users and create groups for the people in your organization who administer the Compute Cloud@Customer infrastructure. 
Perform this task before Compute Cloud@Customer is connected to Oracle Cloud Infrastructure.
  1. Identify your tenancy administrator.
  2. Create at least one group with users who can perform these administrative tasks: 
     * Create, update, and delete Compute Cloud@Customer infrastructures.
     * Create, update, and delete Compute Cloud@Customer upgrade schedules


The groups will be included in policies you define later. See [Add Required Policies](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/preparing-your-tenancy.htm#add-required-policies "Certain IAM policies must be configured before Compute Cloud@Customer is connected to your tenancy.").
## Create or Identify Compartments 🔗 
When Compute Cloud@Customer is connected to Oracle Cloud Infrastructure, one or more compartments are needed.
A compartment is a collection of related resources. Compartments are a fundamental component of Oracle Cloud Infrastructure for organizing and isolating your cloud resources. You use them to separate resources for the purposes of controlling access (using policies), and isolation (separating the resources for one project or business unit from another).
For Compute Cloud@Customer, at least one compartment is needed for the following items:
  * Compute Cloud@Customer infrastructure connection to Oracle Cloud Infrastructure.
  * The VCN you eventually created for the connection to Oracle Cloud Infrastructure.


Compute Cloud@Customer can be connected to your tenancy (root compartment), to an existing compartment, or to a new compartment. You can use multiple compartments. For example, you can use one compartment for the infrastructure connection, and another for the VCN. 
  1. Create or choose a compartment based on how you use compartments to control access to resources.
If you plan to create a new compartment, sign in to OCI and use the Oracle Cloud Console, or use the OCI CLI or OCI API to create the compartment in your tenancy.
**Note**
Compartments used for Compute Cloud@Customer, including compartments for the installation, are created and managed in OCI. Compartments aren't managed in the Compute Cloud@Customer infrastructure. All compartments in the tenancy are automatically synchronized to the Compute Cloud@Customer infrastructure, every ten minutes or so. 
For an introduction to compartments, and for instructions for managing compartments, see [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm).


## Add Required Policies 🔗 
Certain IAM policies must be configured before Compute Cloud@Customer is connected to your tenancy.
  1. Configure the following policies in your tenancy.
For information about how to work with policies, see [Managing Policies](https://docs.oracle.com/iaas/Content/Identity/policymgmt/managingpolicies_topic-tasks.htm).
If your tenancy supports Identity Domains, you can create policies that specify the dynamic group. To determine if your tenancy has Identity Domains or not, see [Determining the Tenancy Type](https://docs.oracle.com/iaas/Content/Security/Reference/determining_the_tenancy_type.htm).
**Note**
Different policy statements can be constructed to achieve the same level of access to resources. The following list of policies provide examples. You can use the example, or create policy variations, as long as the policies allow access to the correct user or group for the particular resource.  

Policy 1 – Allows users to create, read, update, and delete Compute Cloud@Customer infrastructures and upgrade schedules.
    
**Important** Specify an IAM group that only includes the users who require permissions to manage infrastructures and upgrade schedules. Administration of these resources is critical to the functionality of Compute Cloud@Customer, and must not be allowed for unauthorized users.     Policy example for IAM with or without Identity Domains:     
Copy
```
allow group <group_name> to manage ccc-family in tenancy
```


Policy 2 – Allows Compute Cloud@Customer to use your IAM data for identity and access management on Compute Cloud@Customer resources.
    Policy example for IAM with or without Identity Domains:     
Copy
```
allow any-user to {COMPARTMENT_INSPECT, USER_INSPECT, GROUP_INSPECT, DYNAMIC_GROUP_INSPECT, POLICY_READ, TAG_NAMESPACE_INSPECT, USER_READ, TAG_DEFAULT_INSPECT, TAG_NAMESPACE_READ, DOMAIN_READ, DOMAIN_INSPECT } in tenancy where all { request.principal.id='<ccc-infrastructure_OCID>', request.principal.type='cccinfrastructure' }
```
    Policy example for IAM with Identity Domains:     
Copy
```
allow dynamic-group <dynamic-group> to {COMPARTMENT_INSPECT, USER_INSPECT, GROUP_INSPECT, DYNAMIC_GROUP_INSPECT, POLICY_READ, TAG_NAMESPACE_INSPECT, USER_READ, TAG_DEFAULT_INSPECT, TAG_NAMESPACE_READ, DOMAIN_READ, DOMAIN_INSPECT} in tenancy
```


Policy 3 – Allows the Compute Cloud@Customer infrastructure service to send you notifications about upgrades.
    
**Note**
For more information about upgrade notifications and how to subscribe to receive them, see [Subscribing to Upgrade Notifications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/subscribe-to-the-notification-service.htm#enable-the-notification-service).     The following examples show policies for IAM with or without Identity Domains:     
Copy
```
allow any-user to manage ons-topics in tenancy where request.principal.type ='cccinfrastructurenotifier'
```

The policy can be modified to further restrict access as shown in the following example:
Copy
```
allow any-user to manage ons-topics in tenancy where all {request.principal.type='cccinfrastructurenotifier', target.compartment.name = 'mycompartment' }
```


Policy 4 – Allows a user in the specified group to initiate the registration process that enables the infrastructure to communicate with your OCI tenancy.
    
**Important**
Don't specify a regular admin group. Instead, create a unique user group with users who are responsible for registering the infrastructure.     The following policy examples are for IAM with or without Identity Domains.     
This example sets the policy at the tenancy level:
Copy
```
allow group <group_name> to { CCC_CERTIFICATE_REGISTER } in tenancy
```

This example sets the policy at the compartment level. The compartment must be the compartment that's associated with the infrastructure:
Copy
```
allow group <group_name> to { CCC_CERTIFICATE_REGISTER } in compartment '<compartment_name>'
```



For information about Compute Cloud@Customer policies you can use to control access to Compute Cloud@Customer infrastructure and upgrade schedule operations, see [Compute Cloud@Customer Policy Reference](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/iam/policy-reference.htm#policy-reference "Use policies to control access to Compute Cloud@Customer infrastructure and upgrade schedule operations.").
## Create a VCN and Subnet 🔗 
Before Compute Cloud@Customer is connected to your tenancy, create a VCN with a subnet in the tenancy. 
Infrastructures require the following network resources in the tenancy:
  1. One Virtual Cloud Network (VCN). See [Creating a VCN](https://docs.oracle.com/iaas/Content/Network/Tasks/create_vcn.htm). We recommend a small CIDR block, for example `192.168.100.0/29`.
  2. For each infrastructure, create one subnet in the VCN. See [Creating a subnet](https://docs.oracle.com/iaas/Content/Network/Tasks/create_subnet.htm). For example, `192.168.100.0/30`.


### What's Next? 🔗 
Work with Oracle to install and connect Compute Cloud@Customer to your network. After Oracle initializes Compute Cloud@Customer, you then create an Compute Cloud@Customer infrastructure, and connect it to your OCI tenancy. See [Creating a Compute Cloud@Customer Infrastructure in OCI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/create-infrastructure.htm#create-infrastructure "Create a Compute Cloud@Customer infrastructure in Oracle Cloud Infrastructure \(OCI\) to communicate with the corresponding infrastructure in the data center."). 
For a complete list of installation tasks, see [Installing and Configuring Compute Cloud@Customer](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/configuring-compute-cloud-customer.htm#performing-an-initial-configuration "Before you can use Compute Cloud@Customer, you must prepare your site for the installation of the rack, prepare your tenancy, and initialize the connection of the Compute Cloud@Customer infrastructure to Oracle Cloud Infrastructure.").
Was this article helpful?
YesNo


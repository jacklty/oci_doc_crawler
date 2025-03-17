Updated 2025-02-13
# Prerequisites for Oracle Platform Services on Oracle Cloud Infrastructure
This topic describes procedures that are required by some Oracle Platform Services before you can launch them on Oracle Cloud Infrastructure. The information in this topic applies only to the following services: 
  * Oracle Database Cloud Service
  * Oracle Data Hub Cloud Service
  * Oracle Event Hub Cloud Service
  * Oracle Java Cloud Service
  * Oracle SOA Cloud Service


For a list of all services supported on Oracle Cloud Infrastructure, see [Information About Supported Platform Services](https://docs.oracle.com/en-us/iaas/Content/General/Reference/PaaSprereqs.htm#Informat).
## Accessing Oracle Cloud Infrastructure 🔗 
Oracle Cloud Infrastructure has a different interface and credential set than your Oracle Platform Services. 
You can access Oracle Cloud Infrastructure (OCI) by using the [Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm) (a browser-based interface), [REST API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm), or [OCI CLI](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). Instructions for using the Console, API, and CLI are included in topics throughout this documentation. For a list of available SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
To access the [Console](https://cloud.oracle.com/), you must use a [supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#supported-browsers). To go to the Console sign-in page, open the navigation menu at the top of this page and select **Infrastructure Console**. You are prompted to enter your cloud tenant, your user name, and your password.
## Required Identity and Access Management (IAM) Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
See [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top) for more information and examples.
## Resources Created in Your Tenancy by Oracle 🔗 
Oracle creates a **compartment** in your tenancy for Oracle Platform Services. This compartment is specially configured by Oracle for the Oracle Cloud Infrastructure resources that you create through the Platform Services. You can't choose another compartment for Oracle to use.
Along with this compartment, Oracle creates the IAM policies to allow Oracle Platform Services access to the resources. 
The compartment that Oracle creates for Oracle Platform Services is named: `ManagedCompartmentForPaaS`.
The polices that Oracle creates for Oracle Platform Services are: 
  * `PSM-root-policy `
This policy is attached to the root compartment of your tenancy.
  * `PSM-mgd-comp-policy `
This policy is attached to the `ManagedCompartmentForPaaS` compartment.


**Caution** Do not make any changes to these resources. Editing or renaming the policies or the compartment can result in loss of functionality.
## Prerequisites for Oracle Platform Services 🔗 
Before you can create instances of an Oracle Platform Service on Oracle Cloud Infrastructure, you need to have the following resources in your Oracle Cloud Infrastructure tenancy: 
  * A compartment for your resources
  * A virtual cloud network (VCN) with at least one public subnet
  * IAM policies to allow Oracle Platform Services to access the VCN
  * An Object Storage bucket
  * Credentials to use with Object Storage


Some of the Platform Services automatically create some of these resources for you. See details about your service in the following sections. 
## Setting Up the Prerequisites 🔗 
**Note**
To use **Autonomous Data Warehouse Cloud** , you don't need to set up any of the resources listed in this prerequisites section. However, if you optionally choose to use Oracle Cloud Infrastructure Object Storage for data loading, you need to perform these two tasks:
[Create a bucket](https://docs.oracle.com/en-us/iaas/Content/General/Reference/PaaSprereqs.htm#Create_a_bucket)
[Create an auth token](https://docs.oracle.com/en-us/iaas/Content/General/Reference/PaaSprereqs.htm#create_swift_password)
Following are two scenarios with procedure sets. If you need to set up all the required resources, follow Scenario 1. If you already have a VCN in your Oracle Cloud Infrastructure tenancy that you want to use for Oracle Platform Services, follow Scenario 2.
To follow a tutorial on how to set up the prerequisites for Scenario 1, see [Creating the Infrastructure Resources Required for Oracle Platform Services](https://apexapps.oracle.com/pls/apex/f?p=44785:112:0::::P112_CONTENT_ID:22118). 
### Scenario 1: I need to create all the prerequisite resources 🔗 
Use this procedure if you don't have any resources set up in OCI.
[Create a compartment](https://docs.oracle.com/en-us/iaas/Content/General/Reference/PaaSprereqs.htm)
**Important** You cannot use the `ManagedCompartmentForPaaS` for your VCN and bucket. 
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Compartments**.
A list of the existing compartments in your tenancy is displayed.
  2. Click **Create Compartment**. 
  3. Enter the following: 
     * **Name:** For example, PaaSResources. Restrictions for compartment names are: Maximum 100 characters, including letters, numbers, periods, hyphens, and underscores. The name must be unique across all the compartments in your tenancy. Avoid entering confidential information.
     * **Description:** A friendly description.
  4. Click **Create Compartment**.


[Set up your virtual cloud network](https://docs.oracle.com/en-us/iaas/Content/General/Reference/PaaSprereqs.htm)
This procedure creates a VCN with these characteristics:
  * A VCN with the CIDR of your choice (example: 10.0.0.0/16).
  * A regional public subnet with access to the VCN's [internet gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIGs.htm). You can choose the subnet's CIDR (example: 10.0.0.0/24).
  * A regional private subnet with access to the VCN's [NAT gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm) and [service gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm) (and therefore the Oracle Services Network). You can choose the subnet's CIDR (example: 10.0.1.0/24).
  * Use of the [Internet and VCN Resolver](https://docs.oracle.com/iaas/Content/Network/Concepts/dns.htm) for DNS, so your instances can use their hostnames instead of their private IP addresses to communicate with each other.


**Tip** The following VCN quickstart procedure is useful for getting started and trying out Oracle Platform Services on Oracle Cloud Infrastructure. For production, use the procedure in [VCNs and Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/VCNs.htm). That topic explains features such as how to specify the CIDR ranges for your VCN and subnets, and how to secure your network. When you use the advanced procedure in that topic, remember that the VCN that you create must have a public subnet for Oracle Platform Services to use.
  1. Open the **Region** menu and select the region in which you want to create the Oracle PaaS service instance. 
Select a region that's within the default data region of your account. For example, if your default data region is EMEA, then select Germany Central (Frankfurt) or UK South (London).
  2. From the **Compartment** list, select the compartment you created.
  3. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**. 
  4. Click **Networking Quickstart**.
  5. Select **VCN with Internet Connectivity** , and then click **Start Workflow**.
  6. Enter the following:
     * **VCN Name:** Enter a name for your cloud network, for example, <your_initials>_Network. The name is incorporated into the names of all the related resources that are automatically created. Avoid entering confidential information.
     * **Compartment:** Leave the default value (the compartment you're currently working in). All the resources will be created in this compartment.
     * **VCN CIDR Block:** Enter a valid CIDR block for the VCN. For example 10.0.0.0/16.
     * **Public Subnet CIDR Block:** Enter a valid CIDR block for the subnet. The value must be within the VCN's CIDR block. For example: 10.0.0.0/24.
     * **Private Subnet CIDR Block:** Enter a valid CIDR block for the subnet. The value must be within the VCN's CIDR block and not overlap with the public subnet's CIDR block. For example: 10.0.1.0/24.
     * Accept the defaults for any other fields.
  7. Click **Next**.
  8. Review the list of resources that the workflow will create for you. Notice that the workflow will set up security list rules and route table rules to enable basic access for the VCN. 
  9. Click **Create** to start the short workflow.


[Permit Oracle Platform Services to access resources](https://docs.oracle.com/en-us/iaas/Content/General/Reference/PaaSprereqs.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Policies**. 
  2. In the **Compartment** list, select the root compartment of your tenancy. 
  3. Click **Create Policy**. 
  4. Enter the following: 
     * **Name:** A unique name for the policy. The name must be unique across all policies in your tenancy. You cannot change this later.
     * **Description:** A friendly description. You can change this later if you want to.
     * **Policy Builder:** Click **Show manual editor**. To allow Oracle Platform Services access to use the network in your compartment, enter the following policy statements. Replace <compartment_name> with your compartment name where the resources are located. 
Copy
```
Allow service PSM to inspect vcns in compartment <compartment_name>
Allow service PSM to use subnets in compartment <compartment_name>
Allow service PSM to use vnics in compartment <compartment_name>
Allow service PSM to manage security-lists in compartment <compartment_name>
Allow resource psmrp psm to inspect vcns in compartment <compartment_name>
Allow resource psmrp psm to use subnets in compartment <compartment_name>
Allow resource psmrp psm to use vnics in compartment <compartment_name>
Allow resource psmrp psm to manage security-lists in compartment <compartment_name>
```

For more information about policies, see [Policy Basics](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy) and also [Policy Syntax](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policysyntax.htm#Policy_Syntax). 
  5. (Optional) If you want to enable the use of an Autonomous Database for Transaction Processing and Mixed Workloads or Oracle Cloud Infrastructure Database instance in your compartment as the infrastructure schema database for your Oracle Java Cloud Service instance, then add the following statements:
Copy
```
Allow service PSM to inspect autonomous-database in compartment <compartment_name>
Allow service PSM to inspect database-family in compartment <compartment_name>
Allow resource psmrp psm to inspect autonomous-database in compartment <compartment_name>
Allow resource psmrp psm to inspect database-family in compartment <compartment_name>
```

  6. Click **Create**. 


[Create a bucket](https://docs.oracle.com/en-us/iaas/Content/General/Reference/PaaSprereqs.htm)
  1. Open the **Region** menu and select the region in which you want to create the Oracle PaaS service instance. 
Select a region that's within the default data region of your account. For example, if your default data region is EMEA, then select Germany Central (Frankfurt) or UK South (London).
  2. Open the **navigation menu** and select **Storage**. Under **Object Storage & Archive Storage**, select **Buckets**.
  3. Select the compartment you created.
  4. Select **Create Bucket**.
  5. Enter a bucket name, for example: PaasBucket. 
Make a note of the name you enter. You need it when you create an instance for your Oracle Platform Service later.
  6. Select **Create**.


[Set up credentials to use with Object Storage](https://docs.oracle.com/en-us/iaas/Content/General/Reference/PaaSprereqs.htm)
For Big Data Cloud, set up an API signing key:
[Set up an API signing key](https://docs.oracle.com/en-us/iaas/Content/General/Reference/PaaSprereqs.htm)
Follow the instructions in this topic: [Required Keys and OCIDs](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm).
For all other services, create an auth token. Note that your service might refer to this credential as a Swift password. Use the auth token wherever you are asked to provide a Swift password.
[Create an auth token](https://docs.oracle.com/en-us/iaas/Content/General/Reference/PaaSprereqs.htm)
  1. View the user's details:
     * If you're creating an auth token for yourself: In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see.
     * If you're an administrator creating an auth token for another user: In the Console, click **Identity** , and then click **Users**. Locate the user in the list, and then click the user's name to view the details.
  2. On the left side of the page, click **Auth tokens**.
  3. Click **Generate Token**.
  4. Enter a friendly description for the token and click **Generate Token**.
The new token is displayed. 
  5. Copy the token immediately, because you can't retrieve it again after closing the dialog box. Also, make sure you have this token available when you create your Oracle Platform Services instance.


### Scenario 2: I have an existing VCN in Oracle Cloud Infrastructure that I want to use for my Oracle Platform Services instance 🔗 
You can use an existing VCN. The VCN must have at least one public subnet. Perform these tasks to complete the prerequisites:
[Permit Oracle Platform Services to access resources](https://docs.oracle.com/en-us/iaas/Content/General/Reference/PaaSprereqs.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Policies**. 
  2. In the **Compartment** list, select the root compartment of your tenancy. 
  3. Click **Create Policy**. 
  4. Enter the following: 
     * **Name:** A unique name for the policy. The name must be unique across all policies in your tenancy. You cannot change this later. Avoid entering confidential information.
     * **Description:** A friendly description. You can change this later if you want to.
     * **Policy Builder:** Click **Show manual editor**. To allow Oracle Platform Services access to use the network, enter the following policy. In each statement, replace <compartment_name> with the name of the compartment where your VCN resides.
Copy
```
Allow service PSM to inspect vcns in compartment <compartment_name>
Allow service PSM to use subnets in compartment <compartment_name>
Allow service PSM to use vnics in compartment <compartment_name>
Allow service PSM to manage security-lists in compartment <compartment_name>
Allow resource psmrp psm to inspect vcns in compartment <compartment_name>
Allow resource psmrp psm to use subnets in compartment <compartment_name>
Allow resource psmrp psm to use vnics in compartment <compartment_name>
Allow resource psmrp psm to manage security-lists in compartment <compartment_name>
```

For more information about policies, see [Policy Basics](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy) and also [Policy Syntax](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policysyntax.htm#Policy_Syntax). 
  5. (Optional) If you want to enable the use of an Autonomous Database for Transaction Processing and Mixed Workloads or Oracle Cloud Infrastructure Database instance in your compartment as the infrastructure schema database for your Oracle Java Cloud Service instance, then add the following statements:
Copy
```
Allow service PSM to inspect autonomous-database in compartment <compartment_name>
Allow service PSM to inspect database-family in compartment <compartment_name>
Allow resource psmrp psm to inspect autonomous-database in compartment <compartment_name>
Allow resource psmrp psm to inspect database-family in compartment <compartment_name>
```

  6. Click **Create**. 


[Create a bucket](https://docs.oracle.com/en-us/iaas/Content/General/Reference/PaaSprereqs.htm)
  1. Open the **Region** menu and select the region in which you want to create the Oracle PaaS service instance. 
Select a region that's within the default data region of your account. For example, if your default data region is EMEA, then select Germany Central (Frankfurt) or UK South (London).
  2. Open the **navigation menu** and select **Storage**. Under **Object Storage & Archive Storage**, select **Buckets**.
  3. Select the compartment you want to create the bucket in.
  4. Select **Create Bucket**.
  5. Enter a bucket name, for example: PaasBucket. Make a note of the name you enter. You need it when you create an instance for your Oracle Platform Service later. Avoid entering confidential information.
  6. Select **Create**.


[Set up credentials to use with Object Storage](https://docs.oracle.com/en-us/iaas/Content/General/Reference/PaaSprereqs.htm)
For Big Data Cloud, set up an API signing key:
[Set up an API signing key](https://docs.oracle.com/en-us/iaas/Content/General/Reference/PaaSprereqs.htm)
Follow the instructions in this topic: [Required Keys and OCIDs](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm).
For all other services, create an auth token. Note that your service might refer to this credential as a Swift password. Use the auth token wherever you are asked to provide a Swift password.
[Create an auth token](https://docs.oracle.com/en-us/iaas/Content/General/Reference/PaaSprereqs.htm)
  1. View the user's details:
     * If you're creating an auth token for yourself: In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see.
     * If you're an administrator creating an auth token for another user: In the Console, click **Identity** , and then click **Users**. Locate the user in the list, and then click the user's name to view the details.
  2. On the left side of the page, click **Auth Tokens**.
  3. Click **Generate Token**.
  4. Enter a friendly description for the token and click **Generate Token**.
The new token is displayed. 
  5. Copy the auth token immediately, because you can't retrieve it again after closing the dialog box. Also, make sure you have this token available when you create your Oracle Platform Services instance.


## Information About Supported Platform Services 🔗 
The following table lists the services supported on Oracle Cloud Infrastructure and links to more information about using those services on Oracle Cloud Infrastructure:
Service | More Information  
---|---  
Analytics Cloud | [Getting Started with Oracle Analytics Cloud](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acsgs/how-do-i-get-started.html)  
API Platform Cloud Service | [Get Started with Oracle API Platform Cloud Service](https://docs.oracle.com/en/cloud/paas/api-platform-cloud/apfad/get-started-oracle-api-platform-cloud-service.html)  
Autonomous Data Warehouse | [Getting Started with Autonomous Data Warehouse](https://docs.oracle.com/en/cloud/paas/autonomous-data-warehouse-cloud/user/getting-started.html#GUID-4B91499D-7C2B-46D9-8E4D-A6ABF2093414)  
Autonomous Mobile Cloud Enterprise | [About Oracle Autonomous Mobile Cloud Enterprise](https://docs.oracle.com/en/cloud/paas/mobile-autonomous-cloud/service-administration/getting-started.html#GUID-4E78309A-5C28-4357-8CD9-72563F1B6419)  
Database Cloud Service | [About Database Deployments in Oracle Cloud Infrastructure](http://www.oracle.com/pls/topic/lookup?ctx=cloud&id=CSDBI-GUID-7F8F90A0-C643-4201-926C-599E3A67B30A)  
Data Hub Cloud Service | [About Oracle Data Hub Cloud Service Clusters in Oracle Cloud Infrastructure](https://www.oracle.com/pls/topic/lookup?ctx=cloud&id=CSDHU-GUID-C1B35496-BD51-4278-B287-F0768DF0611E)  
Data Integration Platform Cloud | [What is Oracle Data Integration Platform Cloud](https://docs.oracle.com/en/cloud/paas/data-integration-platform-cloud/using/get-started-data-integration-platform-cloud.html#GUID-72E6BAA9-260B-4098-90A8-D42B95FC9010)  
Event Hub Cloud Service | [About Instances in Oracle Cloud Infrastructure](http://www.oracle.com/pls/topic/lookup?ctx=cloud&id=EHDAG-GUID-6B070D54-611A-40EF-ADBD-88CB9D11CF99)  
Integration |  [Getting Started with Oracle Integration Generation 2](https://docs.oracle.com/en/cloud/paas/integration-cloud/int-get-started/welcome-oracle-integration.html) [Getting Started with Oracle Integration 3](https://docs.oracle.com/pls/topic/lookup?ctx=appint&id=INTRA-GUID-3FD7D407-DA8F-42C3-89DB-6E6E105E271E)  
Java Cloud Service | [About Java Cloud Service Instances in Oracle Cloud Infrastructure](https://www.oracle.com/pls/topic/lookup?ctx=cloud&id=JSCUG-GUID-1294F076-EA26-4FBD-B4E8-429959ED2706)  
NoSQL Database Cloud Service | [Oracle NoSQL Database Cloud Service](https://docs.oracle.com/en/cloud/paas/nosql-cloud/index.html)  
Process Automation | [Oracle Cloud Infrastructure Process Automation](https://docs.oracle.com/en/cloud/paas/process-automation/index.html)  
SOA Cloud Service | [About SOA Cloud Service Instances in Oracle Cloud Infrastructure Classic and Oracle Cloud Infrastructure](https://docs.oracle.com/en/cloud/paas/soa-cloud/csbcs/index.html)  
Visual Builder | [Oracle Visual Builder](https://docs.oracle.com/en/cloud/paas/app-builder-cloud/index.html)  
Visual Builder Studio | [Oracle Visual Builder Studio](https://docs.oracle.com/en/cloud/paas/visual-builder/index.html)  
Was this article helpful?
YesNo


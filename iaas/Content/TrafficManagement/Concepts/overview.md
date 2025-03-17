Updated 2025-03-10
# Overview of Traffic Management
Traffic Management helps you guide traffic to endpoints based on various conditions, including endpoint health and the geographic origins of DNS requests.
Use Traffic Management steering policies to serve intelligent responses to DNS queries, meaning different answers (endpoints) might be served for the query depending on the logic defined in the policy. Traffic Management is only available for public DNS, and isn't supported on private DNS.
## Traffic Management Components 🔗 
The following list describes the components used to build a traffic management steering policy. 

STEERING POLICIES
    A framework to define the traffic management behavior for zones. Steering policies contain rules that help to intelligently serve DNS answers. 

ATTACHMENTS
    Allows you to link a steering policy to zones. An attachment of a steering policy to a zone occludes all records at its domain that are of a covered record type, constructing DNS responses from its steering policy rather than from those domain's records. A domain can have at most one attachment covering any particular record type. 

RULES
    The guidelines steering policies use to filter answers based on the properties of a DNS request, such as the requests geolocation or the health of endpoints. 

ANSWERS
    Answers contain the DNS record data and metadata to be processed in a steering policy.
## Ways to Access Traffic Management 🔗 
You can access Oracle Cloud Infrastructure (OCI) by using the [Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm) (a browser-based interface), [REST API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm), or [OCI CLI](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). Instructions for using the Console, API, and CLI are included in topics throughout this documentation. For a list of available SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
To access the [Console](https://cloud.oracle.com/), you must use a [supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#supported-browsers). To go to the Console sign-in page, open the navigation menu at the top of this page and select **Infrastructure Console**. You are prompted to enter your cloud tenant, your user name, and your password.
## Authentication and Authorization 🔗 
Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).
An administrator in an organization needs to set up **groups** , **compartments** , and **policies** that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see [Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm). 
If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.
## Traffic Management Capabilities and Limits 🔗 
Oracle Cloud Infrastructure Traffic Management is limited to 100 policies and 1,000 attachments per tenant. See [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm) for a list of applicable limits and instructions for requesting a limit increase.
## Required IAM Service Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). For more details about policies for Traffic Management, see [Details for DNS and Traffic Management](https://docs.oracle.com/iaas/Content/Identity/policyreference/dnspolicyreference.htm).
## Managing Traffic Management steering policies 🔗 
Traffic Management steering policies can account for health of answers to provide failover capabilities, provide the ability to load balance traffic across many resources, and account for the location where the query originated to provide a flexible and powerful mechanism to efficiently steer DNS traffic.
### Policy Types 🔗  

FAILOVER
    Failover policies let you prioritize the order in which you want answers served in a policy (for example, Primary and Secondary). Oracle Cloud Infrastructure Health Checks monitors and on-demand probes are leveraged to evaluate the health of answers in the policy. If the primary answer is unhealthy, DNS traffic is automatically steered to the secondary answer. 

LOAD BALANCER
    Load Balancer policies distribute traffic across many endpoints. Endpoints can be assigned equal weights to distribute traffic evenly across the endpoints or custom weights can be assigned for ratio load balancing. Oracle Cloud Infrastructure Health Checks monitors and on-demand probes are leveraged to evaluate the health of the endpoint. If an endpoint is unhealthy, DNS traffic is automatically distributed to the other endpoints. 

GEOLOCATION STEERING
    Geolocation steering policies distribute DNS traffic to different endpoints based on the location of the end user. Customers can define geographic regions composed of originating continent, countries or states/provinces (North America) and define a separate endpoint or set of endpoints for each region. 

ASN STEERING
    ASN steering policies enable you to steer DNS traffic based on Autonomous System Numbers (ASN). DNS queries originating from a specific ASN or set of ASNs can be steered to a specified endpoint. 

IP PREFIX STEERING
    IP Prefix steering policies enable customers to steer DNS traffic based on the IP Prefix of the originating query.
## Typical Traffic Steering Scenarios 🔗 
This section describes several typical scenarios for using Traffic Management steering policies.
### Basic Failover
You can leverage Traffic Management steering policies to provide automated failover between primary and secondary servers.
### Cloud Migration
Weighted load balancing supports controlled migration from a data center to Oracle Cloud Infrastructure servers. You can steer a small amount of traffic (1%) to new resources in the cloud to verify everything is working as expected. You can then increase the ratios until you're comfortable with fully migrating all DNS traffic to the cloud.
### Load Balancing Across Many Servers for Scale
You can configure load balancing pools of many servers. Traffic Management steering policies can automatically distribute DNS traffic across the set of servers. You can also use Health Checks to evaluate server traffic. If a server is unhealthy, traffic is automatically redirected to healthy servers.
### Hybrid Environments
Because Traffic Management is an agnostic service, you can use it steer traffic to both OCI resources and any publicly exposed (internet resolvable) resources, including other cloud providers and enterprise data centers.
### Worldwide Geolocation Treatment
You can divide global users into geographically defined regions (for example, state/province level in North America, country level for rest of world) and steer customers to specified resources based on their location. This helps to ensure global, high performing internet resolution, and supports functions such as ring fencing. For example, keeping traffic from China in China and block traffic outside of China into China.
### Canary Testing
Leveraging IP Prefix steering, you can configure policies to serve different responses for internal users and external users.
### Zero-Rating Services
ASN steering conditional steering based on the originating enterprise, mobile operator or other communications provider in support of various commercial agreements that might be in place. Preferred ASNs can be directed to free resources, while all other traffic can be directed to paid resources.
## Traffic Management Tasks 🔗 
### Steering Policy Tasks
You can perform the following tasks with Traffic Management steering policies:
  * [Creating a Load Balancer Policy](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-lb.htm#top "Create a Load Balancer traffic management policy that distributes traffic across many endpoints.")
  * [Creating a Failover Policy](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-failover.htm#top "Create a failover traffic management policy to prioritize the order in which you want answers served in response to DNS queries.")
  * [Creating a Geolocation Steering Policy](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-geo.htm#top "Create a geolocation traffic management policy that distributes DNS traffic to different endpoints based on the location of the end user")
  * [Creating an ASN Steering Policy](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-asn.htm#top "Create an ASN traffic management steering policy that steers DNS traffic based on Autonomous System Numbers \(ASN\).")
  * [Creating an IP Prefix Steering Policy](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/create-tm-policy-ip.htm#top "Create an IP prefix traffic management policy that steers DNS traffic based on the IP prefix of the originating query.")
  * [Listing Steering Policies](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-list.htm#top "View a list of all Traffic Management steering policy attachments in a compartment.")
  * [Viewing a Steering Policy's Details](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-get.htm#top "View details about a Traffic Management steering policy.")
  * [Editing a Steering Policy](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-edit.htm#top "Edit information for a Traffic Management steering policy such as name, TTL, answers, health checks, and tags.")
  * [Moving a Steering Policy Between Compartments](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-move.htm#top "Move a steering policy from one compartment to another.")
  * [Deleting a Steering Policy](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-delete.htm#top "Delete a Traffic Management steering policy.")


### Steering Policy Domain Attachment Tasks
You can perform the following tasks with Traffic Management steering policy attachments: 
  * [Attaching a Domain to a Policy](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-create.htm#top "Create a new attachment between a steering policy and a domain, giving the policy permission to answer queries for the specified domain. A steering policy must be attached to a domain for the policy to answer DNS queries for that domain.")
  * [Listing Steering Policy Domain Attachments](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-list.htm#top "View a list of steering policy domain attachments.")
  * [Viewing Details for an Attached Domain](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-policy-attach-get.htm#top "View details about a domain attached to a Traffic Management steering policy.")
  * [Deleting a Domain Attachment](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Tasks/tm-attach-delete.htm#top "Delete a domain attachment to a Traffic Management steering policy.")


Was this article helpful?
YesNo


Updated 2024-05-07
# Installing and Configuring Compute Cloud@Customer
Before you can use Compute Cloud@Customer, you must prepare your site for the installation of the rack, prepare your tenancy, and initialize the connection of the Compute Cloud@Customer infrastructure to Oracle Cloud Infrastructure.
The following table describes the steps you perform to install Compute Cloud@Customer. Oracle performs some steps. Steps 3 and 4 can be performed at the same time, or in reverse order, depending on when the hardware arrives at your site. You can also watch this [Video: Introduction to Installing and Configuring Oracle Compute Cloud@Customer](https://youtu.be/yw_GRsEZp5k).
No. |  Task |  Links  
---|---|---  
1. |  Prepare your data center for the Compute Cloud@Customer rack installation. | [Preparing Your Site](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/preparing-site.htm#prepare-your-site "Use the information in this section to learn about site requirements before the arrival of Oracle Compute Cloud@Customer.") and [Site Checklists for Compute Cloud@Customer](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/site-checklists.htm#site_checklists "To determine your readiness for the installation of the Compute Cloud@Customer rack in your data center, work with your Oracle representative to review and complete the checklists before the rack arrives.")  
2. | Oracle validates site requirements in your data center.  
3. | Prepare your OCI tenancy by setting up these items: 
  * Federated identity provider
  * Users and groups
  * Compartments
  * Policies
  * Virtual cloud network (VCN) with a subnet

| [Preparing Your Tenancy](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/preparing-your-tenancy.htm#preparing-your-tenancy "Before the Compute Cloud@Customer infrastructure is connected to Oracle Cloud Infrastructure, the tenancy administrator must set up compartments, create policies, and configure a virtual cloud network. This setup is used to connect the Compute Cloud@Customer infrastructure to Oracle Cloud Infrastructure.")  
4. | The Compute Cloud@Customer rack is delivered to your site.Oracle installs the rack in your data center and works with you to connect it to your network.Oracle initializes Compute Cloud@Customer and configures it with site-specific details such as network parameters.  
5. |  Create an infrastructure in the compartment for the physical infrastructure in the data center. | [Creating a Compute Cloud@Customer Infrastructure in OCI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/create-infrastructure.htm#create-infrastructure "Create a Compute Cloud@Customer infrastructure in Oracle Cloud Infrastructure \(OCI\) to communicate with the corresponding infrastructure in the data center.")  
6. |  Connect to the infrastructure using a bootstrap process that involves the exchange of provisioning information to ensure a secure connection.  | [Connecting a Compute Cloud@Customer Infrastructure to OCI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/connecting.htm#connecting "The Compute Cloud@Customer infrastructure in the data center needs to be connected to Oracle Cloud Infrastructure \(OCI\) before it can be used. This task involves a bootstrap process during which a secure connection is established.")  
7. |  Work out an upgrade schedule for the infrastructure and define this in an upgrade schedule resource. | [Creating a Compute Cloud@Customer Upgrade Schedule](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/create-upgrade-schedule.htm#create-upgrade-schedule "Create an upgrade schedule to allow Oracle to upgrade Compute Cloud@Customer hardware and software during defined time periods. After the upgrade schedule is created, attach the schedule to the infrastructures you want upgraded with the schedule.")  
8.  | Subscribe to Compute Cloud@Customer upgrade notification topics so that you receive notifications when and upgrade starts and finishes. | [Subscribing to Upgrade Notifications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/subscribe-to-the-notification-service.htm#enable-the-notification-service)  
You can now use Compute Cloud@Customer to provide compute, storage and other resources. See [Signing in to the Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.").
Was this article helpful?
YesNo


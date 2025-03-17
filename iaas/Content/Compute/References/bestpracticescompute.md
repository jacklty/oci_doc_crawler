Updated 2025-02-13
# Best Practices for Your Compute Instances
Oracle Cloud Infrastructure Compute provides bare metal and virtual machine (VM) compute capacity that delivers performance, flexibility, and control without compromise. It's powered by Oracle's next generation, internet-scale infrastructure, designed to help you develop and run your most demanding applications and workloads in the cloud.
You can provision compute capacity through an easy-to-use web console or the API, SDKs, or CLI. The compute instance, once provisioned, provides you with access to the host. This gives you complete control of your instance.
Though you have full management authority for your instance, we recommend a variety of best practices to ensure system availability and top performance. 
## IP Addresses Reserved for Use by Oracle 🔗 
Certain IP addresses are reserved for Oracle Cloud Infrastructure use and can't be used in an address numbering scheme.
### 169.254.0.0/16 🔗 
These addresses are used for iSCSI connections to the boot and block volumes, instance metadata, and other services.
### Class D and Class E 🔗 
All addresses from 224.0.0.0 to 239.255.255.255 (Class D) are prohibited for use in a VCN, they're reserved for multicast address assignments in the IP standards. See [RFC 3171](https://tools.ietf.org/html/rfc3171) for details. 
All addresses from 240.0.0.0 to 255.255.255.255 (Class E) are prohibited for use in a VCN, they're reserved for future use in the IP standards. See [RFC 1112, Section 4](https://tools.ietf.org/html/rfc1112) for details.
### Three IP Addresses in Each Subnet 🔗 
These addresses consist of:
  * The first IP address in the CIDR (the network address)
  * The last IP address in the CIDR (the broadcast address)
  * The first host address in the CIDR (the subnet default gateway address)


For example, in a subnet with CIDR 192.168.0.0/24, these addresses are reserved:
  * 192.168.0.0 (the network address)
  * 192.168.0.255 (the broadcast address)
  * 192.168.0.1 (the subnet default gateway address)


The remaining addresses in the CIDR (192.168.0.2 to 192.168.0.254) are available for use.
## Essential Firewall Rules 🔗 
All platform images include rules that allow only "root" on Linux instances or "Administrators" on Windows Server instances to make outgoing connections to the iSCSI network endpoints (169.254.0.2:3260, 169.254.2.0/24:3260) that serve the instance's boot and block volumes.
  * We recommend that you do not reconfigure the firewall on your instance to remove these rules. Removing these rules allows non-root users or non-administrators to access the instance's boot disk volume.
  * We recommend that you do not create custom images without these rules unless you understand the security risks.
  * Do not use Uncomplicated Firewall (UFW) to edit firewall rules on an Ubuntu image. Using UFW to edit rules might cause an instance not to boot. Therefore, we recommend you edit UFW rules using the method described in this note: [Ubuntu instance fails to reboot after enabling Uncomplicated Firewall (UFW)](https://docs.oracle.com/en-us/iaas/Content/Compute/known-issues.htm#ufw).


## System Resilience 🔗 
Follow industry-wide hardware failure best practices to ensure the resilience of your solution in the event of a hardware failure. Some best practices include:
  * Design your system with redundant compute nodes in different availability domains to support failover capability.
  * Create a [custom image](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm#Managing_Custom_Images "You can create a custom image of an instance's boot disk and use it to launch other instances. Instances you launch from your image include the customizations, configuration, and software installed when you created the image.") of your system drive each time you change the image.
  * [Back up](https://docs.oracle.com/iaas/Content/Block/Tasks/backingupavolume.htm) your data drives, or sync to spare drives, regularly.

If you experience a hardware failure and have followed these practices, you can terminate the failed instance, launch your custom image to create a new instance, and then apply the backup data. 
## Uninterrupted Access to the Instance 🔗 
Ensure that the DHCP client keeps running so you can always access the instance. If you stop the DHCP client manually or disable NetworkManager (which stops the DHCP client on Linux instances), the instance can't renew its DHCP lease and becomes inaccessible when the lease expires (typically within 24 hours). Don't disable NetworkManager unless you use another method to ensure renewal of the lease. 
Stopping the DHCP client might remove the host route table when the lease expires. Also, loss of network connectivity to iSCSI connections might result in loss of the boot drive. 
## User Access 🔗 
With Linux instances, you can [use SSH to access your instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm#top "You can connect to a running Linux instance by using a Secure Shell \(SSH\) connection.") from a remote host. Default users names are assigned based on the Linux distribution used.
  * For Oracle Linux or Redhat Enterprise Linux compatible platform images the username is `opc`.
  * For Ubuntu platform images to create the instance, the username is `ubuntu`.


After signing in, you can add users on your instance.
If you do not want to share SSH keys, you can [create additional SSH-enabled users](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/addingusers.htm#Adding_Users_on_an_Instance).
With Windows instances, you can [access your instance using a Remote Desktop client](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm#top "You connect to a Windows instance by using a Remote Desktop connection. Most Windows systems include a Remote Desktop client by default."). If you used a Windows platform image to create the instance, the username is `opc`. After signing in, you can add users on your instance. 
For more information about user access, see [Adding Users to an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/addingusers.htm#Adding_Users_on_an_Instance).
## NTP Service 🔗 
Oracle Cloud Infrastructure offers a fully managed, secure, and highly available NTP service that you can use to set the date and time of your compute and Database instances from within your virtual cloud network (VCN). The NTP service is enabled by default on all of the platform images that are available in Oracle Cloud Infrastructure. For information about this service, see [Configuring the Oracle Cloud Infrastructure NTP Service for an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/configuringntpservice.htm#Configuring_the_Oracle_Cloud_Infrastructure_NTP_Service_for_an_Instance).
## Fault Domains 🔗 
A fault domain is a grouping of hardware and infrastructure that is distinct from other fault domains in the same availability domain. Each availability domain has three fault domains. By properly leveraging fault domains, you can increase the availability of applications running on Oracle Cloud Infrastructure. For background information, see [Fault Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#fault).
Your application's architecture determines whether you should separate or group instances using fault domains.
### Scenario 1: Highly Available Application Architecture 🔗 
In this scenario, you have a highly available application, for example you have two web servers and a clustered database. In this scenario, you should group one web server and one database node in one fault domain and the other half of each pair in another fault domain. This placement ensures that a failure of any one fault domain does not result in an outage for your application. 
### Scenario 2: Single Web Server and Database Instance Architecture 🔗 
In this scenario, your application architecture is not highly available, for example you have one web server and one database instance. In this scenario, both the web server and the database instance should be placed in the same fault domain to minimize customer outages. This placement ensures that your application is only impacted by the failure of that single fault domain, providing greater application availability overall.
## Customer-Managed Instance Maintenance 🔗 
Oracle Cloud Infrastructure performs routine data center maintenance on the physical infrastructure for compute instances. This maintenance includes tasks such as upgrading and replacing hardware or performing maintenance that halts power to the host.
Oracle Cloud Infrastructure supports a variety of maintenance actions for compute instances including live migration, scheduled maintenance, rebuild in place, and manual migration. The maintenance action depends on characteristics such as the [shape](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm#Compute_Shapes) that the instance uses. Depending on the type of maintenance action that is performed for an instance, the instance might experience downtime during infrastructure maintenance. For some shapes, you can control how and when the downtime occurs. For more information, see [Infrastructure Maintenance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructure-maintenance.htm#infrastructure-maintenance).
You can use compute infrastructure health metrics to monitor the status of your instances during maintenance. For more information, see [Infrastructure Health Metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructurehealthmetrics.htm#Infrastructure_Health_Metrics).
Was this article helpful?
YesNo


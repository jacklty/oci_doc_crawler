Updated 2024-10-07
# Securing Compute Cloud@Customer
Compute Cloud@Customer provides effective and manageable security that enables you to run mission-critical workloads and to store data with confidence.
Compute Cloud@Customer is a fully-managed, rack-scale, OCI regional resource bringing Oracle’s second-generation cloud services on-premises. The system is installed by Oracle, which provides a level of security independent of local practices. However, this also requires the system administrators to understand exactly what's provided as a security baseline. Then the administrators can adjust security practices and configurations to achieve the required level of security needed for their specific circumstances. 
**Note**
For comprehensive information about Oracle Cloud Infrastructure security, see [ Oracle Cloud Infrastructure: Security.](https://docs.oracle.com/iaas/Content/Security/Concepts/security.htm)
## Main Security Areas 🔗 
Compute Cloud@Customer security is managed in three areas:
  * **Compute Cloud@Customer Infrastructure:** This is the physical rack hardware that's owned by Oracle, and installed on the customer's premises. Some security-related tasks are performed at this basic level when the system is installed.
This infrastructure layer also includes software for controlling the infrastructure. Access to this layer is restricted to, and closely monitored by authorized Oracle personnel only. You can control when authorized Oracle personnel can access the infrastructure.
  * **Compute Cloud@Customer infrastructure-based resources:** This is where your workloads are created, configured and hosted, and where cloud resources such as compute instances, networks, and storage are managed.
You manage security in this area by configuring the resources (networks, instances and storage) in a secure way. For example, to secure your VCN, you can use network security groups (NSGs) and security lists to secure network access, and use other network security features. You can deploy instances that use user SSH keys for authentication. You can use storage features to secure block, file, and object storage.
  * **Oracle Cloud Infrastructure Identity and Access Management (IAM) service:** This is where you configure compartments, and policies to control who has access to your infrastructure-based resources. 
The IAM service handles authentication – identifies users through confidential information such as username and password, or shared keys. IAM also handles authorization – users can only access the resources with the level of access that has been given to them.
**Attention**
For Compute Cloud@Customer, IAM resources are managed in OCI within your tenancy, and synchronized to Compute Cloud@Customer every ten minutes or so. IAM resources can't be managed on the Compute Cloud@Customer infrastructure.
For information about managing IAM, see [IAM with Identity Domains](https://docs.oracle.com/iaas/Content/Identity/home.htm).


When configured, the preceding security areas enable the following secure environments: 
  * **Survivability of Mission-Critical Workloads:** Compute Cloud@Customer prevents or minimizes the damage caused from accidental and malicious actions taken by internal users or external parties. This is accomplished by security testing of components, checking protocols for vulnerabilities, and verifying software continuity even during security breaches.
  * **Defense in Depth to Secure the Operating Environment:** Compute Cloud@Customer employs multiple, independent, and mutually-reinforcing security controls to help organizations create a secure operating environment for their workloads and data. All levels of the system are protected by an array of security capabilities.
  * **Least-Privilege Access for Services and Users:** Compute Cloud@Customer promotes the use of security policies that ensure that applications, services, and users have access to the capabilities that they need to perform their tasks. However, it's equally important to ensure that access to unnecessary capabilities, services, and interfaces are limited. Users and administrators are confined to their particular areas of concern.
  * **Accountability of Events and Actions:** Compute Cloud@Customer offers detailed audit trails at each layer and controls to help account for resources. This helps an administrator detect and report incidents as they occur (such as a denial of service attack) or after they occurred if it wasn't preventable (through traceability through audit logs to resulting changes to resources). 
  * **Accounting:** Accounting lets administrators track inventories of hardware and cloud resources. From the Oracle Cloud Console, an administrator can retrieve the Compute Cloud@Customer rack serial number.


Was this article helpful?
YesNo


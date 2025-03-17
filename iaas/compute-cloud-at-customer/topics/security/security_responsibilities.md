Updated 2024-10-07
# Security Responsibilities
Security in Compute Cloud@Customer is a shared responsibility between you and Oracle. We use best-in-class security technology and operational processes to secure our cloud services. However, for you to securely run your workloads in OCI and Compute Cloud@Customer, you must know your security and compliance responsibilities.
In general, Oracle provides security of cloud infrastructure and operations, such as cloud operator access controls and infrastructure security patching. You are responsible for securely configuring your cloud resources. 
## Oracle's Responsibilities 🔗 
  * **Physical security:** Oracle is responsible for protecting the global infrastructure of Oracle Cloud Infrastructure to which Compute Cloud@Customer is connected. Oracle is also responsible for ensuring the secure delivery, installation, and maintenance of the Compute Cloud@Customer rack that's installed in your data center.
  * **Tamper indicators:** Oracle is responsible for applying, maintaining, and tracking serialized tamper labels that are applied to all rack access panels and doors. A broken, missing, or damaged label provides a visual indication of a potential hardware breach.
  * **Software Upgrades:** Oracle is responsible for creating upgrades that include bug fixes and feature enhancements. Oracle is also responsible for upgrading Compute Cloud@Customer on regular intervals, during upgrade schedule windows of your choosing.


## Your Responsibilities 🔗 
**Your security responsibilities include the following areas:**
  * **Physical Security:** While Oracle is responsible for the installation and maintenance of the rack, you are responsible for the physical security of the Oracle Compute Cloud@Customer rack in your data center. You must ensure that nobody, other than authorized Oracle personnel, access or open the Compute Cloud@Customer rack.
    * Provide a location for the rack that is in a locked, restricted-access room.
    * Store spare field-replaceable units (FRUs) or customer-replaceable units (CRUs) in a locked cabinet. Restrict access to the locked cabinet to authorized personnel.
    * Limit SSH listener ports to the management and private networks. Use SSH protocol 2 (SSH-2) and FIPS 140-2 approved ciphers.
    * Limit SSH allowed authentication mechanisms. Inherently insecure methods are disabled.
    * Keep hardware activation keys and licenses in a secure location that's easily accessible to the system managers in the case of a system emergency.
  * **Cloud resources:** You are responsible for securing your workloads and securely configuring your cloud resources (such as compute, network, storage, and database).You are responsible for actions in your instances, and day-to-day management of databases and applications that run on your instances.
  * **Access Control:** Limit privileges as much as possible. Users must only be granted the access necessary to perform their work.
  * **Encryption and Confidentiality:** Use encryption keys and secrets to protect your data and connect to secured resources. Rotate these keys regularly.
  * **Information and Data:** You always retain control over information and data. You control how and when this data is used. The cloud provider (Oracle) has zero visibility into customer data, and all data access is under your control by design.
  * **Application Logic and Code:** Regardless of how cloud resources are spun up, you secure and control the your proprietary applications during the entire application life cycle. This includes securing code repositories from malicious misuse or intrusion, application build testing during the development and integration process, ensuring secure production access, and maintaining the security of any connected systems.
  * **Identity and Access:** You are always responsible for all aspects of identity and access management (IAM). This includes authentication and authorization mechanisms, any single sign-on (SSO) access, multifactor authentication (MFA), access keys, certificates, the user creation processes, and password management.
  * **Platform and Resource Configuration:** When cloud resources are created, you control the operating environment. How control is maintained over those environments varies, based on whether instances are server-based or serverless (PaaS). A server-based instance requires more hands-on control over security, including OS and application hardening, maintaining OS and application patches, and so on. Server-based instances in the cloud behave like physical servers, and function as an extension of your data center. For serverless resources, the provider’s control plane gives you access to the setup of the configuration. In all cases, you are responsible for knowing how to configure customer instances in a secure manner.
Additionally, you maintain responsibility for securing everything in your organization that connects with the cloud. This includes: 
    * The on-premises infrastructure stack and user devices.
    * Customer-owned networks and applications.
    * The communication layers that connect your users, both internal and external, to the cloud and to each other.
You also need to set up monitoring and alerting for security threats, incidents, and responses for domains that remain under customer control. 
  * **Software Upgrades:** You are responsible for creating upgrade schedules that enable Oracle to upgrade Compute Cloud@Customer in time frames that are least disruptive to your operations.


Was this article helpful?
YesNo


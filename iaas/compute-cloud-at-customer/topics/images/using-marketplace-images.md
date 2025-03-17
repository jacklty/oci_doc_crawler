Updated 2025-02-05
# Marketplace Images
Learn about Marketplace images that you can use on Compute Cloud@Customer.
The following Marketplace images are available for use on Compute Cloud@Customer:
  * **Oracle Weblogic Server Enterprise Edition UCM**
Oracle WebLogic Server provides the following features: 
    * A modern development platform for building applications
    * A runtime platform for high performance and availability
    * Management tooling for efficient and low-cost operations.
The Oracle WebLogic Server includes an implementation of the Java Platform, Enterprise Edition (Java EE) that provides a standard set of APIs for creating distributed Java applications that can access a wide variety of services, such as databases, messaging services, and connections to external enterprise systems.
Oracle WebLogic Server enables you to deploy mission-critical applications in a robust, secure, highly available, and scalable environment. 
These features enable enterprises to configure clusters of Oracle WebLogic Server instances to distribute load and provide extra capacity in case of hardware or other failures. Security features protect access to services, keep enterprise data secure, and prevent malicious attacks.
  * **Oracle WebLogic Suite UCM**
The Oracle WebLogic Suite for OCI UCM image provides binaries of Oracle WebLogic Server and the Oracle JDK along with the entitlement to create Oracle WebLogic Server domains in Compute Cloud@Customer instances. 
The image can also be used to create an Oracle Forms compute instance which installs everything needed to host most Oracle Forms applications. By default, an Oracle Database is also installed within this instance for storing product metadata. However, you can alternatively elect to connect to Oracle's Database Cloud Service (DBCS) or autonomous Database (ADB) at provisioning time instead, in which case the local database isn't installed. 
Oracle WebLogic Suite includes all entitlements included in the Oracle WebLogic Suite license.


For more information, see [Oracle WebLogic Server Get Started](https://docs.oracle.com/en/middleware/fusion-middleware/weblogic-server/12.2.1.4/index.html).
If you want to use these Marketplace images, Request them from Oracle.
## Requesting a Marketplace Image from Oracle 🔗 
Open a support request to have Oracle load the images on your Compute Cloud@Customer infrastructure. See [Creating a Support Request](https://docs.oracle.com/iaas/Content/GSG/support/create-incident.htm). To access support, sign in to the Oracle Cloud Console as described in [Sign In to the OCI Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm#Signing_In_to_the_Console).
## Using Marketplace Images 🔗 
After the Marketplace image is available on Compute Cloud@Customer, you can create instances using the image. The first time a user creates an instance using a Marketplace image, the user is prompted to sign a user agreement. See [Creating an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance.htm#creating-an-instance "On Compute Cloud@Customer, you can create an instance using the Compute Cloud@Customer Console, CLI, and API.") and [Creating an Instance Configuration](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-configuration.htm#creating-an-instance-configuration "On Compute Cloud@Customer, you can create an instance configuration from an existing instance \(a template instance\) or by entering the individual configuration settings.").
## Marketplace Image Restrictions 🔗 
The following restrictions apply to Marketplace images and to instances created with Marketplace images:
  * Only federated users can accept the user agreement and create instances with the Marketplace image.
  * Market place images can't be deleted or updated 
  * You can't create an image from an Marketplace instance’s boot-volume.
  * You can't export a Marketplace image to Object Storage.
  * You can't create another image from a running instance created with a Market place image.
  * If a Marketplace boot volume is attached as a data volume to another instance, then that instance export isn't allowed.


## Permissible Marketplace Image Administration 🔗 
You can perform the following actions on instances that were created from Marketplace images:
  * You can attach the Marketplace instance boot volume as data volume to another instance.
  * You can clone a Marketplace instance boot volume.
  * You can restore a Marketplace instance boot volume backup to a boot volume.
  * You can restore a Marketplace instance volume-group-backup that includes a Marketplace boot-volume.
  * You can create Marketplace instance boot volume backups using backup policies.
  * You can create volume group that has boot-volume of Marketplace instance.


Was this article helpful?
YesNo


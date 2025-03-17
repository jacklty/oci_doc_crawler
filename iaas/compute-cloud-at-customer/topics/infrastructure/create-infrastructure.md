Updated 2024-05-07
# Creating a Compute Cloud@Customer Infrastructure in OCI
Create a Compute Cloud@Customer infrastructure in Oracle Cloud Infrastructure (OCI) to communicate with the corresponding infrastructure in the data center.
Before creating an infrastructure, ensure that the following tenancy setup has been completed. See [Preparing Your Tenancy](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/preparing-your-tenancy.htm#preparing-your-tenancy "Before the Compute Cloud@Customer infrastructure is connected to Oracle Cloud Infrastructure, the tenancy administrator must set up compartments, create policies, and configure a virtual cloud network. This setup is used to connect the Compute Cloud@Customer infrastructure to Oracle Cloud Infrastructure.").
  * A compartment is set up to host the infrastructure definitions.
  * A VCN and subnet are set up as required by the infrastructure.
  * IAM policies are set up to provide appropriate user and resource access to the infrastructure compartment.


Also ensure that an upgrade schedule for this infrastructure is defined. If you don't set up an upgrade schedule, Oracle can upgrade the infrastructure at any time. See [Creating a Compute Cloud@Customer Upgrade Schedule](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/create-upgrade-schedule.htm#create-upgrade-schedule "Create an upgrade schedule to allow Oracle to upgrade Compute Cloud@Customer hardware and software during defined time periods. After the upgrade schedule is created, attach the schedule to the infrastructures you want upgraded with the schedule.").
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/create-infrastructure.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/create-infrastructure.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/create-infrastructure.htm)


  * To create an infrastructure, follow these steps:
    1. In the Oracle Cloud Console, open the navigation menu, click **Hybrid** , and then click **Oracle Compute Cloud@Customer**.
    2. Click **Infrastructures**.
    3. Select the compartment that you want to create the infrastructure in.
    4. Click **Create infrastructure**.
    5. Define the following infrastructure parameters. Avoid entering confidential information.
       * **Display name** : The name shown when listing infrastructures in the Oracle Cloud Console. This name must match the System Name supplied to Oracle in the [Networking Checklist](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/networking-checklist.htm#initial-installation-checklist "This section helps you plan for the configuration information that's required when Oracle installs the Oracle Compute Cloud@Customer rack in your data center.").
       * **Description** : (Optional) Information about the infrastructure to distinguish it from others.
       * **Compartment** : The compartment that you want to create the infrastructure in. This value can't be edited later.
       * **Networking** : The VCN and subnet for this infrastructure. This value can't be edited later.
       * **Upgrade schedule** : (Optional) The upgrade schedule associated with this infrastructure, which defines when it may be upgraded.
    6. Click **Show advanced options** to add tags to the infrastructure if required.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm#Resource_Tags).
    7. Click **Create**.
**What's Next?**
Connect the Compute Cloud@Customer infrastructure to your OCI tenancy. See [Connecting a Compute Cloud@Customer Infrastructure to OCI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/connecting.htm#connecting "The Compute Cloud@Customer infrastructure in the data center needs to be connected to Oracle Cloud Infrastructure \(OCI\) before it can be used. This task involves a bootstrap process during which a secure connection is established.").
  * Use the [ccc infrastructure create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ccc/infrastructure/create.html) command and required parameters to create an infrastructure:
Command
CopyTry It
```
oci ccc infrastructure create --compartment-id <compartment ocid> --display-name <Descriptive name> --subnet-id <subnet to connect infrastructure to>... [OPTIONS]
```

Avoid entering confidential information.
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**What's Next?**
Connect the Compute Cloud@Customer infrastructure to your OCI tenancy. See [Connecting a Compute Cloud@Customer Infrastructure to OCI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/connecting.htm#connecting "The Compute Cloud@Customer infrastructure in the data center needs to be connected to Oracle Cloud Infrastructure \(OCI\) before it can be used. This task involves a bootstrap process during which a secure connection is established.").
  * Use the [CreateCccInfrastructure](https://docs.oracle.com/iaas/api/#/en/compute-cloud-at-customer/latest/CccInfrastructure/CreateCccInfrastructure) operation to create a Compute Cloud@Customer infrastructure.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).
**What's Next?**
Connect the Compute Cloud@Customer infrastructure to your OCI tenancy. See [Connecting a Compute Cloud@Customer Infrastructure to OCI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/connecting.htm#connecting "The Compute Cloud@Customer infrastructure in the data center needs to be connected to Oracle Cloud Infrastructure \(OCI\) before it can be used. This task involves a bootstrap process during which a secure connection is established.").


Was this article helpful?
YesNo


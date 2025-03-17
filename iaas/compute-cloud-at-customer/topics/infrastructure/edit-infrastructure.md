Updated 2024-01-18
# Editing a Compute Cloud@Customer Infrastructure in OCI
Edit the display name, description, or tags of a Compute Cloud@Customer infrastructure, or associate a new upgrade schedule with the infrastructure. 
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/edit-infrastructure.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/edit-infrastructure.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/edit-infrastructure.htm)


  *     1. In the Oracle Cloud Console, open the navigation menu, click **Hybrid** , and then click **Oracle Compute Cloud@Customer**.
    2. Click **Infrastructures**.
    3. Click the name of the infrastructure that you want to edit. If you don't see the infrastructure that you want, you might need to change compartments.
    4. Click **Edit**.
    5. Update the infrastructure parameters. Avoid entering confidential information. For a description of the parameters, see [Creating a Compute Cloud@Customer Infrastructure in OCI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/infrastructure/create-infrastructure.htm#create-infrastructure "Create a Compute Cloud@Customer infrastructure in Oracle Cloud Infrastructure \(OCI\) to communicate with the corresponding infrastructure in the data center.").
    6. Click **Save**.
  * Use the [ccc infrastructure update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ccc/infrastructure/update.html) command and required parameters to update an infrastructure:
Command
CopyTry It
```
oci ccc infrastructure update --infrastructure-id <infrastructure ocid> ... [OPTIONS]
```

Avoid entering confidential information.
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateCccInfrastructure](https://docs.oracle.com/iaas/api/#/en/compute-cloud-at-customer/latest/CccInfrastructure/UpdateCccInfrastructure) operation to update a Compute Cloud@Customer infrastructure.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


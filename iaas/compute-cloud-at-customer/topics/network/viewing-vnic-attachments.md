Updated 2024-08-06
# Viewing VNICs and VNIC Attachments
On Compute Cloud@Customer, you can view VNIC attachments and for a particular instance and view VNIC details.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-vnic-attachments.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-vnic-attachments.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-vnic-attachments.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    2. At the top of the page, select the compartment that contains the instance in which you want to view VNIC attachments.
    3. Click the name of the instance.
The instance details page is displayed.
    4. Under **Resources** , click **Attached VNICs**.
The list of attached VNICs for that instance is displayed.
    5. To view the details page for the VNIC, click the name of the attached VNIC.
  * Use the [oci compute vnic-attachment list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/vnic-attachment/list.html) command and required parameters to list the VNIC attachments in the specified compartment. A VNIC attachment resides in the same compartment as the attached instance.
Copy
```
oci compute vnic-attachment list [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListVnicAttachments](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VnicAttachment/ListVnicAttachments) operation to list the VNIC attachments in the specified compartment. A VNIC attachment resides in the same compartment as the attached instance.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


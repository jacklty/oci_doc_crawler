Updated 2024-04-02
# Viewing Security Lists
On Compute Cloud@Customer, you can view security lists that are associated with a VCN.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-a-security-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-a-security-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-a-security-list.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN in which you want to create a subnet.
    3. Click the name of the VCN for which you want to view security lists. 
The VCN details page is displayed.
    4. Under **Resources** , click **Security Lists**. 
The list of security lists is displayed.
    5. Click the name of the security list to view its ingress and egress rules.
  * Use the [oci network security-list list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/security-list/list.html) command and required parameters to list security lists.
If you specify both the VCN OCID and the compartment OCID arguments, all security lists that belong to the specified VCN and are in the specified compartment are listed.
Copy
```
oci network security-list list --compartment-id ocid1.compartment.unique_ID --vcn-id ocid1.vcn.unique_ID [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListSecurityLists](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/ListSecurityLists) operation to list security lists.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


Updated 2024-04-02
# Deleting a Security List
On Compute Cloud@Customer, you can delete a security list as long as it isn't associated with a subnet. You can't delete a VCN default security list.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-security-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-security-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/deleting-a-security-list.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN in which you want to create a subnet.
    3. Click the name of the VCN for which you want to delete a security list. 
The VCN details page is displayed.
    4. Under **Resources** , click **Security Lists**.
    5. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) for the security list that you want to delete, then **Delete**.
    6. Confirm the deletion.
  * Use the [oci network security-list delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/security-list/delete.html) command and required parameters to delete the specified security list, but only if it’s not associated with a subnet.
Copy
```
oci network security-list delete [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/DeleteSecurityList) operation to delete the specified security list, but only if it’s not associated with a subnet.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


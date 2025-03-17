Updated 2024-04-02
# Updating a Security List
On Compute Cloud@Customer, you can edit the name of the security list and add, edit, or delete rules or tags in any security list, including the default security list.
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-security-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-security-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-a-security-list.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN in which you want to create a subnet.
    3. Click the name of the VCN for which you want to update a security list. 
The VCN details page is displayed.
    4. Under **Resources** , click **Security Lists**.
    5. For the security list that you want to update, do one of the following:
       * Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Edit** to open the **Edit Security List** dialog box. Update rules in the **Allow Rules for Ingress** and **Allow Rules for Egress** sections. 
To delete a rule, click the trash can icon. To add a rule, click **+New Rule**. You can also update the security list name and tags. Click **Save**.
       * Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **View Details** to open the security list details page.
         * Click **Edit** to open the Edit Security List dialog box.
         * To edit only the rules, scroll to the **Resources** section and click either **Ingress Rules** or **Egress Rules**. 
To create a new rule, click **Create Security Rule**. To update a rule, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) for that rule and then click **Edit**. 
To delete a rule, click the Actions menu and then click **Delete**.
  * Use the [oci network security-list update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/security-list/update.html) command and required parameters to update the specified security list’s display name or rules. Avoid entering confidential information.
Copy
```
oci network security-list update --security-list-id <security_list_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/UpdateSecurityList) operation to update the specified security list’s display name or rules.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


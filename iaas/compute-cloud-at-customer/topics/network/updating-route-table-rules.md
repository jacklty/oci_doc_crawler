Updated 2024-04-02
# Updating Route Table Rules
On Compute Cloud@Customer, you can change the name of a route table and add, edit, or delete rules in a route table.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-route-table-rules.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-route-table-rules.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/updating-route-table-rules.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN in which you want to create a subnet.
    3. Click the name of the VCN for which you want to update the route table. 
The VCN details page is displayed.
    4. Under **Resources** , click **Route Tables**.
    5. Click the name of the route table that you want to update.
    6. Edit the route rules:
       * To change the name of the route table, click **Edit** , change the name in the dialog box, and click **Save Changes**.
       * To create a route rule, click **Add Route Rules** and enter the information.
       * To edit an existing rule, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) for that rule, and then click **Edit**.
       * To delete a rule, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) for that rule, and then click **Delete**.
  * Use the [oci network route-table update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/route-table/update.html) command and required parameters to update the specified route table’s display name or route rules. Avoid entering confidential information.
Copy
```
oci network route-table update --rt-id <route_table_OCID> --route-rules <options_to_change> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/UpdateRouteTable) operation to update the specified route table’s display name or route rules. Avoid entering confidential information.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


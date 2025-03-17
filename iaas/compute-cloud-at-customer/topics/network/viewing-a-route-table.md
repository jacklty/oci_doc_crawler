Updated 2024-04-02
# Viewing a Route Table
On Compute Cloud@Customer, you can list the route tables in the specified VCN.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-a-route-table.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-a-route-table.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-a-route-table.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN in which you want to create a subnet.
    3. Click the name of the VCN for which you want to view route tables. 
The VCN details page is displayed.
    4. Under **Resources** , click **Route Tables**. 
The list of route tables is displayed.
    5. Click the name of the route table to view its route rules.
  * Use the [oci network route-table list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/route-table/list.html) command and required parameters to list the route tables in the specified VCN and specified compartment. If the VCN ID is not provided, then the list includes the route tables from all VCNs in the specified compartment. The response includes the default route table that automatically comes with each VCN in the specified compartment, plus any route tables you’ve created.
Copy
```
oci network route-table list --compartment-id ocid1.compartment.unique_ID --vcn-id ocid1.vcn.unique_ID [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListRoutTables](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/ListRouteTables) operation to list the route tables in the specified VCN.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


Updated 2024-12-16
# Creating a Route Table
On Compute Cloud@Customer, route rules are required to send traffic outside the VCN. If you don't need to send traffic outside the VCN, you can use the default route table that was created when the VCN was created. The default route table has no rules.
Each route rule specifies a destination CIDR block and the target (the next hop) for any traffic that matches that CIDR. Before you can create a rule, you must create a target. 
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-route-table.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-route-table.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-route-table.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN in which you want to create a subnet.
    3. Click the name of the VCN for which you want to create a route table. 
The VCN details page is displayed.
    4. Under **Resources** , click **Route Tables**.
    5. Click **Create Route Table**. 
    6. Enter the required information:
       * **Name:** Specify a user-friendly name for the route table. The name doesn't have to be unique, and you can change it later. Avoid entering confidential information
       * **Create in Compartment:** Select the compartment where you want to create the route table. You're not required to create the route table in the same compartment as the VCN. 
    7. To add a rule, click **+New Rule** , and enter the following information:
       * **Target Type:** Select from the list.
       * **CIDR Block** : The destination CIDR block for the traffic. A value of 0.0.0.0/0 means that all non-intra-VCN traffic that is not already covered by other rules in the route table goes to the target specified in this rule.
       * **Target:** The label for this value is the value that you selected for Target Type. Click the arrow and select the target. You might need to change the compartment just above the arrow.
       * **Description:** An optional description of the rule.
    8. **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    9. Click **Create Route Table**.
The details page of the new route table is displayed. You can specify this route table when creating or updating a subnet.
  * Use the [oci network route-table create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/route-table/create.html) command and required parameters to create a new route table for the specified VCN. In the request you must also include at least one route rule for the new route table.
Copy
```
oci network route-table create --compartment-id compartment_OCID --vcn-id vcn_OCID --route-rules route_rules_json [OPTIONS]
```

The --route-rules option includes the collection of rules used for routing destination IPs to network devices. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using the `file://path/to/file` syntax.
The [--generate-param-json-input](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/oci.html#cmdoption-generate-param-json-input) option can be used to generate an example of the JSON which must be provided. We recommend storing this example in a file, modifying it as needed and then passing it back in through the `file://` syntax.
Example:
```
'[{"cidrBlock":"0.0.0.0/0","networkEntityId":"ocid1.internetgateway.oc1.phx.UniqueID"}]'
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateRouteTable](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RouteTable/CreateRouteTable) operation to create a new route table for the specified VCN.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


Updated 2024-08-06
# Creating a Set of DHCP Options
On Compute Cloud@Customer, you can create a set of DHCP options.
For conceptual information, see:
  * [Name Resolution](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/name-resolution.htm#name-resolution "On Compute Cloud@Customer, the Domain Name System \(DNS\) translates human-readable domain names to machine-readable IP addresses.")
  * [Working with DHCP Options](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/working-with-dhcp-options.htm#working-with-dhcp-options "On Compute Cloud@Customer, when you create a subnet, you can specify the set of DHCP options for the subnet. A set of DHCP options is a resource with an OCID. If you don't specify a set of DHCP options, the default set for the VCN is used.")


Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-set-of-dhcp-options.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-set-of-dhcp-options.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-set-of-dhcp-options.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN.
    3. Click the name of the VCN for which you want to create a set of DHCP options. 
The VCN details page is displayed.
    4. Under **Resources** , click **DHCP Options**.
    5. Click **Create DHCP Options**.
    6. Enter the following information:
       * **Name** : A descriptive name for the set of options. The name doesn't have to be unique, and you can change it later.
       * **Create in Compartment:** The compartment where you want to create the set of DHCP options.
       * **DNS Type** : If you want instances in the subnet to resolve internet hostnames and hostnames of instances in the VCN, select Internet and VCN Resolver. To use a DNS server of your choice, select Custom Resolver and then enter the IP address of the DNS server. You can enter up to three DNS server IP addresses. 
       * **Search Domain** : If you want instances in the subnet to append a particular search domain when resolving DNS queries, enter that domain here. Note that the Networking service automatically sets the search domain option in certain situations. 
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    7. Click **Create DHCP Options**.
You can specify this set of options when creating or updating a subnet.
  * Use the [oci network dhcp-options create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/dhcp-options/create.html) command and required parameters to create a new set of DHCP options for the specified VCN.
Copy
```
oci network dhcp-options create --compartment-id <compartment_OCID> --vcn-id <vcn_OCID> --options <JSON_formatted_values> [OPTIONS]
```

--options <JSON_formatted_values> is a set of DHCP options. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using the `file://path/to/file` syntax.
The [--generate-param-json-input](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/oci.html#cmdoption-generate-param-json-input) option can be used to generate an example of the JSON which must be provided. We recommend storing this example in a file, modifying it as needed and then passing it back in using the `file://` syntax.
Example:
```
'[{"type": "DomainNameServer", "customDnsServers": ["202.44.61.9"], "serverType": "CustomDnsServer"}]'
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateDhcpOptions](https://docs.oracle.com/iaas/api/#/en/iaas/latest/DhcpOptions/CreateDhcpOptions) operation to create a new set of DHCP options for the specified VCN.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


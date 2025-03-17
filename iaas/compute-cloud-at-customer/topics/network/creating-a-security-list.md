Updated 2024-08-06
# Creating a Security List
On Compute Cloud@Customer, you can create a security list for a VCN.
Before you create a security list, view the security rules that are already defined in the default security list and any other security list for this VCN. See [Viewing Security Lists](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/viewing-a-security-list.htm#viewing-a-security-list "On Compute Cloud@Customer, you can view security lists that are associated with a VCN.").
A security list must have at least one rule. A security list isn't required to have both ingress and egress rules.
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-security-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-security-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-security-list.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN in which you want to create a subnet.
    3. Click the name of the VCN for which you want to create a security list. 
The VCN details page is displayed.
    4. Under **Resources** , click **Security Lists**.
    5. Click **Create Security List**. 
    6. In the Create Security List dialog box, enter the following information:
       * **Name:** Provide a descriptive name for the security list. The name doesn't have to be unique. Avoid entering confidential information. (The name can't be changed later in the Console but can changed with the CLI).
       * **Create in Compartment:** Select the compartment where you want to create the security list.
    7. Add at least one rule.
To add one or more ingress rules, click **+New Rule** in the **Allow Rules for Ingress** box. Enter the following information:
       * **Stateless:** If you want the new rule to be stateless, check this box. By default, security list rules are stateful and apply to both a request and its coordinated response.
       * **CIDR** : The CIDR block for the ingress or egress traffic.
       * **IP Protocol:** The rule can apply to all IP protocols, or choices such as ICMP, TCP, or UDP. Select the protocol from the drop-down list.
         * **Port Range** : For some protocols, such as TCP or UDP, you can supply a source port range and destination port range.
         * **Parameter Type and Code** : For ICMP, you can select a parameter type and corresponding parameter code.
       * **Description:** An optional description of the rule.
    8. **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    9. Click **Create Security List**.
The details page of the new security list is displayed. You can specify this security list when creating or updating a subnet.
  * Use the [oci network security-list create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/security-list/create.html) command and required parameters to create a new security list for the specified VCN.
Copy
```
oci network security-list create --compartment-id <compartment_OCID> --vcn-id <vcn_OCID> --ingress-security-rules <ingress_rules> --egress-security-rules <egress_rules> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**Procedure**
    1. Gather the information you need to run the command:
       * The OCID of the compartment where you want to create this security list (`oci iam compartment list`)
       * The OCID of the VCN for this security list (`oci network vcn list                --compartment-id **_compartment_OCID_**`)
    2. Construct arguments for the `--ingress-security-rules` and `--egress-security-rules` options.
Security rules are in JSON format. To see how to format a rule, use the following command:
```
oci network security-list create --generate-param-json-input ingress-security-rules > ingress.json
```

Use the same command with `egress-security-rules`.
Ingress and egress security rules are the same except that ingress rules have `source` and `sourceType` properties while egress rules have `destination` and `destinationType` properties.
The value of the `protocol` property is `all` or one of the following numbers: 1 for ICMP, 6 for TCP, or 17 for UDP.
Or, you can `list` or `get` the default security list or another security list and copy the values of the `egress-security-rules` and `ingress-security-rules` properties.
Put the information for rules for this new security list in the appropriate places in the format, or replace the information in the rules that you copied.
The value of both rules options is either a string between single quotation marks or a file specified as `file://**_path_to_file_**.json`.
Egress and ingress rules must be in a list. If the list of egress rules or the list of ingress rules has only one item, that single rule must be enclosed in square brackets just as multiple rules would be. See the command in the next step for an example showing only one ingress rule.
Both egress rules and ingress rules must be specified. See the command in the next step for an example showing no egress rules.
    3. Run the security list create command.
Syntax:
Example:
```
$ oci network security-list create --compartment-id ocid1.compartment.**_unique_ID_** \
--vcn-id ocid1.vcn.**_unique_ID_** --display-name "Limited Port Range" \
--egress-security-rules [] \
--ingress-security-rules '[{"source": "10.0.2.0/24", "protocol": "6", "isStateless": true, \
"tcpOptions": {"destinationPortRange": {"max": 1521, "min": 1521}, \
"sourcePortRange": {"max": 1521, "min": 1521}}}]'
{
 "data": {
  "compartment-id": "ocid1.compartment.**_unique_ID_**",
  "defined-tags": {},
  "display-name": "Limited Port Range",
  "egress-security-rules": [],
  "freeform-tags": {},
  "id": "ocid1.securitylist.**_unique_ID_**",
  "ingress-security-rules": [
   {
    "description": null,
    "icmp-options": null,
    "is-stateless": true,
    "protocol": "6",
    "source": "10.0.2.0/24",
    "source-type": "CIDR_BLOCK",
    "tcp-options": {
     "destination-port-range": {
      "max": 1521,
      "min": 1521
     },
     "source-port-range": {
      "max": 1521,
      "min": 1521
     }
    },
    "udp-options": null
   }
  ],
  "lifecycle-state": "PROVISIONING",
  "time-created": "**_unique_ID_**",
  "vcn-id": "ocid1.vcn.**_unique_ID_**"
 },
 "etag": "**_unique_ID_**"
}
```

  * Use the [CreateSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/CreateSecurityList) operation to create a new security list for the specified VCN.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


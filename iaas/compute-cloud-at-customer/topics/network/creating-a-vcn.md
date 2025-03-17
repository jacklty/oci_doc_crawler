Updated 2024-08-06
# Creating a VCN
On Compute Cloud@Customer, a _virtual cloud network_ (VCN) a virtual, private network that closely resembles a traditional network. VCNs can be further divided into IP subnets. VCNs can communicate with each other through various types of gateways, each type intended for a particular purpose. 
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-vcn.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-vcn.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-vcn.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. Click **Create Virtual Cloud Network**.
    3. Enter the following information:
       * **Name:** Enter a descriptive name for the VCN.
       * **Compartment:** Select the compartment in which to create the VCN.
       * **CIDR Block:** Specify which CIDR range can be used within the VCN.
       * **DNS:** If you check the box to use DNS host names in this VCN, then you can either enter a DNS label or leave the field blank to let the system generate a label for you. The first character of the label must be a letter. Only use letters and numbers. Up to 15 characters are allowed.
    4. **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    5. Click **Create Virtual Cloud Network**.
The details page of the new VCN is displayed.
  * Use the [oci network vcn create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/create.html) command and required parameters to create a VCN.
Copy
```
oci network vcn create --compartment-id compartment_OCID --cidr-block 10.0.0.0/16 --dns-label vcn1 --display-name VCN1 [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**Procedure**
    1. Gather the information that you need to run the command:
       * Compartment OCID (`oci iam compartment list               --compartment-id-in-subtree true`)
    2. Enter the `vcn create` command using at least the compartment OCID and CIDR block options.
To use DNS host names in the VCN, include the DNS label in the create command. It can't be added later.
Optionally, set a descriptive name for the VCN.
```
$ oci network vcn create --compartment-id <compartment_OCID> \
--cidr-blocks '["<cidr-block_eg-10.0.0.0/16>"]' --dns-label <dns_label> --display-name <display_name>
{
 "data": {
  "cidr-block": "10.0.0.0/16",
  "cidr-blocks": [
   "10.0.0.0/16"
  ],
  "compartment-id": "ocid1.compartment.**_unique_ID_**",
  "default-dhcp-options-id": "ocid1.dhcpoptions.**_unique_ID_**",
  "default-route-table-id": "ocid1.routetable.**_unique_ID_**",
  "default-security-list-id": "ocid1.security_list.**_unique_ID_**",
  "defined-tags": {},
  "display-name": "VCN1",
  "dns-label": "vcn1",
  "freeform-tags": {},
  "id": "ocid1.vcn.**_unique_ID_**",
  "ipv6-cidr-block": null,
  "ipv6-private-cidr-block": null,
  "lifecycle-state": "PROVISIONING",
  "time-created": "2023-04-27T04:34:58.722835+00:00",
  "vcn-domain-name": "vcn1.oraclevcn.com"
 },
 "etag": "**_unique_ID_**"
}
```

  * Use the [CreateVCN](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/CreateVcn) operation to create a VCN.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


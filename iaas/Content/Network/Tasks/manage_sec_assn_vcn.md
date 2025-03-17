Updated 2025-01-15
# Adding Security Attributes to a VCN
Use Zero Trust Packet Routing with an existing virtual cloud network (VCN). 
You can use Zero Trust Packet Routing (ZPR) along with or in place of network security groups to control network access to OCI **resources** by applying security attributes to them and creating ZPR policies to control communication among them. For more information, see [Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). 
**Caution** If an endpoint has a ZPR security attribute, traffic to the endpoint must satisfy ZPR rules as well as all NSG and security list rules. For example, if you're already using NSGs and you apply a security attribute to an endpoint, as soon as the attribute is applied, all traffic to the endpoint is blocked. From then onward, a ZPR policy must allow traffic to the endpoint.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/manage_sec_assn_vcn.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/manage_sec_assn_vcn.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/manage_sec_assn_vcn.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN that you want to use with Zero Trust Packet Routing. You might need to change the compartment to find the VCN that you want.
    3. Click the **Security attributes** tab to view or edit the existing security associations. Or click **Add security attributes** to add new ones.
  * Use the [network vcn create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/create.html) command and parameters shown to add security attributes when you create a VCN:
Command
CopyTry It
```
oci network vcn create --compartment-id compartment_id [. . .] --security-attributes securityattributes [OPTIONS]
```

Use the [network vcn update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/update.html) command and parameters shown to add security attributes to an existing VCN:
Command
CopyTry It
```
oci network vcn update --vcn-id ocid [. . .] --security-attributes securityattributes [OPTIONS] 
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/CreateVcn) operation to add security attributes when you create a VCN, and use the securityAttributes attribute.
Run the [UpdateVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/UpdateVcn) operation to add security attributes when you update a VCN, and use the securityAttributes attribute.


Was this article helpful?
YesNo


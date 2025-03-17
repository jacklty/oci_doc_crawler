Updated 2025-01-17
# Configuring Security Rules to Use an LPG
Update a security list in a Virtual Cloud Network (VCN) to include a new rule that allows traffic destined for the other VCN's CIDR to flow through a local peering gateway (LPG). 
Each administrator can perform this task before or after the connection is established. 
**Prerequisite:** Each administrator must have the CIDR block or specific subnets for the other VCN. In general, use the same CIDR block you used in the route table rule in [Task E: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Step4). 
Before you begin, decide which subnets in the VCN need to communicate with the other VCN. Update the security list for each of those subnets to include rules to allow the intended egress or ingress traffic specifically with the CIDR block or subnet of the other VCN.
What rules should you add? 
  * _Ingress rules_ for the types of traffic you want to allow from the other VCN, specifically from the VCN's CIDR or specific subnets.
  * An _egress rule_ to allow outgoing traffic from the VCN to the other VCN. If the subnet already has a broad egress rule for all types of protocols to all destinations (0.0.0.0/0), then you don't need to add a special one for the other VCN.


For more information about security rules, see [Security Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/give-lpg-sl.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/give-lpg-sl.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/give-lpg-sl.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the name of the VCN that you're interested in. 
    3. Under **Resources** , select **Security Lists**. 
    4. Select the security list you're interested in. 
    5. Under **Resources** , select either **Ingress Rules** or **Egress Rules** depending on the type of rule you want to work with. 
    6. To add a rule, select **Add Ingress Rule** or **Add Egress Rule**.
**Example**
You want to add a stateful rule that enables ingress HTTPS (port 443) traffic from the other VCN's CIDR. Here is the basic information that you would enter in the **Add Ingress Rule** panel:: 
       * **Stateless:** Leave this checkbox unselected.
       * **Source Type:** Leave as CIDR.
       * **Source CIDR:** Enter the same CIDR block that the route rules use (see [Configuring VCN Route Tables to Use an LPG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/give-lpg-rt.htm#give-lpg-rt "Update a Virtual Cloud Network \(VCN\) route table to include a new rule that directs traffic destined for the other VCN's CIDR to flow through the local peering gateway \(LPG\).")).
       * **IP Protocol:** Leave as TCP. 
       * **Source Port Range:** Leave as All.
       * **Destination Port Range:** Enter 443.
       * **Description:** An optional description of the rule.
    7. To delete an existing rule, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Remove**.
    8. If you wanted to edit an existing rule, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Edit**.
  * Use the [network security-list update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/security-list/update.html) command and required parameters to update the rules used in a particular security list:
Command
CopyTry It
```
oci network security-list update --security-list-id securitylist-ocid ... [--egress-security-rules | --ingress-security-rules] rules [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/UpdateSecurityList) operation to update the rules used in a particular security list.


Was this article helpful?
YesNo


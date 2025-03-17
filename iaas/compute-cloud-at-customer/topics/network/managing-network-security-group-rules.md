Updated 2024-04-02
# Managing Network Security Group Rules
On Compute Cloud@Customer, you can add, update, and remove NSG rules.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/managing-network-security-group-rules.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/managing-network-security-group-rules.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/managing-network-security-group-rules.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Virtual Cloud Networks**.
    2. At the top of the page, select the compartment that contains the VCN in which you want to create a subnet.
    3. Click the name of the VCN for which you want to manage rules in an NSG. 
The VCN details page is displayed.
    4. Under **Resources** , click **Network Security Groups**.
    5. In the list of NSGs, click the name of the NSG for which you want to manage rules. The NSG details page is displayed.
    6. Under **Resources** , click **Security Rules**.
    7. You can add, edit, and delete rules.
       * To add a rule, click **Create Security Rules**. To add one or more ingress rules, click +**New Rule** in the **Allow Rules for Ingress** box. To add one or more egress rules, click **+New Rule** in the **Allow Rules for Egress** box. Enter the following information:
         * **Stateless:** If you want the new rule to be stateless, check this box. By default, security list rules are stateful and apply to both a request and its coordinated response. 
         * **CIDR** : The CIDR block for the ingress or egress traffic.
         * **IP Protocol:** The rule can apply to all IP protocols, or choices such as ICMP, TCP, or UDP. Select the protocol from the drop-down list.
           * **Port Range** : For some protocols, such as TCP or UDP, you can supply a source port range and destination port range.
           * **Parameter Type and Code** : For ICMP, you can select a parameter type and corresponding parameter code.
         * **Description:** An optional description of the rule. Avoid entering confidential information.
       * To edit a rule, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) for the Egress or Ingress rule, click **Edit** , make the necessary changes, and then click **Update**.
       * To delete a rule, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) for the Egress or Ingress rule, click **Remove** , and then click **Confirm**. While you're editing a rule, click the trash can icon to delete the rule.
  * Use these CLI commands to manage NSG rules:
    * Use the [oci network nsg rules add](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/rules/add.html) command and required parameters to add one or more security rules to the specified network security group.
Copy
```
oci network nsg rules add [OPTIONS]
```

    * Use the [oci network nsg rules list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/rules/list.html) command and required parameters to list the security rules in the specified network security group.
Copy
```
oci network nsg rules list [OPTIONS]
```

    * Use the [oci network nsg rules update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/rules/update.html) command and required parameters to update one or more security rules in the specified network security group.
Copy
```
oci network nsg rules update [OPTIONS]
```

    * Use the [oci network nsg rules remove](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/rules/remove.html) command and required parameters to remove one or more security rules from the specified network security group.
Copy
```
oci network nsg rules remove [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [AddNetworkSecurityGroupSecurityRules](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityRule/AddNetworkSecurityGroupSecurityRules) operation to add one or more security rules to the specified network security group.
Use the [ListNetworkSecurityGroupSecurityRules](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityRule/ListNetworkSecurityGroupSecurityRules) operation to list the security rules in the specified network security group. 
Use the [UpdateNetworkSecurityGroupSecurityRules](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityRule/UpdateNetworkSecurityGroupSecurityRules) operation to update one or more security rules in the specified network security group.
Use the [RemoveNetworkSecurityGroupSecurityRules](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityRule/RemoveNetworkSecurityGroupSecurityRules) operation to remove one or more security rules from the specified network security group.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


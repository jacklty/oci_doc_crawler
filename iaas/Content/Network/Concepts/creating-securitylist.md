Updated 2025-01-15
# Creating a Security List
Create a security list in a Virtual Cloud Network (VCN).
A security list is a virtual firewall used to control traffic at the packet level. For important information about how security lists work, see [Security Lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists). 
A security list uses _security rules_. For important information about how security rules work, and a general comparison of security lists and network security groups (an optional virtual firewall), see [Security Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules). 
When you create a subnet, you must associate at least one security list with it. It can be either the VCN's default security list or another security list that you already created (for the maximum number, see [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm)). You can [change which security lists the subnet uses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/change-use-securitylist.htm#change-rules-securitylist "Change which security lists are used in a particular subnet in a virtual cloud network \(VCN\).") at any time.
You can optionally assign a friendly name to the security list during creation. It doesn't have to be unique, and you can change it later. Oracle automatically assigns the security list a unique identifier called an Oracle Cloud ID (OCID). For more information, see [Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/creating-securitylist.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/creating-securitylist.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/creating-securitylist.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
    3. Under **Resources** , click **Security Lists**.
    4. Click **Create Security List**. 
    5. Enter the following information:
       * **Name:** A descriptive name for the security list. The name doesn't have to be unique, and it can' be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
       * **Create In Compartment:** The compartment where you want to create the security list, if different from the compartment you're currently working in. 
    6. Add either an ingress rule or an egress rule (for examples of rules, see [Networking Scenarios](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarios.htm#networking_scenarios)):
       * Click either **+ Another Ingress Rule** or **+ Another Egress Rule**.
       * Choose whether the rule is stateful or stateless (see [Stateful Versus Stateless Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful)). By default, rules are stateful unless you specify otherwise.
       * Enter either the source CIDR (for ingress) or destination CIDR (for egress). For example, use 0.0.0.0/0 to indicate all IP addresses. Other typical CIDRs you might specify in a rule are the CIDR block for your on-premises network, or for a particular subnet. If you're setting up a security list rule to allow traffic with a **service gateway** , instead see [Task 3: (Optional) Update security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#task_update_security_list). For more information about CIDR notation, see [RFC1817](https://datatracker.ietf.org/doc/html/rfc1817) and [RFC1519](https://datatracker.ietf.org/doc/html/rfc1519).
       * Select the IP protocol (for example, TCP, UDP, or ICMP) or select **All Protocols**. 
       * Enter more details depending on the protocol:
         * If you chose TCP or UDP, enter a source port range and destination port range. You can enter **All** to cover all ports. If you want to allow a specific [port](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml), enter the port number (for example, 22 for SSH or 3389 for RDP) or a port range (for example, 20–22). 
         * If you chose ICMP, you can enter **All** to cover all types and codes. If you want to allow a specific [ICMP type](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml), enter the type and an optional code separated by a comma (for example, 3,4). If the type has multiple codes that you want to allow, create a separate rule for each code.
       * Enter an optional description of the rule to help manage your security list rules.
    7. Repeat the preceding step for each rule you want to add to the list.
    8. Optionally, click **Show Tagging Options** , and assign tags to the security list. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    9. When you're done, click **Create Security List**.
The security list is created and then displayed on the **Security Lists** page in the compartment that you chose. You can now specify this security list when creating or updating a subnet. 
When you view all the rules in a security list, notice that any stateless rules in the list are shown above any stateful rules. Stateless rules in the list take precedence over stateful rules. In other words, if there's traffic that matches both a stateless rule and a stateful rule across all the security lists associated with the subnet, the stateless rule takes precedence and the connection isn't tracked.
  * Use the [network security-list create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/security-list/create.html) command and required parameters to create a security list:
Command
CopyTry It
```
oci network security-list create --compartment-id compartment-ocid --vcn-id vcn-ocid [--egress-security-rules | --ingress-security-rules] rules... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateSecurityList](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/CreateSecurityList) operation to create a security list.


Was this article helpful?
YesNo


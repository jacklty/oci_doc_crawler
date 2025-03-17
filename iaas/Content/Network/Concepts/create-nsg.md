Updated 2025-01-15
# Creating an NSG
Create a network security group (NSG) in a Virtual Cloud Network (VCN).
Each VCN comes with a [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default) that has default security rules in it to enable basic connectivity. However, a VCN has no default NSG. 
When you create an NSG, it's initially empty, without any security rules or VNICs. If you're using the Console, you can add security rules to the NSG during creation. Become familiar with the [parts of security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#sec_rules_parts).
You can optionally assign a friendly name to the NSG during creation. The name doesn't have to be unique, and you can change it later. Oracle automatically assigns the NSG a unique identifier called an **Oracle Cloud ID (OCID)**. For more information, see [Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
For the purposes of access control, you must specify the **compartment** where you want the NSG to reside. If you're not sure which compartment to use, consult an administrator in your organization. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/create-nsg.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/create-nsg.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/create-nsg.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the name of the VCN you're interested in.
    3. Under **Resources** , click **Network Security Groups**.
    4. Click **Create Network Security Group**. 
    5. On the **Basic Info** page, enter the following information:
       * **Name:** A descriptive name for the NSG. The name doesn't have to be unique, and you can change it later. Avoid entering confidential information.
       * **Create In Compartment:** The compartment where you want to create the NSG, if different from the compartment you're currently working in. 
       * **Show advanced options:** You can apply tags to your resources to help you organize them according to your business needs. You can apply tags at the time you create a resource, or you can update the resource later with tags. For general information about applying tags, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). 
    6. Click **Next**.
If you want to create the NSG without any rules yet, click **Create** and you're done. Otherwise proceed to the next step.
    7. For the first security rule, enter the following information (for examples of rules, see [Networking Scenarios](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarios.htm#networking_scenarios)):
       * **Stateful or stateless:** If a rule is stateful, connection tracking is used for traffic matching the rule. If a rule is stateless, no connection tracking is used. By default, rules are stateful unless you specify otherwise. See [Stateful Versus Stateless Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful).
       * **Direction (ingress or egress):** Ingress is inbound traffic to the VNIC, and egress is outbound traffic from the VNIC. 
       * **Source Type** and **Source** (for ingress rules only): Following are the allowed source types and the source values that you can specify for them:
         * **CIDR** : The CIDR block that the traffic originates from. Use 0.0.0.0/0 to indicate all IP addresses. The prefix is required (for example, include the /32 if you're specifying an individual IP address). For more information about CIDR notation, see [RFC1817](https://datatracker.ietf.org/doc/html/rfc1817) and [RFC1519](https://datatracker.ietf.org/doc/html/rfc1519).
         * **Service** : Only for packets coming from an Oracle service through a [service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#Access_to_Oracle_Services_Service_Gateway). The source service is the [service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#overview) that you're interested in.
         * **Network Security Group** : An NSG that is in the same VCN as this rule's NSG.
       * **Destination Type** and **Destination** (for egress rules only): Following are the allowed destination types and the destination values that you can specify for them:
         * **CIDR** : The CIDR block that the traffic goes to. Use 0.0.0.0/0 to indicate all IP addresses. The prefix is required (for example, include the /32 if you're specifying an individual IP address). For more information about CIDR notation, see [RFC1817](https://datatracker.ietf.org/doc/html/rfc1817) and [RFC1519](https://datatracker.ietf.org/doc/html/rfc1519).
         * **Service** : Only for packets going to an Oracle service through a [service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#Access_to_Oracle_Services_Service_Gateway). The destination service is the [service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#overview) that you're interested in.
         * **Network Security Group** : An NSG that is in the same VCN as this rule's NSG.
       * **IP Protocol:** Either a single [IPv4 protocol](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) (for example, TCP or ICMP) or "all" to cover all protocols. 
       * **Source Port Range:** The port that the traffic originates from. For TCP or UDP, you can specify all source ports, or optionally specify a single source [port number](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml), or a range. 
       * **Destination Port Range:** The port that the traffic goes to. For TCP or UDP, you can specify all destination ports, or optionally specify a single destination [port number](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml), or a range. 
       * **ICMP Type and Code:** For ICMP, you can specify all types and codes, or optionally specify a single [ICMP type](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml) with an optional code. If the type has multiple codes, create a separate rule for each code that you want to allow. 
       * **Description** : Enter an optional description of the rule.
    8. To add another security rule, click **+ Another Rule** and enter the rule's information. Repeat for each rule that you want to add.
    9. When you're done, click **Create**.
The NSG is created and then displayed on the **Network Security Group** page in the compartment that you chose. You can now specify this NSG when creating or managing instances or other types of [parent resources](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison). 
When you view all the security rules in an NSG, you can filter the list by ingress or egress.
  * Use the [network nsg create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/nsg/create.html) command and required parameters to create an NSG in a VCN:
Command
CopyTry It
```
oci network nsg create --compartment-id nsg-compartment-ocid --vcn-id vcn-ocid ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateNetworkSecurityGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/CreateNetworkSecurityGroup) operation to create an NSG.


Was this article helpful?
YesNo


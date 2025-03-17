Updated 2025-02-12
# Creating an Internet Gateway
Create an internet gateway (IGW) in a Virtual Cloud Network (VCN) in Networking. 
**Prerequisites:**
  * Determine which subnets in the VCN need access to the internet, and create those public subnets.
Only one internet gateway is needed for each VCN. All public subnets within a VCN have access to the internet gateway if the security rules and route table rules allow that access.
  * Determine the types of ingress and egress internet traffic route rules that you want to enable for the resources in each public subnet (examples: ingress HTTPS connections, ingress ICMP ping connections).
  * The required IAM policy is in place to allow you to work with Networking service resources. For administrators, see [IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Policies). 


**Important**
If the public subnet is configured to use the [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default), remember that the list includes several helpful default rules that enable basic required access (examples: ingress SSH, egress access to all destinations). We recommend that you become familiar with the basic access that these default rules provide. If you decide not to use the default security list, be sure to provide this basic access by implementing these security rules either in [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) (NSGs) or custom [security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists). You also need to [configure route rules in the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm#update-rules-routetable "Add, edit, or delete rules for a Virtual Cloud Network \(VCN\) route table.") used by the public subnets to allow traffic to be routed to and from the internet.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-ig.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-ig.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-ig.htm)


  *     1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Select the name of the VCN that you're interested in.
    3. Under **Resources** , select **Internet Gateway**. 
    4. Select **Create Internet Gateway**. 
    5. Enter the following values:
       * **Name:** A friendly name for the internet gateway. It doesn't have to be unique, and it can't be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
       * **Create in Compartment:** The compartment in which you want to create the internet gateway, if different from the current compartment. 
       * You can select **Show advanced options** to set the following options: 
         * **Route Table Association:** (Advanced option) You can associate a specific VCN route table with this gateway. After you associate a route table, the gateway must always have a route table associated with it. You can change the rules in the current route table or replace it with another route table. 
         * **Tags:** (Advanced option) If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. 
    6. Select **Create Internet Gateway**.
The internet gateway is created and displayed on the **Internet Gateways** page of the compartment that you chose. You still need to [add a route rule](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm#update-rules-routetable "Add, edit, or delete rules for a Virtual Cloud Network \(VCN\) route table.") that allows traffic to flow to the internet gateway, and explicitly [allow that traffic with a security rule in a security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/update-securitylist.htm#update-securitylist "Update the rules used in a security list in a Virtual Cloud Network \(VCN\).") or [network security group](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/manage-nsg-security-rules.htm#manage_security_rules "Add, edit, or remove security rules for a network security group \(NSG\) in a virtual cloud network \(VCN\).").
  * Use the [network internet-gateway create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/internet-gateway/create.html) command and required parameters to create a new internet gateway for the specified VCN:
Command
CopyTry It
```
oci network internet-gateway create --compartment-id compartment-ocid --vcn-id vcn-ocid --is-enabled [true | false] ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateInternetGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InternetGateway/CreateInternetGateway) operation to create a new internet gateway.
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).


Was this article helpful?
YesNo


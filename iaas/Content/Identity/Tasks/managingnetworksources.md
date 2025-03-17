Updated 2025-01-14
# Managing Network Sources
This topic describes the basics of working with network sources.
## Required IAM Policy 🔗 
If you're in the Administrators group, then you have the required access for managing network sources. To write policies specifically for network sources, use the network-sources resource type, found with the other IAM components, in [Details for IAM without Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/iampolicyreference.htm#top).
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm#Getting_Started_with_Policies) and [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top).
## Tagging Resources 🔗 
Apply tags to resources to help organize them according to business needs. Apply tags at the time you create a resource, or update the resource later with the wanted tags. For general information about applying tags, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
## Introduction to Network Sources 🔗 
A network source is a set of defined IP addresses. The IP addresses can be public IP addresses or IP addresses from VCNs within your tenancy. After you create the network source, you can reference it in policy or in your tenancy's authentication settings to control access based on the originating IP address.
Network sources can only be created in the tenancy (or root compartment) and, like other IAM resources, reside in the [home region](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingregions.htm#The). For information about the number of network sources you can have, see [IAM Without Identity Domains Limits](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm#iamlimits). 
You can use network sources to help secure your tenancy in the following ways:
  * Specify the network source in IAM policy to restrict access to resources.
When specified in a policy, IAM validates that requests to access a resource originate from an allowed IP address. 
For example, you can restrict access to Object Storage buckets in your tenancy to only users that are signed in to Oracle Cloud Infrastructure through your corporate network. Or, you can allow only resources belonging to specific subnets of a specific VCN to make requests over a [service gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm).
  * Specify the network source in your tenancy's authentication settings to restrict sign in to the Console.
You can set up your tenancy's authentication policy to allow sign in to the Console from only those IP addresses specified in your network source. Users attempting to sign in from an IP address not on the allowed list in your network source will be denied access. For information on using a network source restriction in authentication policy, see [Managing Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingpasswordrules.htm#Managing_Authentication_Settings).


## Allowing Access to Resources from Only Specified IP Addresses 🔗 
To restrict access to requests made from a set of IP addresses, do the following:
  1. Create a network source that specifies the allowed IP addresses.
  2. Write a policy that uses the network source variable in a condition.


### 1. Create the Network Source
Follow the instructions provided for the [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingnetworksources.htm#Using) or the [API](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingpasswordrules.htm#api) to create the network source.
A single network source can include IP addresses from a specific VCN, public IP addresses, or both. 
To specify the VCN, you need the VCN OCID and the subnet IP ranges that you want to allow. 
Examples:
  * **Public IP addresses or CIDR blocks:** 192.0.2.143 or 192.0.2.0/24
  * **VCN OCID:** ocid1.vcn.oc1.iad.aaaaaaaaexampleuniqueID
    * **Subnet IP addresses or CIDR blocks:** 10.0.0.4, 10.0.0.0/16
To allow any IP address from a specific VCN, use 0.0.0.0/0.


### 2. Write the Policy
The IAM service includes a variable to use in policy that allows you to scope your policy using a condition. The variable is:
`request.networkSource.name`
After you have created your network source, you can scope policies by using this variable in a condition. For example, assume you create a network source named "corpnet". You can restrict users of the group "CorporateUsers" to access your Object Storage resources only when their requests originate from IP addresses you specified in corpnet. To do this, write a policy like the following: 
Copy
```
allow group CorporateUsers to manage object-family in tenancy where request.networkSource.name='corpnet'
```

This policy allows users in the CorporateUsers group to manage Object Storage resources only when their requests originate from an allowed IP address specified in the network source "corpnet". Requests made from outside the specified IP ranges are denied. For general information about writing policies, see [How Policies Work](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#How_Policies_Work).
## Using the Console to Manage Network Sources 🔗 
[To create a network source](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingnetworksources.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Network Sources**. A list of the network sources in your tenancy is displayed.
  2. Select **Create Network Source**. 
  3. Enter the following: 
     * **Name:** A unique name for the network source. The name must be unique in your tenancy. You cannot change this later. Avoid entering confidential information.
     * **Description:** A friendly description. You can change this later if you want to.
     * **Network Type:** Select one of the following:
       * **Public Network:** Enter a specific IP address or CIDR block range. For example: 192.0.2.143. 
Select **Another IP Address/CIDR Block** to add another allowed address or range.
       * **Virtual Cloud Network:** Enter the following for this option:
         * **VCN OCID:** Enter the OCID from the VCN you want to allow. 
For example: ocid1.vcn.oc1.iad.aaaaaaaaexampleuniqueID
         * **IP Address/CIDR Block:** Enter an IP address from the VCN or a subnet CIDR block. For example: 10.0.0.0/16 or 10.0.0.4. 
If you want to allow all subnets from the specified VCN, enter 0.0.0.0/0.
Select **Another IP Address/CIDR Block** to add another allowed address or range from the same VCN.
  4. To add more IP ranges to this network source, select **Add Source**.
  5. **Show Advanced Options:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. 
  6. Select **Create**.


[To update a network source](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingnetworksources.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Network Sources**. A list of the network sources in your tenancy is displayed.
  2. Locate the network source in the list and select its name to view its details.
  3. Edit the network source:
     * To add more allowed IP addresses to this network source, select **Add Sources**. In the **Add Sources** dialog, select **Add Source** again, and enter the [details](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingnetworksources.htm#one) for each IP address or CIDR block you want to add to this network source.
     * To remove an allowed source, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) and select **Delete**.


[To delete a network source](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingnetworksources.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. The list of network sources in your tenancy is displayed.
  2. Locate the network source in the list and select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the item.
  3. Select **Delete**.
  4. Confirm when prompted.


[To apply tags to a network source](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingnetworksources.htm)
For instructions, see [Resource Tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm#Resource_Tags). 
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use these API operations to manage network sources:
  * [CreateNetworkSource](https://docs.oracle.com/iaas/api/#/en/identity/latest/NetworkSources/CreateNetworkSource)
  * [ListNetworkSources](https://docs.oracle.com/iaas/api/#/en/identity/latest/NetworkSourcesSummary/ListNetworkSources)
  * [GetNetworkSource](https://docs.oracle.com/iaas/api/#/en/identity/latest/NetworkSources/GetNetworkSource)
  * [UpdateNetworkSource](https://docs.oracle.com/iaas/api/#/en/identity/latest/NetworkSources/UpdateNetworkSource)
  * [DeleteNetworkSource](https://docs.oracle.com/iaas/api/#/en/identity/latest/NetworkSources/DeleteNetworkSource)


### Creating the Network Source Object
A sample network source object looks like the following example:
Copy
```
{
"compartmentId" : "ocid1.tenancy.oc1..aaaaaaaabaexampleuniqueID",
"description" : "Corporate IP ranges to be used for IP-based authorization",
"name" : "corpnet",
"virtualSourceList": [
{"vcnId": "ocid1.vcn.oc1.iad.aaaaaaaaexampleuniqueID", "ipRanges": [ "129.213.39.0/24" ]}
],
"publicSourceList": [ "192.0.2.5", "192.0.2.6" ],
"services": ["all"]
]
}
```

The elements are:
  * `virtualSourceList` - specifies the VCN (OCID) and subnet IP ranges within that VCN that are allowed access. The `virtualSourceList` must contain both the VCN OCID and the subnet IP ranges:
    * `vcnID` - the OCID of the VCN 
    * `IpRanges` - comma-separated list of the IP addresses or CIDR blocks of the subnets belonging to the specified VCN that are allowed to access the resource. To allow all ranges in the specified VCN, enter 0.0.0.0/0.
  * `publicSourceList` - comma-separated list of the public IP ranges that are allowed access.


Example:
Copy
```
{
"virtualSourceList": [{vcnId: "ocid1.vcn.oc1.iad.aaaaaaaaexampleuniqueID", "ipRanges": [ "129.213.39.0/24" ]}],
"publicSourceList": [ "192.0.2.0/25", "192.0.2.200" ]
}
```

Was this article helpful?
YesNo


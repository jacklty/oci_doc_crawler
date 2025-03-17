Updated 2023-05-23
# Using the API
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use these API operations to manage network sources:
  * [CreateNetworkSource](https://docs.oracle.com/iaas/api/#/en/identity/latest/NetworkSources/CreateNetworkSource)
  * [ListNetworkSources](https://docs.oracle.com/iaas/api/#/en/identity/latest/NetworkSourcesSummary/ListNetworkSources)
  * [GetNetworkSource](https://docs.oracle.com/iaas/api/#/en/identity/latest/NetworkSources/GetNetworkSource)
  * [UpdateNetworkSource](https://docs.oracle.com/iaas/api/#/en/identity/latest/NetworkSources/UpdateNetworkSource)
  * [DeleteNetworkSource](https://docs.oracle.com/iaas/api/#/en/identity/latest/NetworkSources/DeleteNetworkSource)


## Creating the Network Source Object
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


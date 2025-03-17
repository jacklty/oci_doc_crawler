Updated 2024-09-30
# Scoping Policy by the IP Address of the Requestor
You can scope access to only a set of allowed IP addresses.
For example, you can write policy to allow only requests from a given public IP range to access a specific Object Storage bucket; or, you can allow only specific subnets of a specific VCN to make requests over a service gateway. For a list of supported services, see [Support for Network Sources](https://docs.oracle.com/iaas/Content/Identity/networksources/Support_for_Network_Sources.htm).
To restrict access to a set of IP addresses, do the following:
  1. Create a network source object that specifies the allowed IP addresses. See [Overview of Network Sources](https://docs.oracle.com/en-us/iaas/Content/Identity/networksources/managingnetworksources.htm#Managing_Network_Sources) for details.
  2. Write a policy that uses the network source object in a condition.


Use the following variable in your policy:
Copy
```
request.networkSource.name='<network_source_name>'
```

For example:
Copy
```
allow group GroupA to manage object-family in tenancy where request.networkSource.name='corpnet'
```

Was this article helpful?
YesNo


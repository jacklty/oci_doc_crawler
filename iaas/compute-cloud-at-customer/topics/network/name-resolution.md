Updated 2023-09-28
# Name Resolution
On Compute Cloud@Customer, the Domain Name System (DNS) translates human-readable domain names to machine-readable IP addresses. 
For example, when you type a domain name into a browser, the OS queries several DNS name servers until it finds the authoritative name server for that domain. The authoritative name server then responds with an IP address or other requested record data; the answer is relayed back to your browser and the DNS record is resolved to the web page.
For DNS name resolution within your VCN provides two options. You choose an option for each subnet in the VCN, using the subnet's set of DHCP options.
The default choice is the **Internet and VCN Resolver**. It consists of two parts: the Internet Resolver and the VCN Resolver. The Internet Resolver lets instances resolve host names that are publicly published on the internet, without requiring the instances to have internet access by way of either an internet gateway or a connection to the on-premises network. The VCN resolver lets instances resolve host names, which you can assign, of other instances in the same VCN.
Or, you can use a **Custom Resolver**. This enables you to use up to three DNS servers of your choice for name resolution. These could be DNS servers that are available through the internet, in your VCN, or in your on-premises network, which is connected to your VCN through a DRG.
## Domains and Host Names 🔗 
When you create a VCN and subnets, you can specify DNS labels for each. Subnet DNS labels can only be set if the VCN itself is created with a DNS label. The labels, along with the parent domain of `oraclevcn.com` form the VCN domain name and subnet domain name. Next, when you create an instance, you can assign a host name. The host name is assigned to the primary VNIC that is automatically created during instance creation. Along with the subnet domain name, the host name forms the instance's fully qualified domain name (FQDN).
  * **VCN domain name:** `**_<VCN_DNS_label>_**.oraclevcn.com`
  * **Subnet domain name:** `**_<subnet_DNS_label>_**.**_<VCN_DNS_label>_**.oraclevcn.com`
  * **Instance FQDN:** `**_<host_name>_**.**_<subnet_DNS_label>_**.**_<VCN_DNS_label>_**.oraclevcn.com`


The FQDN resolves to the instance's private IP address. The Internet and VCN Resolver also enables reverse DNS lookup, which lets you decide the host name corresponding to the private IP address.
If you add a secondary VNIC to an instance, you can specify a host name. The resulting FQDN resolves to the VNIC primary private IP address. The resulting FQDN resolves to that private IP address.
DNS labels and host names must meet these requirements:
  * VCN and subnet labels must start with a letter and have a maximum length of 15 alphanumeric characters. Hyphens and underscores are not allowed. The value can't be changed later.
  * Host names can be up to 63 characters in length and must be compliant with RFCs [952](https://tools.ietf.org/html/rfc952) and [1123](https://tools.ietf.org/html/rfc1123). The value can be changed later.
  * VCN DNS labels must be unique across the VCNs in your tenancy. Subnet DNS labels must be unique within the VCN, and host names must be unique within the subnet.


## Host Name Validation and Generation 🔗 
If you set DNS labels for VCN and subnet, the host name is validated for compliance during instance creation. If you haven't specified a host name, the system tries to use the instance display name. If the display name doesn't pass validation, or if you didn't specify one, the system generates a DNS-compliant host name. 
If you create an instance using the CLI or SDK, and you haven't specified a host name or display name, the system doesn't generate them for you. This means the instance isn't resolvable using the Internet and VCN Resolver.
If you add a secondary VNIC to an instance, the system never generates a host name. You must provide a valid host name if you want the private IP address to be resolvable using the Internet and VCN Resolver.
## Public DNS Zones 🔗 
To enable DNS name resolution for instances deployed inside your VCNs, from outside the Compute Cloud@Customer network environment, Compute Cloud@Customer provides configuration support for public DNS zones. Within your tenancy, you create the DNS zones, or sections of the DNS namespace, that you intend to manage. The edge network of the Compute Cloud@Customer handles all DNS queries for the domains.
For more information, see [Managing Public DNS Zones](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/managing-public-dns-zones.htm#managing-public-dns-zones "On Compute Cloud@Customer, the Domain Name System \(DNS\) lets computers use hostnames instead of IP addresses to communicate with each other.").
Was this article helpful?
YesNo


Updated 2024-08-21
# IP Address Ranges
This topic provides information about public IP address ranges for services that are deployed in Oracle Cloud Infrastructure. Allow traffic to these CIDR blocks to ensure access to the services.
Endpoints for [Oracle YUM repos](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/addressranges.htm#yum-endpoints) are listed on this page. You can use DNS lookup to determine the public IP address for each endpoint.
## Public IP Addresses for VCNs and the Oracle Services Network 🔗 
Public IP address ranges for VCNs and the Oracle Services Network are published to a JSON file which you can download and view manually or consume programmatically. 
The _Oracle Services Network_ is a conceptual network in Oracle Cloud Infrastructure that is reserved for Oracle services. A [service gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm) offers private access to the Oracle Services Network from workloads in your VCN and your on-premises network. The published addresses correspond to the [service CIDR label](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm#overview) called **All <region> Services in Oracle Services Network**. For a list of the services available with a service gateway, see [Service Gateway: Supported Cloud Services in Oracle Services Network](https://www.oracle.com/cloud/networking/service-gateway/service-gateway-supported-services/).
### Downloading the JSON File
[Use this link to download the current list of public IP ranges](https://docs.oracle.com/iaas/tools/public_ip_ranges.json). 
You can poll the published file to check for new IP address ranges as frequently as every 24 hours. We recommend that you poll the published file at least weekly.
### JSON File Contents and Syntax
IP addresses are published in the `public_ip_ranges.json` file with the fields in the following table. 
[Example of the public_ip_ranges.json file](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/addressranges.htm)
Copy
```
{
  "last_updated_timestamp": "2019-11-18T19:55:47.204985",
  "regions": [
    {
      "region": "us-phoenix-1",
      "cidrs": [
        {
          "cidr": "129.146.0.0/21",
          "tags": [
            "OCI"
          ]
        },
        {
          "cidr": "134.70.8.0/21",
          "tags": [
            "OSN",
            "OBJECT_STORAGE"
          ]
        },
      ]
    }
    {
      "region": "us-ashburn-1",
      "cidrs": [
        {
          "cidr": "129.213.8.0/21",
          "tags": [
            "OCI"
          ]
        },
        {
          "cidr": "134.70.24.0/21",
          "tags": [
            "OSN",
            "OBJECT_STORAGE"
          ]
        }
      ]
    }
  ]
}

```

Field Name | Definition | Type | Example  
---|---|---|---  
`last_updated_timestamp` |  File creation time in ISO 8601 format.  Expressed as `<date>T<time>` | string | `"last_updated_timestamp": "2019-11-18T19:55:47.204985"`  
`regions` | IP CIDR ranges grouped by region.  | array | See preceding [Example of the public ip ranges.json file](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/addressranges.htm#json-example__t-example)  
`region` |  The region of the IP CIDR ranges.  Valid values: Any region in the Oracle Cloud Infrastructure commercial realm.  For a complete list of regions, see [Regions and Availability Domains](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm#top). | string |  `"region": "us-phoenix-1"`  
`cidrs` | A group of IP address CIDR ranges. | array | See preceding [Example of the public ip ranges.json file](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/addressranges.htm#json-example__t-example)  
`cidr` | One or more IPv4 IP addresses expressed in CIDR notation.  | string | `"cidr": "147.154.0.0/18" `  
`tags` |  The services associated with the IP address CIDR range.  Valid values: 
  * `OCI`: The VCN CIDR blocks.
  * `OSN`: The CIDR block ranges for the [Oracle Services Network](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/addressranges.htm#osn-ranges). 
  * `OBJECT_STORAGE`: The CIDR block ranges used by the Object Storage service. For more information, see [Overview of Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm). 

| array of string values | `"tags": [            "OCI"          ]`  
#### Filtering the JSON file contents
After you download the JSON file, you can use a command line tool such as `jq` to filter the contents. 
[Download `jq`](https://stedolan.github.io/jq/)
Here are some examples of how you can use the tool to find and filter the information you need: 
**Find the creation date of the JSON file:**
Copy
```
jq .last_updated_timestamp < public_ip_ranges.json
```

**Get all IPv4 addresses for a specific region:**
Copy
```
jq -r '.regions[] | select (.region=="us-phoenix-1") | .cidrs[] | select (.cidr | contains(".")) | .cidr ' < public_ip_ranges.json
```

## Public IP Addresses for the Oracle YUM Repos 🔗 
The Oracle YUM repos have the following regional public endpoints.
Region | YUM Server Endpoint  
---|---  
Netherlands Northwest (Amsterdam)  | https://yum-eu-amsterdam-1.oracle.com  
Australia East (Sydney)  | https://yum-ap-sydney-1.oracle.com  
Canada Southeast (Toronto)  | https://yum-ca-toronto-1.oracle.com  
Germany Central (Frankfurt)  | https://yum-eu-frankfurt-1.oracle.com  
India West (Mumbai)  | https://yum-ap-mumbai-1.oracle.com  
Japan Central (Osaka)  | https://yum-ap-osaka-1.oracle.com  
Japan East (Tokyo)  | https://yum-ap-tokyo-1.oracle.com  
Saudi Arabia West (Jeddah)  | https://yum-me-jeddah-1.oracle.com  
Australia Southeast (Melbourne)  | https://yum-ap-melbourne-1.oracle.com  
South Korea Central (Seoul)  | https://yum-ap-seoul-1.oracle.com  
UK South (London)  | https://yum-uk-london-1.oracle.com  
US East (Ashburn)  | https://yum-us-ashburn-1.oracle.com  
US West (Phoenix)  | https://yum-us-phoenix-1.oracle.com  
You can use DNS lookup to determine the public IP address for each endpoint.
Was this article helpful?
YesNo


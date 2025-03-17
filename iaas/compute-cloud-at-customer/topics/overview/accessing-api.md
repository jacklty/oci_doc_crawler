Updated 2024-08-06
# Using the API to Manage Compute Cloud@Customer Resources
The Compute Cloud@Customer API is a subset of the Oracle Cloud Infrastructure (OCI) REST API that uses HTTPS requests and responses. 
To see the API references for Compute Cloud@Customer, use the links in the following table:
Description | API Reference  
---|---  
The API used to manage resources on the Compute Cloud@Customer infrastructure in your data center. For example, API operations to manage instances, virtual cloud networks, and storage resources. |  [REST API for Oracle Private Cloud Appliance](https://docs.oracle.com/en/engineered-systems/private-cloud-appliance/3.0-latest/ceapi/)  
The API used to manage Compute Cloud@Customer specific resources in your OCI tenancy. For example, API operations to manage infrastructures and upgrade schedules. |  [Compute Cloud@Customer API](https://docs.oracle.com/iaas/api/#/en/compute-cloud-at-customer/)  
  * Endpoints follow this format```
https://<service>.<system_name>.<domain_name>
```

Where `<service>` is the name of the OCI service providing the API you want to use. For example, `iaas` for the core services. `<system_name>` is the name of the infrastructure, typically the same as the display name. `<domain_name>` is the domain the infrastructure is in.
  * For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


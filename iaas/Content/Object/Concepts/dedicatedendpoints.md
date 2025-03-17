Updated 2024-08-15
# Object Storage Dedicated Endpoints
Learn how Object Storage dedicated endpoints provides you new endpoints to access the storage buckets securely.
The tenant isolation will have unique, immutable, system-generated, and namespace-prefixed dedicated endpoints. Using these tenancy-specific endpoints by having a dedicated namespace string in the URLs will ensure full isolation to help meet your organization's security and compliance requirements.
The current Object Storage service API endpoint URLs will continue to function. Use of the new endpoints is optional for tenants writing their own clients to access Object Storage buckets. You can point your custom client requests to any of these new domains for better security posture. We do not mandate you to use a specific domain. However, we encourage you to use dedicated endpoints with namespace prefix on the customer-oci.com domain.
## Advantages of the new feature and why you should use dedicated endpoints
  * The dedicated endpoint feature isolates Object Storage customers from each other, preventing a malicious or inadvertent API usage by customer, causing the common URL to be blocked, thus impacting all other customers.
  * The new feature helps minimize the broad impact of DNS-based blocking of Object Storage endpoints by security software.
  * It also provides protection against malicious cyber-attacks and blocking on a per-tenancy level.


## Prerequisites
Firewalls, proxy servers, or other devices that your network administrators use to control access to the internet can affect your ability to connect to the new domain. In order to allow access to the new URL, you need to whitelist the new second level domain.
To allow network access to the Console, your network administrator should add *.**customer-oci.com** to the allowlist of your firewall or proxy server.
**Note** The new URLs are shown in detail in the table below. Note that these changes in the URL apply only to OC1, other areas will continue with existing URLs.
## New URLs 🔗 
The domain URLs that are currently used by Object Storage users will change. To introduce dedicated URLs, Object Storage now registers DNS records with wild-card prefix on the new OCI customer zone SLD (customer-oci.com). The following table shows what is changing on the API endpoints with this new feature. Changes are in **bold**.
API Type | Current URL | New URL  
---|---|---  
Native |  objectstorage.$region.oraclecloud.com |  objectstorage.$region.**oci**.**customer-oci.com**(only used in cases where namespace is not known. For e.g. GetNamespace / WorkRequests etc. ) **$namespace**.objectstorage.$region.**oci**.**customer-oci.com**  
S3 compatible |  $namespace.compat.objectstorage.$region.oraclecloud.com | $namespace.compat.objectstorage.$region.**oci**.**customer-oci.com**  
Swift |  swiftobjectstorage.$region.oraclecloud.com |  swiftobjectstorage.$region.**oci**.**customer-oci.com** **$namespace**.swiftobjectstorage.$region.**oci**.**customer-oci.com**  
PARs | objectstorage.$region.oraclecloud.com/p/<>/n/<>/b/<>/o/ | **$namespace**.objectstorage.$region.**oci.customer-oci.com** /p/<>/n/<>/b/<>/o/  
**Note** **$namespace** refers to the Object Storage Namespace. See [Understanding Object Storage Namespaces](https://docs.oracle.com/iaas/Content/Object/Tasks/understandingnamespaces.htm) to know more about Object Storage Namespaces.
## OCI UI (Object Storage Console) 🔗 
OCI Console will start using dedicated endpoints for Object Storage, this will keep the overall flow of using Object Storage completely unchanged. 
## OCI SDK / CLI 🔗 
Uptake of dedicated endpoints with SDK/CLI can be done via setting environment variables or command line flags. Examples will be updated for each SDK and CLI under [SDK Guides](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm). Accessing dedicated endpoints is currently optional for tenants but later releases will default to the dedicated endpoints. There will be an announcement made sufficiently in advance before this is done.
## Known Issues
This feature works best for tenants with Object Storage namespace strings not containing any special characters. While Object Storage Console handles this automatically, but for using dedicated endpoints with SDKs/CLI, tenants might encounter errors in case their namespace string has a special character.
Was this article helpful?
YesNo


Updated 2025-03-10
# HTTP Redirects
The DNS service lets you redirect HTTP traffic to another URL.
You can use HTTP redirects to:
  * Redirect all HTTP traffic for an entire domain name service (DNS) **zone** to another zone. For example, if a company owns `example.net` and `example.com`, HTTP Redirect lets the company redirect all HTTP traffic for `example.net` to `example.com`. This is a one-to-one mapping. Wildcards aren't supported.
  * Redirect a specific subdomain to an HTTP URL. For example, `test.example.com` can be redirected to `http://example.net/test/test.php`.
  * Redirect a subdomain to a URL with a port number. For example, `camera.example.com` can be redirected to `http://office.example.com:8080` so a user can view their camera system without typing in the port number each time.
  * Permanently redirect a **domain name** that has been deprecated by displaying a 301 response code. Permanently redirecting a domain name informs search engines and browsers what to do with the information.


**Important**
During the **Create HTTP redirect** workflow, it's important that you check the **Create DNS record** option so that when the redirect is created, OCI deploys a record for `redirect.waf.oci.oraclecloud.net`. OCI deploys an ALIAS record for root (apex) domains and CNAME records for non root (apex) domains.
If you don't check the **Create DNS record** now, you can't edit the redirect later to obtain the record for `redirect.waf.oci.oraclecloud.net`. You must either delete the redirect and start over, or manually add the record to the DNS. 
**This record must be added to the originating DNS zone for the redirect to work**.
## Required IAM Policies 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
This sample policy allows a specific group to manage HTTP redirects:
```
Allow group <GroupName> to manage http-redirects in compartment <CompartmentName>
```

If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). For more details about policies for HTTP Redirect, see [DNS Policy Reference](https://docs.oracle.com/iaas/Content/Identity/policyreference/dnspolicyreference.htm).
## HTTP Redirect Tasks 🔗 
You can perform the following tasks with HTTP redirects:
  * [Creating HTTP Redirects](https://docs.oracle.com/iaas/Content/DNS/Tasks/http-redirect-create.htm)
  * [Listing HTTP Redirects](https://docs.oracle.com/iaas/Content/DNS/Tasks/http-redirect-list.htm)
  * [Viewing HTTP Redirects](https://docs.oracle.com/iaas/Content/DNS/Tasks/http-redirect-get.htm)
  * [Editing HTTP Redirects](https://docs.oracle.com/iaas/Content/DNS/Tasks/http-redirect-edit.htm)
  * [Moving a HTTP Redirect to a Different Compartment](https://docs.oracle.com/iaas/Content/DNS/Tasks/http-redirect-move-compartment.htm)
  * [Deleting HTTP Redirects](https://docs.oracle.com/iaas/Content/DNS/Tasks/http-redirect-delete.htm)


Was this article helpful?
YesNo


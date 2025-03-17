Updated 2025-03-10
# Deleting an HTTP Redirect
You can delete an HTTP redirect.
See [HTTP Redirects](https://docs.oracle.com/iaas/Content/DNS/Tasks/httpredirect.htm) for a feature overview and more information.
For general service information, see the [DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-delete.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **HTTP redirects**.
    2. Under **List scope** , select the compartment that contains the redirect.
    3. Select the name of the HTTP redirect to open its details page.
    4. Select **Delete**.
    5. In the **Delete HTTP Redirect** dialog box, select **Delete HTTP Redirect**. 
You need to remove any associated ALIAS or CNAME records to ensure proper resolution. See [DNS Zone Management](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/managingdnszones.htm#managing-zones "The Oracle Cloud Infrastructure DNS service lets you manage zones using the Console, CLI, or API.").
  * Use the [http-redirect delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/http-redirect/delete.html) command and required parameters to delete an HTTP redirect.
```
oci waas http-redirect delete --http-redirect-id http_redirect_OCID ...[OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteHttpRedirect](https://docs.oracle.com/iaas/api/#/en/waas/latest/HttpRedirect/DeleteHttpRedirect) operation to delete an HTTP redirect.


Was this article helpful?
YesNo


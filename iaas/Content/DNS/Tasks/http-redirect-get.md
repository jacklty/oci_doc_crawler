Updated 2025-03-10
# Getting an HTTP Redirect's Details
View details for a specific HTTP redirect.
See [HTTP Redirects](https://docs.oracle.com/iaas/Content/DNS/Tasks/httpredirect.htm) for a feature overview and more information.
For general service information, see the [DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-get.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **HTTP redirects**.
    2. Under **List scope** , select the compartment that contains the redirect.
    3. Select the HTTP redirect top open its details page.
The details page contains information about the HTTP redirect, both general information and links to its resources. Some items in the page are read-only, and other items are editable. See [Editing an HTTP Redirect](https://docs.oracle.com/iaas/Content/DNS/Tasks/http-redirect-edit.htm).
  * Use the [http-redirect get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/http-redirect/get.html) command and required parameters to get details about a HTTP redirect:
```
oci waas http-redirect get --http-redirect-id http_redirect_OCID ...[OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetHttpRedirect](https://docs.oracle.com/iaas/api/#/en/waas/latest/HttpRedirect/GetHttpRedirect) operation to view details about an HTTP redirect.


Was this article helpful?
YesNo


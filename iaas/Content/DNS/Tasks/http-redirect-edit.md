Updated 2025-03-10
# Editing an HTTP Redirect
Update the information for an HTTP redirect.
See [HTTP Redirects](https://docs.oracle.com/iaas/Content/DNS/Tasks/httpredirect.htm) for a feature overview and more information.
For general service information, see the [DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-edit.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-edit.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-edit.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **HTTP redirects**.
    2. Under **List scope** , select the compartment that contains the redirect.
    3. Select the name of the HTTP redirect to open its details page.
    4. Select **Edit**.
    5. In the **Edit Redirect** panel, make the changes. 
For information about the fields, see [Creating an HTTP Redirect](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-create.htm#top "Create an HTTP redirect that lets you redirect HTTP traffic to another URL."). 
    6. Select **Save Changes**.
  * Use the [http-redirect update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/http-redirect/update.html) command and required parameters to edit an HTTP redirect.
```
oci waas http-redirect update --http-redirect-id http_redirect_OCID ...[OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateHttpRedirect](https://docs.oracle.com/iaas/api/#/en/waas/latest/HttpRedirect/UpdateHttpRedirect) operation to edit an HTTP redirect.


Was this article helpful?
YesNo


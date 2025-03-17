Updated 2025-03-10
# Moving an HTTP Redirect Between Compartments
You can move an HTTP redirect from one compartment to another. 
See [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm) for information about compartments and access control.
See [HTTP Redirects](https://docs.oracle.com/iaas/Content/DNS/Tasks/httpredirect.htm) for a resource overview and more information.
For general service information, see the [DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-move-compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-move-compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-move-compartment.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **HTTP redirects**.
    2. Under **List scope** , select the compartment that contains the redirect.
    3. Find the HTTP redirect in the list, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Move resource**.
    4. Select a destination compartment from the list.
    5. Select **Move resource**.
  * Use the [http-redirect change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/http-redirect/change-compartment.html) command and required parameters to move an HTTP redirect to a different compartment.
Command
CopyTry It
```
oci dns http-redirect change-compartment --http-redirect-id http_redirect_OCID --compartment-id compartment_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeHttpRedirectCompartment](https://docs.oracle.com/iaas/api/#/en/waas/latest/HttpRedirect/ChangeHttpRedirectCompartment) operation to move an HTTP redirect to a different compartment.


Was this article helpful?
YesNo


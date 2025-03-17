Updated 2025-03-10
# Creating an HTTP Redirect
Create an HTTP redirect that lets you redirect HTTP traffic to another URL.
See [HTTP Redirects](https://docs.oracle.com/iaas/Content/DNS/Tasks/httpredirect.htm) for a feature overview and more information.
For general service information, see the [DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-create.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-create.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/http-redirect-create.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **HTTP redirects**.
    2. Under **List scope** , select the compartment to create the redirect in.
    3. Select **Create HTTP Redirect**. 
    4. In the **Create Redirect** panel, enter the following information:
       * **Name:** (Optional) Enter a descriptive name for the redirect. Avoid entering confidential information.
       * **Select a zone:** (Optional) Select a zone from a list of configured zones. If the **Create DNS Record** checkbox is selected, the zone is used to build records for the redirect.
       * **Domain:** Enter the domain name from which traffic is redirected.
       * **Target:** Enter the information for the redirect endpoint:
         * **Protocol:** The network protocol used to interact with the target.
         * **Host:** The hostname of the target.
         * **Port:** (Optional) The port used to connect to the endpoint. The default is 80 for HTTP and 443 for HTTPS.
         * **Path:** (Optional) The specific path on the target for the redirect. A value of `{path}` copies the path from the incoming request.
         * **Query:** (Optional) The query component of the target URL. For example, `?redirected` is the query component in `https://target.example.com/path/to/resource?redirected`. Use of the `\` character isn't allowed except to escape a following `\`, `{`, or `}`. An empty value results in a redirection target URL with no query component. A static value must begin with a leading `?`, optionally followed by other query characters. A request-copying value must exactly match`{query}` and is replaced with the query component of the request URL. If the request URL query component has a leading`?`, it's included.
       * **Response code:** The response code returned with the redirect. 
         * If the website was permanently moved to the redirection URL and you want it to be indexed by search engines, select **301 - Moved permanently**. 
         * To indicate that the URL has been temporarily changed to a different address, select **302 - Found**.
       * **Create DNS record:** Select this checkbox for OCI to deploy an associated CNAME or ALIAS record for the redirect in the specified zone. If a record for the specified zone already exists, the DNS record isn't created. If no zone is selected, this checkbox is disabled. 
**Important**
Check the **Create DNS record** option so that when the redirect is created, OCI deploys a record for `redirect.waf.oci.oraclecloud.net`. OCI deploys an ALIAS record for root (apex) domains and CNAME records for non root (apex) domains.
If you don't check the **Create DNS record** now, _it's not possible to edit_ the redirect to obtain the record for `redirect.waf.oci.oraclecloud.net`. You must either delete the redirect and start over, or manually add the record to the DNS. 
**This record must be added to the originating DNS zone for the redirect to work**.
       * **ALIAS TTL in seconds:** The time to live for the ALIAS record before a new ALIAS record is retrieved. The default value is 300.
       * **Tags:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    5. To create the HTTP redirect now, select **Create**.
    6. To create the redirect later using Resource Manager and Terraform, select **Save as Stack** to save the resource definition as a Terraform configuration.
For more information about saving stacks from resource definitions, see [Creating a Stack from a Resource Creation Page](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-resource.htm).
  * Use the [http-redirect create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/waas/http-redirect/create.html) command and required parameters to create an HTTP redirect:
```
oci waas http-redirect create --compartment-id compartment_id --domain domain --target file://target.json
```

The `--generate-full-command-json-input` option can be used to generate a sample `.json` file to be used with this command option. The key names are already populated and match the command option names, converted to `camelCase` format. For example, `compartment-id` becomes `compartmentId`. The values of the keys need to be populated by the user before using the sample file as an input to this command. For any command option that accepts more than one value, the value of the key can be a `JSON` array.
For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateHttpRedirect](https://docs.oracle.com/iaas/api/#/en/waas/latest/HttpRedirect/CreateHttpRedirect) operation to create an HTTP redirect.


Was this article helpful?
YesNo


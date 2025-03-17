Updated 2023-06-14
# Creating a Quick-Create Link for a Stack
Use a quick-create link to get a Resource Manager stack up and running quickly from the Oracle Cloud Console.
You can specify the configuration location and variable overrides in URL query parameters to prepopulate a single **Create Stack** page. A quick-create link simplifies the process of creating stacks. The link reduces the number of workflow pages and requires less user input. These links optimize configuration reuse because you can create multiple URLs that specify different values for the same Terraform configuration.
## Supported Parameters 🔗 
Resource Manager supports the following URL query parameters in quick-create links for stacks.
Parameter | Comments  
---|---  
`zipUrl` |  Required. Specifies the URL of the .zip file to a Terraform configuration that is stored in a supported provider. [Supported providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-quick-create-links-stacks.htm)The following providers are supported for the `zipUrl` parameter in quick-create links for stacks:
  * GitHubExample URL 1: Direct: `https://github.com/myrepo/mydirectory/master.zip`Example URL 2: Release: `https://github.com/myrepo/mydirectory/0.0.1.zip`To get the zip URL to a release in GitHub, see <https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/linking-to-releases>.
  * GitLabExample URL 1: Direct: `https://gitlab.com/myrepo/mydirectory/master.zip`Example URL 2: Release: `https://gitlab.com/myrepo/mydirectory/0.0.1.zip`
  * Object Storage ([pre-authenticated request URL](https://docs.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm))Example URL: `https://objectstorage.region.oraclecloud.com/p/encrypted-string/n/object-storage-namespace/b/bucket/o/filename`

  
`zipUrlVariables` | Optional. Specifies values for specified variables. Must be valid JSON format.  
## Example 🔗 
The following example is based on the **MuShop Basic Quickstarts** template. The query string includes the required `zipURL` parameter and the optional `zipUrlVariables` parameter specifying a value for a resource name.
**Note** For more information about Resource Manager templates, see [Oracle-Provided Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Reference/templates.htm#top "Review the Oracle-provided templates available for Resource Manager. A template is a prebuilt Terraform configuration for deploying cloud resources in a common scenario.").
The following URL has line breaks added to facilitate scanning.
```
https://cloud.oracle.com/resourcemanager/stacks/create
?zipUrl=https://github.com/oracle-quickstart/oci-cloudnative/releases/latest/download/mushop-basic-stack-latest.zip
&zipUrlVariables={"autonomous_database_name": "overrideName"} 
```

The following URL includes the same parameters as the previous example, but the line breaks are removed. This URL is the actual URL format.
Copy
```
https://cloud.oracle.com/resourcemanager/stacks/create?zipUrl=https://github.com/oracle-quickstart/oci-cloudnative/releases/latest/download/mushop-basic-stack-latest.zip&zipUrlVariables={"autonomous_database_name": "overrideName"} 
```

The example URL opens the **Create Stack** page in the Oracle Cloud Console, with the supplied values automatically used for the parameters.
Was this article helpful?
YesNo


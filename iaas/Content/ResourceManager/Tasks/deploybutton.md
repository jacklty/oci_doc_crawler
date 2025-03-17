Updated 2025-01-07
# Using the Deploy to Oracle Cloud Button
Launch a remote Terraform configuration with the **Deploy to Oracle Cloud** button.
This page describes the advanced topic of constructing a URL for a **Deploy to Oracle Cloud** button.
When properly linked, this button provides a direct option for your users to create stacks with your Terraform configuration.
![This image shows the Deploy to Oracle Cloud button.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/deploy-to-oracle-cloud.svg)
This button takes a user directly to the **Create Stack** page in the Oracle Cloud Infrastructure Console. The button is linked to a Terraform configuration file package that you specify, so the Terraform configuration is already selected for the user when they [create the stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/deploybutton.htm#tocreatestack). You can store Terraform configuration files in a [supported provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/deploybutton.htm#deploybutton-supportedproviders).
## Example of Functioning Deploy Button 🔗 
**Tip** Quickly create stacks with example OCI Terraform configurations. Go to [Terraform Oracle Cloud Infrastructure Provider Examples](https://github.com/oracle/terraform-provider-oci/tree/master/examples), navigate to the folder for the configuration you want (such as `adm`), and then select the **Deploy to Oracle Cloud** button under "Magic Button" in the readme.
The following **Deploy to Oracle Cloud** button is configured to launch the template from <https://github.com/oracle-quickstart/oci-cloudnative>.
[ ![Deploy to Oracle Cloud](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/deploy-to-oracle-cloud.svg) ](https://cloud.oracle.com/resourcemanager/stacks/create?zipUrl=https://github.com/oracle-quickstart/oci-cloudnative/releases/latest/download/mushop-basic-stack-latest.zip)
## Supported Providers 🔗 
The following providers are supported for forming package URLs to use with the **Deploy to Oracle Cloud** button:
  * GitHub
Example URL 1: Direct: `https://github.com/myrepo/mydirectory/master.zip`
Example URL 2: Release: `https://github.com/myrepo/mydirectory/0.0.1.zip`
To get the zip URL to a release in GitHub, see <https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/linking-to-releases>.
  * GitLab
Example URL 1: Direct: `https://gitlab.com/myrepo/mydirectory/master.zip`
Example URL 2: Release: `https://gitlab.com/myrepo/mydirectory/0.0.1.zip`
  * Object Storage ([pre-authenticated request URL](https://docs.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm))
Example URL: `https://objectstorage.region.oraclecloud.com/p/encrypted-string/n/object-storage-namespace/b/bucket/o/filename`


To troubleshoot an error code, see [Error Code 400 for Deploy Button](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/deploy-button.htm#top "Troubleshoot error code 400 when using the Deploy to Oracle Cloud button.").
## To display the linked deploy button 🔗 
**Important** Ensure that your Terraform configuration file is valid. See[Authoring Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/authoring-configurations.htm#top "Write a Terraform configuration to describe infrastructure using the HashiCorp Configuration Language format \(HCL\).") and [Terraform Configurations for Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#top "Review requirements and recommendations for Terraform configurations used with Resource Manager. Use Terraform and Resource Manager to install, configure, and manage resources using the infrastructure-as-code model."). 
You can display the linked **Deploy to Oracle Cloud** button on repository pages and other web pages.
### Markdown code 🔗 
To display the **Deploy to Oracle Cloud** button on a repository page, add the following Markdown code to a README.md file.
Copy
```
[
![Deploy to Oracle Cloud]
(https://oci-resourcemanager-plugin.plugins.oci.oraclecloud.com/latest/deploy-to-oracle-cloud.svg)
]
(https://cloud.oracle.com/resourcemanager/stacks/create
?zipUrl=<package-url>)
```

<package-url> is the URL for the .zip file to a Terraform configuration that is stored in a [supported provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/deploybutton.htm#deploybutton-supportedproviders).
Example Markdown code with a package URL from GitHub: 
Copy
```
[![Deploy to Oracle Cloud](https://oci-resourcemanager-plugin.plugins.oci.oraclecloud.com/latest/deploy-to-oracle-cloud.svg)](https://cloud.oracle.com/resourcemanager/stacks/create?zipUrl=https://github.com/myrepo/mydirectory/master.zip)
```

### HTML code 🔗 
To display the **Deploy to Oracle Cloud** button on a web page, add the following HTML code.
Copy
```
<a 
href="https://cloud.oracle.com/resourcemanager/stacks/create?zipUrl=<package-url>" 
target="_blank">
 <img 
src="https://oci-resourcemanager-plugin.plugins.oci.oraclecloud.com/latest/deploy-to-oracle-cloud.svg" 
alt="Deploy to Oracle Cloud"/>
</a>
```

<package-url> is the URL for the .zip file to a Terraform configuration that is stored in a [supported provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/deploybutton.htm#deploybutton-supportedproviders).
Example HTML code with a package URL from GitHub: 
Copy
```
<a href="https://cloud.oracle.com/resourcemanager/stacks/create?zipUrl=https://github.com/myrepo/mydirectory/master.zip" target="_blank">
 <img src="https://oci-resourcemanager-plugin.plugins.oci.oraclecloud.com/latest/deploy-to-oracle-cloud.svg" alt="Deploy to Oracle Cloud"/>
</a>
```

## To create a stack from the linked deploy button 🔗 
  1. Select **Deploy to Oracle Cloud** (the deploy button linked to the Terraform configuration).
To troubleshoot an error code, see [Error Code 400 for Deploy Button](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/deploy-button.htm#top "Troubleshoot error code 400 when using the Deploy to Oracle Cloud button.").
  2. If you're not yet signed in to the Oracle Cloud Infrastructure Console, then sign in. See [Signing In for the First Time](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm).
The **Create stack** page appears with the selected package identified.
  3. Enter a name for the new stack (or accept the default name provided). Avoid entering confidential information.
  4. Optionally enter a description. 
  5. To view the resources in a different compartment, use the **Compartment** filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see [Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
  6. For **Terraform version** , select the version that you want to use for the new stack.
**Note** Terraform versions aren't backward compatible.
  7. Optionally add tags:
     * To add a defined tag, select the namespace and key, then enter a value.
     * To add a free-form tag, enter a key and value.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
  8. Select **Next**.
The **Configure variables** panel displays variables from the selected Terraform configuration file.
  9. Review the variables and make changes as necessary.
**Important** Don't add your private key or other confidential information to configuration variables.
  10. Select **Next**.
  11. In the **Review** panel, verify your stack configuration.
**Run apply** is selected by default. Preserve this setting to automatically provision resources on stack creation.
  12. Select **Create** to create your stack.
The stack details page for the new stack appears.
If you selected **Run apply** , then Resource Manager runs the apply action on the new stack.


To deploy the defined resources (if you didn't select **Run apply** in the **Create stack** page), [run an apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager.") on your new stack.
Was this article helpful?
YesNo


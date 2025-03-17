Updated 2025-01-07
# Creating a Private Endpoint
Create a private endpoint in Resource Manager.
## Before You Begin 🔗 
Gather the network information that you need:
  * [Virtual cloud network (VCN) and subnet](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm)
  * The private endpoint connection is at the VCN level. If you have many subnets per VCN, you need to create only one private endpoint for that VCN. Ensure that security rules meet your requirements.
  * [Network security groups](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm) (optional)
  * [DNS zones](https://docs.oracle.com/iaas/Content/DNS/Concepts/gettingstarted.htm) (optional, for private Git servers)
For example, for a private Git server at `https://privateGitServer.examplesub.exampledomain`, create a DNS zone for `examplesub.exampledomain`.


Additionally:
  * Ensure that the subnet allows access to the private resource: Set up a [security rule](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm#rules) for ingress.
  * Ensure that the subnet has available IP addresses.
If no IP addresses are available in the specified subnet, then the work request for creating the private endpoint [fails](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/pe-work-request-fails.htm#top "Troubleshoot a failed work request for a private endpoint.").
  * For private Git servers, import the certificates you want to use. See the [GitHub](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-github.htm#import-cert "To access a private GitHub server, make its associated SSL certificate available in the OCI Certificates service.") and [GitLab](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-gitlab.htm#import-cert "To access a private GitLab server, make its associated SSL certificate available in the Oracle Cloud Infrastructure Certificates service.") instructions.


## Using a Terraform Configuration 🔗 
Create a private endpoint by using a Terraform configuration.
  * To create a stack that creates a Resource Manager private endpoint, use the **Resource Manager create private endpoint** [template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Reference/templates.htm#top "Review the Oracle-provided templates available for Resource Manager. A template is a prebuilt Terraform configuration for deploying cloud resources in a common scenario.").
  * For example Terraform configurations that use Resource Manager private endpoints, see [Private endpoint Terraform configuration examples](https://github.com/oracle/terraform-provider-oci/tree/master/examples/resourcemanager). Also, review [Terraform Configurations for Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#top "Review requirements and recommendations for Terraform configurations used with Resource Manager. Use Terraform and Resource Manager to install, configure, and manage resources using the infrastructure-as-code model.").


  1. Add code to the Terraform configuration that creates a private endpoint.
For an example, see [Example Usage (oci_resourcemanager_private_endpoint)](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/resourcemanager_private_endpoint#example-usage).
  2. [Create a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack.htm#top "Create a stack in Resource Manager. You can optionally postpone variables and other stack settings until after the stack is created.") that references this Terraform configuration.
  3. [Run an apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager.") on the stack.
A work request for creation runs, and then the private endpoint is created. You can now [reference](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoints.htm#tf-config-ref "Get details for an existing private endpoint by adding code to reference it from a Terraform configuration.") the private endpoint from any Terraform configuration or [configuration source provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/managingconfigurationsourceproviders.htm#top "Remotely store Terraform configurations using configuration source providers in Resource Manager.").


  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-private-endpoints.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-private-endpoints.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-private-endpoints.htm)


  * To create a private endpoint by using the Console, follow these steps.
    1. On the **Private endpoints** list page, select **Create private endpoint**. If you need help finding the list page or the private endpoint, see [Listing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-private-endpoints.htm#top "List private endpoints in Resource Manager.").
    2. In the **Create private endpoint** panel, enter a name and optional description for the private endpoint. Avoid entering confidential information.
    3. Select the compartment that you want to store the private endpoint in.
    4. Enter the following values:
       * **Virtual cloud network** : The virtual cloud network (VCN) to use with the private endpoint. See [VCNs and Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/VCNs.htm). To select a VCN in a different compartment, select **Change Compartment**.
       * **Subnet** : The subnet to use with the private endpoint. See [VCNs and Subnets](https://docs.oracle.com/iaas/Content/Network/Tasks/VCNs.htm). To select a subnet in a different compartment, select **Change Compartment**.
       * **Allow this private endpoint to be used with a configuration source provider** : When enabled, allows use with [configuration source providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/managingconfigurationsourceproviders.htm#top "Remotely store Terraform configurations using configuration source providers in Resource Manager.") (for example, private Git servers). If you enable this option, it can't be disabled after the endpoint is created.
       * **DNS zones** : The DNS zones to use with the private endpoint. This field is displayed when ****Allow this private endpoint to be used with a configuration source provider**** is selected. For more information about DNS zones, see [Public DNS](https://docs.oracle.com/iaas/Content/DNS/Concepts/gettingstarted.htm).
       * **Network security groups** : The [network security groups (NSGs)](https://docs.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm) to use with the private endpoint. To select a NSG in a different compartment, select **Change Compartment**.
    5. (Optional) Add tags:
      1. To show tagging options, select **Show advanced options**.
      2. To add a defined tag, select the namespace and key, then enter a value.
      3. To add a free-form tag, enter a key and value.
    6. Select **Create**.
The new private endpoint appears on the **Private endpoints** list page. While the work request for creation runs, the new private endpoint's status is **Creating** , and the new private endpoint's [details page](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoints.htm#top "Get details for a private endpoint in Resource Manager.") shows the work request in progress. When the work request reaches succeeded status, the new private endpoint's status is **Active**.
  * Use the `oci resource-manager private-endpoint create[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/private-endpoint/create.html)` command to create a private endpoint.
Copy
```
oci resource-manager private-endpoint create --compartment-id <compartment_ocid> --display-name <text> --subnet-id <subnet_ocid> --vcn-id <vcn_ocid>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [CreatePrivateEndpoint](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/PrivateEndpoint/CreatePrivateEndpoint) operation to create a private endpoint.


## What's Next 🔗 
To troubleshoot a failed work request for creation of a private endpoint, see [Private Endpoint Work Request Fails](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Troubleshoot/pe-work-request-fails.htm#top "Troubleshoot a failed work request for a private endpoint.").
Was this article helpful?
YesNo


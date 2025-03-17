Updated 2025-01-23
# Managing Private Endpoints
Create, edit, and delete private endpoints in Resource Manager.
With private endpoints, you can access nonpublic cloud resources in your tenancy from Resource Manager. For example, configure a private compute instance using Terraform's remote exec functionality and access Terraform configurations in a private GitHub server.
You can perform the following tasks with private endpoints:
  * [Creating a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-private-endpoints.htm#top "Create a private endpoint in Resource Manager.")
  * [Listing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-private-endpoints.htm#top "List private endpoints in Resource Manager.")
  * [Getting a Private Endpoint's Details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoints.htm#top "Get details for a private endpoint in Resource Manager.")
  * [Getting the Reachable IP Address for a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoint-reachable-ip.htm#top "Get the reachable IP address of a private endpoint in Resource Manager.")
  * [Updating a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-private-endpoints.htm#top "Update a private endpoint in Resource Manager.")
  * [Moving a Private Endpoint to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/move-private-endpoints.htm#top "Move a Resource Manager private endpoint to another compartment.")
  * [Deleting a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-private-endpoints.htm#top "Delete a Resource Manager private endpoint.")


## Required IAM Policy 🔗 
To manage private endpoints, you must have permission to manage private endpoints in the tenancy, and to use virtual network resources, such as VCNs and subnets. For more information, see [Manage Private Templates](https://docs.oracle.com/iaas/Content/Security/Reference/resourcemanager_security.htm#iam-policies__templates).
If you're new to policies, see [How Policies Work](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm). 
## Scenarios 🔗 
Review common scenarios for using private endpoints with Resource Manager.
Other scenarios also exist. You can reach any private resource with a private IP, using a private endpoint in Resource Manager. For example, connect to a [Kubernetes cluster](https://docs.oracle.com/iaas/Content/ContEng/home.htm).
### Private Git Server 🔗 
Give Resource Manager access to a Git server that isn't accessible over the internet. User these instructions for a private server that you host at Oracle Cloud Infrastructure or on-premises.
  1. If the private server is on-premises, then set up site-to-site VPN or FastConnect.
For more information, see [Site-to-Site VPN](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIPsec.htm) and [FastConnect](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm).
  2. Import the private Git server's associated SSL certificate into the Certificates service.
For more information, see the relevant page:
     * [**Bitbucket Server** prerequisites](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-server.htm#prereqs)
     * [GitHub](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-github.htm#import-cert "To access a private GitHub server, make its associated SSL certificate available in the OCI Certificates service.")
     * [GitLab](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-gitlab.htm#import-cert "To access a private GitLab server, make its associated SSL certificate available in the Oracle Cloud Infrastructure Certificates service.")
  3. [Create a private endpoint.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-private-endpoints.htm#top "Create a private endpoint in Resource Manager.")
  4. [Get the reachable IP address for the private endpoint.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoint-reachable-ip.htm#top "Get the reachable IP address of a private endpoint in Resource Manager.")
  5. [Create a configuration source provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp.htm#top "Create a configuration source provider in Resource Manager.") that references this private endpoint (and the associated SSL certificate that you imported into the Certificates service).
  6. [Create a stack that references this configuration source provider.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-git.htm#top "Create a stack in Resource Manager from a Terraform configuration stored in Git. Select a configuration source provider that specifies the Git information needed to access the configurations.")


### Private Remote Exec 🔗 
Access private instances with Remote Exec.
**Note** When accessing a private instance with Remote Exec, you must use a reachable IP address.
See also [Getting the Reachable IP Address for a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoint-reachable-ip.htm#top "Get the reachable IP address of a private endpoint in Resource Manager.").
  1. Write a Terraform configuration that creates a private instance.
  2. In the Terraform configuration, either create or reference a private endpoint:
     * [Add code to your Terraform configuration to create the private endpoint.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-private-endpoints.htm#tf-config-create "Create a private endpoint by using a Terraform configuration.")
**Note** You can also create a private endpoint using the Console, SDK, CLI, or API. See [Creating a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-private-endpoints.htm#top "Create a private endpoint in Resource Manager.").
     * [Add code to your Terraform configuration to reference an existing private endpoint.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoints.htm#tf-config-ref "Get details for an existing private endpoint by adding code to reference it from a Terraform configuration.")
For example Terraform configurations that use Resource Manager private endpoints, see [Private endpoint Terraform configuration examples](https://github.com/oracle/terraform-provider-oci/tree/master/examples/resourcemanager).
  3. Add code to your Terraform configuration to convert the private IP address to a reachable IP address.
The reachable IP address is in the range 240.0.0.0 to 255.255.255.255 [(Class E; see RFC 1112, Section 4)](https://tools.ietf.org/html/rfc1112).
To get the reachable IP address, see [Getting the Reachable IP Address for a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-private-endpoint-reachable-ip.htm#top "Get the reachable IP address of a private endpoint in Resource Manager.").
[Example code](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/private-endpoints.htm)
```
resource "null_resource" "remote-exec" {
 depends_on = [oci_core_instance.private_endpoint_instance]
 provisioner "remote-exec" {
  connection {
   agent = false
   timeout = "30m"
   host = data.oci_resourcemanager_private_endpoint_reachable_ip.test_private_endpoint_reachable_ips.ip_address
   user = "opc"
   private_key = tls_private_key.public_private_key_pair.private_key_pem
  }
  inline = [
   "echo 'remote exec showcase' > ~/remoteExecTest.txt"
  ]
 }
}
```

For example Terraform configurations that use Resource Manager private endpoints, see [Private endpoint Terraform configuration examples](https://github.com/oracle/terraform-provider-oci/tree/master/examples/resourcemanager).
  4. Store the Terraform configuration in a [supported location](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#sources).
  5. [Create a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack.htm#top "Create a stack in Resource Manager. You can optionally postpone variables and other stack settings until after the stack is created.") that references this Terraform configuration.
  6. [Run an apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager.") on the stack.
The private instance and private endpoint are created. You can now use [Remote Exec](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/usingremoteexec.htm#top "With Resource Manager, you can use Terraform's remote exec functionality to execute scripts or commands on a remote computer. You can also use this technique for other provisioners that require access to the remote resource.") to access your private instance.


Was this article helpful?
YesNo


Updated 2025-01-23
# Managing Configuration Source Providers
Remotely store Terraform configurations using configuration source providers in Resource Manager.
**Note** For remote Terraform configurations in DevOps, see [Creating a Stack from DevOps](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-devops.htm#top "Create a stack in Resource Manager from a Terraform configuration stored in DevOps.").
You can perform the following management tasks with configuration source providers:
  * [Creating a Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp.htm#top "Create a configuration source provider in Resource Manager.")
    * [Creating a Bitbucket Cloud Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-cloud.htm#top "Create a configuration source provider in Resource Manager from Bitbucket Cloud.")
    * [Creating a Bitbucket Server Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-server.htm#top "Create a configuration source provider in Resource Manager from Bitbucket Server.")
    * [Creating a GitHub Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-github.htm#top "Create a configuration source provider in Resource Manager from GitHub.")
    * [Creating a GitLab Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-gitlab.htm#top "Create a configuration source provider in Resource Manager from GitLab.")
  * [Listing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-csp.htm#top "List configuration source providers in Resource Manager.")
  * [Creating a Stack from a Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-from-csp.htm#top "Create a stack from a configuration source provider in Resource Manager.")
    * [Creating a Stack from Bitbucket Cloud](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-from-csp-bitbucket-cloud.htm#top "Create a stack in Resource Manager from a Terraform configuration stored in Bitbucket Cloud. Select a configuration source provider that specifies the Bitbucket Cloud information needed to access the configurations.")
    * [Creating a Stack from Bitbucket Cloud](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-from-csp-bitbucket-server.htm#top "Create a stack in Resource Manager from a Terraform configuration stored in Bitbucket Server. Select a configuration source provider that specifies the Bitbucket Server information needed to access the configurations.")
    * [Creating a Stack from Git](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-from-csp-git.htm#top "Create a stack in Resource Manager from a Terraform configuration stored in Git. Select a configuration source provider that specifies the Git information needed to access the configurations.")
  * [Getting a Configuration Source Provider's Details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-csp.htm#top "Get details about a configuration source provider in Resource Manager.")
  * [Updating a Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp.htm#top "Update a configuration source provider in Resource Manager.")
    * [Updating a Configuration Source Provider (Any Type)](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp-basic.htm#top "Update a configuration source provider in Resource Manager.")
    * [Updating a Bitbucket Cloud Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp-bb-cloud.htm#top "Update a Bitbucket Cloud configuration source provider in Resource Manager.")
    * [Updating a Bitbucket Server Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp-bb-server.htm#top "Update a Bitbucket Server configuration source provider in Resource Manager.")
    * [Updating a GitHub Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp-github.htm#top "Update a GitHub configuration source provider in Resource Manager.")
    * [Updating a GitLab Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp-gitlab.htm#top "Update a GitLab configuration source provider in Resource Manager.")
  * [Validating the Connection for a Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/validate-connection-csp.htm#top "Confirm that Resource Manager can access a configuration source provider's server URL with the provided authentication information. You can validate a connection by using the Console only.")
  * [Moving a Configuration Source Provider to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/change-compartment-csp.htm#top "Move a configuration source provider in Resource Manager to another compartment.")
  * [Tagging a Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/tag-csp.htm#top "Add metadata to a configuration source provider in Resource Manager.")
    * [Tagging a Configuration Source Provider at Creation](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/tag-create-csp.htm#top "Add metadata to a configuration source provider when you first create it. This metadata enables you to define keys and values and to associate them with resources.")
    * [Tagging a Configuration Source Provider When Updating](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/tag-update-csp.htm#top "Add metadata to a configuration source provider when you update it. This metadata enables you to define keys and values and to associate them with resources.")
  * [Deleting a Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-csp.htm#top "Delete a configuration source provider in Resource Manager.")


## Required IAM Policy 🔗 
Use policies to grant access to configuration source providers in Resource Manager.
To manage configuration source providers, you must be given the required type of access in a **policy** written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. To create a configuration source provider, you need `manage orm-config-source-providers`. To create a stack with an existing configuration source provider, you need `manage orm-stacks` and `read orm-config-source-providers`. If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm).
Administrators: For common policies that give groups access to configuration source providers in Resource Manager, see [Manage Configuration Source Providers (Securing Resource Manager)](https://docs.oracle.com/iaas/Content/Security/Reference/resourcemanager_security.htm#iam-policies__csp).
## Supported Products 🔗 
Review the products supported for configuration source providers in Resource Manager.
**Note** For product-specific prerequisites, see the product-specific instructions for creating configuration source providers. For example, for GitHub, see [Creating a GitHub Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-github.htm#top "Create a configuration source provider in Resource Manager from GitHub.").
[Submodules](https://git-scm.com/book/en/Git-Tools-Submodules) are supported. When accessing a Terraform configuration in a repository with submodules, as when running an apply job on a stack that uses a configuration source provider in Git, Resource Manager recursively clones the repository.
A configuration source provider can be one of the following types:
  * Bitbucket
  * GitHub
  * GitLab


Following are the supported products for each type of configuration source provider.
  * Bitbucket:
    * Bitbucket Cloud
    * Bitbucket Server
  * GitHub:
    * [GitHub Enterprise](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/githubs-products#github-enterprise)
      * GitHub Enterprise Server
      * GitHub Enterprise Cloud
    * [GitHub Free for organizations](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/githubs-products#github-free-for-organizations)
    * [GitHub Free for user accounts](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/githubs-products#github-free-for-user-accounts)
    * [GitHub Team](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/githubs-products#github-team)
  * GitLab:
    * GitLab Community Edition
    * GitLab Enterprise Edition
    * GitLab.com


## Example Server URLs 🔗 
[Bitbucket Cloud](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-cloud.htm#top "Create a configuration source provider in Resource Manager from Bitbucket Cloud."):
  * `https://bitbucket.org/`


[Bitbucket Server](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-bb-server.htm#top "Create a configuration source provider in Resource Manager from Bitbucket Server."):
  * `my-private-bitbucket-server.example.com`


[GitHub](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-github.htm#top "Create a configuration source provider in Resource Manager from GitHub."):
  * GitHub Enterprise Cloud: `https://github.com/org-name`
  * GitHub Enterprise Server: `https://hostname/api/v3`
  * GitHub Free for Organization: `https://github.com/org-name`
  * GitHub Free for User Accounts: `https://github.com`
  * GitHub team: `https://github.com/team-name`


[GitLab](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-gitlab.htm#top "Create a configuration source provider in Resource Manager from GitLab."):
  * GitLab.com product: `https://gitlab.com/`
  * GitLab installation (relative URL): `https://example.com/gitlab`
  * GitLab installation (subdomain): `https://gitlab.example.com/`


Was this article helpful?
YesNo


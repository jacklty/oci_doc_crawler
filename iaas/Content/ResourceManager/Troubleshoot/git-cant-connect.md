Updated 2023-06-27
# Can't Connect to Git
Troubleshoot connection issues to Git servers while working with Resource Manager.
Can't connect to GitHub or GitLab. 
This issue can occur in the following situations: 
  * Creating a [GitHub](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-github.htm#top "Create a configuration source provider in Resource Manager from GitHub.") or [GitLab configuration source provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-gitlab.htm#top "Create a configuration source provider in Resource Manager from GitLab.").
  * [Creating a stack from a Git configuration source provider.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-git.htm#top "Create a stack in Resource Manager from a Terraform configuration stored in Git. Select a configuration source provider that specifies the Git information needed to access the configurations.")
  * [Running a job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job.htm#top "Create a job in Resource Manager, such as plan, apply, or destroy.") on a stack that uses a Terraform configuration stored in Git. 
  * Receiving an error message when [confirming accessibility to a configuration source provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/validate-connection-csp.htm#top "Confirm that Resource Manager can access a configuration source provider's server URL with the provided authentication information. You can validate a connection by using the Console only.").


## Cause: The Personal Access Token (PAT) was revoked
## Remedy: Re-create the PAT
Re-create the Personal Access Token (PAT), ensuring that the token scope includes required permissions.
See the relevant Git documentation.
  * GitHub: <https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token>
  * GitLab: <https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html>


## Cause: The required permission scopes changed and are insufficient
## Remedy: Re-create the PAT
Re-create the Personal Access Token (PAT), ensuring that the token scope includes required permissions.
See the relevant Git documentation.
  * GitHub: <https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token>
  * GitLab: <https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html>


## Cause: The Git repository permissions changed or are insufficient
## Remedy: Use admin or owner
Ensure that the GitHub or GitLab repository permissions meet requirements (admin or owner). 
## Cause: The Git server isn't accessible over the internet
## Remedy: For a public server, use a public IP address
Ensure that the Git server uses a [public IP address](https://docs.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm).
## Remedy: For a private server, use a certificate and private endpoint
**Note** Ensure that the certificate in the Certificates service matches the certificate on the Git server.
  * For certificate instructions, see [GitHub](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-github.htm#import-cert "To access a private GitHub server, make its associated SSL certificate available in the OCI Certificates service.") and [GitLab](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-gitlab.htm#import-cert "To access a private GitLab server, make its associated SSL certificate available in the Oracle Cloud Infrastructure Certificates service.").
  * For private endpoint instructions, see [Creating a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-private-endpoints.htm#top "Create a private endpoint in Resource Manager.").
  * For high-level instructions on private servers, see [Private Git Server](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/private-endpoints.htm#private-git "Give Resource Manager access to a Git server that isn't accessible over the internet. User these instructions for a private server that you host at Oracle Cloud Infrastructure or on-premises.").


## Remedy: Ensure that the Git server meets all prerequisites
See [GitHub](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-github.htm#prereqs) and [GitLab prerequisites](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp-gitlab.htm#prereqs).
Was this article helpful?
YesNo


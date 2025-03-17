Updated 2023-01-04
# Supported Terraform Providers
Review the Terraform providers supported by Resource Manager.
## Minimum OCI Provider Versions 🔗 
Resource Manager supports the latest version of `terraform-provider-oci` for any given Terraform version.
Following are the minimum versions of `terraform-provider-oci` supported for each indicated Terraform version.
Terraform version | Minimum supported version of `terraform-provider-oci`  
---|---  
0.12.x | 3.16.0  
0.13.x | 3.16.0  
0.14.x | 3.16.0  
1.0.x | 3.30.0  
## Third-party Providers 🔗 
Review Resource Manager stack sourcing of third-party providers.
New and updated stacks fetch providers from [Terraform Registry](https://registry.terraform.io/browse/providers). To update older stacks to use Terraform Registry, see [Using Terraform Registry with an Older Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-reg.htm#top "Update an older stack to fetch providers from Terraform Registry.").
See also [Third-party Provider Configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#third-party-providers "Reference third-party Terraform providers in Terraform configurations used with Resource Manager.").
### Older Stacks 🔗 
Stacks created before Terraform Registry sourcing was available fetch third-party providers from Resource Manager. For details, see the following table.
**Note** To update older stacks to fetch third-party providers from Terraform Registry, see [Using Terraform Registry with an Older Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-reg.htm#top "Update an older stack to fetch providers from Terraform Registry.").
Third-party Terraform Provider | 0.12.x | 0.13.x | 0.14.x | 1.0.x  
---|---|---|---|---  
`terraform-provider-ansible[](https://github.com/nbering/terraform-provider-ansible)` | 1.0.3 | 1.0.3 | 1.0.3 | 1.0.3  
`terraform-provider-archive[](https://registry.terraform.io/providers/hashicorp/archive/latest/docs)` |  1.1.0, 1.2.2 |  1.1.0, 1.2.2 |  1.1.0, 1.2.2 |  2.1.0  
`terraform-provider-aviatrix[](https://github.com/AviatrixSystems/terraform-provider-aviatrix)` | - | - | - | 2.19.1  
`terraform-provider-checkpoint[](https://registry.terraform.io/providers/CheckPointSW/checkpoint/latest/docs)` | 1.0.0, 1.0.3 | 1.0.0, 1.0.3 | 1.0.0, 1.0.3 | 1.4.0  
`terraform-provider-chef[](https://github.com/hashicorp/terraform-provider-chef/blob/stable-website/website/docs/index.html.markdown)` | 0.2.0 | 0.2.0 | 0.2.0 | 0.2.0  
`terraform-provider-cloudinit[](https://registry.terraform.io/providers/hashicorp/cloudinit/latest/docs)` | 1.0.0 | 1.0.0 | 1.0.0 | 2.2.0  
`terraform-provider-digitalocean[](https://registry.terraform.io/providers/digitalocean/digitalocean/latest/docs)` |  1.13.0 |  1.13.0 |  1.13.0 | 2.7.0  
`terraform-provider-dyn[](https://registry.terraform.io/providers/dynatrace-oss/dynatrace/latest/docs)` | 1.2.0 | 1.2.0 | 1.2.0 | 1.2.0  
`terraform-provider-github[](https://registry.terraform.io/providers/integrations/github/latest/docs)` |  2.3.1, 2.9.2 |  2.3.1, 2.9.2 |  2.3.1, 2.9.2 | 2.9.2  
`terraform-provider-gitlab[](https://registry.terraform.io/providers/gitlabhq/gitlab/latest/docs)` |  2.5.0  |  2.5.0  |  2.5.0  | 3.5.0  
`terraform-provider-helm[](https://registry.terraform.io/providers/hashicorp/helm/latest/docs)` |  0.9.1, 1.1.1 |  0.9.1, 1.1.1 |  0.9.1, 1.1.1 | 2.1.0  
`terraform-provider-http[](https://registry.terraform.io/providers/hashicorp/http/latest)` | 2.0.0 | 2.0.0 | 2.0.0 | 2.1.0  
`terraform-provider-kubernetes[](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs)` |  1.8.1, 1.11.2 |  1.8.1, 1.11.2 |  1.8.1, 1.11.2 | 1.11.2  
`terraform-provider-local[](https://registry.terraform.io/providers/hashicorp/local/latest/docs)` |  1.1.0, 1.2.2, 1.4.0 |  1.1.0, 1.2.2, 1.4.0 |  1.1.0, 1.2.2, 1.4.0 | 2.1.0  
`terraform-provider-null[](https://registry.terraform.io/providers/hashicorp/null/latest/docs)` |  1.0.0, 2.1.2 |  1.0.0, 2.1.2 |  1.0.0, 2.1.2 | 3.1.0  
`terraform-provider-panos[](https://registry.terraform.io/providers/PaloAltoNetworks/panos/latest/docs)` |  1.6.2  |  1.6.2  |  1.6.2  | 1.8.1  
`terraform-provider-random[](https://registry.terraform.io/providers/hashicorp/random/latest/docs)` |  2.1.2, 2.3.0 |  2.1.2, 2.3.0 |  2.1.2, 2.3.0 | 3.1.0  
`terraform-provider-template[](https://registry.terraform.io/providers/hashicorp/template/latest/docs)` |  1.0.0, 2.1.2 |  1.0.0, 2.1.2 |  1.0.0, 2.1.2 | 2.1.2  
`terraform-provider-time[](https://registry.terraform.io/providers/hashicorp/time/latest)` | 0.6.0 | 0.6.0 | 0.6.0 | 0.7.0  
`terraform-provider-tls[](https://registry.terraform.io/providers/hashicorp/tls/latest/docs)` |  1.2.0, 2.0.1 |  1.2.0, 2.0.1 |  1.2.0, 2.0.1 | 3.1.0  
`terraform-provider-vault[](https://registry.terraform.io/providers/hashicorp/vault/latest/docs)` | 2.7.1 | 2.7.1 | 2.7.1 | 2.19.0  
Was this article helpful?
YesNo


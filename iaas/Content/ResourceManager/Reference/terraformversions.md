Updated 2025-02-24
# Supported Terraform Versions
Review the Terraform versions supported by the Resource Manager service.
## Terraform Versions Supported by Resource Manager 🔗 
Resource Manager supports the following [versions of Terraform](https://releases.hashicorp.com/terraform/) and Terraform CLI versions.
**Note** The `terraform_` version prefix (seen in [the Terraform list](https://releases.hashicorp.com/terraform/)) is omitted in the table. The `.x` suffix indicates coverage of minor versions. Patch versions aren't supported.
Terraform version | Terraform CLI version | Date that support began | Comments  
---|---|---|---  
1.5.x | 1.5.7 | July 30, 2024  
1.2.x | 1.2.9 | February 24, 2023  
1.1.x | 1.1.3 | May 7, 2022  
1.0.x | 1.0.0 | June 24, 2021  
0.14.x | 0.14.11 | February 19, 2021 | In the future, Resource Manager plans to remove support for this version.*  
0.13.x | 0.13.7 | November 9, 2020 | In the future, Resource Manager plans to remove support for this version.*  
0.12.x | 0.12.31 | September 12, 2019 | In the future, Resource Manager plans to remove support for this version.*  
*A job can't be created for a stack that uses an unsupported version of terraform, so stacks using these versions can't be used to manage infrastructure. To continue using an older stack, [upgrade the stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/upgradingstacks.htm#top "Upgrade a stack in Resource Manager to a later Terraform version.") to a supported Terraform version.
## Terraform Versions Previously Supported by Resource Manager 🔗 
Resource Manager previously supported the following [versions of Terraform](https://releases.hashicorp.com/terraform/).
**Note** The `terraform_` version prefix (seen in [the Terraform list](https://releases.hashicorp.com/terraform/)) is omitted in the table. The `.x` suffix indicates coverage of minor versions.
Terraform version | Date that support ended  
---|---  
0.11.x | September 1, 2021  
Was this article helpful?
YesNo


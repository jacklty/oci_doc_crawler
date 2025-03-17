Updated 2024-10-08
# Known Issues for Resource Manager
Known issues have been identified for Resource Manager.
See also [Troubleshooting Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/troubleshooting.htm#top "Use troubleshooting information to identify and address common issues that can occur while working with Resource Manager.").
## Error: Circuit breaker is open 🔗  

Details
    The logs for a job show the following: `Error: Circuit breaker is open`. This error usually indicates an error with a downstream service. 

Workaround
    
We're working on a resolution. Follow these instructions to identify the downstream service causing the error, then contact that service to determine resolution.
  1. Gather debugging information by running a new job on the stack:
    1. Display the job panel for the type of job you want to run ([Plan](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm#top "Create a plan job in Resource Manager."), [Apply](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager."), or [Destroy](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-destroy.htm#top "Create a destroy job in Resource Manager to release \(tear down\) resources associated with a stack and clean up the tenancy. Released resources are eventually deleted by the related OCI service. For example, a released compute instance is eventually deleted by the OCI Compute service.")).
    2. In the job panel, select **Show Advanced Options**.
    3. Set **Detailed Log Level** to **Debug**.
Wait for the job to finish running.
For more information about debugging Terraform job logs, see [Debugging Terraform](https://developer.hashicorp.com/terraform/internals/debugging).
  2. Download the detailed log: On the **Job Details** page for the job you just ran, select **Download Detailed Log File** (in the **Job Information** tab, to the right of **Detailed Log Level**).
  3. Review the downloaded log to identify the error-associated downstream services.
  4. Contact the associated downstream service to determine resolution.


## Object Storage buckets may not be available in the Console for new stacks 🔗  

Details
    When using the Console to create a stack from a bucket in Object Storage, the list of values for **Object Storage Buckets** is only available when the bucket namespace is identical to the tenancy name.  

Workaround
    Create the stack using the SDK, CLI, or API instead. We're working on a resolution.
## Resource Discovery fails (permissions issue) 🔗  

Details
    When using Resource Discovery to create a stack from a compartment, the work request fails.     Possible cause: The user who is creating the stack lacks permissions to inspect compartments for the tenancy. 

Workaround
     To work around this issue, make sure that the user who is creating the stack has permissions to inspect compartments for the tenancy. For the group that the user belongs to, create the following [policy](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm).```
Allow group <group name> to inspect compartments in tenancy 
```

## Missing attributes in some discovered resources 🔗  

Details
    Attributes are missing from some supported resources captured using resource discovery.
Service | Resource type | Missing fields (with links to oci Terraform provider documentation)  
---|---|---  
Big Data Service | Instances  |  [cluster_admin_password](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/bds_bds_instance.html#cluster_admin_password) [cluster_public_key](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/bds_bds_instance.html#cluster_public_key)  
Block Volume (core) | Volumes | [volume_backup_id](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_volume.html#volume_backup_id)  
Compute (core) | Images | [instance_id](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_image.html#instance_id)[image_source_details](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_image.html#image_source_details)  
Compute (core) | Instance Configurations | [instance_id](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_instance_configuration.html#instance_id)[source](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_instance_configuration.html#source)  
Compute (core) | Instance Console Connections | [public_key](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_instance_console_connection.html#public_key)  
Compute (core) | Instances |  [hostname_label](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_instance.html#hostname_label) (deprecated) [is_pv_encryption_in_transit_enabled](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_instance.html#is_pv_encryption_in_transit_enabled) [subnet_id](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_instance.html#subnet_id) (deprecated)  
Compute (core) | Volume Attachments | [use_chap](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_volume_attachment.html#use_chap)  
Kubernetes Engine  | Node Pools | [node_source_details](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/containerengine_node_pool.html#node_source_details)  
Data Catalog  | Connections | [enc_properties](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/datacatalog_connection.html#enc_properties)  
Database  | Autonomous Container Databases | [maintenance_window_details](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_autonomous_container_database.html#maintenance_window_details)  
Database  | Autonomous Databases |  [admin_password](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_autonomous_database.html#admin_password) [autonomous_database_backup_id](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_autonomous_database.html#autonomous_database_backup_id) [autonomous_database_id](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_autonomous_database.html#autonomous_database_id) [clone_type](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_autonomous_database.html#clone_type) [is_preview_version_with_service_terms_accepted](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_autonomous_database.html#is_preview_version_with_service_terms_accepted) [source](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_autonomous_database.html#source) [source_id](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_autonomous_database.html#source_id) [timestamp](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_autonomous_database.html#timestamp)  
Database  | Autonomous Exadata Infrastructures | [maintenance_window_details](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_autonomous_exadata_infrastructure.html#maintenance_window_details)  
Database  | Databases |  [admin_password](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_database.html#admin_password) [backup_id](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_database.html#backup_id) [backup_tde_password](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_database.html#backup_tde_password) [db_version](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_database.html#db_version) [source](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_database.html#source)  
Database  | Db Homes |  [admin_password](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_db_home.html#admin_password) [backup_id](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_db_home.html#backup_id) [backup_tde_password](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_db_home.html#backup_tde_password) [source](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_db_home.html#source)  
Database  | Db Systems |  [admin_password](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_db_system.html#admin_password) [backup_id](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_db_system.html#backup_id) [backup_tde_password](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_db_system.html#backup_tde_password) [maintenance_window_details](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/database_db_system.html#maintenance_window_details)  
IAM  | Identity Providers | [metadata](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/identity_identity_provider.html#metadata)  
Load Balancer  | Load Balancers | [ip_mode](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/load_balancer_load_balancer.html#ip_mode)  
Marketplace  | Accepted Agreements  | [signature](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/marketplace_accepted_agreement.html#signature)  
Networking (core) | Cross Connects  |  [far_cross_connect_or_cross_connect_group_id](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_cross_connect.html#far_cross_connect_or_cross_connect_group_id) [near_cross_connect_or_cross_connect_group_id](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_cross_connect.html#near_cross_connect_or_cross_connect_group_id)  
NoSQL Database Cloud  | Indexes | [is_if_not_exists](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/nosql_index.html#is_if_not_exists)  
Object Storage  |  Objects |  [cache_control ](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/objectstorage_object.html#cache_control) [content](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/objectstorage_object.html#content) [content_disposition](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/objectstorage_object.html#content) [content_encoding](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/objectstorage_object.html#content_encoding) [content_language](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/objectstorage_object.html#content_language) [source ](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/objectstorage_object.html#source) [source_uri_details](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/objectstorage_object.html#source_uri_details)  
Web Application Acceleration and Security  | Certificates |  [certificate_data](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/waas_certificate.html#certificate_data) [is_trust_verification_disabled](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/waas_certificate.html#is_trust_verification_disabled) [private_key_data](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/waas_certificate.html#private_key_data)  
Web Application Acceleration and Security  | Policies |  [are_redirects_challenged](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/waas_waas_policy.html#are_redirects_challenged-1) [is_case_sensitive](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/waas_waas_policy.html#is_case_sensitive-2) [is_nat_enabled](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/waas_waas_policy.html#is_nat_enabled) (human_interaction_challenge) [is_nat_enabled](https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/waas_waas_policy.html#is_nat_enabled-1) (js_challenge) 

Workaround
    We're working on a resolution.  
Was this article helpful?
YesNo


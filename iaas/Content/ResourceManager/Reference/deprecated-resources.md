Updated 2024-06-26
# Deprecated Resources
Review the list of deprecated Oracle Cloud Infrastructure Terraform provider resources.
This topic covers the list of resources and data sources that have been marked deprecated by the Oracle Cloud Infrastructure (OCI) Terraform provider and their respective suggested replacements, if any. Resource Manager uses the latest version of the Terraform provider, unless you've specified a particular version of the provider in your configuration.
This topic covers the list of resources and data sources that have been marked deprecated by the Oracle Cloud Infrastructure (OCI) Terraform provider and their respective suggested replacements, if any. Resource Manager uses the latest version of the Terraform provider, unless you've specified a particular version of the provider in your configuration.
Resources and data sources marked for deprecation trigger warnings during Terraform `plan` and `apply` jobs. In Resource Manager, look for these warning messages in the [job logs](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/get-job-logs.htm).
For example:
`The 'oci_autonomous_data_warehouse' resource has been deprecated. Please             use 'oci_autonomous_database' instead.`
Resources on path to deprecation might stop working in future, use the respective guide, if available, on how to migrate using the new replacements.
## Deprecated Resources and Data Sources 🔗 
Resources that have a migration path have deprecation guides available on how to rename and migrate them to their new replacements. Data sources don't have deprecation guide as you can directly replace them in their Terraform configuration and refresh the state.
"NA" in the following table means not applicable.
**Caution** Before executing any deprecation guide, ensure that you have backed up your Terraform state file to avoid any data loss.
Provider Version | Type | Old Deprecated Resource Name | New Resource Name | Migration? | Guide  
---|---|---|---|---|---  
4.103.0 | Data Source | `oci_adm_vulnerability_audit_application_dependency_vulnerability` | `oci_adm_vulnerability_audit_application_dependency_vulnerabities` | NA | NA  
4.103.0 | Data Source | `oci_apm_synthetics_public_vantage_point` | `oci_apm_synthetics_public_vantage_points` | NA | NA  
4.103.0 | Data Source | `oci_cloud_bridge_appliance_image` | `oci_cloud_bridge_appliance_images` | NA | NA  
4.103.0 | Data Source | `oci_cloud_guard_data_source_event` | `oci_cloud_guard_data_source_events` | NA | NA  
4.103.0 | Data Source | `oci_cloud_guard_problem_entity` | `oci_cloud_guard_problem_entities` | NA | NA  
4.103.0 | Data Source | `oci_cloud_migrations_migration_plan_available_shape` | `oci_cloud_migrations_migration_plan_available_shapes` | NA | NA  
4.103.0 | Data Source | `oci_data_labeling_service`/`data_labeling_service_annotation_format` | `oci_data_labeling_service_annotation_formats` | NA | NA  
4.103.0 | Data Source | `oci_data_safe_alert_policy_rule` | `oci_data_safe_alert_policy_rules` | NA | NA  
4.103.0 | Data Source | `oci_data_safe_audit_event_analytic` | `oci_data_safe_audit_event_analytics` | NA | NA  
4.103.0 | Data Source | `oci_data_safe_audit_profile_available_audit_volume` | `oci_data_safe_audit_profile_available_audit_volumes` | NA | NA  
4.103.0 | Data Source | `oci_data_safe_audit_profile_collected_audit_volume` | `oci_data_safe_audit_profile_collected_audit_volumes` | NA | NA  
4.103.0 | Data Source | `oci_data_safe_discovery_analytic` | `oci_data_safe_discovery_analytics` | NA | NA  
4.103.0 | Data Source | `oci_data_safe_masking_analytic` | `oci_data_safe_masking_analytics` | NA | NA  
4.103.0 | Data Source | `oci_data_safe_masking_reports_masked_column` | `oci_data_safe_masking_reports_masked_columns` | NA | NA  
4.103.0 | Data Source | `oci_database_management_db_management_private_endpoint_associated_database` | `oci_database_management_db_management_private_endpoint_associated_databases` | NA | NA  
4.103.0 | Data Source | `oci_database_management_job_executions_status` | `oci_database_management_job_executions_statuses` | NA | NA  
4.103.0 | Data Source | `oci_database_management_managed_database_sql_tuning_advisor_task` | `oci_database_management_managed_database_sql_tuning_advisor_tasks` | NA | NA  
4.103.0 | Data Source | `oci_database_management_managed_database_sql_tuning_advisor_tasks_finding` | `oci_database_management_managed_database_sql_tuning_advisor_tasks_findings` | NA | NA  
4.103.0 | Data Source | `oci_database_management_managed_database_sql_tuning_advisor_tasks_recommendation` | `oci_database_management_managed_database_sql_tuning_advisor_tasks_recommendations` | NA | NA  
4.103.0 | Data Source | `oci_database_management_managed_database_user_consumer_group_privilege` | `oci_database_management_managed_database_user_consumer_group_privileges` | NA | NA  
4.103.0 | Data Source | `oci_database_management_managed_database_user_data_access_container` | `oci_database_management_managed_database_user_data_access_containers` | NA | NA  
4.103.0 | Data Source | `oci_database_management_managed_database_user_object_privilege` | `oci_database_management_managed_database_user_object_privileges` | NA | NA  
4.103.0 | Data Source | `oci_database_management_managed_database_user_proxied_for_user` | `oci_database_management_managed_database_user_proxied_for_users` | NA | NA  
4.103.0 | Data Source | `oci_database_management_managed_database_user_role` | `oci_database_management_managed_database_user_roles` | NA | NA  
4.103.0 | Data Source | `oci_database_management_managed_databases_asm_property` | `oci_database_management_managed_databases_asm_properties` | NA | NA  
4.103.0 | Data Source | `oci_database_management_managed_databases_database_parameter` | `oci_database_management_managed_databases_database_parameters` | NA | NA  
4.103.0 | Data Source | `oci_database_management_managed_databases_user_proxy_user` | `oci_database_management_managed_databases_user_proxy_users` | NA | NA  
4.103.0 | Data Source | `oci_database_management_managed_databases_user_system_privilege` | `oci_database_management_managed_databases_user_system_privileges` | NA | NA  
4.103.0 | Data Source | `oci_devops_repository_author` | `oci_devops_repository_authors` | NA | NA  
4.103.0 | Data Source | `oci_devops_repository_path` | `oci_devops_repository_paths` | NA | NA  
4.103.0 | Data Source | `oci_em_warehouse_em_warehouse_etl_run` | `oci_em_warehouse_em_warehouse_etl_runs` | NA | NA  
4.103.0 | Data Source | `oci_fusion_apps_fusion_environment_time_available_for_refresh` | `oci_fusion_apps_fusion_environment_time_available_for_refreshs` | NA | NA  
4.103.0 | Data Source | `oci_golden_gate_message` | `oci_golden_gate_messages` | NA | NA  
4.103.0 | Data Source | `oci_golden_gate_trail_file` | `oci_golden_gate_trail_files` | NA | NA  
4.103.0 | Data Source | `oci_golden_gate_trail_sequence` | `oci_golden_gate_trail_sequences` | NA | NA  
4.103.0 | Data Source | `oci_jms_fleet_installation_site` | `oci_jms_fleet_installation_sites` | NA | NA  
4.103.0 | Data Source | `oci_opensearch_opensearch_version` | `oci_opensearch_opensearch_versions` | NA | NA  
4.103.0 | Data Source | `oci_opsi_awr_hub_awr_snapshot` | `oci_opsi_awr_hub_awr_snapshots` | NA | NA  
4.103.0 | Data Source | `oci_opsi_importable_compute_entity` | `oci_opsi_importable_compute_entities` | NA | NA  
4.103.0 | Data Source | `oci_optimizer_profile_level` | `oci_optimizer_profile_levels` | NA | NA  
4.103.0 | Data Source | `oci_optimizer_recommendation_strategy` | `oci_optimizer_recommendation_strategies` | NA | NA  
4.103.0 | Data Source | `oci_osp_gateway_invoices_invoice_line` | `oci_osp_gateway_invoices_invoice_lines` | NA | NA  
4.103.0 | Data Source | `oci_usage_proxy_subscription_product` | `oci_usage_proxy_subscription_products` | NA | NA  
4.103.0 | Data Source | `oci_usage_proxy_subscription_redemption` | `oci_usage_proxy_subscription_redemptions` | NA | NA  
4.103.0 | Data Source | `oci_usage_proxy_subscription_reward` | `usage_proxy_subscription_rewards` | NA | NA  
3.97.0 | Resource | `oci_dns_record` | `oci_dns_rrset` | NA | NA  
3.97.0 | Resource | `oci_dns_records` | `oci_dns_rrset` | NA | NA  
3.18 | Resource | `oci_autonomous_data_warehouse` | `oci_autonomous_database` | Yes | NA  
3.18 | Data Source | `oci_autonomous_data_warehouse` | `oci_autonomous_database` | NA | NA  
3.18 | Resource | `oci_autonomous_data_warehouse_backup` | `oci_autonomous_database_backup` | Yes | NA  
3.18 | Data Source | `oci_autonomous_data_warehouse_backup` | `oci_autonomous_database_backup` | NA | NA  
3.18 | Data Source | `oci_autonomous_data_warehouse_backups` | `oci_autonomous_database_backups` | NA | NA  
3.18 | Data Source | `oci_autonomous_data_warehouses` | `oci_autonomous_databases` | NA | NA  
2.1.12 | Resource | `oci_swift_password` | `oci_identity_auth_token` | No | NA  
2.1.12 | Data Source | `oci_swift_passwords` | `oci_identity_auth_tokens` | NA | NA  
Column | Details  
---|---  
Provider Version | Provider version in which said resource or data source was marked deprecated  
Type | Type of the deprecated resource or data source  
Old Deprecated Resource Name | Deprecated resource or data source name  
New Resource Name | New resource or data source name that provides the same functionality  
Migration? | If migration is possible to the new resource through Terraform `state` import  
Guide | Link to deprecation guide on how to rename and migrate to new resource, if applicable  
## Deprecated Fields 🔗 
Deprecation notices for fields can be found in any of the previously released [CHANGELOG](https://github.com/oracle/terraform-provider-oci/blob/master/CHANGELOG.md). Deprecated fields are also shown as deprecated during Terraform `plan` and `apply` jobs. In Resource Manager, look for these warning messages in the [job logs](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/get-job-logs.htm). For example:
`The 'size_in_mbs' field has been deprecated. Please use 'size_in_gbs'             instead.`
Was this article helpful?
YesNo


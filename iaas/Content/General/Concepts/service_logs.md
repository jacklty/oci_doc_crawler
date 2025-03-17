Updated 2024-01-10
# Service Logs
You can enable service logs for some resources. Service logs provide diagnostic information about the resources in your tenancy. When you enable logging on resources, you receive information about the resource in a log file. This information allows you to analyze, optimize, and troubleshoot your resources. 
## Working with Service Logs 🔗 
Not all resources support Logging. See [Supported Services](https://docs.oracle.com/iaas/Content/Logging/Concepts/service_logs.htm) for the list of services with resources that produce logs. 
To enable logs on a resource, you must have permission to update the resource and permission to create the log in the log group. See [Required Permissions for Working with Logs and Log Groups](https://docs.oracle.com/iaas/Content/Logging/Task/managinglogs.htm#required_permissions_logs_groups), and [Enabling Logging for a Resource](https://docs.oracle.com/iaas/Content/Logging/Task/enabling_logging.htm).
For more information about Logging, see [Logging Overview](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm).
## Using the API  🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
To enable logging for a resource using the API, use the appropriate resource's `create` or `update` operation. 
  * [Logging Management API](https://docs.oracle.com/iaas/api/#/en/logging-management/latest/)
  * [Logging Ingestion API](https://docs.oracle.com/iaas/api/#/en/logging-dataplane/latest/)
  * [Logging Search API](https://docs.oracle.com/iaas/api/#/en/logging-search/latest/)


Was this article helpful?
YesNo


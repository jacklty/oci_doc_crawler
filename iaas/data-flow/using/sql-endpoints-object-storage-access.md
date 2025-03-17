Updated 2025-02-12
# Object Storage Access
To access the data, the Data Flow SQL Endpoints need to have access to the Object Storage where the data is stored. To store the metadata, the Data Flow SQL Endpoint needs to have access to Metastore, where the metadata of the data is stored.
Allow the newly created SQL Endpoint to read buckets, manage objects, and read data. Create a dynamic group and add the following rules:
Copy
```
ALL {resource.compartment.id = ' _<compartment_id>_'}
ALLOW DYNAMIC-GROUP _<dynamic-group-name>_ to {CATALOG_METASTORE_EXECUTE, CATALOG_METASTORE_INSPECT, CATALOG_METASTORE_READ}
in tenancy WHERE ALL {request.principal.type='dataflowsqlendpoint'}
ALLOW DYNAMIC-GROUP _<dynamic-group-name>_ TO MANAGE objects IN TENANCY WHERE ALL {request.principal.type='dataflowsqlendpoint'}
ALLOW DYNAMIC-GROUP _<dynamic-group-name>_ TO MANAGE buckets IN TENANCY WHERE ALL {request.principal.type='dataflowsqlendpoint'}
```

Was this article helpful?
YesNo


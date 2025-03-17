Updated 2024-04-29
# Enabling Asynchronous Operations
Enable asynchronous operation in a Terraform configuration.
**Note** To prevent starting operations before asynchronous resources are fully created, make sure that the Terraform configuration does not code resource dependencies on asynchronous resources. For asynchronous resources, Terraform does not check the stage of a resource after initiating its creation or deletion. 
Even though Terraform uses multiple threads to run operations in parallel, each individual thread bringing a resource through its lifecycle states still needs to handle its operations synchronously. By default, when Terraform creates, updates, or deletes a resource it waits for that resource to reach its expected lifecycle state before proceeding. To avoid this waiting stage during Terraform operations, you can use an advanced option to create, update, or delete resources asynchronously.
To enable this feature, you can add the `async = true` flag to the resource. Terraform then considers `creating` or `deleting` as the target lifecycle stage. For example:
```
resource "oci_core_instance" "test_instance" {
 async        = true
 count        = var.num_instances
 availability_domain = data.oci_identity_availability_domain.ad.name
 compartment_id   = var.compartment_ocid
 display_name    = "TestInstance${count.index}"
 shape        = var.instance_shape
}
```

Use this feature for a faster way to create and delete resources in exchange for overriding Terraform's native behavior. When using the `async` option, consider that:
  * The state file doesn't have the full information of the resource because the resource is not yet created.
  * The resource's stage must be [refreshed](https://docs.oracle.com/iaas/Content/dev/terraform/async.htm#top__refresh-state) to get its full information, including whether the resource failed to be created.
  * Terraform does not check the stage of a resource again after initiating its creation or deletion. Failed operations are only shown in subsequent refreshes of the resource.
  * The asynchronous resource must have no dependencies, because the resource is not fully created before another operation begins.


**Important** The Terraform OCI provider currently supports the `async` flag for the `oci_core_instance` resource.
## Refreshing the State File 🔗 
When you run `terraform apply` and new resources use the `async` option, the state file is created with incomplete information for the resource. The state file includes many null values and the resource might be in the `PROVISIONING` state, for example:
```
...
"async": true,
...
"state": "PROVISIONING",
...
"private_ip": null,
"public_ip": null,
"subnet_id": null,
...
```

After the resource is created, you can run `terraform refresh`, `terraform plan`, or `terraform apply` to update the state file with complete resource information. The state file would be updated to look something like this:
```
...
"async": true,
...
"state": "RUNNING",
...
"private_ip": "10.255.255.254",
"public_ip": "192.0.2.2",
"subnet_id": "ocid1.subnet.oc1..exampleuniqueID",
...
```

Was this article helpful?
YesNo


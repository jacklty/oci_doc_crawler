Updated 2023-10-19
# Using Tags to Automatically Add User Names and Creation Dates to Resources
On Oracle Cloud Infrastructure (OCI), all resources are automatically tagged with the name of the user that created the resource and the time the resource was created. This task describes how to achieve the same result on Compute Cloud@Customer. 
This task can be done using either the Oracle Cloud Console or the CLI. Only the CLI is shown. Ensure that you create the tag namespace and tags in the OCI tenancy where the Compute Cloud@Customer infrastructure is located.
  1. Create the `Oracle-Tags` tag namespace.
Get the OCID of the compartment in which you want to create the tag namespace. Because the goal of this task is for these tag defaults to be applied to every resource in every compartment, create the tag namespace in the tenancy (root compartment). Use the following command to find the OCID of the tenancy:
```
$ oci iam compartment list --include-root
```

Create the tag namespace.
```
$ oci iam tag-namespace create -c ocid1.tenancy.**_unique_ID_** --name "Oracle-Tags" \
--description "OCI compatibility: add creator and create date of resource"
{
 "data": {
  "compartment-id": "ocid1.tenancy.**_unique_ID_**",
  "defined-tags": {},
  "description": "OCI compatibility: add creator and create date of resource",
  "freeform-tags": {},
  "id": "ocid1.tag_namespace.**_unique_ID_**",
  "is-retired": false,
  "lifecycle-state": "ACTIVE",
  "name": "Oracle-Tags",
  "time-created": "2022-06-07T14:51:23.256790+00:00"
 },
 "etag": "a000d250-3aea-4faf-b0e6-b6db486ffb42"
}
```

  2. Create a `CreatedBy` tag in the `Oracle-Tags` tag namespace.
Use the value of the `id` property from the `tag-namespace create` command for the tag namespace ID. The `--validator` option is not required.
```
$ oci iam tag create --tag-namespace-id ocid1.tag_namespace.**_unique_ID_** \
--name CreatedBy --description "user that created this resource" \
--validator '{"validator-type":"ENUM","values":["${iam.principal.name}"]}'
{
 "data": {
  "compartment-id": "ocid1.tenancy.**_unique_ID_**",
  "defined-tags": {},
  "description": "user that created this resource",
  "freeform-tags": {},
  "id": "ocid1.tag.**_unique_ID_**",
  "is-cost-tracking": false,
  "is-retired": false,
  "lifecycle-state": "ACTIVE",
  "name": "CreatedBy",
  "tag-namespace-id": "ocid1.tag_namespace.**_unique_ID_**",
  "tag-namespace-name": "Oracle-Tags",
  "time-created": "2022-06-07T15:32:22.226554+00:00",
  "validator": {
   "validator-type": "ENUM",
   "values": [
    "${iam.principal.name}"
   ]
  }
 },
 "etag": "fa18d128-fc7b-420d-87d6-c44a574e522a"
}
```

  3. Create a `CreatedOn` tag in the Oracle-Tags tag namespace.
```
$ oci iam tag create --tag-namespace-id ocid1.tag_namespace.**_unique_ID_** \
--name CreatedOn --description "date this resource was created" \
--validator '{"validator-type":"ENUM","values":["${oci.datetime}"]}'
```

  4. Create a `CreatedBy` tag default.
To apply this tag default to every new resource created in any compartment, create the tag default in the tenancy.
Use the value of the `id` property from Step 2 for the tag definition ID. The `--value` option is required.
```
$ oci iam tag-default create -c ocid1.tenancy.**_unique_ID_** 
--tag-definition-id ocid1.tag.**_unique_ID_** --value "\${iam.principal.name}"
{
 "data": {
  "compartment-id": "ocid1.tenancy.**_unique_ID_**",
  "id": "ocid1.tag_default.**_unique_ID_**",
  "is-required": null,
  "lifecycle-state": "ACTIVE",
  "tag-definition-id": "ocid1.tag.**_unique_ID_**",
  "tag-definition-name": "CreatedBy",
  "tag-namespace-id": "ocid1.tag_namespace.**_unique_ID_**",
  "time-created": null,
  "value": "${iam.principal.name}"
 },
 "etag": "None"
}
```

  5. Create a `CreatedOn` tag default.
Use the value of the `id` property from Step 3 for the tag definition ID.
```
$ oci iam tag-default create -c ocid1.tenancy.**_unique_ID_** 
--tag-definition-id ocid1.tag.**_unique_ID_** --value "\${oci.datetime}"
```



Whenever a new resource is created in the tenancy or any subcompartment of the tenancy, the following tags are applied, even if no tags are specified when the resource is created:
```
"defined-tags": {
 "Oracle-Tags": {
  "CreatedBy": "flast",
  "CreatedOn": "2022-06-07T16:09:47.01Z"
 }
}
```

For more information about CLI tag commands, refer to these CLI Reference pages:
  * [tag](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/tag.html)
  * [tag-default](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/tag-default.html)
  * [tag-namespace](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/tag-namespace.html)


Was this article helpful?
YesNo


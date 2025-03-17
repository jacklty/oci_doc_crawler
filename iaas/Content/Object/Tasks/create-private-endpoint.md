Updated 2025-01-22
# Creating a Private Endpoint in Object Storage
Create a private endpoint to reach Object Storage using a private IP address within your VCN without accessing the public internet.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/create-private-endpoint.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/create-private-endpoint.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/create-private-endpoint.htm)


  *     1. On the **Private Endpoints** list page, select **Create private endpoint**. If you need help finding the list page, see [Listing Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-private-endpoint.htm#top "View a list of the Object Storage private endpoints in a Oracle Cloud Infrastructure compartment.").
    2. Select **Create private endpoint**.
    3. Enter a **Name** for the private endpoint. The name value is a case-insensitive string using alpha-numeric characters (no special characters). 
    4. Enter a **DNS Prefix** for the private endpoint.
This value is part of the URL used to access Object Storage. The DNS prefix is a case-insensitive string using alpha-numeric characters (no special characters). It must be unique within the VCN.
    5. Select the VCN for your private endpoint from the **Select VCN in <compartment>** list.
    6. Select a **subnet** under the VCN from the list.
    7. Add an access target to the private endpoint. Enter the following information:
       * **Namespace** : Enter the namespace for the access target. You can enter either the namespace's name or "*" to specify a wildcard. You can only use the wildcard if the compartment and buckets values also specified as "*" as described below. See [Namespaces](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/understandingnamespaces.htm#namespaces "Learn about how to access and use your namespace for running Object Storage tasks.") for more information.
       * **Compartment OCID** : Enter the OCID of the compartment for the access target. You can enter either the compartment's OCID, or "*" to indicate all the compartments are available.
       * **Bucket name** : Enter the name of the bucket for the target. You can enter either the bucket's name, or "*" to indicate all the buckets within the compartments are available.
Select **Access target** to create another access target. You can create a total of 10 access targets.
    8. (Optional) Select **Show advanced options** to perform any of the following tasks under the**Advanced option** tab:
       * **IP Address** : Enter or select the IP address you prefer used with the private endpoint.
       * **+NSG** : Select to add a Network security group (NSG) to the private endpoint. Enter the name of the NSG from the list. The available NSGs are determined by the VCN you selected earlier.
       * **+Additional DNS prefix** : Select to add another DNS prefix to the private endpoint.
    9. (Optional) Select the **Tags** tab.
The Tagging options appear where you can apply tags to the resource. See [Tagging a Private Endpoint at Creation](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/tag-create-private-endpoint.htm#top "Add metadata to an Object Storage private endpoint when you first create it. This metadata enables you to define keys and values and associate them with resources.") for more information about using tagging with an Object Storage private endpoint. See [Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm) for general information about tagging.
    10. Select **Create**.
  * Use the [oci os private-endpoint create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/private-endpoint/create.html) command and required parameters to create a private endpoint in Object Storage:
Command
CopyTry It
```
oci os private-endpoint create --name name --compartment-id compartment_ocid --subnet-id subnet_ocid --prefix prefix --access-targets access_targets [OPTIONS]
```

where the following variables apply:
    * `prefix` is the DNS prefix of the private endpoint.
    * `access_targets` are listed in JSON format. Separate each access target with a comma (",").
For example:
```
oci os private-endpoint create --compartment-id ocid1.tenancy.oc1..exampleuniqueID --subnet-id ocid1.subnet.region1.sea..exampleuniqueID --name pe1 --prefix pe1 --access-targets '[{"namespace":"MyNamespace", "compartmentId":"*", "bucket":"*"}]'
{
 "opc-work-request-id": "99f4f963-cf65-49c4-8923-4e5210742105"
}
```

If you have several access targets, the output would appear as this:
```
oci os private-endpoint create --compartment-id ocid1.tenancy.oc1..exampleuniqueID --subnet-id ocid1.subnet.region1.sea..exampleuniqueID --name pe1 --prefix pe1 --access-targets '[{"namespace":"MyNamespace", "compartmentId":"*", "bucket":"*"}, {"namespace":"MyNamespace2", "compartmentId":"*", "bucket":"*"}]'
{
 "opc-work-request-id": "1f270b21-473e-4adf-8d13-5a35e8240d1e"
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the following API operation:
```
POST n/object_storage_namespace/pe/
```

These are the available payload properties:
    * **name** : The name of the private endpoint.
    * **compartmentId** : The ID of the compartment the private endpoint is created.
    * **subnetId** : The OCID of the customer's subnet where the private endpoint VNIC resides.
    * **prefix** : The DNS prefix to use for the private endpoint FQDN in the VCN's private DNS zone.
    * **accessTargets** : A list of targets that can be accessed by the private endpoint.
    * **additionalPrefixes** (optional): A list of more DNS prefixes that you can provide.
    * **privateEndpointIp** (optional): The private IP address to assign to this private endpoint if its available. Will return an error if IP address unavailable.
    * **nsgIds** (optional): A list of the OCIDs of the network security groups (NSGs) to add the private endpoint's VNIC.
    * **freeformTags** (optional): Free-form tags for this resource.
    * **definedTags** (optional): Defined tags for this resource. 


Was this article helpful?
YesNo


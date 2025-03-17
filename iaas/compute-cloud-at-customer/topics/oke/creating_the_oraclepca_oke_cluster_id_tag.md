Updated 2024-12-16
# Create the OraclePCA-OKE.cluster_id Tag 
The `OraclePCA-OKE.cluster_id` defined tag consists of an `OraclePCA-OKE` tag namespace with a `cluster_id` tag. This defined tag is required to create or update an OKE cluster or node pool. When you create a node pool, or update the node pool to add nodes, this tag is applied to every node to identify instances that need to be members of the dynamic group.
This procedure describes how to create the `OraclePCA-OKE` tag namespace and the `cluster_id` tag key. You must create both the tag namespace and the tag key.
**Important**
See the rules at the beginning of this topic.
The tag namespace name must be exactly `OraclePCA-OKE`, and the tag key name must be exactly `cluster_id`.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating_the_oraclepca_oke_cluster_id_tag.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating_the_oraclepca_oke_cluster_id_tag.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating_the_oraclepca_oke_cluster_id_tag.htm)


  *     1. If you're not already signed in to your tenancy, use the Oracle Cloud Console to sign in to your tenancy.
    2. Open the navigation menu and click **Governance & Administration**. Under **Tenancy Management** , click **Tag Namespaces**.
Ensure that the compartment that's selected is the compartment where you want to create the tag.
    3. If `OraclePCA-OKE` isn't shown in the Tag Namespaces list, click **Create Tag Namespace**. If the tag already exists, go to Step [5](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating_the_oraclepca_oke_cluster_id_tag.htm#creating_the_oraclepca_tag_using_the_console__cluster-id-step).
    4. Enter the following information:
       * **Namespace Definition Name** : Enter `OraclePCA-OKE`
       * **Description** : Enter a description for the tag namespace. For example, `Required to create or update an OKE cluster or node pool.` Avoid entering confidential information.
       * Click **Create Tag Namespace**.
The details page for the OraclePCA-OKE tag namespace is shown.
    5. On the details page, click **Create Tag Key Definition**.
Enter the following information:
       * **Tag Key** : Enter `cluster_id`
       * **Description** : Enter a description for the tag key. For example, `Required to create or update an OKE cluster or node pool.` Avoid entering confidential information.
       * In the **Tag Value Type** section:
         * **Static Value** : Ensure that **Static Value** is selected.
    6. Click **Create Tag Key Definition**.
**What's Next:**
[Create OraclePCA Tags For OKE](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/oke-creating_oraclepca_tags.htm#creating_oraclepca_tags "In your OCI tenancy that's associated with Compute Cloud@Customer, create specific defined tags to enable OKE attributes on Oracle Compute Cloud@Customer.")
  *     1. Use the [oci iam tag-namespace create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/tag-namespace/create.html) command and required parameters to create the `OraclePCA-OKE` tag namespace in your OCI tenancy.
**Note**
If the `OraclePCA-OKE` tag has already been created in a different compartment, then it's available to use in any other compartment, and you will receive an error message from this create tag namespace command.
Example:
Copy
```
$ oci iam tag-namespace create --compartment-id <compartment_OCID> --name OraclePCA-OKE --description "Required to create or update an OKE cluster or node pool."
{
 "data": {
  "compartment-id": "ocid1.compartment. _unique_ID_",
  "defined-tags": {
   "Oracle-Tags": {
    "CreatedBy": "okeuser",
    "CreatedOn": "2024-06-06T14:37:29.26Z"
   }
  },
  "description": "Required to create or update an OKE cluster or node pool.",
  "freeform-tags": {},
  "id": "ocid1.tag_namespace._unique_ID_",
  "is-retired": false,
  "lifecycle-state": "ACTIVE",
  "locks": null,
  "name": "OraclePCA-OKE",
  "time-created": "2024-06-06T14:37:29.357678+00:00"
 },
 "etag": "a86bcf9b-f9a3-4891-b632-37d490161fe5"
}
```

    2. Use the [oci iam tag create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/tag/create.html) and required parameters to create the `cluster_id` tag in the `OraclePCA-OKE` tag namespace.
Example:
Copy
```
$ oci iam tag create --tag-namespace-id <compartment_OCID> --name "cluster_id" --description "Required to create or update an OKE cluster or node pool."
--validator '{"validatorType": "DEFAULT"}'
{
 "data": {
  "compartment-id": " _unique_ID_",
  "defined-tags": {
   "Oracle-Tags": {
    "CreatedBy": "okeuser",
    "CreatedOn": "2024-06-06T21:36:51.38Z"
   }
  },
  "description": "Required to create or update an OKE cluster or node pool.",
  "freeform-tags": {},
  "id": "ocid1.tag._unique_ID_",
  "is-cost-tracking": false,
  "is-retired": false,
  "lifecycle-state": "ACTIVE",
  "name": "cluster_id",
  "tag-namespace-id": "ocid1.tag_namespace._unique_ID_",
  "tag-namespace-name": "OraclePCA-OKE",
  "time-created": "2024-06-06T21:36:51.456538+00:00",
  "validator": {
   "validator-type": "DEFAULT"
  }
 },
 "etag": "5bf59d9a-5998-4857-a590-fca2a3386cc2"
}
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**What's Next:**
[Create OraclePCA Tags For OKE](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/oke-creating_oraclepca_tags.htm#creating_oraclepca_tags "In your OCI tenancy that's associated with Compute Cloud@Customer, create specific defined tags to enable OKE attributes on Oracle Compute Cloud@Customer.")
  * Use the [CreateTagNamespace](https://docs.oracle.com/iaas/api/#/en/identity/latest/TagNamespace/CreateTagNamespace) operation to create the `OraclePCA-OKE` tag namespace in your OCI tenancy.
Use the [CreateTag](https://docs.oracle.com/iaas/api/#/en/identity/latest/Tag/CreateTag) operation to create the `cluster_id` tag in the `OraclePCA-OKE` tag namespace.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).
**What's Next:**
[Create OraclePCA Tags For OKE](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/oke-creating_oraclepca_tags.htm#creating_oraclepca_tags "In your OCI tenancy that's associated with Compute Cloud@Customer, create specific defined tags to enable OKE attributes on Oracle Compute Cloud@Customer.")


Was this article helpful?
YesNo


Updated 2025-03-04
# Object Storage Data Retention Rules
Learn how to use retention rules to preserve Object Storage data.
Retention rules are configured at the bucket level and are applied to all individual objects in the bucket.
It's important to understand retention duration for time-bound rules. Even though you are creating retention rules for a bucket, the duration of a rule is applied to each object in the bucket individually, and is based on the object's **Last Modified** timestamp. Let's say you have two objects in the bucket, ObjectX and ObjectY. ObjectX was last modified 14 months ago and ObjectY was last modified 3 months ago. You create a retention rule with a duration of 1 year. This rule prevents the modification or deletion of ObjectY for the next 9 months. The rule allows the modification or deletion of ObjectX because the retention rule duration (1 year) is less that the object's **Last Modified** timestamp (14 months). If ObjectX is overwritten some time in the coming year, modification and deletion would be prevented for the rule duration time remaining.
**Important**
Locking a retention rule is an irreversible operation. **Not even a tenancy administrator or Oracle Support can delete a locked rule.** There's a mandatory 14-day delay before a rule is locked. This delay lets you thoroughly test, modify, or delete the rule or the rule lock before the rule is permanently locked.
A rule is active at the time of creation. The lock only controls whether the rule itself can be modified. After a rule is locked, only increases in the duration are allowed. Object modification is prevented and the rule can only be deleted by deleting the bucket. A bucket must be empty before it can be deleted.
We recommend you set up notices for yourself for 7 days and 3 days before the 14-day period ends to remove the rule if you're not sure about using it.
For an independent assessment of the Object Storage retention rules feature's ability to meet regulatory requirements for record management and retention, see Cohasset Associate's [SEC 17a-4(f), FINRA 4511(c), CFTC 1.31(c)-(d) and MiFID II Compliance Assessment](https://www.oracle.com/a/ocom/docs/oracle-object-storage-compliance-assessment-report.pdf).
## Data Retention Rule Tasks 🔗 
You can perform the following data retention rules tasks:
  * [List the retention rules for a bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_list_retention_rules.htm#top "View a list of the retention rules for an Object Storage bucket.")
  * [Create a retention rule](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_create_a_retention_rule.htm#top "Create a retention rule for an Object Storage bucket.")
  * [Get a retention rule's details](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-Get_retention_rule.htm#top "View a retention rule's details for an Object Storage bucket.")
  * [Update a retention rule's settings](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_edit_a_retention_rule.htm#top "Update a retention rule for an Object Storage bucket.")
  * [Delete a retention rule from a bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_delete_a_retention_rule.htm#top "Delete a retention rule from an Object Storage bucket.")


## Retention Use Cases 🔗 
Object Storage provides a flexible approach to data retention that supports the following use cases: 
### Regulatory Compliance
Your industry might require you to retain a certain class of data for a defined length of time. Your data retention regulations might also require that you lock the retention settings. If you lock the settings, the only change you can make is to increase the retention duration.
For Object Storage regulatory compliance, you create a time-bound retention rule and specify a duration. Object modification and deletion are prevented for the duration specified. Duration is applied to each object individually, and is based on the object's **Last Modified** timestamp. Lock the rule as required.
### Data Governance
You might need to protect certain data sets as a part of internal business process requirements. While retaining the data for a defined length of time is necessary, that time period could change.
For Object Storage data governance, you create a time-bound retention rule and specify a duration. Object modification and deletion are prevented for the duration specified. Duration is applied to each object individually, and is based on the object's **Last Modified** timestamp. To be able to delete the rule and allow changes to the duration as required, don't lock the rule.
### Legal Hold
You might need to preserve certain business data in response to potential or on-going lawsuits. A legal hold does not have a defined retention period and remains in effect until removed.
For Object Storage legal holds, you create an indefinite retention rule. Object modification and deletion are prevented until you delete the rule. You cannot lock an indefinite retention rule because the rule has no duration.
## Required IAM Policies 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
If you're new to policies, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).
For administrators:
  * You can create a policy that lets the specified IAM group manage Object Storage namespaces, buckets, and their associated objects in all compartments in the tenancy. For example, to let the IAM group StorageAdmins do everything in the tenancy:
Copy
```
Allow group StorageAdmins to manage object-family in tenancy
```

  * Alternatively, you can create policies that reduce the scope of access. For example, you can create the policies to let the StorageAdmins group manage only buckets and objects in a compartment called ObjectStore in the tenancy:
Copy
```
Allow group StorageAdmins to manage buckets in compartment ObjectStore
Allow group StorageAdmins to manage objects in compartment ObjectStore
```

  * If you create more restrictive policies that grant individual permissions, BUCKET_UPDATE and RETENTION_RULE_MANAGE is required to create, edit, and delete retention rules. BUCKET_UPDATE, RETENTION_RULE_MANAGE, and RETENTION_RULE_LOCK is required to lock retention rules.


For more information about other alternatives for writing policies, see [Details for Object Storage, Archive Storage, and Data Transfer](https://docs.oracle.com/iaas/Content/Identity/policyreference/objectstoragepolicyreference.htm).
## Scope and Constraints 🔗 
  * Retention rules can be applied to a bucket in the Standard ([Object Storage](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorageoverview.htm#overview "Learn how to use Object Storage to store and easily access an unlimited amount of data at low cost.")) or [Archive Storage](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm) tier.
  * The actions that you can perform on a bucket with active retention rules are limited. You cannot update, overwrite, or delete objects or object metadata until the retention rule is deleted (indefinite rule) or for the duration specified (time-bound rules). The duration for time-bound rules is applied to each object individually, and is based on the object's Last Modified timestamp.
  * You can create multiple retention rules for a bucket. Indefinite retention rule is applied before any time-bound rule is considered.
  * When a retention rule is locked, the rule can only be deleted by deleting the bucket. A bucket must be empty before it can be deleted.


## Interaction Between Retention and Other Object Storage Features 🔗 
Carefully review the policies and rules that you have in place for the other Object Storage features that you are using. Some of these policies and rules may no longer make sense with retention rules. This section describes some key things you need to know about the interaction between retention rules and other Object Storage features. 
### Bucket Re-Encryption
Retention rules do not block bucket re-encryption using either Oracle or your own Vault master encryption keys. 
### Multipart Uploads
Uncommitted (unfinished or failed) multipart uploads are not protected by retention rules and can be deleted at any time.
### Lifecycle Management
  * Lifecycle policies can update the storage tier of objects protected by retention rules.
  * Lifecycle Management can't remove objects protected by active retention rules.


### Replication
  * You can create retention rules on a replication source bucket.
  * You cannot create retention rules on a replication destination bucket.
  * You cannot enable replication on a destination bucket that has retention rules.


### Versioning
  * You cannot add retention rules to a bucket that has versioning enabled.
  * You cannot enable versioning on a bucket with active retention rules.
  * You can add retention rules to bucket that has versioning suspended. However, you cannot resume versioning with active retention rules.


Was this article helpful?
YesNo


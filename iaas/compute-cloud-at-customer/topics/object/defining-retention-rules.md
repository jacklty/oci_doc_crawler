Updated 2023-08-15
# Defining Retention Rules
On Compute Cloud@Customer, retention rules provide immutable storage options for data written to Object Storage for data governance, regulatory compliance, and legal hold requirements. Retention rules can also protect your data from accidental or malicious writes or deletion. Retention rules can be locked to prevent rule modification and data deletion or modification even by administrators.
Retention rules are configured at the bucket level and are applied to all individual objects in the bucket.
Object Storage provides a flexible approach to data retention that supports the following use cases.
  * **Regulatory Compliance**
Your industry might require you to retain a certain class of data for a defined length of time. Your data retention regulations might also require that you lock the retention settings. If you lock the settings, the only change you can make is to increase the retention duration.
For Object Storage regulatory compliance, you create a time-bound retention rule and specify a duration. Object modification and deletion are prevented for the duration specified. Duration is applied to each object individually, and is based on the object's Last Modified timestamp. Lock the rule as required.
  * **Data Governance**
You might need to protect certain datasets as a part of internal business process requirements. While retaining the data for a defined length of time is necessary, that time period could change.
Create a time-bound retention rule and specify a duration. Object modification and deletion are prevented for the duration specified. Duration is applied to each object individually, and is based on the object's Last Modified timestamp. To be able to delete the rule and allow changes to the duration as required, do not lock the rule.
  * **Legal Hold**
You might need to preserve certain business data in response to potential or on-going lawsuits. A legal hold does not have a defined retention period and remains in effect until removed.
For Object Storage legal holds, you create an indefinite retention rule. Object modification and deletion are prevented until you delete the rule. You can't lock an indefinite retention rule because the rule has no duration.


It's important to understand retention duration for time-bound rules. Even though you are creating retention rules for a bucket, the duration of a rule is applied to each object in the bucket individually, and is based on the object's Last Modified timestamp. Let's say you have two objects in the bucket, ObjectX and ObjectY. ObjectX was last modified 14 months ago and ObjectY was last modified 3 months ago. You create a retention rule with a duration of 1 year. This rule prevents the modification or deletion of ObjectY for the next 9 months. The rule allows the modification or deletion of ObjectX because the retention rule duration (1 year) is less that the object's Last Modified timestamp (14 months). If ObjectX is overwritten some time in the coming year, modification and deletion would be prevented for the rule duration time remaining.
**Locking a retention rule is an irreversible operation**. Not even a tenancy administrator can delete a locked rule. There is a mandatory 14-day delay before a rule is locked. This delay lets you thoroughly test, modify, or delete the rule or the rule lock before the rule is permanently locked. A rule is active at the time of creation. The lock only controls whether the rule itself can be modified. After a rule is locked, only increases in the duration are allowed. Object modification is prevented and the rule can only be deleted by deleting the bucket. A bucket must be empty before it can be deleted.
## Scope and Constraints 🔗 
  * Retention rules can be applied to a bucket in the Object Storage.
  * The actions that you can perform on a bucket with active retention rules are limited. You can't update, overwrite, or delete objects or object metadata until the retention rule is deleted (indefinite rule) or for the duration specified (time-bound rules). The duration for time-bound rules is applied to each object individually, and is based on the object's Last Modified timestamp.
  * You can create multiple retention rules for a bucket. Indefinite retention rule is applied before any time-bound rule is considered.
  * When a retention rule is locked, the rule can only be deleted by deleting the bucket. A bucket must be empty before it can be deleted.


## Interaction Between Retention and Other Object Storage Features 🔗 
Carefully review the policies and rules that you have in place for the other Object Storage features that you are using. Some of these policies and rules might not make sense with retention rules. This section describes some key things you need to know about the interaction between retention rules and other Object Storage features. 
**Multipart Uploads**
Uncommitted (unfinished or failed) multipart uploads are not protected by retention rules and can be deleted at any time.
**Versioning**
  * You can't add retention rules to a bucket that has versioning enabled.
  * You can't enable versioning on a bucket with active retention rules.
  * You can add retention rules to bucket that has versioning suspended. However, you can't resume versioning with active retention rules.


Was this article helpful?
YesNo


Updated 2023-10-19
# Troubleshooting Retention Rules
Identify and address common issues that can occur while working with Object Storage retention rules on Compute Cloud@Customer.
## Unable to Create a Retention Rule 🔗 
If creating a retention rule fails, the most likely cause is missing or incomplete IAM permissions. Rule creation requires:
  * User permissions that let you access the bucket and manage the objects in those buckets. 
  * Minimally, BUCKET_UPDATE and RETENTION_RULE_MANAGE permissions. 
  * Minimally, BUCKET_UPDATE and RETENTION_RULE_MANAGE permissions. 


## Unable to Lock a Retention Rule 🔗 
If locking a retention rule fails, the most likely cause is missing or incomplete IAM permissions. Minimally, BUCKET_UPDATE, RETENTION_RULE_MANAGE, and RETENTION_RULE_LOCK permissions are required to lock retention rules.
## Unable to Delete a Retention Rule 🔗 
You can't delete a time-bound retention rule that's locked. When a retention rule is locked, the rule can only be deleted by deleting the bucket. A bucket must be empty before it can be deleted.
If deleting an indefinite retention rule fails, the most likely cause is missing or incomplete IAM permissions. Rule deletion requires:
  * User permissions that let you access the bucket and manage the objects in those buckets. 
  * Minimally, BUCKET_UPDATE and RETENTION_RULE_MANAGE permissions. 


Was this article helpful?
YesNo


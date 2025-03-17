Updated 2024-04-13
# Troubleshooting Object Storage Retention Rules
Learn troubleshooting solutions for issues you might encounter using retention rules.
## Unable to create a retention rule 🔗 
If creating a retention rule fails, the most likely cause is missing or incomplete IAM permissions. Rule creation requires the following:
  * User permissions that let you access the bucket and manage the objects in those buckets. 
  * Minimally, BUCKET_UPDATE and RETENTION_RULE_MANAGE permissions. 


Review the existing policies that grant user permissions. For more information, see [Required IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules.htm#Permissions).
## Unable to lock a retention rule 🔗 
If locking a retention rule fails, the most likely cause is missing or incomplete IAM permissions. Minimally, BUCKET_UPDATE, RETENTION_RULE_MANAGE, and RETENTION_RULE_LOCK permissions are required to lock retention rules.
Review the existing policies that grant user permissions. For more information, see [Required IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules.htm#Permissions).
## Unable to delete a retention rule 🔗 
You cannot delete a time-bound retention rule that is locked. When a retention rule is locked, the rule can only be deleted by deleting the bucket. A bucket must be empty before it can be deleted.
If deleting an indefinite retention rule fails, the most likely cause is missing or incomplete IAM permissions. Rule deletion requires:
  * User permissions that let you access the bucket and manage the objects in those buckets. 
  * Minimally, BUCKET_UPDATE and RETENTION_RULE_MANAGE permissions. 


Was this article helpful?
YesNo


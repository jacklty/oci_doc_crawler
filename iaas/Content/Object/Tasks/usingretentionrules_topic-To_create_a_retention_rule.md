Updated 2025-03-04
# Creating an Object Storage Retention Rule
Create a retention rule for an Object Storage bucket.
**Important**
Locking a retention rule is an irreversible operation. **Not even a tenancy administrator or Oracle Support can delete a locked rule.** There's a mandatory 14-day delay before a rule is locked. This delay lets you thoroughly test, modify, or delete the rule or the rule lock before the rule is permanently locked.
A rule is active at the time of creation. The lock only controls whether the rule itself can be modified. After a rule is locked, only increases in the duration are allowed. Object modification is prevented and the rule can only be deleted by deleting the bucket. A bucket must be empty before it can be deleted.
We recommend you set up notices for yourself for 7 days and 3 days before the 14-day period ends to remove the rule if you're not sure about using it.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_create_a_retention_rule.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_create_a_retention_rule.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_create_a_retention_rule.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Retention Rules**.
    3. Select **Create Rule**.
    4. Enter the following information:
       * **Name** : Enter a name for the rule. The system generates a rule name that reflects the current year, month, day, and time, for example, **retention-rule-20200229-1002**. If you change this name, use letters, numbers, dashes, underscores, and periods.
       * **Retention Type** : Select the retention rule type that you want to create:
         * **Time-Bound** rules have a user-defined duration. Object modification is prevented for the duration specified. Duration is applied to each object individually, and is based on the object's **Last Modified** timestamp. Enter values for the **Retention Duration** settings that appear.
         * **Indefinite** rules have no duration or expiration. Object modification is prevented until an indefinite rule is deleted.
       * **Retention Duration** : (Time-Bound type rules only) Enter values for the **Retention Time Amount** time amount and **Retention Time Unit** time unit in **Days** or **Years**.
       * **Enable Retention Rule Lock** : (optional) Select the check box to lock the rule. When a rule is locked, only an increase in the retention duration is allowed and the rule can only be deleted by deleting the bucket. A bucket must be empty to be deleted.
    5. Select **Create**.
The rule is displayed in the **Retention Rules** list.
  * Use the [oci os retention-rule create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/retention-rule/create.html) command and required parameters to create a retention rule for a bucket:
Command
CopyTry It
```
oci os retention-rule create --bucket-name bucket_name [OPTIONS]
```

For example:
```
oci os retention-rule create --display-name LegalHold
{
 "data": {
  "duration": null,
  "etag": "7f51ef6c-3fca-48f7-9060-c129911c1a50",
  "id": "5772c87f-6723-4ecc-b44c-bef86643be92",
  "time-created": "2020-03-25T14:53:20.792000+00:00",
  "time-modified": "2020-03-25T14:53:20.792000+00:00",
  "time-rule-locked": null
 },
 "etag": "7f51ef6c-3fca-48f7-9060-c129911c1a50"
}
```

#### Giving the Retention Rule a Display Name 🔗 
Include the `display-name` parameter to give a user-specified name for the retention rule. Names can be helpful in identifying retention rules. For example:
```
oci os retention-rule create --bucket-name MyBucket --display-name LegalHold
{
 "data": {
  "display-name": "LegalHold",
  "duration": null,
  "etag": "7f51ef6c-3fca-48f7-9060-c129911c1a50",
  "id": "5772c87f-6723-4ecc-b44c-bef86643be92",
  "time-created": "2020-03-25T14:53:20.792000+00:00",
  "time-modified": "2020-03-25T14:53:20.792000+00:00",
  "time-rule-locked": null
 },
 "etag": "7f51ef6c-3fca-48f7-9060-c129911c1a50"
}
```

#### Creating a Time-Bound Retention Rule 🔗 
Include the `time-amount` and `time-unit` parameters to set a time period in days or years for how long the retention rule applies. For example:
```
oci os retention-rule create --bucket-name MyBucket --time-amount 5 --time-unit days
{
 "data": {
  "duration": {
   "time-amount": 5,
   "time-unit": "DAYS"
  },
  "etag": "efb9178f-4213-49f7-878d-7bbe57decc0b",
  "id": "89f4ca0c-4ad9-4fa5-8005-95e7741c531c",
  "time-created": "2020-03-25T15:08:01.601000+00:00",
  "time-modified": "2020-03-25T15:08:01.601000+00:00",
  "time-rule-locked": null
 },
 "etag": "efb9178f-4213-49f7-878d-7bbe57decc0b"
}
```

If you don't specify a time amount and unit, there is no time limit and the objects in the bucket are preserved indefinitely.
#### Locking the Retention Rule 🔗 
Include the `time-rule-locked` parameter and a date timestamp after which this rule is locked and can only be deleted by deleting the bucket. For example:
```
oci os retention-rule create --bucket-name MyBucket --time-rule-locked 2017-09-15T20:30:00.123Z
{
 "data": {
  "etag": "efb9178f-4213-49f7-878d-7bbe57decc0b",
  "id": "89f4ca0c-4ad9-4fa5-8005-95e7741c531c",
  "time-created": "2020-03-25T15:08:01.601000+00:00",
  "time-modified": "2020-03-25T15:08:01.601000+00:00",
  "time-rule-locked": 2017-09-15T20:30:00.123Z
 },
 "etag": "efb9178f-4213-49f7-878d-7bbe57decc0b"
}
```

See [oci os retention-rule create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/retention-rule/create.html) for the supported date timestamp formats you can use with this parameter. 
After a rule is locked, only increases in the duration are allowed and no other properties can be changed. You can't update this property for rules that are in a locked state. Specifying it when a duration isn't specified is considered an error.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateRetentionRule](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/RetentionRule/CreateRetentionRule) operation to create a retention rule for a bucket.


Was this article helpful?
YesNo


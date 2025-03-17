Updated 2025-01-30
# Creating the Object Lifecycle Policy in Object Storage
Create the object lifecycle policy for an Object Storage bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_create_a_lifecycle_policy_rule.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_create_a_lifecycle_policy_rule.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_create_a_lifecycle_policy_rule.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Lifecycle Policy Rules**.
    3. Select **Create Rule**.
The Console checks the IAM policies that are in place to perform this task successfully. If you see a policy missing warning, you can let the Console try to create any missing policies or copy the missing policy details to the clipboard to email your administrator. If you have the required policies in place, create the lifecycle policy rule.
    4. Enter the following information:
       * **Name** : Enter a name or accept the default system name. The system generates a rule name that reflects the current year, month, day, and time, for example, **lifecycle-rule-20190321-1559**. If you change this name, use letters, numbers, dashes, underscores, and periods.
       * **Target** : Select the target to which the lifecycle rule applies:
         * If object versioning is disabled, select **Objects** or **Uncommitted Multipart Uploads**.
         * If object versioning is enabled or suspended, select **Latest Version of Objects** , **Previous Versions of Objects** , or **Uncommitted Multipart Uploads**.
       * **Lifecycle Action** : Select one of the following actions:
         * If the rule target is **Objects** , **Latest Version of Objects** , or **Previous Versions of Objects** , select **Move to Archive** , Move to Infrequent Access, or **Delete**. If auto-tiering is enabled on the bucket, **Move to Infrequent Access** isn't available for selection.
         * If the rule target is **Uncommitted Multipart Uploads** , **Delete** is the only option and is selected by default.
       * **Number of Days** : Enter the number of days until the specified action is taken.
**Note**
If the rule archives or deletes a previous object version, the "number of days" countdown is based on when the object version transitioned from being the latest object version to being a previous object version. You can determine this time by looking at the "last modified" time of the previous most recent version of the object.
    5. If the rule target is **Objects** , **Latest Version of Objects** , or **Previous Versions of Objects** , you can optionally add one or more object name filters to specify which objects the lifecycle rule applies to. You can choose objects or object versions by using [prefixes](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm#PrefixesOLM) and [pattern matching](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm#PatternsOLM). If no object name filters are specified, the rule applies to all objects in the bucket. 
To create an object name filter:
      1. Select **Add Filter**.
      2. Select the filter type.
      3. Enter the filter value.
    6. Use the **State** switch to specify whether the rule is enabled or disabled after it's created.
    7. Select **Create**.
**Tip**
From the **Actions** menu for the lifecycle policy rule you want, select **Enable** or **Disable** to enable or disable the rule.
The rule appears in the **Lifecycle Policy Rules** list.
  * Use the [oci os object-lifecycle-policy put](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object-lifecycle-policy/put.html) command and required parameters to create the object lifecycle policy for a bucket:
Command
CopyTry It
```
oci os object-lifecycle-policy put --bucket-name bucket_name [OPTIONS]
```

#### Specifying the Lifecycle Policy Rules 🔗 
Use the `items` parameter to specify the bucket's set of lifecycle policy rules:
```
oci os object-lifecycle-policy put --bucket-name bucket_name --items json_formatted_lifecycle_policy

```

The `items` parameter requires that you provide key-value pair input as valid formatted JSON. See [Passing Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#Managing_CLI_Input_and_Output) and [Using a JSON File for Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON) for information about JSON formatting.
The `items` key-value pair input must specify the following:```
[
  {
   "action": "string",
   "isEnabled": true,
   "name": "string",
   "objectNameFilter": {
    "exclusionPatterns": [
     "string",
     "string"
    ],
    "inclusionPatterns": [
     "string",
     "string"
    ],
    "inclusionPrefixes": [
     "string",
     "string"
    ]
   },
   "target": "string",
   "timeAmount": 0,
   "timeUnit": "string"
  }
 ]
```

Specify one of the following values for `action`: 
Value | Description  
---|---  
`ARCHIVE` | Specify this action to move objects, object versions, or previous object versions to the [Archive](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topi-Archive) tier.  
`INFREQUENT_ACCESS` | Specify this action to move objects, object versions, or previous object versions to the [Infrequent Access](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topic-Infrequent_Access) tier. If Auto-Tiering is enabled on the bucket, you can't specify `INFREQUENT_ACCESS`.  
`DELETE` | Specify this action to delete objects, object versions, or object versions.  
`ABORT` | Use this action to delete failed or incomplete multipart uploads.  
Specify one of the following values for `target`: 
Value | Description  
---|---  
`objects` | Use this action to move objects, object versions, or previous object versions to the [Archive](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topi-Archive) tier.  
`object-versions` | Use this action to move objects, object versions, or previous object versions to the [Infrequent Access](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm#understandingobjectstoragetiers_topic-Infrequent_Access) tier.  
`multipart-uploads` | Use this action to delete objects, object versions, or previous object versions.  
Specify `timeUnit` in days.
The following example creates or replaces a lifecycle policy that includes a rule for moving previous object versions with names that include the pattern `*.doc` from the Standard tier to the Archive tier after 60 days. The policy also includes a rule that deletes previous object versions after 180 days.
Command
CopyTry It
```
oci os object-lifecycle-policy put --bucket-name MyStandardBucket --items
'[
   {
    "action": "ARCHIVE",
    "is-enabled": true,
    "name": "Move-to-Archive-Rule",
    "object-name-filter": {
     "exclusion-patterns": null,
     "inclusion-patterns": [
      "*.doc"
     ],
     "inclusion-prefixes": null
    },
    "target": "previous-object-versions",
    "time-amount": 60,
    "time-unit": "DAYS"
   },
   {
    "action": "DELETE",
    "is-enabled": true,
    "name": "Delete-Rule",
    "object-name-filter": {
     "exclusion-patterns": null,
     "inclusion-patterns": [
      "*.doc"
     ],
     "inclusion-prefixes": null
    },
    "target": "previous-object-versions",
    "time-amount": 180,
    "time-unit": "DAYS"
   }
]'
```

The following example creates or replaces a lifecycle policy that includes a rule for moving all objects from the Standard tier to the Infrequent Access tier after 45 days. The policy also includes a rule that moves all objects to the Archive tier after 90 days.
Command
CopyTry It
```
oci os object-lifecycle-policy put --bucket-name MyStandardTierBucket --items
'[
   {
    "action": "INFREQUENT_ACCESS",
    "is-enabled": true,
    "name": "Move-to-Infrequent-Access-Rule",
    "object-name-filter": null,
    "target": "objects",
    "time-amount": 45,
    "time-unit": "DAYS"
   },
   {
    "action": "ARCHIVE",
    "is-enabled": true,
    "name": "Move-to-Archive-Rule",
    "object-name-filter": null,
    "target": "objects",
    "time-amount": 90,
    "time-unit": "DAYS"
   }
]'
```

The following example creates or replaces a lifecycle policy rule that deletes previous object versions from the Archive tier after 240 days. 
```
oci os object-lifecycle-policy put --bucket-name MyArchiveTierBucket --items
'[
  {
    "action": "DELETE", 
    "is-enabled": true, 
    "name": "Delete-from-Archive-Rule", 
    "object-name-filter": null,
    "target": "previous-object-versions",
    "time-amount": 240, 
    "time-unit": "DAYS"
   }
]'
```

The following example creates or replaces a lifecycle policy rule that deletes all uncommitted or failed multipart uploads after 5 days:
```
oci os object-lifecycle-policy put --bucket-name MyBucket --items
'[
  {
    "action": "ABORT", 
    "is-enabled": true, 
    "name": "Delete-Failed-Multipart-Uploads-Rule", 
    "object-name-filter": null,
    "target": "multipart-uploads",
    "time-amount": 5, 
    "time-unit": "DAYS"
   }
]'
```

Instead of using the `items` option, you can pass the JSON key-value pairs in a file. For example:
Command
CopyTry It
```
oci os object-lifecycle-policy put --bucket-name MyStandardTierBucket --file /path/to/file/filename
```

##### Using Windows 🔗 
On Windows, to pass complex input to the CLI as a JSON string, you must enclose the entire block in double quotes. Inside the block, each double quote for the key and value strings must be escaped with a backslash (\\) character.
For example:
Command
CopyTry It
```
oci os object-lifecycle-policy put --bucket-name MyStandardTierBucket --items "[{\"action\":\"ARCHIVE\",\"isEnabled\":true,\"name\":\"move-to-Archive-rule\",\"target\":\"previous-object-versions\",\"timeAmount\":180,\"timeUnit\":\"DAYS\"}]"
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [PutObjectLifecyclePolicy](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/ObjectLifecyclePolicy/PutObjectLifecyclePolicy) operation to create the object lifecycle policy for a bucket.


Was this article helpful?
YesNo


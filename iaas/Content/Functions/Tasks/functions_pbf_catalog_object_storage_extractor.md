Updated 2025-02-24
# Object Storage File Extractor Function
_Find out how to use the Object Storage File Extractor pre-built function in OCI Functions to read a zip file from an OCI Object Storage bucket and extract it to the specified target bucket._
## Common Usage Scenarios 🔗 
Common ways to use the Object Storage File Extractor function include:
  * Place a zip in object storage and use Data Integration to unzip the file and store the result in object storage.
  * Place a zip in object storage and directly invoke the function to unzip the files and store the result in object storage.


Services related to the Object Storage File Extractor function include:
  * [Data Integration](https://docs.oracle.com/iaas/data-integration/home.htm)
  * [Object Storage](https://docs.oracle.com/iaas/Content/Object/home.htm)


## Scope 🔗 
Scope considerations for this function include:
  * The pre-built function works best if the default timeout is set to 300 seconds.


## Prerequisites and Recommendations 🔗 
The following are best practices when using this pre-built function:
  * Set the pre-built function timeout to 300 seconds.
  * The VCN linked to the application facilitates access to other OCI services by using a Service Gateway, Internet Gateway, or NAT gateway.
  * Set the default memory size to the maximum memory allowed for a function.


## Configuring the Object Storage File Extractor Function 🔗 
To configure an Object Storage File Extractor function, perform the following steps:
  1. On the **Pre-Built Functions** page, select **Object Storage File Extractor** , and then select **Create function**.
  2. Configure the **Name** , **Compartment** , and **Application** as follows:
     * **Name:** A name of your choice for the new function. The name must start with a letter or underscore, followed by letters, numbers, hyphens, or underscores. Length can be 1–255 characters. Avoid entering confidential information.
To create the function in a different compartment, select **Change Compartment**.
     * **Application:** Select the application in which you want to create the function.
If a suitable application doesn't already exist in the current compartment, select **Create new application** and specify the following details:
       * **Name:** A name for the new application. Avoid entering confidential information.
       * **VCN:** The VCN (virtual cloud network) in which to run functions in the application. Optionally, select **Change Compartment** to select a VCN from a different compartment.
       * **Subnets:** The subnet (or subnets, up to a maximum of three) in which to run functions. Optionally, select **Change Compartment** to select a subnet from a different compartment.
       * **Shape:** The processor architecture of the compute instances on which to deploy and run functions in the application. All the functions in the application are deployed and run on compute instances with the same architecture. The function's image must contain the necessary dependencies for the architecture you select.
       * **Tagging options:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
  3. Configure the IAM policy for pre-built functions.
By default, OCI Functions creates a dynamic group and an IAM policy with the policy statements required to run the pre-built function. Make no changes to accept the default behavior.
If you don't want OCI Functions to automatically create the dynamic group and policy, select **Do not create a dynamic group and IAM policy**.
**Important** If you select the **Do not create a dynamic group and IAM policy** option, you must define the dynamic group and the IAM policy yourself. For more information, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_object_storage_extractor.htm#pbf-object-storage-extractor-policies-plus__permissions-object-extractor).
  4. Configure function memory and timeout values as follows:
     * **Memory:** The maximum amount of memory that the function can use while running, in megabytes. This is the memory available to the function image. (Default: 256 MB)
     * **Timeout:** The maximum amount of time that the function can run for, in seconds. If the function doesn’t complete in the specified time, the system cancels the function. (Default: 300)
  5. (Optional) Configure **Provisioned concurrency** to minimize any initial delays when invoking the function by specifying a minimum number of concurrent function invocations for which you want to have execution infrastructure constantly available. (Default: Not selected)
If selected, specify the number of provisioned concurrency units assigned to this function. **Default:** 10.
For more information about provisioned concurrency, see [Reducing Initial Latency Using Provisioned Concurrency](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingprovisionedconcurrency.htm#functionsusingprovisionedconcurrency "Find out how to use provisioned concurrency to minimize initial delays when invoking functions in OCI Functions.").
  6. Set the function configuration parameters as described in [Configuration Parameters](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_catalog_object_storage_extractor.htm#pbf-object-storage-extractor-policies-plus__configuration-parameters-object-extractor).
  7. Optionally enter any tags in the **Tagging options** section. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
  8. Select **Create**.


The deploy dialog displays the tasks to deploy the function (see [Finishing Pre-Built Function Deployment](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_finishing_prebuilt_deploy.htm#pbf-final-deploy-steps "Find out how to complete pre-built function deployment in OCI Functions, and find out about the different deployment states shown in the deployment dialog.")).
## Configuration Options 🔗 
### Configuration Parameters 🔗 
Name | Description | Required  
---|---|---  
`PBF_LOG_LEVEL` | Logging level, options are `DEBUG`, `INFO`, `WARN`, and `ERROR`. Defaults to INFO. | No  
### Permissions 🔗 
Running a function requires certain IAM policies. If you selected the **Do not create a dynamic group and IAM policy** option when creating the function, you must define the dynamic group and the IAM policy yourself.
To set the proper policies, perform the following steps:
  * Create a dynamic group with the rule: 
Copy
```
ALL {resource.id = '<function_ocid>', resource.compartment.id = '<compartment_ocid>'}
```

  * Configure an IAM policy using the dynamic group: 
Copy
```
Allow dynamic-group <dynamic-group-name> to read objectstorage-namespaces in compartment <compartment-name>
Allow dynamic-group <dynamic-group-name> to manage objects in compartment <compartment-name>
Allow dynamic-group <dynamic-group-name> to manage buckets in compartment <compartment-name>
Allow dynamic-group <dynamic group name> to read compartments in compartment <compartment-name>
```



**Note** Replace `<function-ocid>` with the OCID of the function that you created in preceding steps. 
**Note** Replace `<dynamic-group-name>` with the name of the dynamic group that you created using the function's OCID.
**Note** Replace `<compartment_ocid>` with the OCID of the compartment that contains the function.
### Invoking This Function 🔗 
You can invoke the function in the following ways:
  * Invoke the function directly as documented in [Invoking Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm) by creating a request body as shown in the following JSON example.
  * Invoke the function through Data Integration. Leverage the REST API task to configure the invoke endpoint with request body along with parameters to trigger the function. The REST body adheres to the following JSON values.


**HTTP Request JSON Values**
Name | Description | Required  
---|---|---  
COMPARTMENT_ID | Compartment OCID of the source bucket. | Yes  
REGION | The region in which the buckets exist. Defaults to the region in which the function is created. | No  
SOURCE_BUCKET | Name of the source bucket which contains the zip file. | Yes  
ZIP_FILE_NAME | Name of the zip file. | Yes  
TARGET_BUCKET | Name of the target bucket. If the target bucket with the provided name doesn't exist, the bucket is created by the pre-built function. | Yes  
ALLOW_OVERWRITE | Accepts `true` or `false`. If the attribute isn't provided, the default value is `false`. A value of `true` means unzipping the file overwrites the files with same name in the destination. A value of `false` means the unzipping creates a versioned copy of the file or the parent folder. Example zip file content: ```
folder_1/text_file_1.txt
folder_1/sub_folder_1/text_file_2.txt
text_file_3.txt
```
If the destination already has `folder_1` and `text_file_3.txt` in the root, the destination bucket is now: ```
folder_1/text_file_1.txt      # already existing folder      
 folder_1/text_file_4.txt      # already existing folder
 folder_1 (1)/text_file_1.txt
 folder_1 (1)/sub_folder_1/text_file_2.txt
 text_file_3.txt          # already existing file
 text_file_3 (1).txt
```
| No  
**Sample Request Body**
Copy
```
{
  "COMPARTMENT_ID": "ocid1.compartment.oc1...",
  "REGION": "us-ashburn-1",
  "SOURCE_BUCKET": "origin-storage",
  "ZIP_FILE_NAME": "object_extractor_example.zip",
  "TARGET_BUCKET": "target-storage ",
  "ALLOW_OVERWRITE": "false"
}
```

### Response Body 🔗 
  * **Timestamp:** Using UTC to avoid time zone issues.
  * **Code:** The function returns a 200 code if the task completes successfully.
  * **Status:** The function returns "Success" as the status if the task completes successfully.
  * **data:** A JSON message body that includes specific response information for the task. The additional information provides a confirmation message of the successful unzip operation.


**Example**
The following example shows the JSON return data:
Copy
```
{
  "startTime": "2023-02-22T05:55:06.544Z",
  "endTime": "2023-02-22T05:55:17.730Z",
  "runTime": "PT11.186S",
  "code": 200,
  "status": "Success",
  "data": {
    "additionalInformation": {
      "Message": "Unzip task is successfully done"
    }
  }
}
```

### Troubleshooting 🔗 
**OCI Functions common status codes**
The following table summarizes common OCI Functions errors that you might encounter when working with pre-built functions:
Error Code | Error Message | Action  
---|---|---  
200 | Success | None  
404 | NotAuthorizedOrNotFound | Verify that the required policies are configured (see [Running Fn Project CLI commands returns a 404 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-setting-up-and-running-Oracle-Functions.htm#Running_Fn_Project_CLI_commands_returns_a_404_error)).  
444 | Timeout |  The connection between the client and OCI Functions was interrupted during function execution (see [Invoking a function causes the client to report a timeout, and a 444 error is shown in the function's logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#functionstroubleshooting_topic_Function_timeout_client_message_and_a_444_error)). A retry might solve the issue. Note that most clients have an inner timeout of 60 seconds. Even when the pre-built function timeout is set to 300 seconds, the following might be required:
  * When using the **OCI CLI** : Use **--read-timeout 300**
  * When using the **OCI SDK** : Set the read timeout to 300 when creating the client
  * When using **DBMS_CLOUD.SEND_REQUEST** : Use **UTL_HTTP.set_transfer_timeout(300);**

For more information, see [Invoking Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsinvokingfunctions.htm#Invoking_Functions "Find out the different ways to invoke functions deployed to OCI Functions.").  
502, 504 | (various) | Most issues return a 502 status code (see [Invoking a function returns a Function failed message and a 502 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#Invoking_a_function_returns_a_Functionfailed_message_and_a_502_error)). A 502 error with the message "error receiving function response" might be resolved by increasing the memory allocation. A 502 might occur occasionally when the function is in some transient state. A retry might solve the issue.  
To further identify the cause, enable logging features for the pre-built function (see [Storing and Viewing Function Logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsexportingfunctionlogfiles.htm#Storing_and_Viewing_Function_Logs "Find out how to store and view function logs with OCI Functions.")). For detailed information on troubleshooting a function, see [Troubleshooting OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionstroubleshooting.htm#Troubleshooting_Oracle_Functions "Find out how to troubleshoot problems with OCI Functions, and possible solutions to common issues.").
**Object Storage File Extractor pre-built function status codes**
The following table summarizes the errors that you might encounter when working with this pre-built function:
Error Code | Error Message | Action  
---|---|---  
400 | Missing mandatory configuration value | The error message indicates the required field name. Verify the correct field is provided in the request body.  
400 | Invalid zip file name | Verify the name of the file provided for field` ZIP_FILE_NAME` has a `.zip` extension.  
409 | Destination bucket already contains zipped file with the same name | If `ALLOW_OVERWRITE` is set to `false`, verify the destination bucket doesn't already have a zip file with the same name.  
To further identify the cause, enable logging features for the pre-built function (see [Storing and Viewing Function Logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsexportingfunctionlogfiles.htm#Storing_and_Viewing_Function_Logs "Find out how to store and view function logs with OCI Functions.")). 
**Log Analysis Tips**
All the pre-built functions provide an option to specify the logging level as a configuration parameter. You can set the logging level to `DEBUG` to get more information.
Since an application has multiple functions, the pre-built function log entries are identified by the prefix "PBF | <PBF NAME> ".
For example, a log entry for the Media Workflow Job Spawner pre-built function looks similar to the following:
```
"PBF | Media Workflow Job Spawner | INFO | 2023-02-07T18:06:50.809Z | Fetching details from Events JSON"
```

Was this article helpful?
YesNo


Updated 2025-01-30
# Tagging a Private Endpoint when Updating in Object Storage
Add metadata to an Object Storage private endpoint when you update an existing one. This metadata enables you to define keys and values and associate them with resources.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/tag-update-private-endpoint.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/tag-update-private-endpoint.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/tag-update-private-endpoint.htm)


  *     1. Begin the steps for editing an Object Storage private endpoint using the Oracle Cloud Infrastructure Console as described in [Editing a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/update-private-endpoint.htm#top "Update an Object Storage private endpoint's configuration.").
    2. In the selected private endpoint's **Details** page, select **Add tags**. The **Add tags** dialog box appears.
    3. Complete the following. See [Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm) for descriptions of these fields. 
       * **Tag namespace**
       * **Tag key**
       * **Value**
    4. Select **Add tags**. The dialog box closes and you're returned to the **Details** page.
  * Use the `--defined-tags` or `--freeform-tags` options when running the [oci os private-endpoint update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/private-endpoint/update.html) command to tag a private endpoint you're updating:
Command
CopyTry It
```
oci os private-endpoint update --pe-name private_endpoint_name ... --defined-tags JSON_formatted_defined_tag --freeform-tags JSON_formatted_free-form_tag [OPTIONS]
```

Provide key-value pair input for `--defined-tags` and `--freeform-tags` as valid formatted JSON. See [Passing Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#Managing_CLI_Input_and_Output) and [Using a JSON File for Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON) for information about JSON formatting.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Include the `definedTags` and `freeformTags` attributes and their values when updating the private endpoint.


Was this article helpful?
YesNo


Updated 2025-01-30
# Tagging a Private Endpoint in Object Storage at Creation
Add metadata to an Object Storage private endpoint when you first create it. This metadata enables you to define keys and values and associate them with resources.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/tag-create-private-endpoint.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/tag-create-private-endpoint.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/tag-create-private-endpoint.htm)


  *     1. Begin the steps for creating an Object Storage private endpoint using the Oracle Cloud Infrastructure Console as described in [Creating a Private Endpoint](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/create-private-endpoint.htm#top "Create a private endpoint to reach Object Storage using a private IP address within your VCN without accessing the public internet.").
    2. At the end of the **Create private endpoint** dialog box, select **Show advanced options**. The advanced options tabs appear.
    3. Select the **Tags** tab.
    4. Complete the following. See [Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm) for descriptions of these fields. 
       * **Tag namespace**
       * **Tag key**
       * **Value**
You can create the private endpoint or continue with other settings.
  * Use the `--defined-tags` or `--freeform-tags` options when running the [oci os private-endpoint create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/private-endpoint/create.html) command to tag a private endpoint at the time of its creation:
Command
CopyTry It
```
oci os private-endpoint create --compartment-id compartment_ocid --name name ... --defined-tags JSON_formatted_defined_tag --freeform-tags JSON_formatted_free-form_tag [OPTIONS]
```

Provide key-value pair input for `--defined-tags` and `--freeform-tags` as valid formatted JSON. See [Passing Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#Managing_CLI_Input_and_Output) and [Using a JSON File for Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON) for information about JSON formatting.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Include the `definedTags` and `freeformTags` attributes and their values when creating the private endpoint.


Was this article helpful?
YesNo


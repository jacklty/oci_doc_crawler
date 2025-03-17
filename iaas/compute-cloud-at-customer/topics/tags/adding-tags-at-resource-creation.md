Updated 2024-01-18
# Adding Tags at Resource Creation
On Compute Cloud@Customer, any tag defaults that are defined on a compartment are automatically added to all resources that are created in that compartment, or any child compartment of that compartment, after the tag default was defined. A tag default might require you to enter a value for the tag to create the resource.
**Note** Defined tags and tag namespaces must be configured in your OCI tenancy. See [Defined tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm).
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/adding-tags-at-resource-creation.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/adding-tags-at-resource-creation.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/adding-tags-at-resource-creation.htm)


  *     1. In the Create dialog for the resource, scroll to the Tagging section.
    2. Select the Tag Namespace or select None (to apply a free-form tag).
       * If you selected a Tag Namespace, then select the Tag Key, and enter a value or select a value from the list.
       * If you selected None (apply a free-form tag), then enter a Tag Key and enter a value.
    3. To apply another tag, click the Additional Tag button.
You can't specify more than one tag with the same tag namespace and the same tag key for a defined tag, or more than one tag with the same tag key for a free-form tag.
    4. To review the tags on the resource, to go the details page for the new resource.
On the resource details page, click the Tags tab to display the tags that are applied to this resource.
  * To add a tag to a resource when you create the resource, use the resource `create` or `launch` command.
    1. Get the information for each tag that you want to add to the resource.
       * Get the namespace, key, and value for each defined tag that you want to add to the resource.
Construct an argument for the `--defined-tags` option. Specify each tag namespace and tag key pair only one time.
       * Get the key and value for each free-form tag that you want to add to the resource.
Construct an argument for the `--freeform-tags` option. Specify each tag key only one time.
The value of the `--defined-tags` option argument and the `--freeform-tags` option argument is a JSON definition of the tags. This JSON definition can be provided as a string on the command line or in a file.
You can generate a template of the correct JSON to provide by using the `--generate-param-json-input` option with the base command that you will use to tag the resource. The argument for the `--generate-param-json-input` option is the name of the option that you use to specify the tags (`--defined-tags` in this example) without the option indicator (`--`), as shown in the following example:
```
$ oci service resource create --generate-param-json-input defined-tags > defined_tags.json
```

The content of the output `defined_tags.json` file is:
```
{
 "tagNamespace1": {
  "tagKey1": "tagValue1",
  "tagKey2": "tagValue2"
 },
 "tagNamespace2": {
  "tagKey1": "tagValue1",
  "tagKey2": "tagValue2"
 }
}
```

If you specify `freeform-tags` instead of `defined-tags` in the preceding command, you get the following output:
```
{
 "tagKey1": "tagValue1",
 "tagKey2": "tagValue2"
}
```

Edit these templates to provide the appropriate tags. Specify the result in the final command as shown in the following step.
    2. Run the resource `create` or `launch` command.
To add one or more defined tags, use the `--defined-tags` option. To add one or more free-form tags, use the `--freeform-tags` option.
Syntax:
```
oci <service> <resource> create --compartment-id <compartment_OCID> --defined-tags <defined_tags_json> --freeform-tags <freeform_tags_json> <other_resource_create_options>
```

Example:
In the following example, one or more defined tags is added using a file, and a free-form tag is added using a string argument. Use the `file://` syntax to specify a file as the option argument.
```
oci <service> <resource> create --compartment-id <compartment_OCID> --defined-tags file://defined_tags.json --freeform-tags '{"MyTag":"val-u"}' <other_resource_create_options>
```

The output of the resource `create` or `launch` command is the same as the output of the resource `get` command. The output shows the defined and free-form tags.
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * To add a tag to a resource when you create the resource, use the `create`<resource> or `launch`<resource> command.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


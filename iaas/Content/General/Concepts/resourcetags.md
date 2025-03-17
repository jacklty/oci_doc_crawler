Updated 2025-01-13
# Resource Tags
When you have many resources (for example, instances, VCNs, load balancers, and block volumes) across multiple compartments in your tenancy, it can become difficult to track resources used for specific purposes, or to aggregate them, report on them, or take bulk actions on them. _Tagging_ allows you to define keys and values and associate them with resources. You can then use the tags to help you organize and list resources based on your business needs.
There are two types of tags:
_[Defined tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm)_ are set up in your tenancy by an administrator. Only users granted permission to work with the defined tags can apply them to resources. 
_[Free-form tags](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm)_ can be applied by any user with permissions on the resource. 
For more detailed information about tags and their features, see [Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm).
**Tip** Watch a video to introduce you to the concepts and features of tagging: [Introduction to Tagging](https://www.youtube.com/watch?v=7l5vQtxJFFE).
**Caution** Avoid entering confidential information when assigning descriptions, tags, or friendly names to cloud resources through the Oracle Cloud Infrastructure Console, API, or CLI.
## Working with Resource Tags 🔗 
[To bulk add defined tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
How to add multiple defined tags to existing resources. To apply defined tags, you must have permission to use the namespace.
  1. Open the **navigation menu** and select **Governance & Administration**. Under **Tenancy Management** , select **Tenancy Explorer**.
  2. Select the resources to which you want to add tags. Optionally, use the **Filter by resource type** drop-down menu to narrow the list of resources.
  3. In the **Actions** menu, click **Manage Tags**.
The Manage Tags page opens. The first table displays the tags currently applied to the selected resources. The second table displays the selected resources.
  4. Under the list of existing tags, click **+ Add New**.
    1. Select the **Tag Namespace**.
    2. Select the **Tag Key**.
    3. For **Value** , enter a value.
  5. To apply another tag, repeat the previous step. To remove a row, click the **Remove (x)** button.
  6. When you have added all the desired tags, click **Next**.
A confirmation page opens that lists the actions to take and the resources that the actions apply to.
  7. Click **Submit**.


The Work Request page launches to show you the status of the work request to add tags to the resources.
[To add defined tags to one existing resource](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
To apply a defined tag, you must have permission to use the namespace. 
  1. Open the Console, go to the details page of the resource you want to tag.
For example, to tag a compute instance: Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**. A list of the instances in your current compartment is displayed. Find the instance that you want to tag, and click its name to view its details page.
  2. Click **Apply Tags**. Depending on the resource, this option might appear in the **More Actions** menu.
  3. In the **Apply Tags to the Resource** dialog:
    1. Select the **Tag Namespace**.
    2. Select the **Tag Key**.
    3. In **Value** , either enter a value or select one from the list.
    4. To apply another tag, click **+ Additional Tag**.
    5. When finished adding tags, click **Apply Tag(s)**.


[To add a free-form tag to an existing resource](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
  1. Open the Console, go to the details page of the resource you want to tag.
For example, to tag a compute instance: Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**. A list of the instances in your current compartment is displayed. Find the instance that you want to tag, and click its name to view its details page.
  2. Click **Apply Tags**. Depending on the resource, this option might appear in the **More Actions** menu.
  3. In the **Apply Tags to the Resource** dialog:
    1. Select **None (apply a free-form tag)**.
    2. Enter the **Tag Key**.
    3. Enter a **Value**.
    4. To apply another tag, click **+ Additional Tag**.
    5. When finished adding tags, click **Apply Tag(s)**.


[To add a tag during resource creation](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
You can apply tags during resource creation. The location of the **Apply Tag(s)** option in the dialog varies by resource. The general steps are:
  1. In the resource Create dialog, click **Apply Tags**. 
On some resources, you have to click **Show Advanced Options** to apply a tag.
  2. In the **Apply Tags to the Resource** dialog:
    1. Select the **Tag Namespace** , or select **None** to apply a free-form tag.
    2. Select or enter the **Tag Key**.
    3. In **Value** , either enter a value or select one from the list.
    4. To apply another tag, click **+ Additional Tag**.
    5. Click **Apply Tag(s)**.


[To filter a list of resources by a tag](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
Open the Console, click the service name and then click the resource you want to view. The left side of the page shows all the filters currently applied to the list.
For example, to view compute instances: Click **Compute** and then click **Instances** , to see the list of instances in your current compartment. 
[To filter a list of resources by a defined tag](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
  1. Next to **Tag filters** , select **add**.
  2. In the **Add a tag filter** dialog, enter the following:
     * **Tag namespace:** Select the tag namespace.
     * **Tag key:** Select the key.
     * **Tag value:** Select from the following:
       * **Match any value** - returns all resources tagged with the selected namespace and key, regardless of the tag value.
       * **Specify matching values** - returns resources with the tag value you enter in the text box. Enter a single value in the text box. To specify multiple values for the same namespace and key, select **+** to display another text box. Enter one value per text box.
  3. Select **Apply filter**.


[To filter a list of resources by a free-form tag](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
  1. Next to **Tag filters** , select **add**.
  2. In the **Add a tag filter** dialog, enter the following:
     * **Tag namespace:** Select None (free-form tag).
     * **Tag key:** Enter the key.
     * **Tag value:** Select from the following:
       * **Match any value** - returns all resources tagged with the selected namespace and key, regardless of the tag value.
       * **Specify matching values** - returns resources with the tag value you enter in the text box. Enter a single value in the text box. To specify multiple values for the same namespace and key, select **+** to display another text box. Enter one value per text box.
  3. Select **Apply filter**.


[To bulk update defined tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
How to update defined tags applied to one or more resources.
  1. Open the **navigation menu** and select **Governance & Administration**. Under **Tenancy Management** , select **Tenancy Explorer**.
  2. Select the resources whose tags you want to update. Optionally, use the **Filter by resource type** drop-down menu to narrow the list of resources.
  3. In the **Actions** menu, click **Manage Tags**.
The Manage Tags page opens. The first table displays the tags currently applied to the selected resources. The second table displays the selected resources.
  4. In the list of tags, find the tag that you want to update and enter a new value. To revert the change, click the **Undo** button.
  5. For **Action** , select **Apply tag to all selected resources**.
  6. If desired, update more tag values. Then, click **Next**.
A confirmation page opens that lists the actions to take and the resources that the actions apply to.
  7. Click **Submit**.


The Work Request page launches to show you the status of the work request to update the tags on the resources.
[To update a tag applied to a single resource](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
  1. Open the Console, click the service name, and then click the resource you want to view.
For example, to view compute instances: Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**. A list of the instances in your current compartment is displayed. Find the instance that you want to update, and click its name to view its details page.
  2. Click **Tags**.
The list of tags applied to the resource is displayed.
  3. Find the tag you want to update and click the pencil icon next to it.
  4. Enter or select a new value.
  5. Click **Save**. 


[To bulk remove defined tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
How to remove multiple defined tags from resources.
  1. Open the **navigation menu** and select **Governance & Administration**. Under **Tenancy Management** , select **Tenancy Explorer**.
  2. Select the resources from which you want to remove tags. Optionally, use the **Filter by resource type** drop-down menu to narrow the list of resources.
  3. In the **Actions** menu, click **Manage Tags**.
The Manage Tags page opens. The first table displays the tags currently applied to the selected resources. The second table displays the selected resources.
  4. In the list of tags, find the tag that you want to remove. For **Action** , select **Remove tag from all selected resources**.
  5. To remove another tag, repeat the previous step.
  6. Click **Next**.
A confirmation page opens that lists the actions to take and the resources that the actions apply to.
  7. Click **Submit**.


The Work Request page launches to show you the status of the work request to remove tags from the resources.
[To remove a tag from a single resource](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm)
  1. Open the Console, click the service name and then click the resource you want to view.
For example, to view a compute instance: Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**. A list of the instances in your current compartment is displayed. Find the instance that you want to remove the tag from, and click its name to view its details page.
  2. Click **Tags**.
The list of tags applied to the resource is displayed.
  3. Find the tag you want to remove and click the pencil icon next to it.
  4. Click **Remove Tag**.


## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
  * To apply a tag to an individual resource using the API, use the appropriate resource's `create` or `update` operation. 
  * [BulkEditTags](https://docs.oracle.com/iaas/api/#/en/identity/latest/Tag/BulkEditTags) - adds, updates, and removes multiple tag key definitions on the selected resources
  * [ListBulkEditTagsResourceTypes](https://docs.oracle.com/iaas/api/#/en/identity/latest/BulkEditTagsResourceTypeCollection/ListBulkEditTagsResourceTypes) - lists the resource types that support bulk tag editing


Was this article helpful?
YesNo


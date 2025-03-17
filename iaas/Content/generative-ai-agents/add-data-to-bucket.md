Updated 2025-03-13
# Adding Data with Custom URL to an Object Storage Bucket
Create an Object Storage bucket and upload source files for RAG responses in OCI Generative AI Agents. Optionally, add a custom URL to each file for citation.
  1. In the navigation bar of the Console, select a region that hosts Generative AI Agents, for example, US Midwest (Chicago). If you don't know which region to select, see [Regions with Generative AI Agents](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/overview.htm#regions "Oracle hosts its OCI services in regions and availability domains. A region is a localized geographic area, and an availability domain is one or more data centers in that region. OCI Generative AI Agents is hosted in the following regions:").
  2. Open the **navigation menu** and select **Storage**. Under **Object Storage & Archive Storage**, select **Buckets**.
  3. Select the compartment in which you want to create a bucket or the compartment that contains the bucket that you want to use. You must already have the following permission to add Object Storage resources to this compartment.
Copy
```
allow group <your-group-name> to manage object-family in compartment <compartment-with-bucket>
```

  4. To create a bucket follow these steps:
    1. Select **Create Bucket**.
    2. Enter a name unique to your region for the bucket.
    3. For other fields, select the **Learn more** links and then select options that apply to your data. Also see [Creating an Object Storage Bucket](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm).
    4. Select **Create**.
By default, a new **bucket** is private. You can change the visibility of a **bucket** after you create it.
  5. Select the name of the **bucket** that you want to use.
  6. On the bucket details page, under **Objects** , select **Upload**.
  7. (Optional) Select **Show Optional Headers and Metadata** and then select and enter the following values.
     * **Type** : Metadata
     * **Name** : `customized_url_source`
     * **Value** : <Custom-URL-for-the-file>
**Important** For the citation link override to work, you must use **Name** : `customized_url_source`. If you don't want the agent to return a custom URL in its citations, skip this step.
  8. Add one or more files for the data source and select **Upload**.
**Note** If you added the `customized_url_source` metadata to an object in step 7, this custom URL applies to all the files that you upload for this object. You can't update the `metadata` property of existing objects. Instead, you can copy a file, add a new metadata to that file, and then delete the old file. To add or update a file with the `customized_url_source` metadata, using OCI CLI, see [Assigning a Custom URL to a Citation](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/add-custom-URL.htm#add-custom-URL "When an agent uses the RAG for its responses, you can get citations. By default, the citations point to Object Storage where the files are stored. To reference a URL instead of the file that's being referenced, you can add a custom URL to the metadata object for that file.").


Was this article helpful?
YesNo


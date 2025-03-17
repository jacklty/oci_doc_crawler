Updated 2025-01-10
# Object Storage Guidelines in Generative AI Agents
To make your data available to OCI Generative AI Agents, you have the following data options:
  * **Object Storage data** : Upload data files to OCI Object Storage and let Generative AI Agents automatically ingest the data. This option is service-managed. Review this topic if your data files are in Object Storage.
  * **OpenSearch data** : Bring your own (BYO) ingested and indexed OCI Search with OpenSearch data for the agents to use. Skip this topic if you have this option.
  * **Oracle Database vector store** : Bring your own (BYO) vector embeddings from an Oracle Base Database 23ai or an Autonomous Database 23ai vector store to Generative AI Agents. Skip this topic if you have this option.


**Important**
Set up the following Object Storage permissions before you proceed.
  * User access to Object Storage files
  * Data ingestion job access to Object Storage files for long-running jobs


See [ Getting Access](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/iam-policies.htm#access-agents) for the permissions.
To prepare your data for Generative AI Agents data sources in OCI Generative AI Agents follow these guidelines:
  * **Data Sources** : Data for Generative AI Agents must be uploaded as files to an Object Storage bucket.
  * **Number of Buckets** : Only one bucket is allowed per data source.
  * **Supported File Types** : Only `PDF` and `txt` files are supported.
  * **File Size Limit** : Each file must be no larger than 100 MB.
  * **PDF Contents** : `PDF` files can include images, charts, and reference tables but these must not exceed 8 MB.
  * **Chart Preparation** : No special preparation is needed for charts, as long as they're two-dimensional with labeled axes. The model can answer questions about the charts without explicit explanations.
  * **Table Preparation** : Use reference tables with several rows and columns. For example, the agent can read the table on the[ limits](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/limits.htm#limits "Learn about OCI Generative AI Agents resource limits. See which limits are preset and which can be increased.") page.
  * **URLs** : All the hyperlinks present in the `PDF` documents are extracted and displayed as hyperlinks in the chat response.
  * **Data Not Ready** : If your data isn't yet available, create an empty folder for the data source and populate it later. This way, you can ingest data into the source after the folder is populated.


**Note**
**Beta Customers:**
If you created a knowledge base in the Beta phase, you might need to delete and re-create the data source for the URL handling feature to work.
For guidance on adding your dataset to an Object Storage bucket consult the [documentation](https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/add-data-to-bucket.htm#add-data-to-bucket "Create an Object Storage bucket and upload source files for RAG responses in OCI Generative AI Agents. Optionally, add a custom URL to each file for citation.").
Was this article helpful?
YesNo


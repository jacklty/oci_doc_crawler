Updated 2024-12-16
# Creating OraclePCA Tags
On Oracle Compute Cloud@Customer you can use the `OraclePCA` tag namespace to enable resource attributes that aren't available as CLI options or API attributes. 
**Note**
This section covers the Tag Key Definitions for Block Volume and File System attributes, and SR-IOV. There are more Tag Key Definitions, and other administrative tasks required to enable Container Engine for Kubernetes (OKE) on Oracle Compute Cloud@Customer. For those details, see [Tenancy Administrator Tasks](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/administrator-tasks.htm#administrator-tasks "Learn about the set of tasks you perform in the OCI tenancy to enable the OKE service on Compute Cloud@Customer.").
You can configure the OraclePCA tag namespace to enable these attributes:
**Block Volume Attributes**
  * **Synchronous Write Bias**
You can enable the selection of `LATENCY` or `THROUGHPUT` when a block volume is created.
  * **Secondary Cache**
You can enable the selection of `ALL`, `METADATA`, or `NONE` when a block volume is created.


**File System Attributes**
  * **Quota**
You can enable the setting of a quota limitation when a file system is created. 
  * **Database record size**
You can enable the selection of different database record sizes when a file system is created.
  * **Backing store pool**
You can enable the selection of `PCA_POOL_HIGH` and `poolName` when a file system is created.


The following procedures describe how to configure the OraclePCA tags so that the resource attributes are available when you create your resource, such as a block volume or file system. 
## Creating the `OraclePCA` Tag Namespace 🔗 
  1. In the Oracle Cloud Console, open the navigation menu, click **Governance & Administration**, and then click **Tag Namespaces**.
  2. If `OraclePCA` isn't shown in the **Tag Namespaces** list, click **Create Tag Namespace**.
If the OraclePCA namespace already exists, don't continue. Instead, go to [Creating the OraclePCA Tag Key Definitions](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/creating_oraclepca_tags.htm#creating_oraclepca_tags__usr-tag-namespace-create-cecli).
  3. In the **Create Tag Namespace** dialog box, enter the following information:
     * **Create in Compartment** : Select the compartment in which you want to create the namespace definition.
     * **Namespace Definition Name** : Enter **OraclePCA**.
     * **Description** : Enter a description. For example, `Support resource attributes that are available.`
  4. Click **Create Tag Namespace**.
The details page for the new `OraclePCA` tag namespace definition is displayed.


Next, create tag key definitions. See [Creating the OraclePCA Tag Key Definitions](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/creating_oraclepca_tags.htm#creating_oraclepca_tags__usr-tag-namespace-create-cecli).
## Creating the `OraclePCA` Tag Key Definitions 🔗 
  1. On the `OraclePCA` tag namespace details page, click **Create Tag Key Definition**.
  2. In the **Create Tag Key Definition** dialog box, enter values for an attribute you want to enable. The attributes and values are shown in the following table.
**Note**
You don't need to configure all the following tag key definitions. Configure only the tag key definitions for the attributes you want to enable.
Attribute | Value  
---|---  
**Block Volume Synchronous Write Bias Tag Key Definition** | 
     * **Tag Key:** Enter `logBias`.
     * **Description:** Enter a description. For example, `Control the use of the write cache flash devices for a share or LUN.` Avoid entering confidential information.
     * **Tag Value Type:** Select **A List of Values**.
     * **Values:** Enter the following values, each on a separate line:
       * `LATENCY`
       * `THROUGHPUT`  
**Block Volume Secondary Cache Tag Key Definition** | 
     * **Tag Key** : Enter `secondaryCache`.
     * **Description:** Enter a description. For example, `Control the use of the read cache flash devices for a share or LUN`. Avoid entering confidential information.
     * **Tag Value Type:** Select **A List of Values**.
     * **Values:** Enter the following values, each on a separate line:
       * `ALL`
       * `METADATA`
       * `NONE`  
**File System Quota** | 
     * **Tag Key** : Enter `quota`.
     * **Description** : Enter a description. For example, `The quota value in gigabytes includes the data in the file system and all snapshots created under the file system. `Avoid entering confidential information.
     * **Tag Value Type** : Select **Static Value**.  
**File System Database Record Size** | 
     * **Tag Key** : Enter `databaseRecordSize`.
     * **Description** : Enter a description. For example, `The size of a database record in bytes.` Avoid entering confidential information.
     * **Tag Value Type** : Select **A List of Values**.
     * **Values** : Enter the following values, each on a separate line:
       * `512`
       * `1024`
       * `2048`
       * `4096`
       * `8192`
       * `16384`
       * `32768`
       * `65536`
       * `131072`
       * `262144`
       * `524288`
       * `1048576`  
**File System Backing Store Pool** | 
     * **Tag Key** : Enter `poolName`.
     * **Description** : Enter a description. For example, `Whether to use the default storage pool, or use a high performance pool as the backing store pool.` Avoid entering confidential information.
     * **Tag Value Type** : Select **A List of Values**.
     * **Values** : Enter the following values, each on a separate line: 
       * `PCA_POOL`
       * ` PCA_POOL_HIGH`  
**Network Configuration for SR-IOV** | 
     * **Tag Key** : Enter `networkType`.
     * **Description** : Enter a description. For example, `DRG and VCN network configuration required for SR-IOV.`
     * **Tag Value Type** : Select **Static Value**.
     * **Values** : Enter `VFIO`.  
  3. Click **Create Tag Key Definition**.
The details page for the new tag key definition is displayed.
  4. (Optional) Repeat this procedure to create more tag key definitions.


## Configuring Resources to Use Attributes Provided by OraclePCA Tags 🔗 
Depending on the resource you want to create, see one of these sections:
  * [Creating a Block Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-block-volume.htm#creating-a-block-volume "On Compute Cloud@Customer, block volumes are detachable block storage devices that you can use to dynamically expand the storage capacity of an instance.")
  * [Creating a File System](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system.htm#creating-a-file-system "On Compute Cloud@Customer, you can create a shared file system using the File Storage service.")


Was this article helpful?
YesNo


Updated 2024-12-16
# Create OraclePCA Tags For OKE
In your OCI tenancy that's associated with Compute Cloud@Customer, create specific defined tags to enable OKE attributes on Oracle Compute Cloud@Customer. 
**Important**
Don't delete these tag keys. Don't create this tag namespace and these keys unless you plan to use the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") to create clusters. If you create this tag namespace and these keys, create them exactly as shown, don't modify them, and don't delete them.
Oracle Compute Cloud@Customer uses the `OraclePCA` tag namespace to set attributes that aren't available as CLI options or API attributes. For OKE, some cluster attributes must be set using `OraclePCA` tags.
**Note**
Other attributes that can only be set by using `OraclePCA` tags, such as some block volume and file system attributes, are documented in [Creating OraclePCA Tags](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/creating_oraclepca_tags.htm#creating_oraclepca_tags "On Oracle Compute Cloud@Customer you can use the OraclePCA tag namespace to enable resource attributes that aren't available as CLI options or API attributes."). You might want to set some of these for nodes in a node pool.
To use the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") to set these attributes, you must first create the `OraclePCA` tag namespace, tag keys, and value choices.
The following sections describe how to create the `OraclePCA` tag namespace, and how to create the tag key definitions for the OKE attributes.
## Creating the OraclePCA Tag Namespace 🔗 
  1. Sign in to your OCI tenancy. In the Oracle Cloud Console, open the navigation menu, click **Governance & Administration**, and then click **Tag Namespaces**.
  2. If **OraclePCA** isn't shown in the **Tag Namespaces** list, click **Create Tag Namespace**.
If the OraclePCA namespace already exists, don't continue. Instead, go to [Creating the OraclePCA Tag Key Definitions](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/oke-creating_oraclepca_tags.htm#creating_oraclepca_tags__oke-tag-definitions).
  3. In the **Create Tag Namespace** dialog box, enter the following information:
     * **Create in Compartment** : Select the compartment in which you want to create the namespace definition.
     * **Namespace Definition Name** : Enter `OraclePCA`.
     * **Description** : Enter a description. For example, `Support resource attributes that are available on Compute Cloud@Customer.`
  4. Click **Create Tag Namespace**.
The details page for the new `OraclePCA` tag namespace definition is displayed.
Next, create tag key definitions. See [Creating the OraclePCA Tag Key Definitions](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/oke-creating_oraclepca_tags.htm#creating_oraclepca_tags__oke-tag-definitions).


## Creating the OraclePCA Tag Key Definitions 🔗 
Use this procedure to create four tag key definitions to enable OKE attributes.
  1. On the OraclePCA tag namespace details page, click **Create Tag Key Definition**.
  2. In the **Create Tag Key Definition** dialog box, enter values for one tag key, as shown in the following table.
Attribute | Values  
---|---  
**SSH Key** | 
     * **Tag Key** : Enter `sshkey`.
     * **Description** : Enter a description. For example, `Your public SSH key.` Avoid entering confidential information.
     * **Tag Value Type** : Select **Static Value**.  
**Number of Control Plane Nodes** | 
     * **Name** : Enter `cpNodeCount`.
     * **Description** : For example, `Number of nodes in the control plane`. Avoid entering confidential information
     * **Tag Value Type** : Select **A List of Values**
     * **Values** : Enter these numbers, each on a separate line:  `1` `3` `5`  
**Shape of Control Plane Nodes** | 
     * **Name** : Enter `cpNodeShape`.
     * **Description** : For example, `The shape of the control plane nodes.` Avoid entering confidential information
     * **Tag Value Type** : Select **Static Value**.  
**Shape Configuration of Control Plane Nodes** | 
     * **Name** : Enter `cpNodeShapeConfig`.
     * **Description** : For example, `The number of OCPUs and optionally amount of memory for a flexible node shape.` Avoid entering confidential information
     * **Tag Value Type** : Select **Static Value**.  
  3. Click **Create Tag Key Definition**.
  4. Repeat Steps [1](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/oke-creating_oraclepca_tags.htm#creating_oraclepca_tags__click-create-definition) through [3](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/oke-creating_oraclepca_tags.htm#creating_oraclepca_tags__click-create-tag-key), until all the following tag key definitions are created:
     * **SSH Key**
     * **Number of Control Plane Nodes**
     * **Shape of Control Plane Nodes**
     * **Shape Configuration of Control Plane Nodes**


**What's Next:**
[Create a User Group and Policies for OKE Users](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/create-a-user-group-and-policies-that-authorize-members-to-use-oke.htm#create-a-user-group-and-policies-that-authorize-members-to-use-oke "In your OCI tenancy that's associated with Compute Cloud@Customer, create a user group and policies that authorize users to use OKE.")
Was this article helpful?
YesNo


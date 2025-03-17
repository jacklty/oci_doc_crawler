Updated 2025-02-13
# License Manager
License Manager is a free, opt-in service that allows you to bring your own licenses (BYOL) into Oracle Cloud Infrastructure.
Use License Manager to:
  * Automate the license portability rules for Oracle Database products to OCI Database PaaS services. This eliminates overhead for Software Asset Managers (SAMs) and developers in an enterprise. Developers can create BYOL Oracle Database resources, such as Autonomous Database, without needing to worry about creating visibility into their infrastructure for their SAM. A resource can be _BYOL_ , which means Oracles charges you for infrastructure, but not licensing fees for software running on it. A resource can also be _license included_ , which means the cost includes infrastructure and the software licensing fee.
  * Track license usage for Oracle Database products or third-party products by Compute resources. As a result, you have a single observation and license usage tracking location of all Oracle and third-party licenses in OCI. 
  * Obtain reporting of BYOL resources that have licensing needs. Monitor and manage a list of email addresses to be notified about the expiration or over-subscription of licenses.


## Supported Products 🔗 
License Manager supports the following Oracle products and options:
  * Oracle Database Enterprise Edition
  * Oracle Database Standard Edition
  * Oracle Database Standard Edition One
  * Oracle Database Standard Edition 2
  * Real Application Clusters
  * Multitenant
  * Active Data Guard


## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm#Getting_Started_with_Policies) and [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top). 
To use License Manager, the following policy statements are required:
```
ALLOW GROUP <Group Name> to Manage licensemanager-settings in tenancy
ALLOW GROUP <Group Name> to Manage licensemanager-record in tenancy
```

## Authentication and Authorization 🔗 
Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).
An administrator in an organization needs to set up **groups** , **compartments** , and **policies** that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see [Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm). 
If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.
## Viewing License Summary Activity  🔗 
The License Manager **Overview** page provides an overall summary of your license activity. The page allows you to get quick insights into your most utilized licenses, Bring Your Own License (BYOL) resources needing the most licenses by OCPUs and ECPUs, an overall count of BYOL and license included resources, and licenses at or near expiration.
To view the **Overview** page and its details, open the navigation menu and click ****Governance & Administration****. Under **License Management** , click **Overview**. The License Manager **Overview** page opens.
The top of the page has tiles to indicate the totals for:
  * **Product Licenses** : The total number of product licenses.
  * **BYOL Resources** : The total number of BYOL resources. Corresponds to what is listed in the **Top BYOL resources by OCPUs** and **Top BYOL resources by ECPUs** tables.
  * **License Included Resources** : The count of license-included Database PaaS resources you have created in the tenancy.
  * **Licenses at or near expiration** : The total number of license records within 90 days of expiration.


Following the totals summary, the **Top Utilized Product Licenses** table displays the following:
  * **Product License** : The product license name. Click the linked name to go to its [details](https://docs.oracle.com/en-us/iaas/Content/LicenseManager/Concepts/licensemanageroverview.htm#licensemanager-viewlicense_details "You can view the list of licenses and product license details from the Product Licenses page.") page.
  * **Status** : The license status, which can be the following:
    * **Ok** : The license has active license records for Oracle products, and active license records and an image associated for third-party licenses.
    * **Incomplete** : The Oracle product license was created without any active license records within it. For third-party products, the status is **Incomplete** if there aren't any active records or images associated with the license.
    * **Issues Found** : Over-subscribed licenses. The license requirement exceeds the entitlement.
    * **Warning** : Shown for license records when all licensing requirements (mandatory options or base product licenses) aren't found in License Manager. **Warning** is also shown if data hasn't been updated in more than 24 hours.
  * **Requirement** : What all the resources attributed to a license need, to be considered fully licensed. The licensing requirement is calculated every hour.
  * **Entitlement** : The sum of all license counts in your license records.
  * **Metric** : The metric that matches your licensing terms.


The **Top BYOL resources by OCPUs** table lists the following:
  * **Resource OCID** : Click the link to go directly to the BYOL resource.
  * **OCPUs** : The total number of OCPUs used by the BYOL resource.
  * **Compartment** : The associated compartment.


The **Top BYOL resources by ECPUs** table lists the following:
  * **Resource OCID** : Click the link to go directly to the BYOL resource.
  * **ECPUs** : The total number of ECPUs used by the BYOL resource.
  * **Compartment** : The associated compartment.


## Adding a License 🔗 
You can view and add licenses from the **Product Licenses** page. Licenses are defined in terms of their requirements and entitlements, according to the metric the license is created for. 
You can create either Oracle or third-party licenses. Adding third-party licenses is similar to the process of adding Oracle products, however, you are restricted to OCPUs as the only metric. Work with your third-party vendor to better understand how a licensing term translates.
From the **Product Licenses** page you can view the overall list of product licenses, and view, add, import, or delete product licenses. The page lists the following:
  * **Product License** : Click the linked product license name to go to the [license details](https://docs.oracle.com/en-us/iaas/Content/LicenseManager/Concepts/licensemanageroverview.htm#licensemanager-viewlicense_details "You can view the list of licenses and product license details from the Product Licenses page.") page, or select **View** from the Actions menu.
  * **Status** : The license status. 
    * **Ok**
    * **Incomplete**
    * **Issues Found**
    * **Warning**
See [Viewing License Summary Activity](https://docs.oracle.com/en-us/iaas/Content/LicenseManager/Concepts/licensemanageroverview.htm#licensemanager_viewingoverview "The License Manager Overview page provides an overall summary of your license activity. The page allows you to get quick insights into your most utilized licenses, Bring Your Own License \(BYOL\) resources needing the most licenses by OCPUs and ECPUs, an overall count of BYOL and license included resources, and licenses at or near expiration.") for **Status** field descriptions.
  * **Requirement**
  * **Entitlement**
  * **Metric**
  * **License Records**


To add a license:
  1. Open the navigation menu and click **Governance & Administration**. Under **License Manager** , click **Product Licenses**. The License Manager **Product Licenses** page opens.
  2. Click **Add Product License**. The **Add Product License** panel opens.
  3. From **Vendor** , you can choose between Oracle or a third party. Select either **Oracle** (the license vendor for all Oracle products), or **Third Party** (the license vendor for all non-Oracle product licenses).
    1. (**Oracle** only) Select a **Product** from the list:
       * Oracle Database Enterprise Edition
       * Oracle Database Standard Edition
       * Oracle Database Standard Edition One
       * Oracle Database Standard Edition 2
You can also create a license by selecting **Options** and choosing the following from the **Product** list: 
       * Real Application Clusters
       * Multitenant
       * Active Data Guard
Select a **Metric** that matches your licensing terms, whether **Processors** or **Named User Plus**.
    2. (**Third Party** only) In **Vendor** and **Product** , enter the vendor and product names.
**Note** You cannot specify the metric, since **OCPU** is the only supported metric for third-party licenses.
  4. Under **License record** , enter the license record details.
**Note** You can add more license records after you create the product license.
     * **Record Name** : Specify a license record name. Avoid entering confidential information.
     * **Customer Support Identifier (CSI)** : Refer to your support contract and enter the CSI corresponding to the license.
     * **License Term** : You can specify if your license is unlimited (Unlimited License Agreement licenses), or has a specific count associated with it (Full Use licenses). Select either **Perpetual** or **Limited**. If **Perpetual** , specify the **Support Contract End Date**. If **Limited** , specify both the **License End Date** and the **Support Contract End Date**.
     * **License Quantity** : Specify the license quantity available for use based on your contractual terms, and accounting for licenses used on-premises or on other cloud platforms. Choose from **Unlimited** , or **Count**. If selecting **Count** , specify a license quantity value in the field (default is 1).
  5. Specify any license record [tagging settings](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm) to organize and track resources in your tenancy.
  6. To track license utilization on Compute resources, you can associate a compute image with your license. An _image_ is a template of a virtual hard drive that determines the operating system and other software for an instance.
Under **Image** , click **Choose Image**. The **Browse All Images** panel opens. The **Image Source** field changes based on whether the license you are creating is an **Oracle** or **Third Party** license.
When creating an **Oracle** license, **Oracle Images** is selected and the list of available images is displayed. Choose from the list of BYOL Oracle enterprise images and solutions enabled for Oracle Cloud Infrastructure. For any image under **Image Name** , you can click the down arrow (![Logging down arrow](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/inline-dropdownarrow.png)) to expand the **Image Build** details, and select the version number for the particular image. Only one image can be selected when creating the product license, but you can add more images after creation.
When creating a third-party license, **Partner Images** is selected and the list of available third-party partner images is displayed, in terms of the **Image Name** and the **Publisher**. Click the down arrow (![Logging down arrow](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/inline-dropdownarrow.png)) to expand the **Image Build** details, and select the version number for the particular partner image. As with Oracle images, one image can be selected when creating the product license, but you can add more images after creation.
After choosing the image, select the option to indicate that you agree to the legal terms for the chosen image. Click **Select Image**.
  7. Specify any product license [tagging settings](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm) to organize and track resources in your tenancy.
  8. Click **Add**.


A notification is displayed that the new license was saved successfully, and a new [license details](https://docs.oracle.com/en-us/iaas/Content/LicenseManager/Concepts/licensemanageroverview.htm#licensemanager-viewlicense_details "You can view the list of licenses and product license details from the Product Licenses page.") page (for the license you created) opens. The new license is also added to the **Product Licenses** page.
## Importing Oracle Product Licenses 🔗 
You can perform bulk import of Oracle product licenses, using a predefined Excel template.
From the **Product Licenses** page, you can download the provided template file, edit it, and then import it to add licenses.
The following types of licenses can be bulk-imported: 
  * **Full Use** : Licenses that have a specific count associated with them.
  * **ULA** : Unlimited License Agreement. A count does not need to be entered for ULA licenses.


Refer to your support contract for any licensing details, and account for any usage outside of Oracle Cloud Infrastructure when entering quantities for Full Use licenses. You can import multiple files but they can only be imported one at a time.
To import Oracle product licenses:
  1. Open the navigation menu and click **Governance & Administration**. Under **License Manager** , click **Product Licenses**. The License Manager **Product Licenses** page opens.
  2. Click **Import Oracle Product Licenses**. The **Import Oracle Product Licenses** panel opens.
  3. Click **Download Template**. The default file name is **bulkUploadTemplate.xlsx** , which you can then save to your file system and change if needed.
  4. The template file has the following fields where you can enter your license information:
     * Product Name
     * Metric
     * License Term
     * License End Date
**Note** A license end date is not needed for a perpetual license.
     * License Level
     * License Count
     * CSI
     * Support Contract End Date
  5. Save your bulk import file.
  6. On the **Product Licenses** page, **Import Oracle Product Licenses** panel, you can drag and drop your saved bulk import template, or click **browse to a location** to upload your file. The file appears in the panel.
  7. Click **Import**. The file is uploaded and a confirmation message is displayed on the **Product Licenses** page to indicate how many license records were imported, and if any duplicates were found.


Your newly imported licenses are accessible on the **Product Licenses** page, whereby you can then [view more details](https://docs.oracle.com/en-us/iaas/Content/LicenseManager/Concepts/licensemanageroverview.htm#licensemanager-viewlicense_details "You can view the list of licenses and product license details from the Product Licenses page.") about the licenses. 
## Viewing Licenses and their Details 🔗 
You can view the list of licenses and product license details from the **Product Licenses** page. 
License Manager helps you better understand your licensing needs, and facilitates making business decisions based on your licensing needs. After you have created your licenses, your licensing requirements are calculated every hour. You can view license entitlements and requirements, in the metric a license was created for, from the **Product Licenses** page. Licenses that do not meet your licensing requirements have a status of **Issues Found**. 
### Product Licenses List 🔗 
The **Product Licenses** page includes a tabular list of all product licenses. The following table describes the fields:
Field | Description  
---|---  
**Product License** | Click the linked product license name to go to the license details page, or select **View** from the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)).The page contains a **Product License Information** tab, and a **Tags** tab with tagging information. On a product details page you can:
  * View the overall status.
  * View or download resource consumption details.
  * View, edit, delete, and download license records.
  * View or add images associated with a product license.

  
**Status** |  The license status:
  * **Ok**
  * **Incomplete**
  * **Issues Found**
  * **Warning**

See [Viewing License Summary Activity](https://docs.oracle.com/en-us/iaas/Content/LicenseManager/Concepts/licensemanageroverview.htm#licensemanager_viewingoverview "The License Manager Overview page provides an overall summary of your license activity. The page allows you to get quick insights into your most utilized licenses, Bring Your Own License \(BYOL\) resources needing the most licenses by OCPUs and ECPUs, an overall count of BYOL and license included resources, and licenses at or near expiration.") for **Status** field descriptions.  
**Requirement** | What all the resources attributed to a license need, to be considered fully licensed.  
**Entitlement** | The sum of all license counts in your license records.  
**Metric** | The metric that matches your licensing terms.  
**License Records** | The number of records in the product license.  
**Actions (three dots) menu** |  Open this menu to:
  * View the product license details page.
  * Delete the product license.

  
You can drill into the details of a license by clicking its name in the **Product License** field, which displays the product license details page. The page contains a **Product License Information** tab, and a **Tags** tab with tagging information. On a product license details page you can:
  * View the overall status.
  * View or download resource consumption details.
  * View, edit, delete, and download license records.
  * View, add, or remove images associated with a product license.


The **Product License Information** tab contains the following information:
  * **OCID**
  * **Type**
  * **Metric**
  * **Vendor**
  * **Entitlement**
  * **Requirement** : Indicates the license requirement status and value. A green status indicates that the product is fully licensed. A red status indicates an overage, for cases where the license requirement exceeds the entitlement.
  * **Compartment**


### Viewing Consumption 🔗 
The **Consumption** table shows BYOL resource license requirements in the tenancy, allowing you to view the resources that are attributed to a license and their individual licensing requirements. Data is delayed by one hour. The table is organized in terms of the following:
  * **Resource OCID** : Click the link to go directly to the particular BYOL resource.
  * **Product Name** : The license product (ECPU-supported products are indicated in this field).
  * **Compartment** : The associated compartment.
  * **Requirement** (<type>): The license, where <type> refers to the metric type.


The warning icon indicates that you might not have licenses created for mandatory options to meet the licensing needs of a specific resource, per the license portability rules. You can navigate directly to the resources shown in the list by clicking the direct link for each Resource OCID shown in the **Consumption** table. As a result, you can make right-sizing changes as needed.
Click **Download CSV** to get a CSV version of the consumption information. The CSV file also has the same field listing as the **Consumption** table, including a **Missing Licensing Requirements** field. The **OCI Metric of Resource** field in the CSV file also indicates whether the resource refers to OCPU or ECPU.
### Viewing and Working with License Records 🔗 
The **License Records** table shows all the license records in a product license. From **License Records** you can view all license record details, add more license records, and edit or delete license records. The table has the following fields:
  * **Record Name** : Click the linked record name to open the license record details page, or select **View** from the Actions menu. From the license record details page, you can delete the record or add tags. The following information is displayed:
    * **OCID**
    * **Entitlement**
    * **Metric**
    * **Support End Date**
    * **Product**
    * **License Term**
    * **Customer Support Identifier (CSI)**
  * **Customer Support Identifier (CSI)**
  * **Quantity**
  * **License Expiration**
  * **Support Expiration Date** : If a license is at or near (within 90 days) its expiration date, the status is indicated in this field.


[To add more license records](https://docs.oracle.com/en-us/iaas/Content/LicenseManager/Concepts/licensemanageroverview.htm)
Click **Add** from a record's Actions menu. The **Add License Record** panel opens. You can add license records in the same manner as when you are [adding a new product license](https://docs.oracle.com/en-us/iaas/Content/LicenseManager/Concepts/licensemanageroverview.htm#licensemanager_addlicense "You can view and add licenses from the Product Licenses page. Licenses are defined in terms of their requirements and entitlements, according to the metric the license is created for."). Optionally, add any tagging options, or click **Add** to add the record. A message is displayed that the new record was saved successfully, and the **License Records** table reloads to display the new record.
[To edit a license record](https://docs.oracle.com/en-us/iaas/Content/LicenseManager/Concepts/licensemanageroverview.htm)
Click **Edit** from a record's Actions menu. The **Edit License Record** panel opens. You can modify the same fields as when you are [adding a new product license](https://docs.oracle.com/en-us/iaas/Content/LicenseManager/Concepts/licensemanageroverview.htm#licensemanager_addlicense "You can view and add licenses from the Product Licenses page. Licenses are defined in terms of their requirements and entitlements, according to the metric the license is created for."). Optionally, add any tagging options, or click **Save** when finished editing. A message is displayed to indicate that you saved successfully and the **License Records** table reloads to display the updated record.
[To delete a license record](https://docs.oracle.com/en-us/iaas/Content/LicenseManager/Concepts/licensemanageroverview.htm)
Click **Delete** from a record's Actions menu. Confirm the record deletion and click **Delete**. The **License Records** table reloads with the deleted record removed.
### Viewing and Working with Images 🔗 
The **Images** table shows the list of images associated with the product license. From **Images** , you can view all the associated images, or add and remove images. The table has the following fields:
  * **Image Name**
  * **Version**
  * **Publisher**


[To add more images](https://docs.oracle.com/en-us/iaas/Content/LicenseManager/Concepts/licensemanageroverview.htm)
Click **Add Image** from a record's Actions menu. The **Browse All Images** panel opens. You can add images in the same manner as when you are [adding a new product license](https://docs.oracle.com/en-us/iaas/Content/LicenseManager/Concepts/licensemanageroverview.htm#licensemanager_addlicense "You can view and add licenses from the Product Licenses page. Licenses are defined in terms of their requirements and entitlements, according to the metric the license is created for."). Agree to the legal terms and click **Select Image** when you're ready to add the new image. A message is displayed that the new image was saved successfully, and the image appears in the **Images** table. 
[To remove an image](https://docs.oracle.com/en-us/iaas/Content/LicenseManager/Concepts/licensemanageroverview.htm)
Click **Remove** from an image's Actions menu. Confirm the image removal and click **Remove**. The **Images** table updates with the image removed.
## Using Notifications 🔗 
The License Manager **Notifications** page allows you to manage the list of email addresses that can be notified about expirations or subscription overages. Emails are sent on a weekly basis.
If there are items that require action, you receive an email that provides a License Manager summary. The email highlights the product licenses that are over-subscribed, and license records near or past their license or support contract expiration dates. 
To manage notifications, open the navigation menu and click ****Governance & Administration****. Under **License Management** , click **Notifications**. The License Manager **Notifications** page opens.
In the **Email Recipients** field, enter one or more email addresses to receive alert notifications. Multiple addresses can be separated using commas, spaces, tabs, or newlines.
When finished adding email addresses, click **Save**. A message is displayed to indicate that the email addresses were saved successfully.
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following in the [License Manager API](https://docs.oracle.com/iaas/api/#/en/licensemanager/) for license management.
To manage bulk uploads:
  * [BulkUploadLicenseRecords](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/BulkUploadLicenseRecordsDetails/BulkUploadLicenseRecords)
  * [GetBulkUploadTemplate](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/BulkUploadTemplate/GetBulkUploadTemplate)


To manage compartment configuration:
  * [GetConfiguration](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/Configuration/GetConfiguration)
  * [UpdateConfiguration](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/Configuration/UpdateConfiguration)


To manage license metrics:
  * [GetLicenseMetric](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/LicenseMetric/GetLicenseMetric)


To manage license records:
  * [CreateLicenseRecord](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/LicenseRecord/CreateLicenseRecord)
  * [DeleteLicenseRecord](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/LicenseRecord/DeleteLicenseRecord)
  * [GetLicenseRecord](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/LicenseRecord/GetLicenseRecord)
  * [UpdateLicenseRecord](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/LicenseRecord/UpdateLicenseRecord)
  * [ListLicenseRecords](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/LicenseRecordCollection/ListLicenseRecords)


To manage product licenses:
  * [CreateProductLicense](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/ProductLicense/CreateProductLicense)
  * [DeleteProductLicense](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/ProductLicense/DeleteProductLicense)
  * [GetProductLicense](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/ProductLicense/GetProductLicense)
  * [UpdateProductLicense](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/ProductLicense/UpdateProductLicense)
  * [ListProductLicenses](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/ProductLicenseCollection/ListProductLicenses)
  * [ListProductLicenseConsumers](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/ProductLicenseConsumerCollection/ListProductLicenseConsumers)


To manage top utilized product licenses and resources:
  * [ListTopUtilizedProductLicenses](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/TopUtilizedProductLicenseCollection/ListTopUtilizedProductLicenses)
  * [ListTopUtilizedResources](https://docs.oracle.com/iaas/api/#/en/licensemanager/latest/TopUtilizedResourceCollection/ListTopUtilizedResources)


Was this article helpful?
YesNo


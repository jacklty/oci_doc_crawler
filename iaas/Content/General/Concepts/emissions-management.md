Updated 2025-02-13
# Emissions Management
Use the Carbon Emissions Analysis page to track the estimated carbon emissions footprint while using Oracle Cloud Infrastructure services.
## Carbon Emissions Analysis Overview 🔗 
Carbon Emissions Analysis is an easy-to-use visualization tool that allows paying commercial OCI customers to track their estimated carbon emissions footprint. Charts and corresponding data tables of carbon emissions usage can be generated, based on the selected time range, filters, and grouping dimensions.
OCI uses Green House Gas (GHG) protocol guidance to automate calculating carbon emissions for customers' purchased goods using the by-spend method across most services, based on the customer cost before discounts and the [Oracle Clean Cloud OCI Data Sheet](https://www.oracle.com/a/ocom/docs/corporate/citizenship/clean-cloud-oci.pdf).
**Important** Carbon Emissions Analysis isn't intended to be used as a developer tool to reduce emissions. All customer carbon emissions provided by the OCI Carbon Emissions Analysis tool and [Usage API](https://docs.oracle.com/iaas/api/#/en/usage/) are estimates.
You can use Carbon Emissions Analysis for spot checks of carbon emissions trends, and for generating reports. Common scenarios you might be interested in include the following:
  * Viewing carbon emissions for compartment X and its children for a chosen time range, grouped by service or by tag.
  * Viewing carbon emissions for tag key A and tag key B for a chosen time range, values X, Y, and Z, grouped by service and product description (SKU).
  * Viewing carbon emissions for a service by a chosen time range, grouped by compartment name.


You can view one of the predefined, default **System Reports** from the **Reports** menu, and you can choose the dates you're interested in. By default, the **Customer Carbon Footprint by Service** report is shown when the Carbon Emissions Analysis page first opens. Use the **Filters** menu to filter by the specific tags, compartments, services, or other filter you want, and pick how you want it grouped using the **Grouping dimensions** menu. As a result, a chart and corresponding data table are generated, and can also be downloaded as a CSV data table, PDF, or chart image. You can also save a custom set of dates, filters, and grouping dimensions into a [saved report](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/carbon-analysis-savingreports.htm#carbon-analysis-savingreports "Use the Report actions menu in Carbon Emissions Analysis to create a saved report.") and then view it later in the Console.
Up to 50 custom reports can be saved, which allows you to create custom reports with charts and tables of carbon emissions data using different combinations of date ranges, filters, and grouping dimensions. See [Viewing Carbon Emissions Reports](https://docs.oracle.com/en-us/iaas/Content/General/Tasks/carbon-analysis-viewreports.htm#carbon-analysis-viewreports "View carbon emissions reports using the Console or the API.") for more information on viewing reports and the related Carbon Emissions Analysis query settings.
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). 
To use Carbon Emissions Analysis, the following policy statements are required:
```
Allow group <group_name> to read carbon-emission-reports in tenancy
Allow group <group_name> to manage carbon-emission-reports in tenancy
```

## Authentication and Authorization 🔗 
Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).
An administrator in an organization needs to set up **groups** , **compartments** , and **policies** that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see [Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm). 
If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.
Was this article helpful?
YesNo


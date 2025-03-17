Updated 2025-03-11
# Resource Identifiers
This topic describes the different ways your Oracle Cloud Infrastructure resources are identified.
## Oracle Cloud IDs (OCIDs) 🔗 
Most types of Oracle Cloud Infrastructure resources have an Oracle-assigned unique ID called an _Oracle Cloud Identifier_ (OCID). It's included as part of the resource's information in both the Console and API. 
**Important** To use the API, you need the OCID for your **tenancy**. For information about where to find it, see the next section. 
OCIDs use this syntax: 
Copy
```
ocid1.<RESOURCE TYPE>.<REALM>.[REGION][.FUTURE USE].<UNIQUE ID>
```

  * **ocid1:** The literal string indicating the version of the OCID.
  * **resource type:** The type of resource (for example, `instance`, `volume`, `vcn`, `subnet`, `user`, `group`, and so on). 
  * **realm:** The realm the resource is in. A _realm_ is a set of regions that share entities. Possible values are `oc1` for the [commercial realm](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm#About), `oc2` for the [Government Cloud realm](https://docs.oracle.com/iaas/Content/gov-cloud/govfedramp.htm#Regions), or `oc3` for the [Federal Government Cloud realm](https://docs.oracle.com/iaas/Content/gov-cloud/govfeddod.htm#US_Federal_Cloud_with_DISA_Impact_Level_5_Authorization_Console_Signin_URLs). The regions in the commercial realm (OC1) belong to the domain `oraclecloud.com`. The regions in the Government Cloud (OC2) belong to the domain `oraclegovcloud.com`.
  * **region** : The region the resource is in (for example, `phx`, `iad`, `eu-frankfurt-1`). With the introduction of the Frankfurt region, the format switched from a three-character code to a longer string. This part is present in the OCID only for regional resources or those specific to a single availability domain. If the region is not applicable to the resource, this part might be blank (see the example tenancy ID below). 
  * **future use:** Reserved for future use. Currently blank.
  * **unique ID:** The unique portion of the ID. The format may vary depending on the type of resource or service. 


### Example OCIDs
_Tenancy:_
Copy
```
ocid1.tenancy.oc1..aaaaaaaaba3pv6wkcr4jqae5f44n2b2m2yt2j6rx32uzr4h25vqstifsfdsq
```

_Instance:_
Copy
```
ocid1.instance.oc1.phx.abuw4ljrlsfiqw6vzzxb43vyypt4pkodawglp3wqxjqofakrwvou52gb6s5a
```

## Where to Find Your Tenancy's OCID 🔗 
If you use the Oracle Cloud Infrastructure API, you need your tenancy's OCID in order to sign the API requests. You also use the tenancy ID in some of the IAM API operations.
Get the tenancy OCID from the Oracle Cloud Console on the **Tenancy Details** page: 
  1. In the navigation bar, select the **Profile** menu and then select **Tenancy: <your_tenancy_name>**.
  2. The tenancy OCID is shown under **Tenancy Information**. Select **Show** to display the entire ID or select **Copy** to copy it to your clipboard.
[![Tenancy Details page showing the location of the tenancy OCID](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/tenancy-details-page.png)](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/tenancy-details-page.png)


The tenancy OCID looks something like this (notice the word "tenancy" in it):
Copy
```
ocid1. _tenancy_.oc1..<unique_ID>
```

## Name and Description 🔗 
The IAM service requires you to assign a unique, unchangeable _name_ to each of your IAM resources (users, groups, dynamic groups, federations, and policies). The name must be unique within the scope of the type of resource (for example, you can only have one user with the name BobSmith). Notice that this requirement is specific to IAM, but also applies to some other services. (Most services let you assign an optional display name.)
The name you assign to a user at creation is their login for the Console. 
You can use these names instead of the OCID when writing a policy (for example, `Allow group <GROUP NAME> to manage all-resources in compartment <COMPARTMENT NAME>`). 
In addition to the name, you must also assign a _description_ to each of your IAM resources (although it can be an empty string). It can be a friendly description or other information that helps you easily identify the resource. The description does not have to be unique, and you can change it whenever you like. For example, you might want to use the description to store the user's email address if you're not already using the email address as the user's unique name. 
## Display Name 🔗 
For most of the Oracle Cloud Infrastructure resources you create (other than those in IAM and other services that require resources to have a unique, unchangeable name and a description), you can optionally assign a _display name_. It can be a friendly description or other information that helps you easily identify the resource. The display name does not have to be unique, and you can change it whenever you like. The Console shows the resource's display name along with its OCID. 
**Caution** Avoid entering confidential information when assigning descriptions, tags, or friendly names to cloud resources through the Oracle Cloud Infrastructure Console, API, or CLI.
Was this article helpful?
YesNo


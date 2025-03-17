Updated 2024-09-26
# Overview of Self-Registration Profiles
Use self-registration profiles to create accounts in a verified or unverified state. Customize the self-registration process by specifying the user's email domains allowed when self-registering, and adding header, footer, success, and user consent text.
## Introduction
Using self-registration profiles, you can: 
  * Create a self-registration **consumer flow** that allows users to create an account in a verified state. Use the REST API to turn off the `activationEmailRequired` option. The user can then directly sign in using a username and password to authenticate. 
  * Create a self-registration **partner flow** that allows users to create an account in an unverified state. Use the REST API to turn on the `activationEmailRequired` option so that a user receives a link in the welcome email to verify the user. After the user clicks this link, the user's state is changed to verified and the user can sign in. 
  * Delete profiles using the user interface or the REST API.
  * Specify whether users are prompted and must accept a user consent before self-registering.
  * Assign groups to a profile so that users are assigned to all the groups that are part of that profile.
  * Specify the user's email domains allowed when accessing the self-registration process. Only users with access to these specific email domains are allowed to register.
  * Customize the self-registration login page with your header and footer logos.
  * Customize the header, footer, success, and user consent text.


This section contains the following topics:
  * [Creating a Self-Registration Profile](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/create-self-registration-profiles.htm#create-self-registration-profiles "Create self-registration profiles in IAM to manage self-registration for different sets of users, approval policies, and applications.")
  * [Activating a Self-Registration Profile](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/activating-self-registration-profiles.htm#activating-self-registration-profiles "Activate a newly created profile in IAM so that you can use it.")
  * [Listing a Self-Registration Profile](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/list-self-registration-profiles.htm#create-self-registration-profiles "List self-registration profiles in IAM.")
  * [Updating a Self-Registration Profile](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/editing-self-registration-profiles.htm#editing-self-registration-profiles "Edit options in self-registration profiles in IAM. For example, you can assign the profile to new groups or change the allowed email domains.")
  * [Deactivating a Self-Registration Profile](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/deactivating-self-registration-profiles.htm#activating-self-registration-profiles "Deactivate a self-registration profile in IAM when you no longer need it.")
  * [Deleting a Self-Registration Profile](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/deleting-self-registration-profiles.htm#deleting-self-registration-profiles "You can delete self-registration profiles in IAM that you aren't using.")


## Required Policy or Role 🔗 
To create self-registration profiles, you must have one of the following access grants:
  * Be a member of the Administrators group
  * Be granted the Identity Domain Administrator role
  * Be a member of a group granted `manage` domains


To understand more about policies and roles, see [The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/getstarted/identity-domains.htm#The), [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed."), and [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
Was this article helpful?
YesNo


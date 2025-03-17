Updated 2025-02-28
# Managing Password Policies
Create and manage group-based password policies for an identity domain in IAM.
The following overview topics are in this section:
  * [Working with Password Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordpolicies/Managing-Password-Policies.htm#concept_nps_lqs_l4b "Password policies let you define a set of criteria for user passwords in an identity domain in IAM. The criteria are enforced when a user creates their own password for an identity domain.")
  * [Limits for Password Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordpolicies/Managing-Password-Policies.htm#password_limits "An identity domain in IAM has the following password policy limits.")


You can perform the following tasks related to password policies:
  * [Listing Password Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordpolicies/listing-password-policies.htm#untitled1 "Retrieve a list of password policies.")
  * [Creating a Password Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordpolicies/Managing-Password-Policies_set-password-policies-your-identity-domain.htm#set-password-policies "Create up to ten password policies in an identity domain in IAM, assign relative priorities to them, and attach them to groups. A group can't be assigned to more than one password policy.")
  * [Modifying the Custom Password Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordpolicies/modify-custom-password-policy.htm#modify-custom-password-policy "Adjust the strength of the custom password policy in an identity domain in IAM to meet the business and security requirements for your enterprise applications.")
  * [Testing a Password Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordpolicies/Managing-password-policies_To-test-a-password-policy.htm#test-password-policy "Test a password policy in an identity domain in IAM.")
  * [Removing a Password Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordpolicies/To-remove-a-password-policy.htm#remove-password-policy "Remove a password policy that you no longer need in an identity domain in IAM.")


## Required Policy or Role 🔗 
To manage identity domain settings, you must have one of the following access grants:
  * Be a member of the Administrators group
  * Be granted the Identity Domain Administrator role or the Security Administrator role
  * Be a member of a group granted `manage` domains


## Working with Password Policies 🔗 
Password policies let you define a set of criteria for user passwords in an identity domain in IAM. The criteria are enforced when a user creates their own password for an identity domain.
Password policies are assigned to groups. All users who are members of the group must meet the requirements of the password policy when creating passwords for their accounts. You can create up to 10 password policies per identity domain and assign each policy a priority. When a user is a member of more than one group, the password policy with the highest priority applies when that user creates their password.
If a user is a member of a group that doesn't have a password policy assigned, the default password policy is enforced. 
### Password Policy Validation 🔗 
When a user changes an existing password or resets a forgotten password, password policy validation happens _after_ the user enters the new password and _then_ clicks the button to change or reset it. See [Changing Your Password](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/change-your-password.htm#change-your-password "Passwords are valid only for the period specified by the password policy defined by your administrator. When your password expires, you must update your password to access an identity domain.").
**Note** Password validation doesn't happen at runtime.
### Deleting Password Policies 🔗 
When you delete a password policy, the groups, and therefore users of the groups, are no longer associated with it. Password criteria for those users reverts to the highest-priority password policy assigned to them.
When you delete a group, the password policy attached to the group is no longer be assigned to users who had been members of the group. Instead, the highest priority password policy available is applied to the users.
### Types of Password Policies 🔗 
You can set the following types of password policies for an identity domain: 
  * Simple: Use this policy for developer services and demos when you don't want to customize a policy for them. You can't change this type of password policy.
  * Standard: Use this policy when you don't want to use the Oracle-recommended password policy for your enterprise applications. You can't change this type of password policy.
  * Custom: Use this policy to tailor the strength of your password policy to meet the business and security requirements for your enterprise applications. It's your responsibility to make the minimal requirements of the custom password policy strong.


## Limits for Password Policies 🔗 
An identity domain in IAM has the following password policy limits.
You can create up to 10 password policies per identity domain.
You can't assign a group to more than one password policy.
Was this article helpful?
YesNo


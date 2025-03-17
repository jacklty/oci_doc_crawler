Updated 2024-09-26
# Getting Started with Policies
If you're new to Oracle Cloud Infrastructure Identity and Access Management (IAM) policies, this topic gives guidance on how to proceed.
## If You're Doing a Proof-of-Concept 🔗 
If you're just trying out Oracle Cloud Infrastructure or doing a proof-of-concept project with infrastructure resources, you may not need more than a few administrators with full access to everything. In that case, you can simply create any new users you need and add them to the Administrators group. The users will be able to do anything with any kind of resource. And you can create all your resources directly in the tenancy (the root compartment). You don't need to create any compartments yet, or any other policies beyond the Tenant Admin Policy, which automatically comes with your tenancy and can't be changed.
**Note**
Don't forget to add your new users to the Administrators group; it's easy to forget to do that after creating them.
## If You're Past the Proof-of-Concept Phase 🔗 
If you're past the proof-of-concept phase and want to restrict access to your resources, first:
  * Make sure you're familiar with the basic IAM components, and read through the example scenario: [Overview of Identity and Access Management](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/overview.htm#Overview_of_Oracle_Cloud_Infrastructure_Identity_and_Access_Management)
  * Think about how to organize your resources into compartments: [Learn Best Practices for Setting Up Your Tenancy](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm)
  * Learn the basics of how policies work: [How Policies Work](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#How_Policies_Work)
  * Check out some typical policies: [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top)
  * Read the FAQs below


## Policy FAQs 🔗 
[Which of the services within Oracle Cloud Infrastructure can I control access to through policies?](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm)
All of them, including IAM itself. You can find specific details for writing policies for each service in the [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
[Can users do anything without an administrator writing a policy for them?](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm)
Yes. All users can automatically do these things without an explicit policy:
  * Change or reset their own Console password. 
  * Manage their own API signing keys and other credentials.


[Why should I separate resources by compartment? Couldn't I just put all the resources into one compartment and then use policies to control who has access to what?](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm)
You could put all your resources into a single compartment and use policies to control access, but then you would lose the benefits of measuring usage and billing by compartment, simple policy administration at the compartment level, and clear separation of resources between projects or business units.
[Can I control or deny access to an individual user?](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm)
Yes. However, a couple things to know first:
  * Enterprise companies typically have multiple users that need similar permissions, so policies are designed to give access to _groups_ of users, not individual users. A user gains access by being in a group. 
  * Policies are designed to _allow_ access; there's no explicit "deny" when you write a policy. 


If you need to grant access to a particular user, you can add a condition to the policy that specifies the user's OCID in a variable. This construction restricts the access granted in the policy to only the user specified in the condition. For example:
Copy
```
allow any-group to read object-family in compartment ObjectStorage where request.user.id ='ocid1.user.oc1..<user_OCID>'
```

For information about using conditions and variables in policies, see [Conditions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#one).
If you need to restrict a particular user's access, you can:
  * Remove the user from the particular group of interest 
  * Delete the user entirely from IAM (you have to remove the user from all groups first)


[How do I delete a user?](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm)
First ensure the user isn't in any groups. Only then can you delete the user.
[How do I delete a compartment?](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm)
See [To delete a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm#To_delete_a_compartment).
[How can I tell which policies apply to a particular group or user?](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm)
You need to look at the individual statements in all your policies to see which statements apply to which group. There's not currently an easy way to get this information. 
[How can I tell which policies apply to a particular compartment?](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm)
You need to look at the individual statements in all the policies in the tenancy to see if any apply to the particular compartment. You also need to look at any policies in the compartment itself. Policies in any of the sibling compartments _cannot_ refer to the compartment of interest, so you don't need to check those policies.
Was this article helpful?
YesNo


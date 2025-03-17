Updated 2024-09-26
# Policy Attachment
When you create an IAM policy, you must attach it to a compartment in IAM.
When you write a policy in the root compartment, the policy applies to the entire tenancy. Typically the Administrators group, or a similar group you create, manages policies. If you attach a policy to a tenancy, anyone who can manage policies in the tenancy can then change or delete the policy for the entire tenancy. Users with access only to a child compartment can't change or delete a policy attached to the root compartment. 
If you attach the policy to a child compartment, then users with access to manage the policies in that compartment manage the policy. This means it's easy to let compartment administrators manage their own compartment's policies, without giving them broader access in other compartments or tenancies. 
Was this article helpful?
YesNo


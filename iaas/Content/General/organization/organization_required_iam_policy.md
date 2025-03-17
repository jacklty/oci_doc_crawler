Updated 2025-02-13
# Required IAM Policy
Learn about Organization Management required IAM policies.
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm#Getting_Started_with_Policies) and [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top).
To use Organization Management, the following policy statements are required:
Copy
```
Allow group linkUsers to use organizations-family in tenancy
Allow group linkAdmins to manage organizations-family in tenancy
```

To accept an invitation but not create one use the following:
Copy
```
allow group linkAccepters to manage organizations-recipient-invitations in tenancy
```

To view the current linked tenancies but not the invitations:
Copy
```
allow group linkViewers to read organizations-links in tenancy
```

Was this article helpful?
YesNo


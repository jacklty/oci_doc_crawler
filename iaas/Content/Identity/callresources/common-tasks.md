Updated 2023-07-21
# Common Tasks
Find out how to perform common tasks to call services from an instance.
[How do I query the instance metadata service to query the certificate on the instance?](https://docs.oracle.com/en-us/iaas/Content/Identity/callresources/common-tasks.htm)
Use this curl command: `curl http://169.254.169.254/opc/v1/identity/cert.pem`
[How frequently is the certificate rotated on each instance?](https://docs.oracle.com/en-us/iaas/Content/Identity/callresources/common-tasks.htm)
The certificate is rotated multiple times each day.
[What happens if I receive a 401-Not Authenticated error?](https://docs.oracle.com/en-us/iaas/Content/Identity/callresources/common-tasks.htm)
If you receive a 401-Not Authenticated error, check the following issues:
  * Try to run the command again. Sometimes the certificate rotation and the request occur at the same time.
  * The certificate might be expired. Verify the certificate is valid.


[Can I change the frequency at which the certificate is rotated?](https://docs.oracle.com/en-us/iaas/Content/Identity/callresources/common-tasks.htm)
No. You can't change the frequency at which the certificate is rotated. However, you can change the policy on the dynamic group. If you think an instance has been compromised, you can either change the policy on the dynamic group to revoke permissions for all members of the group, or you can remove the instance from the dynamic group. See [Can I remove an instance from a dynamic group?](https://docs.oracle.com/en-us/iaas/Content/Identity/callresources/common-tasks.htm#Can)
[What happens if the certificate is rotated in the middle of a long running operation?](https://docs.oracle.com/en-us/iaas/Content/Identity/callresources/common-tasks.htm)
The token expiration is independent of the certificate expiration period. And, it also depends on the application you are interacting with. For example, if Object Storage does not have a multipart PUT operation, then it does not matter how long the operation runs.
[Are the certificates accessible for all users on an instance?](https://docs.oracle.com/en-us/iaas/Content/Identity/callresources/common-tasks.htm)
Yes. Ensure that only users who should be granted the access that you have granted to the dynamic group, have access to the instance.
[Are dynamic groups created at the tenancy level?](https://docs.oracle.com/en-us/iaas/Content/Identity/callresources/common-tasks.htm)
Yes.
[Can I remove an instance from a dynamic group?](https://docs.oracle.com/en-us/iaas/Content/Identity/callresources/common-tasks.htm)
Yes. You can remove it by modifying the matching rule to exclude it. See below for an example.
[Can I exclude specific instances in a compartment from the dynamic group?](https://docs.oracle.com/en-us/iaas/Content/Identity/callresources/common-tasks.htm)
Yes. For example, assume you want to exclude two specific instances in a compartment from the dynamic group. Write a matching rule like this:
```
All {instance.compartment.id = '<compartment_ocid>',
 instance.id != '<instance1_to_exclude_ocid>', instance.id != '<instance2_to_exclude_ocid>'}

```

The above rule includes all instances in the compartment except those with the OCIDs specified.
Was this article helpful?
YesNo


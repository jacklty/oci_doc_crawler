Updated 2025-02-12
# How-to: Automatically Start and Stop a VM Instance
You can automatically start and stop Compute VM instances using the OCI CLI.
The OCI console doesn't have a built-in feature to perform the scheduled stop and start of a Compute instance. As a workaround, set up OCI CLI on a server and perform a scheduled task at the operating system level.
Use the `compute instance action` command to stop and start instances. For example:
```
oci compute instance action --action STOP --instance-id
oci compute instance action --action START --instance-id
```

Create a `cron` job or task scheduler to perform this action at regular intervals. For more information, see:
  * [Installing the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliinstall.htm)
  * [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest)


Was this article helpful?
YesNo


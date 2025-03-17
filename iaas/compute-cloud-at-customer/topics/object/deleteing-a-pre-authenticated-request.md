Updated 2024-01-18
# Deleting a Preauthenticated Request
On Compute Cloud@Customer, you can delete preauthenticated requests.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/deleteing-a-pre-authenticated-request.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/deleteing-a-pre-authenticated-request.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/deleteing-a-pre-authenticated-request.htm)


  * This task isn't available in the Console.
  * Use the [oci os preauth-request delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/preauth-request/delete.html) command and required parameters to delete a preauthenticated request.
Copy
```
oci os preauth-request delete --namespace-name <object_storage_namespace> --bucket-name <bucket_name> --par-id <preauthenticated_request_id> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeletePreauthenticatedRequest](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/PreauthenticatedRequest/DeletePreauthenticatedRequest) operation to delete a preauthenticated request.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


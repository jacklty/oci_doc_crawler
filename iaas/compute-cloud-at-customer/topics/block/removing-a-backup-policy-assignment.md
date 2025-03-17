Updated 2024-04-19
# Removing a Backup Policy Assignment
On Compute Cloud@Customer, you can remove a backup policy assignment from a volume or volume group. A volume group cannot be assigned a backup policy if any of the volumes in the group already is assigned a backup policy.
## Using the CLI
  1. Use the appropriate `list` command to get the OCID of the volume or volume group from which you want to remove the backup policy assignment. For example: `oci bv volume list`.
  2. Use the volume or volume group OCID from the preceding step as the argument of the `--asset-id` option in the following command to get the backup policy assignment OCID.
```
$ oci bv volume-backup-policy-assignment get-volume-backup-policy-asset-assignment \
--asset-id ocid1.volume._unique_ID_
{
 "data": [
  {
   "asset-id": "ocid1.volume._unique_ID_",
   "id": "ocid1.backuppolicyassignment._unique_ID_",
   "policy-id": "ocid1.volumebackuppolicy._unique_ID_",
   "time-created": "2023-06-07T02:03:53.466062+00:00"
  }
 ]
}
```

  3. Use the backup policy assignment OCID from the preceding step to delete this assignment so that this resource has no backup policy assigned.
```
$ oci bv volume-backup-policy-assignment delete \
--policy-assignment-id ocid1.backuppolicyassignment.AK00661530.scasg01._unique_ID_ \
--force
{
 "etag": "7a0ca7dd-50f7-4d60-9689-aaa442ac4348",
 "opc-work-request-id": "ocid1.workrequest._unique_ID_"
}
```

The following command shows that this asset has no backup policy assigned.
```
$ oci bv volume-backup-policy-assignment get-volume-backup-policy-asset-assignment \
--asset-id ocid1.volume.**_unique_ID_**
$ 
```



Was this article helpful?
YesNo


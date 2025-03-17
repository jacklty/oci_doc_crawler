Updated 2023-09-26
# Deleting an Instance Backup
On Compute Cloud@Customer, you can use the `DELETE` API to delete exported and imported instance backups. 
The API sets the exported backup lifecycle state to ****TERMINATED**** and performs one of these actions based on the type of backup:
  * **Imported instance backups:** Deletes the instance backup.
  * **Exported instance backups:** Deletes the instance backup (source for importing) from object storage bucket


Terminated instance backups are eventually cleaned up by a background task.
**Using the API**
`DELETE` API – Deletes instance backups.
**API endpoint**
```

https://<mgmt_node_VIP>:30003/20160918/instancesBackups<instance_backup_OCID>
```

where: 
  * <mgmt_node_VIP> is the management node VIP host name or IP address.
  * <instance_backup_OCID> is the instance backup ID.


Was this article helpful?
YesNo


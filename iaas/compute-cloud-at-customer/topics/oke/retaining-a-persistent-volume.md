Updated 2024-10-07
# Retaining a Persistent Volume
Learn how to retain a persistent volume (PV) on Compute Cloud@Customer. 
Rather than delete a PV, you might prefer to retain the PV after all associated PVCs are deleted, for example if the volume contains critical data. See [Changing the Reclaim Policy of a Persistent Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/retaining-a-persistent-volume.htm#retaining-a-persistent-volume__change_pv_reclaim_policy) for instructions to change the reclaim policy of the PV so that the PV will be retained after all associated PVCs are deleted.
If the Persistent Volume Reclaim Policy is Delete, the PV is automatically deleted when all PVCs that are associated with this PV are deleted. To prevent this behavior, specify the Retain policy. With the Retain policy, the PV isn't deleted but is released of its claim. See [Recovering the Data from a Released Persistent Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/retaining-a-persistent-volume.htm#retaining-a-persistent-volume__recover_pvc_data) for instructions to recover the data.
If you decide you want to delete the PV even though it was retained, or you want to delete the PV after you have recovered the data, use the following command:
Copy
```
$ kubectl delete pv pv_name
```

## Changing the Reclaim Policy of a Persistent Volume 🔗 
  1. List the PVs in the cluster.
Copy
```
$ kubectl get pv
NAME  CAPACITY ACCESS MODES RECLAIM POLICY STATUS CLAIM      STORAGECLASS REASON AGE
fss-pv 200Gi   RWX      Delete     Bound  default/fss-pvc pca-fss        20h
```

  2. Change the reclaim policy of the PV.
Copy
```
$ kubectl patch pv fss-pv -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'
```

  3. Verify the reclaim policy change.
The `RECLAIM POLICY` column should now say `Retain`.
Copy
```
$ kubectl get pv
```



## Recovering the Data from a Released Persistent Volume 🔗 
The PV isn't available for another claim after the PV has been released of its previous claim because the previous claimant's data is still on the volume. Recover the data and then re-create the PV using the same storage to make a new claim on that storage.
  1. Delete the PV.
Copy
```
$ kubectl delete pv pv_name
```

The associated block volume or file system still exists after the PV is deleted.
  2. Manually recover and clean up the data on the block volume or file system.
  3. (Optional) Manually delete the block volume or file system.
To reuse the same block volume or file system, create a new PV with the same storage asset definition.


Was this article helpful?
YesNo


Updated 2024-04-02
# Deleting a Persistent Volume
Learn how to delete a persistent volume (PV), or retain a PV after all associated persistent volume claims (PVCs) are deleted on Compute Cloud@Customer.
To delete a PVC, see [Deleting a Persistent Volume Claim](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/deleting-a-persistent-volume-claim.htm#deleting-a-persistent-volume-claim "On Compute Cloud@Customer, to delete a PVC, first delete all pods that are using that PVC. If you attempt to delete the PVC while a pod is still using the PVC, the PVC will be stuck in Terminating state and will not be deleted. When all the pods that are using that PVC are deleted, the PVC is deleted.").
For file system storage, the default behavior is to retain the PV when all associated PVCs are deleted.
For block volume storage, the default behavior is to delete the PV when all associated PVCs are deleted. You might prefer to retain the PV after all associated PVCs are deleted, for example, if the volume contains critical data. See [Retaining a Persistent Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/retaining-a-persistent-volume.htm#retaining-a-persistent-volume "Learn how to retain a persistent volume \(PV\) on Compute Cloud@Customer.").
If a PV is retained, you can optionally delete the PV later.
Was this article helpful?
YesNo


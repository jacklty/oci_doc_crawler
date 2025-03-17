Updated 2024-04-02
# Deleting a Persistent Volume Claim
On Compute Cloud@Customer, to delete a PVC, first delete all pods that are using that PVC. If you attempt to delete the PVC while a pod is still using the PVC, the PVC will be stuck in Terminating state and will not be deleted. When all the pods that are using that PVC are deleted, the PVC is deleted.
  1. List all pods that are using the PVC.
Ensure that you have JQ command line utilities installed to query JSON objects.
Use the following command to list pods across all the namespaces that are associated with the PVC that you want to delete.
```
$ kubectl get pods --all-namespaces -o=json | jq -c '.items[] | {name: .metadata.name, namespace: .metadata.namespace, claimName: .spec | select(has("volumes")).volumes[] | select(has("persistentVolumeClaim")).persistentVolumeClaim.claimName} | select(.claimName != null)'
{"name":"pod1_name","namespace":"namespace1_name","claimName":"claim1_name"}
{"name":"pod2_name","namespace":"namespace1_name","claimName":"claim1_name"}
{"name":"pod3_name","namespace":"namespace2_name","claimName":"claim2_name"}
```

To list pods only in the current namespace, use the same command as the preceding command except omit the `--all-namespaces` option.
  2. Delete all pods that are using the PVC.
Use the pod names reported by the `kubectl get pods` command that are associated with the `claimName` that you want to delete.
Copy
```
$ kubectl delete pod pod1_name
        pod2_name
      
```

  3. Delete the PVC.
Copy
```
$ kubectl delete pvc claim1_name
      
```

  4. (Optional) Delete the PV.
If the Persistent Volume Reclaim Policy is Delete, the PV is automatically deleted when all PVCs that are associated with this PV are deleted.
To list all PVCs, use the `kubectl get pvc` command.
If the Persistent Volume Reclaim Policy is Retain, you can use the following command to delete the PV:
Copy
```
$ kubectl delete pv pv_name
      
```



Was this article helpful?
YesNo


Updated 2024-06-05
# Troubleshooting the OCI Native Ingress Controller
_Find out how to fix common problems with the OCI native ingress controller._
Having installed and configured the OCI native ingress controller (either as a standalone program or as a cluster add-on), use the information in this topic to identify and resolve common problems.
## Reviewing Validation Errors 🔗 
The OCI native ingress controller identifies conflicting declarations in ingress resource manifests, and outputs validation errors in pod logs. 
To review the log of the pod running the OCI native ingress controller:
  1. Obtain the name of the OCI native ingress controller pod by entering:
Copy
```
kubectl get pods -n native-ingress-controller-system --selector='app.kubernetes.io/name in (oci-native-ingress-controller)' -o wide

```

If multiple pod names are returned, identify the leader by reviewing the log for each pod and eliminating pods that are stuck in an acquiring lease state. 
  2. Stream the OCI native ingress controller pod's log by entering:
Copy
```
kubectl logs -f <pod-name> -n native-ingress-controller-system
```

For example:
```
kubectl logs -f oci-native-ingress-controller-6dc86789b8-6rbkb -n native-ingress-controller-system
```

  3. Review validation errors output by the OCI native ingress controller by searching the log for `validation failure` strings.


Was this article helpful?
YesNo


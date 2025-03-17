Updated 2023-10-06
# Service Mesh Kubernetes Resource Conditions
In Kubernetes, you manage Service Mesh resources using `kubectl` tooling. Manage Service Mesh components through custom resources which are extensions to the Kubernetes API. To find out what state a resource is in, look at the status condition for a custom resource.
**Service Mesh Custom Resource Conditions Example**
Copy
```
status:
 conditions:
  - lastTransitionTime: '2022-05-17T02:13:25Z'
   message: Dependencies resolved successfully
   observedGeneration: 1
   reason: Successful
   status: 'True'
   type: ServiceMeshDependenciesActive
  - lastTransitionTime: '2022-05-17T02:13:25Z'
   message: Resource configured successfully
   observedGeneration: 1
   reason: Successful
   status: 'True'
   type: ServiceMeshConfigured
  - lastTransitionTime: '2022-05-17T02:13:58Z'
   message: Resource in the control plane is Active, successfully reconciled
   observedGeneration: 1
   reason: Successful
   status: 'True'
   type: ServiceMeshActive
```

## Status Condition Fields 🔗 
The following table describes the fields included in the preceding sample output.
Field | Type | Description  
---|---|---  
lastTransitionTime | datetimestamp | `lastTransitionTime` is the last time the condition transitioned from one status to another.  
message | string | `message` is a human readable message indicating details about the transition.  
observedGeneration | int | `observedGeneration` represents the `.metadata.generation` that the condition was based upon. For instance, if `metadata.generation` is currently 12, but the `status.conditions[x].observedGeneration` is 9, the condition is out of date with respect to the current state of the instance.  
reason | string | `reason` contains a programmatic identifier indicating the reason for the condition's last transition.  
status | string | Status of the condition. Can be one of the following: `True`, `False`, or `Unknown`  
type | enum | Indicates status of the service mesh resource in the control-plane. Allowed values are: `ServiceMeshActive`, `ServiceMeshDependenciesActive` or `ServiceMeshConfigured`  
## Condition Type
A custom resource has condition types indicating the current status of the Service Mesh resource. The following table shows the different conditions a custom resource has:
Condition | Status | Reason  
---|---|---  
ServiceMeshActive | True | The custom resource is in active state in the OCI control plane.   
ServiceMeshActive | False | The custom resource is not in active state in the OCI control plane. This could mean the resource encountered an error while processing.  
ServiceMeshActive | Unknown | The custom resource is currently being processed and has not reached a terminal state in the OCI control plane.  
ServiceMeshConfigured | True | The request to the OCI control plane was accepted for the operation on the custom resource.  
ServiceMeshConfigured | False | The request to the OCI control plane was rejected for the operation on the custom resource.   
ServiceMeshConfigured | Unknown | The request to the OCI control plane encountered an internal error for the operation on the custom resource.  
ServiceMeshDependenciesActive | True | All dependencies for the resource reached `ServiceMeshActive` status of `True`.  
ServiceMeshDependenciesActive | False | One or more dependencies for the resource encountered an error and did not reach `ServiceMeshActive` status of `True`.  
ServiceMeshDependenciesActive | Unknown | One or more dependencies are currently being processed and have not reached a `ServiceMeshActive` status of `True`.  
Was this article helpful?
YesNo


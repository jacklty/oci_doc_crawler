Updated 2024-11-25
# Supported Admission Controllers
_Find out about the admission controllers that are turned on in Kubernetes clusters you create using Kubernetes Engine (OKE)._
The Kubernetes version you select when you create a cluster using Kubernetes Engine determines the default set of admission controllers that are turned on in the created cluster. The set follows the recommendation given in the [Kubernetes documentation](https://kubernetes.io/docs/admin/admission-controllers/#is-there-a-recommended-set-of-admission-controllers-to-use) for that version. This topic shows the supported admission controllers, the Kubernetes versions in which they are supported, and the order in which they run in the Kubernetes API server.
Note that if you install other admission controllers in a way that mutates or rejects requests in the `kube-system` namespace, the Kubernetes control plane components might stop functioning or behave unexpectedly. For more information, see [Avoiding operating on the kube-system namespace](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#avoiding-operating-on-the-kube-system-namespace) in the Kubernetes documentation.
## Admission Controllers (sorted alphabetically) 🔗 
The tables list, in alphabetical order, the admission controllers that are turned on in the Kubernetes clusters you create using Kubernetes Engine. For each admission controller, the tables show the Kubernetes version in which it is supported.
### Mutating Admission Controllers (sorted alphabetically)
Admission Controllers (in alphabetical order) | Supported in 1.28? | Supported in 1.29? | Supported in 1.30? | Supported in 1.31?  
---|---|---|---|---  
DefaultIngressClass | Yes | Yes | Yes | Yes  
DefaultStorageClass | Yes | Yes | Yes | Yes  
DefaultTolerationSeconds | Yes | Yes | Yes | Yes  
ExtendedResourceToleration | Yes | Yes | Yes | Yes  
LimitRanger | Yes | Yes | Yes | Yes  
MutatingAdmissionWebhook | Yes | Yes | Yes | Yes  
NamespaceLifecycle | Yes | Yes | Yes | Yes  
NodeRestriction | Yes | Yes | Yes | Yes  
PodSecurityPolicy (optional, see [Using Pod Security Polices with Kubernetes Engine](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingpspswithoke.htm#Using_Pod_Security_Polices_with_Container_Engine_for_Kubernetes "Find out how to use pod security policies with Kubernetes clusters you've created using Kubernetes Engine \(OKE\).")) | No | No | No | No  
Priority | Yes | Yes | Yes | Yes  
RuntimeClass | Yes | Yes | Yes | Yes  
ServiceAccount | Yes | Yes | Yes | Yes  
StorageObjectInUseProtection | Yes | Yes | Yes | Yes  
TaintNodesByCondition | Yes | Yes | Yes | Yes  
### Validating Admission Controllers (sorted alphabetically)
Admission Controllers (in alphabetical order) | Supported in 1.28? | Supported in 1.29? | Supported in 1.30? | Supported in 1.31?  
---|---|---|---|---  
CertificateApproval | Yes | Yes | Yes | Yes  
CertificateSigning | Yes | Yes | Yes | Yes  
CertificateSubjectRestriction | Yes | Yes | Yes | Yes  
ClusterTrustBundleAttest  | Yes | Yes | Yes | Yes  
ImagePolicyWebhook | Yes | Yes | Yes | Yes  
LimitRanger | Yes | Yes | Yes | Yes  
PersistentVolumeClaimResize | Yes | Yes | Yes | Yes  
PodSecurity | Yes | Yes | Yes | Yes  
PodSecurityPolicy (optional, see [Using Pod Security Polices with Kubernetes Engine](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingpspswithoke.htm#Using_Pod_Security_Polices_with_Container_Engine_for_Kubernetes "Find out how to use pod security policies with Kubernetes clusters you've created using Kubernetes Engine \(OKE\).")) | No | No | No | No  
Priority | Yes | Yes | Yes | Yes  
ResourceQuota | Yes | Yes | Yes | Yes  
RuntimeClass | Yes | Yes | Yes | Yes  
ServiceAccount | Yes | Yes | Yes | Yes  
ValidatingAdmissionPolicy | Yes | Yes | Yes | Yes  
ValidatingAdmissionWebhook | Yes | Yes | Yes | Yes  
## Admission Controllers (sorted by run order) 🔗 
The tables list the admission controllers that are turned on in the Kubernetes clusters you create using Kubernetes Engine. The tables show the order in which supported admission controllers run in the Kubernetes API server. Note that the run order can be different in different Kubernetes versions.
### Mutating Admission Controllers (sorted by run order)
Run order in Kubernetes 1.28 clusters: | Run order in Kubernetes 1.29 clusters: | Run order in Kubernetes 1.30 clusters: | Run order in Kubernetes 1.31 clusters:  
---|---|---|---  
NamespaceLifecycle | NamespaceLifecycle | NamespaceLifecycle | NamespaceLifecycle  
LimitRanger | LimitRanger | LimitRanger | LimitRanger  
ServiceAccount | ServiceAccount | ServiceAccount | ServiceAccount  
NodeRestriction | NodeRestriction | NodeRestriction | NodeRestriction  
TaintNodesByCondition | TaintNodesByCondition | TaintNodesByCondition | TaintNodesByCondition  
Priority | Priority | Priority | Priority  
DefaultTolerationSeconds | DefaultTolerationSeconds | DefaultTolerationSeconds | DefaultTolerationSeconds  
ExtendedResourceToleration | ExtendedResourceToleration | ExtendedResourceToleration | ExtendedResourceToleration  
DefaultStorageClass | DefaultStorageClass | DefaultStorageClass | DefaultStorageClass  
StorageObjectInUseProtection | StorageObjectInUseProtection | StorageObjectInUseProtection | StorageObjectInUseProtection  
RuntimeClass | RuntimeClass | RuntimeClass | RuntimeClass  
DefaultIngressClass | DefaultIngressClass | DefaultIngressClass | DefaultIngressClass  
MutatingAdmissionWebhook | MutatingAdmissionWebhook | MutatingAdmissionWebhook | MutatingAdmissionWebhook  
### Validating Admission Controllers (sorted by run order)
Run order in Kubernetes 1.28 clusters: | Run order in Kubernetes 1.29 clusters: | Run order in Kubernetes 1.30 clusters: | Run order in Kubernetes 1.31 clusters:  
---|---|---|---  
LimitRanger | LimitRanger | LimitRanger | LimitRanger  
ServiceAccount | ServiceAccount | ServiceAccount | ServiceAccount  
ImagePolicyWebhook | ImagePolicyWebhook | ImagePolicyWebhook | ImagePolicyWebhook  
PodSecurity | PodSecurity | PodSecurity | PodSecurity  
Priority | Priority | Priority | Priority  
PersistentVolumeClaimResize | PersistentVolumeClaimResize | PersistentVolumeClaimResize | PersistentVolumeClaimResize  
RuntimeClass | RuntimeClass | RuntimeClass | RuntimeClass  
CertificateApproval | CertificateApproval | CertificateApproval | CertificateApproval  
CertificateSigning | CertificateSigning | CertificateSigning | CertificateSigning  
ClusterTrustBundleAttest | ClusterTrustBundleAttest | ClusterTrustBundleAttest | ClusterTrustBundleAttest  
CertificateSubjectRestriction | CertificateSubjectRestriction | CertificateSubjectRestriction | CertificateSubjectRestriction  
ValidatingAdmissionPolicy | ValidatingAdmissionPolicy | ValidatingAdmissionPolicy | ValidatingAdmissionPolicy  
ValidatingAdmissionWebhook | ValidatingAdmissionWebhook | ValidatingAdmissionWebhook | ValidatingAdmissionWebhook  
ResourceQuota | ResourceQuota | ResourceQuota | ResourceQuota  
Was this article helpful?
YesNo


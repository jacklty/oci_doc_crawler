Updated 2025-02-05
# Compatibility Matrix
_Find out about the versions of different products and components that are supported on the version of Kubernetes running on clusters you create using Kubernetes Engine._
You can deploy different products and components on the clusters you create using Kubernetes Engine, some of which are compatible with particular versions of Kubernetes and Kubernetes Engine. For more information, see:
  * [Calico Compatibility](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengCompatibilitymatrix_topic.htm#contengCompatibilitymatrix_topic-Calico-compatibility-matrix)
  * [Cluster Add-on Compatibility](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengCompatibilitymatrix_topic.htm#contengCompatibilitymatrix_topic-Cluster-addon-compatibility-matrix)
  * [Admission Controller Compatibility](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengCompatibilitymatrix_topic.htm#contengCompatibilitymatrix_topic-Admission-controller-compatibility-matrix)
  * [Ubuntu Node Package Compatibility](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengCompatibilitymatrix_topic.htm#contengCompatibilitymatrix_topic_Ubuntu_compatibility_matrix)


## Calico Compatibility 🔗 
The table lists the versions of the Calico network plugin that Oracle has successfully tested on clusters created using Kubernetes Engine. Oracle only supports Calico versions that have been successfully tested. For each Calico version, the table shows the Kubernetes version that was running on clusters in successful tests.
Note that only the use of open source Calico is supported. Use of Calico Enterprise is not supported.
For more information, see [Example: Installing Calico and Setting Up Network Policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupcalico.htm#Example_Installing_Calico_and_Setting_Up_Network_Policies "Find out how to install Calico and set up network policies on a cluster you've created using Kubernetes Engine \(OKE\).").
Calico Version | Tested (and supported) on clusters running Kubernetes 1.28? | Tested (and supported) on clusters running Kubernetes 1.29? | Tested (and supported) on clusters running Kubernetes 1.30? | Tested (and supported) on clusters running Kubernetes 1.31?  
---|---|---|---|---  
3.25.1 | (not tested) | (not tested) | (not tested) | (not tested)  
3.26.1 | (not tested) | (not tested) | (not tested) | (not tested)  
3.26.4 | Yes | (not tested) | (not tested) | (not tested)  
3.27.2 | (not tested) | Yes | (not tested) | (not tested)  
3.28.0 | (not tested) | (not tested) | Yes | (not tested)  
3.28.2 | (not tested) | (not tested) | (not tested) | Yes  
## Cluster Add-on Compatibility 🔗 
This table lists the latest versions of essential and optional cluster add-ons for each version of Kubernetes that Kubernetes Engine (OKE) supports.
For more information, see [Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm#contengconfiguringclusteraddons "Find out about configuring cluster add-ons in clusters you create using Kubernetes Engine \(OKE\).").
Cluster add-on | Latest add-on image version supported with Kubernetes 1.28 | Latest add-on image version supported with Kubernetes 1.29 | Latest add-on image version supported with Kubernetes 1.30 | Latest add-on image version supported with Kubernetes 1.31  
---|---|---|---|---  
kube-proxy | 1.28.10 | 1.29.10 | 1.30.1 | 1.31.1  
CoreDNS | 1.10.1 | 1.10.1 | 1.10.1 | 1.10.1  
OCI VCN-Native Pod Networking CNI plugin | 2.0.1 | 2.0.1 | 2.1.0 | 2.2.3  
flannel | 0.20.2 | 0.20.2 | 0.20.2 | 0.24.4  
Kubernetes Dashboard | 2.7.0 | 2.7.0 | 2.7.0 | 2.7.0  
Tiller (not recommended) | 2.16.0 | 2.16.0 | 2.16.0 | 2.16.0  
Oracle Database Operator for Kubernetes | 0.2.0 | 1.0.0 | 1.1.0 | 1.1.0  
WebLogic Kubernetes Operator | 4.1.7 | 4.1.7 | 4.2.1 | 4.2.1  
Certificate Manager | 1.11.0 | 1.14.2 | 1.14.2 | 1.15.0  
Cluster Autoscaler | 1.28.0 | 1.29 | 1.29 | 1.31.0  
Istio | 1.19.0 | 1.20.3 | 1.20.5 | 1.22.1  
OCI Native Ingress Controller | 1.3.3 | 1.3.3 | 1.3.8 | 1.3.9  
Kubernetes Metrics Server | 0.7.0 | 0.7.0 | 0.7.1 | 0.7.1  
NVIDIA GPU Plugin | 
  * 0.17.0
  * 0.16.2
  * 0.15.1
  * 0.14.2

| 
  * 0.17.0
  * 0.16.2
  * 0.15.1
  * 0.14.2

| 
  * 0.17.0
  * 0.16.2
  * 0.15.1
  * 0.14.2

| 
  * 0.17.0
  * 0.16.2
  * 0.15.1
  * 0.14.2

  
## Admission Controller Compatibility 🔗 
The tables list, in alphabetical order, the admission controllers that are turned on in the Kubernetes clusters you create using Kubernetes Engine. For each admission controller, the tables show the Kubernetes version in which it is supported.
For more information, see [Supported Admission Controllers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengadmissioncontrollers.htm#Supported_Admission_Controllers "Find out about the admission controllers that are turned on in Kubernetes clusters you create using Kubernetes Engine \(OKE\).").
### Admission Controller Compatibility (sorted alphabetically) 🔗 
These tables list, in alphabetical order, the admission controllers that are turned on in the Kubernetes clusters you create using Kubernetes Engine. For each admission controller, the tables show the Kubernetes version in which it is supported.
#### Mutating Admission Controllers (sorted alphabetically)
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
#### Validating Admission Controllers (sorted alphabetically)
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
### Admission Controller Compatibility (sorted by run order) 🔗 
These tables list the admission controllers that are turned on in the Kubernetes clusters you create using Kubernetes Engine. The tables show the order in which supported admission controllers run in the Kubernetes API server. Note that the run order can be different in different Kubernetes versions.
#### Mutating Admission Controllers (sorted by run order)
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
#### Validating Admission Controllers (sorted by run order)
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
## Ubuntu Node Package Compatibility 🔗 
This table lists the Ubuntu releases for which Oracle provides node packages, along with the Kubernetes versions that each node package is compatible with. The node packages that Oracle provides are designed to work on both x86 and ARM architectures. 
For more information, see [Running Ubuntu on Worker Nodes Using Custom Images](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingubuntubasedworkernodes.htm#contengcreatingubuntubasedworkernodes "Find out how to include worker nodes that run the Ubuntu Linux distribution in clusters created with Kubernetes Engine \(OKE\), using custom images and cloud-init scripts.").
Ubuntu release | Package to use with Kubernetes 1.27 | Package to use with Kubernetes 1.28 | Package to use with Kubernetes 1.29 | Package to use with Kubernetes 1.30 | Package to use with Kubernetes 1.31  
---|---|---|---|---|---  
Jammy (Ubuntu 22.04) | `oci-oke-node-all-1.27.10` | `oci-oke-node-all-1.28.10` | `oci-oke-node-all-1.29.1` | `oci-oke-node-all-1.30.1` | `oci-oke-node-all-1.31.1`  
Noble (Ubuntu 24.04) | `oci-oke-node-all-1.27.10` | `oci-oke-node-all-1.28.10` | `oci-oke-node-all-1.29.1` | `oci-oke-node-all-1.30.1` | `oci-oke-node-all-1.31.1`  
Was this article helpful?
YesNo


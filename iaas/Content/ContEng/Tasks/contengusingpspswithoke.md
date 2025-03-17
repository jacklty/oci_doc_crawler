Updated 2025-01-15
# Using Pod Security Policies with Kubernetes Engine (OKE)
_Find out how to use pod security policies with Kubernetes clusters you've created using Kubernetes Engine (OKE)._
**Note**
The upstream Kubernetes project deprecated pod security policies in Kubernetes version 1.21, and removed the feature in Kubernetes version 1.25. Consequently, Kubernetes Engine does not support pod security policies and the PodSecurityPolicy admission controller in clusters running Kubernetes version 1.25 and later.
If you require similar functionality, consider using Kubernetes pod security standards and the PodSecurity admission controller instead (along with the Privileged, Baseline, and Restricted policies). By default, Kubernetes Engine enables the PodSecurity admission controller in clusters running Kubernetes version 1.23 and later, in order to support pod security standards. For more information about Kubernetes pod security standards, and the PodSecurity admission controller, see [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) in the Kubernetes documentation.
Alternatively, consider using other alternatives that are being developed in the Kubernetes ecosystem to enforce policies.
If you do decide to move from using pod security policies and the PodSecurityPolicy admission controller to using pod security standards and the PodSecurity admission controller, see [Migrate from PodSecurityPolicy to the Built-In PodSecurity Admission Controller](https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/) in the Kubernetes documentation. Note that it is important to complete the migration before creating a new cluster running Kubernetes version 1.25, or before upgrading an existing Kubernetes version 1.24 cluster to run Kubernetes version 1.25. Also note that the Console provides a convenient way to disable the use of the PodSecurityPolicy admission controller in existing Kubernetes clusters created and managed by Kubernetes Engine (see [Using the Console to Disable the PodSecurityPolicy Admission Controller](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contengusingpspswithoke.htm#contengusingpspswithoke_topic-Using_the_Console_to_Disable_the_PodSecurityPolicy_Admission_Controller)).
You can control the operations that pods are allowed to perform on a cluster you have created with Kubernetes Engine by setting up pod security policies for the cluster. Pod security policies are a way to ensure that pods meet security-related conditions before they can be accepted by a cluster. For example, you can use pod security polices to:
  * limit the storage choices available to pods
  * restrict the host networking and ports that pods can access
  * prevent pods from running as the root user
  * prevent pods from running in privileged mode


You can also use pod security policies to provide default values for pods, by 'mutating' the pod.
Having defined a pod security policy for a cluster, you have to authorize the requesting user or target pod's service account to use the policy. You do this by creating a role (or clusterrole) to access the pod security policy, and then creating a rolebinding (or clusterrolebinding) between the role (or clusterrole) and the requesting user or target pod's service account. For more information about roles, clusterroles, and bindings, see [About Access Control and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutaccesscontrol.htm#About_Access_Control_and_Container_Engine_for_Kubernetes "Find out about the permissions required to access clusters you've created using Kubernetes Engine \(OKE\).").
You specify whether a cluster enforces the pod security policies defined for it by enabling the cluster's PodSecurityPolicy admission controller. The PodSecurityPolicy admission controller acts on creation and modification of a pod and determines if the pod should be admitted to the cluster based on the requested security context in the pod spec and the cluster's pod security policies. If multiple pod security policies exist, the PodSecurityPolicy admission controller first compares the pod against non-mutating policies in alphabetical order and uses the first policy that successfully validates the pod. If no non-mutating pods validate the pod, the PodSecurityPolicy admission controller compares the pod against mutating policies in alphabetical order and uses the first policy that successfully validates the pod.
**Caution**
**Caution 1:**
It is very important to note that when you enable a cluster's PodSecurityPolicy admission controller, no application pods can start on the cluster unless suitable pod security policies exist, along with roles (or clusterroles) and rolebindings (or clusterrolebindings) to associate pods with policies. You will not be able to run application pods on a cluster with an enabled PodSecurityPolicy admission controller unless these prerequisites are met. 
We strongly recommend you use PodSecurityPolicy admission controllers as follows:
  * Whenever you create a new cluster, enable the Pod Security Admission Controller.
  * Immediately after creating a new cluster, create pod security policies, along with roles (or clusterroles) and rolebindings (or clusterrolebindings).


**Caution 2:**
You must create pod security policies before enabling the PodSecurityPolicy admission controller of an existing cluster that is already in production (that is, some time after you created it). If you decide to enable an existing cluster's PodSecurityPolicy admission controller, we strongly recommend you first verify the cluster's pod security policies in a development or test environment. That way, you can be sure the pod security policies work as you expect and correctly allow (or refuse) pods to start on the cluster.
When you enable the PodSecurityPolicy admission controller of a cluster you've created with Kubernetes Engine, a pod security policy for Kubernetes system privileged pods is automatically created (along with the associated clusterrole and clusterrolebinding). This pod security policy, and the clusterrole and clusterrolebinding, enable the Kubernetes system pods to run. The pod security policy, clusterrole, and clusterrolebinding are defined in the kube-system.yaml file (see [kube-system.yaml Reference](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingpspswithoke.htm#systempsp)).
Note that you can create pod security policies for a cluster before enabling the cluster's PodSecurityPolicy admission controller. Also note that you can disable a cluster's PodSecurityPolicy admission controller that was previously enabled. In this case, any previously created pod security policies, roles (or clusterroles), and rolebindings (or clusterrolebindings) are not deleted. The pod security policies are simply not enforced. Any application pod will be able to run on the cluster.
For more information about pod security policies and the PodSecurityPolicy admission controller, see the [Kubernetes documentation](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/).
## Creating a Pod Security Policy for Application Pods 🔗 
To create a pod security policy for application pods, create a role to access the pod security policy, and create a rolebinding to enable the application pods to use the pod security policy:
  1. Create the pod security policy for application pods:
    1. Define and save the pod security policy in a file. For example, in `acme-app-psp.yaml`).
For example, this policy (taken from the [Kubernetes documentation](https://kubernetes.io/docs/concepts/policy/pod-security-policy/#example)) simply prevents the creation of privileged pods:
Copy
```

apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
 name: acme-app-psp
spec:
 privileged: false # Don't allow privileged pods!
 # The rest fills in some required fields.
 seLinux:
  rule: RunAsAny
 supplementalGroups:
  rule: RunAsAny
 runAsUser:
  rule: RunAsAny
 fsGroup:
  rule: RunAsAny
 volumes:
 - '*'
```

    2. Enter the following command to create the pod security policy:
Command
CopyTry It
```
kubectl create -f <filename>.yaml
```

For example:
Command
CopyTry It
```
kubectl create -f acme-app-psp.yaml
```

  2. Create the role (or clusterrole) to access the pod security policy:
    1. Define and save a role (or clusterrole) in a file. For example, in `acme-app-psp-crole.yaml`.
For example:
Copy
```
# Cluster role which grants access to the app pod security policy
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
 name: acme-app-psp-crole
rules:
- apiGroups:
 - policy
 resourceNames:
 - acme-app-psp
 resources:
 - podsecuritypolicies
 verbs:
 - use

```

    2. Enter the following command to create the role (or clusterrole):
Command
CopyTry It
```
kubectl create -f <filename>.yaml
```

For example:
Command
CopyTry It
```
kubectl create -f acme-app-psp-crole.yaml
```

  3. Create the rolebinding (or clusterrolebinding) to authorize the application pods to use the pod security policy:
    1. Define and save the rolebinding (or clusterrolebinding) in a file. For example, in `acme-app-psp-crole-bind.yaml`.
For example:
Copy
```

# Role binding which grants access to the app pod security policy
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
 name: acme-app-psp-binding
 namespace: acme-namespace
roleRef:
 apiGroup: rbac.authorization.k8s.io
 kind: ClusterRole
 name: acme-app-psp-crole
subjects:
# For all service accounts in acme-namespace
- apiGroup: rbac.authorization.k8s.io
 kind: Group
 name: system:serviceaccounts:acme-namespace
```

    2. Enter the following command to create the rolebinding (or clusterrolebinding):
Command
CopyTry It
```
kubectl create -f <filename>.yaml
```

For example:
Command
CopyTry It
```
kubectl create -f acme-app-psp-crole-bind.yaml
```



Having defined a pod security policy and authorized application pods to use it by creating a role and rolebinding (or a clusterrole and clusterrolebinding), enable the cluster's PodSecurityPolicy admission controller to enforce the pod security policy (if it's not enabled already). 
## Using the Console to Enable the PodSecurityPolicy Admission Controller 🔗 
To enable the PodSecurityPolicy admission controller when creating new clusters using the Console:
  1. Log in to the Console.
  2. Follow the instructions to create a new cluster in [Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm#create-custom-cluster "Find out how to use the 'Custom Create' workflow to create a Kubernetes cluster with explicitly defined settings and existing network resources using Kubernetes Engine \(OKE\)."), click **Show Advanced Options** , and select the **Pod Security Policies - Enforced** option. This option enables the PodSecurityPolicy admission controller.
No application pods will be accepted into the new cluster unless suitable pod security policies exist, along with roles (or clusterroles) and rolebindings (or clusterrolebindings) to associate pods with policies. 
  3. Follow the instructions to set the remaining cluster details, and click **Create Cluster** to create the new cluster.
  4. Follow the instructions in [Creating a Pod Security Policy for Application Pods](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingpspswithoke.htm#Creating) to create pod security policies for the PodSecurityPolicy admission controller to enforce when accepting pods into the new cluster.


To enable the PodSecurityPolicy admission controller in existing clusters using the Console:
  1. Follow the instructions in [Creating a Pod Security Policy for Application Pods](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingpspswithoke.htm#Creating) to create pod security policies for the PodSecurityPolicy admission controller to enforce when accepting pods into the existing cluster.
We strongly recommend you first verify the pod security policies in a development or test environment. That way, you can be sure the pod security policies work as you expect and correctly allow (or refuse) pods to start on the cluster.
  2. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
  3. Choose a **Compartment** you have permission to work in.
  4. On the **Cluster List** page, click the name of the cluster you want to modify.
  5. On the Cluster Details tab, click **Not Enforced** beside **Pod Security Policies**.
  6. In the **Pod Security Policies** window, select **Enforced**. 
From now on, no new application pods will be accepted into the cluster unless suitable pod security policies exist, along with roles (or clusterroles) and rolebindings (or clusterrolebindings) to associate pods with policies. Note that any currently running pods will continue to run regardless.
  7. Click **Save Changes**.


## Using the Console to Disable the PodSecurityPolicy Admission Controller 🔗 
To disable the PodSecurityPolicy admission controller in clusters where it was previously enabled:
  1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
  2. Choose a **Compartment** you have permission to work in.
  3. On the **Cluster List** page, click the name of the cluster you want to modify.
  4. On the Cluster Details tab, click **Enforced** beside **Pod Security Policies**.
  5. In the **Pod Security Policies** window, select **Not Enforced**. 
From now on, new application pods will be accepted into the cluster without pod security policies, roles (or clusterroles) and rolebindings (or clusterrolebindings) being required. Note that any currently running pods will continue to run regardless.
  6. Click **Save Changes**.


## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
To enable the PodSecurityPolicy admission controller, use the:
  * [CreateCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CreateCluster) operation when creating new clusters 
  * [Update Cluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/UpdateCluster) operation when modifying existing clusters 


## kube-system.yaml Reference 🔗 
The pod security policy, and the associated clusterrole and clusterrolebinding, for Kubernetes system privileged pods are automatically created when you enable a cluster's PodSecurityPolicy admission controller. These allow any pod in the kube-system namespace to run. They are created from definitions in the kube-system.yaml shown below:
Copy
```

apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
 annotations:
  # See https://kubernetes.io/docs/concepts/policy/pod-security-policy/#seccomp
  seccomp.security.alpha.kubernetes.io/allowedProfileNames: '*'
 name: oke-privileged
spec:
 allowedCapabilities:
 - '*'
 allowPrivilegeEscalation: true
 fsGroup:
  rule: 'RunAsAny'
 hostIPC: true
 hostNetwork: true
 hostPID: true
 hostPorts:
 - min: 0
  max: 65535
 privileged: true
 readOnlyRootFilesystem: false
 runAsUser:
  rule: 'RunAsAny'
 seLinux:
  rule: 'RunAsAny'
 supplementalGroups:
  rule: 'RunAsAny'
 volumes:
 - '*'
 
---
 
# Cluster role which grants access to the privileged pod security policy
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
 name: oke-privileged-psp
rules:
- apiGroups:
 - policy
 resourceNames:
 - oke-privileged
 resources:
 - podsecuritypolicies
 verbs:
 - use
 
---
 
# Role binding for kube-system - allow kube-system service accounts - should take care of CNI i.e. flannel running in the kube-system namespace
# Assumes access to the kube-system is restricted
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
 name: kube-system-psp
 namespace: kube-system
roleRef:
 apiGroup: rbac.authorization.k8s.io
 kind: ClusterRole
 name: oke-privileged-psp
subjects:
# For all service accounts in the kube-system namespace
- apiGroup: rbac.authorization.k8s.io
 kind: Group
 name: system:serviceaccounts:kube-system

```

Was this article helpful?
YesNo


Updated 2024-08-23
# About Access Control and Kubernetes Engine (OKE)
_Find out about the permissions required to access clusters you've created using Kubernetes Engine (OKE)._
To perform operations on a Kubernetes cluster, you must have appropriate permissions to access the cluster.
For most operations on Kubernetes clusters created and managed by Kubernetes Engine, Oracle Cloud Infrastructure Identity and Access Management (IAM) provides access control. A user's permissions to access clusters comes from the IAM groups (including dynamic groups) to which they belong. The permissions for a group are defined by policies. Policies define what actions members of a group can perform, and in which compartments. Users can then access clusters and perform operations based on the policies set for the groups they are members of. 
IAM provides control over:
  * whether a user can create or delete clusters
  * whether a user can add, remove, or modify node pools
  * which Kubernetes object create/delete/view operations a user can perform on all clusters within a compartment or tenancy


See [Policy Configuration for Cluster Creation and Deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm#Policy_Configuration_for_Cluster_Creation_and_Deployment "Find out about the IAM policies to create before using Kubernetes Engine \(OKE\).").
In addition to IAM, the Kubernetes RBAC Authorizer can enforce additional fine-grained access control for users on specific clusters via Kubernetes RBAC roles and clusterroles. A Kubernetes RBAC role is a collection of permissions. For example, a role might include read permission on pods and list permission for pods. A Kubernetes RBAC clusterrole is just like a role, but can be used anywhere in the cluster. A Kubernetes RBAC rolebinding maps a role to a user or group, granting that role's permissions to the user or group for resources in that namespace. Similarly, a Kubernetes RBAC clusterrolebinding maps a clusterrole to a user or group, granting that clusterrole's permissions to the user or group across the entire cluster.
IAM and the Kubernetes RBAC Authorizer work together to enable users who have been successfully authorized by at least one of them to complete the requested Kubernetes operation. You can use OCIDs to map Kubernetes RBAC rolebindings and clusterrolebindings to IAM users and groups (including dynamic groups).
When a user attempts to perform any operation on a cluster (except for create role and create clusterrole operations), IAM first determines whether a group (or dynamic group) to which the user belongs has the appropriate and sufficient permissions. If so, the operation succeeds. If the attempted operation also requires additional permissions granted via a Kubernetes RBAC role or clusterrole, the Kubernetes RBAC Authorizer then determines whether the user or group has been granted the appropriate Kubernetes role or clusterrole. 
Typically, you'll want to define your own Kubernetes RBAC roles and clusterroles when deploying a Kubernetes cluster to provide additional fine-grained control. When you attempt to perform a create role or create clusterrole operation, the Kubernetes RBAC Authorizer first determines whether you have sufficient Kubernetes privileges. To create a role or clusterrole, you must have been assigned an existing Kubernetes RBAC role (or clusterrole) that has at least the same or higher privileges as the new role (or clusterrole) you're attempting to create.
By default, users are not assigned any Kubernetes RBAC roles (or clusterroles) by default. So before attempting to create a new role (or clusterrole), you must be assigned an appropriately privileged role (or clusterrole). A number of such roles and clusterroles are always created by default, including the cluster-admin clusterrole (for a full list, see [Default Roles and Role Bindings](https://kubernetes.io/docs/admin/authorization/rbac/#default-roles-and-role-bindings) in the Kubernetes documentation). The cluster-admin clusterrole essentially confers super-user privileges. A user granted the cluster-admin clusterrole can perform any operation across all namespaces in a given cluster. 
Note that Oracle Cloud Infrastructure tenancy administrators already have sufficient privileges, and do not require the cluster-admin clusterrole.
[Example 1: Granting the Kubernetes RBAC cluster-admin clusterrole](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutaccesscontrol.htm)
**Note**
The following instructions assume:
  * You have the required access to create Kubernetes RBAC roles and clusterroles, either because you're in the tenancy's Administrators group, or because you have the Kubernetes RBAC cluster-admin clusterrole.


  * The user to which you want to grant the RBAC cluster-admin clusterrole is not an OCI tenancy administrator. If they are an OCI tenancy administrator, they do not require the Kubernetes RBAC cluster-admin clusterrole. 


Follow these steps to grant a user who is not a tenancy administrator the Kubernetes RBAC cluster-admin clusterrole on a cluster deployed on Oracle Cloud Infrastructure:
  1. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  2. In a terminal window, grant the Kubernetes RBAC cluster-admin clusterrole to the user by entering:
Command
CopyTry It
```

kubectl create clusterrolebinding <my-cluster-admin-binding> --clusterrole=cluster-admin --user=<user_OCID>
```

where:
     * `<my-cluster-admin-binding>` is a string of your choice to be used as the name for the binding between the user and the Kubernetes RBAC cluster-admin clusterrole. For example, `jdoe_clst_adm`
     * `<user_OCID>` is the user's OCID (obtained from the Console ). For example, `ocid1.user.oc1..aaaaa...zutq` (abbreviated for readability).
For example:
Command
CopyTry It
```

kubectl create clusterrolebinding jdoe_clst_adm --clusterrole=cluster-admin --user=ocid1.user.oc1..aaaaa...zutq
```



[Example 2: Creating a Kubernetes role and rolebinding to enable a non-administrator user to read pods in a cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutaccesscontrol.htm)
Follow these steps to give a non-administrator user the necessary Oracle Cloud Infrastructure and Kubernetes RBAC permissions to view pods running on a Kubernetes cluster. In this example, a non-administrator user is given explicit access to the cluster (rather than as a member of a group).
### As a tenancy administrator:
**Note** The following instructions assume you're in the tenancy's Administrators group, and therefore have the required permissions to create users, groups, and IAM policies.
  1. Create a new Oracle Cloud Infrastructure IAM user account for the non-administrator user (for example, jdoe@acme.com). See [To create a user](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingusers.htm#create_user). 
  2. Make a note of the new IAM user account's OCID (for example, `ocid1.user.oc1..aa______tx5a`, abbreviated for readability). 
  3. Create a new Oracle Cloud Infrastructure IAM group (for example, called `acme-developer-group`), and add the new IAM user account to the group. See [To create a group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managinggroups.htm#To).
  4. Create a new Oracle Cloud Infrastructure policy that grants the new group the CLUSTER_USE permission on clusters, with a policy statement like: 
Copy
```
Allow group acme-developer-group to use clusters in <location>
```

In the above policy statement, replace `<location>` with either `tenancy` (if you are creating the policy in the tenancy's root compartment) or `compartment <compartment-name>` (if you are creating the policy in an individual compartment). See [To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy).
Note that if a group is not in the default identity domain, prefix the group name with the identity domain name, in the format `group '<identity-domain-name>'/'group-name'`. You can also specify a group using its OCID, in the format `group id <group-ocid>`.


### As the cluster administrator:
**Note** The following instructions assume you have the required permissions to create and manage clusters, and the required access to create Kubernetes RBAC roles and clusterroles.
  1. In a text editor, create the following manifest (for example, called `pod-reader-user.yaml`) to define a Kubernetes RBAC role and role binding to enable the new IAM user account to list pods in the kube-system namespace: 
Copy
```
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
 name: pod-reader-ks
 namespace: kube-system
rules:
- apiGroups: [""]
 resources: ["pods"]
 verbs: ["get", "watch", "list"]
---
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
 name: pod-reader-ks-role-binding
 namespace: kube-system
subjects:
- kind: User
 name: <user-ocid>
 apiGroup: rbac.authorization.k8s.io
roleRef:
 kind: Role
 name: pod-reader-ks
 apiGroup: rbac.authorization.k8s.io

```

where `name: <user-ocid>` specifies the OCID of the new IAM user account you created previously. For example, `name:               ocid1.user.oc1..aa______tx5a`
  2. Create the new role and rolebinding by entering:
Command
CopyTry It
```
kubectl apply -f pod-reader-user.yml
```



### As the non-administrator user:
**Note** The following instructions assume you have the credentials of the new IAM user account created earlier. As such, you have the required permissions to use Kubernetes clusters in the tenancy or compartment.
  1. Sign in to the Console using the new IAM user account's credentials.
  2. Configure cluster access by following the instructions in [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  3. List the pods in the kube-system namespace by entering:
Command
CopyTry It
```
kubectl get pods -n kube-system
```



[Example 3: Creating a Kubernetes role and rolebinding to enable a group to read pods in a cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutaccesscontrol.htm)
Follow these steps to give non-administrator users in a group the necessary Oracle Cloud Infrastructure and Kubernetes RBAC permissions to view pods running on a Kubernetes cluster. In this example, non-administrator users are given access to the cluster as members of an IAM group (you could specify a dynamic group instead).
### As a tenancy administrator:
**Note** The following instructions assume you're in the tenancy's Administrators group, and therefore have the required permissions to create users, groups, and IAM policies.
  1. Create a new Oracle Cloud Infrastructure IAM user account for a non-administrator user (for example, jsmith@acme.com). See [To create a user](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingusers.htm#create_user). 
  2. Create a new Oracle Cloud Infrastructure IAM group (for example, called `acme-developer-group`), and add the new IAM user account to the group. See [To create a group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managinggroups.htm#To).
  3. Make a note of the new IAM group's OCID (for example, `ocid1.group.oc1..aa______m7dt`, abbreviated for readability). 
  4. Create a new Oracle Cloud Infrastructure policy that grants the new group the CLUSTER_USE permission on clusters, with a policy statement like: 
Copy
```
Allow group acme-developer-group to use clusters in <location>
```

In the above policy statement, replace `<location>` with either `tenancy` (if you are creating the policy in the tenancy's root compartment) or `compartment <compartment-name>` (if you are creating the policy in an individual compartment). See [To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy).
Note that if a group is not in the default identity domain, prefix the group name with the identity domain name, in the format `group '<identity-domain-name>'/'group-name'`. You can also specify a group using its OCID, in the format `group id <group-ocid>`.


### As the cluster administrator:
**Note** The following instructions assume you have the required permissions to create and manage clusters, and the required access to create Kubernetes RBAC roles and clusterroles.
  1. In a text editor, create the following manifest (for example, called `pod-reader-group.yaml`) to define a Kubernetes RBAC role and role binding to enable users in the new IAM group to list pods in the kube-system namespace: 
Copy
```
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
 name: pod-reader-ks
 namespace: kube-system
rules:
- apiGroups: [""]
 resources: ["pods"]
 verbs: ["get", "watch", "list"]
---
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
 name: pod-reader-ks-role-binding
 namespace: kube-system
subjects:
- kind: Group
 name: <group-ocid>
 apiGroup: rbac.authorization.k8s.io
roleRef:
 kind: Role
 name: pod-reader-ks
 apiGroup: rbac.authorization.k8s.io

```

where `name: <group-ocid>` specifies the OCID of the new IAM group you created previously. For example, `name:               ocid1.group.oc1..aa______m7dt`
  2. Create the new role and rolebinding by entering:
Command
CopyTry It
```
kubectl apply -f pod-reader-group.yml
```



### As the non-administrator user:
**Note** The following instructions assume you have the credentials of the new IAM user account created earlier as a member of the new IAM group. As such, you have the required permissions to use Kubernetes clusters in the tenancy or compartment.
  1. Sign in to the Console using the new IAM user account's credentials.
  2. Configure cluster access by following the instructions in [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  3. List the pods in the kube-system namespace by entering:
Command
CopyTry It
```
kubectl get pods -n kube-system
```



[Example 4: Creating a Kubernetes clusterrole and clusterrolebinding to enable users and groups to list secrets in a cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutaccesscontrol.htm)
Follow these steps to give non-administrator users in a group the necessary Oracle Cloud Infrastructure and Kubernetes RBAC permissions to view pods running on a Kubernetes cluster. In this example, a non-administrator user is given access to the cluster either explicitly or as member of an IAM group (you could specify a dynamic group instead).
### As a tenancy administrator:
**Note** The following instructions assume you're in the tenancy's Administrators group, and therefore have the required permissions to create users, groups, and IAM policies.
  1. Create a new Oracle Cloud Infrastructure IAM user account for a non-administrator user (for example, jjones@acme.com). See [To create a user](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingusers.htm#create_user). 
  2. If you intend to enable just this user to list secrets, make a note of the new IAM user account's OCID (for example, `ocid1.user.oc1..aa______4gs6`, abbreviated for readability).
  3. Create a new Oracle Cloud Infrastructure IAM group (for example, called `acme-developer-group`), and add the new IAM user account to the group. See [To create a group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managinggroups.htm#To).
  4. If you intend to enable all users in this group to list secrets, make a note of the new IAM group's OCID (for example, `ocid1.group.oc1..aa______e26f`, abbreviated for readability). 
  5. Create a new Oracle Cloud Infrastructure policy that grants the new group the CLUSTER_USE permission on clusters, with a policy statement like: 
Copy
```
Allow group acme-developer-group to use clusters in <location>
```

In the above policy statement, replace `<location>` with either `tenancy` (if you are creating the policy in the tenancy's root compartment) or `compartment <compartment-name>` (if you are creating the policy in an individual compartment). See [To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy).
Note that if a group is not in the default identity domain, prefix the group name with the identity domain name, in the format `group '<identity-domain-name>'/'group-name'`. You can also specify a group using its OCID, in the format `group id <group-ocid>`.


### As the cluster administrator:
**Note** The following instructions assume you have the required permissions to create and manage clusters, and the required access to create Kubernetes RBAC roles and clusterroles.
  1. In a text editor, do one of the following, depending on whether you want to enable just the new IAM user or all users in the new IAM group to list secrets in a Kubernetes cluster:
     * If you want to enable just the new IAM user to list secrets in a Kubernetes cluster, create the following manifest (for example, called `secrets-reader.yaml`):
Copy
```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
 name: secret-reader
rules:
- apiGroups: [""]
 resources: ["secrets"]
 verbs: ["get", "watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
 name: read-secrets-global
subjects:
- kind: User
 name: <user-ocid>
 apiGroup: rbac.authorization.k8s.io
roleRef:
 kind: ClusterRole
 name: secret-reader
 apiGroup: rbac.authorization.k8s.io

```

where `name: <user-ocid>` specifies the OCID of the new IAM user you created previously. For example, `name: ocid1.user.oc1..aa______4gs6`
     * If you want to enable all users in the new IAM group to list secrets in a Kubernetes cluster, create the following manifest (for example, called `secrets-reader.yaml`):
Copy
```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
 name: secret-reader
rules:
- apiGroups: [""]
 resources: ["secrets"]
 verbs: ["get", "watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
 name: read-secrets-global
subjects:
- kind: Group
 name: <group-ocid>
 apiGroup: rbac.authorization.k8s.io
roleRef:
 kind: ClusterRole
 name: secret-reader
 apiGroup: rbac.authorization.k8s.io

```

where `name: <group-ocid>` is the OCID of the new IAM group you created previously. For example, `ocid1.group.oc1..aa______e26f`
  2. Create the new clusterrole and clusterrolebinding by entering:
Command
CopyTry It
```
kubectl apply -f secret-reader.yml
```



### As the non-administrator user:
**Note** The following instructions assume you have the credentials of the new IAM user account created earlier as a member of the new IAM group. As such, you have the required permissions to use Kubernetes clusters in the tenancy or compartment either explicitly or as member of a group.
  1. Sign in to the Console using the new IAM user account's credentials.
  2. Configure cluster access by following the instructions in [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  3. List the secrets in all namespaces by entering:
Command
CopyTry It
```
kubectl get secrets --all-namespaces
```



Was this article helpful?
YesNo


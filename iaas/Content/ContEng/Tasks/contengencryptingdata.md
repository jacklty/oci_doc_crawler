Updated 2025-01-15
# Encrypting Kubernetes Secrets at Rest in Etcd
_Find out how to encrypt configuration data stored as Kubernetes secrets in etcd when using Kubernetes Engine (OKE)._
The Kubernetes cluster control plane stores sensitive configuration data (such as authentication tokens, certificates, and credentials) as Kubernetes secret objects in etcd. Etcd is an open source distributed key-value store that Kubernetes uses for cluster coordination and state management. In the Kubernetes clusters created by Kubernetes Engine, etcd writes and reads data to and from block storage volumes in the Oracle Cloud Infrastructure Block Volume service. By default, Oracle encrypts data in block volumes at rest, including etcd and Kubernetes secrets. Oracle manages this default encryption using a master encryption key, without requiring any action on your part. For additional control over the lifecycle of the master encryption key and how it is used, you can choose to manage the master encryption key yourself, rather than have Oracle manage it for you. 
If you choose to manage the master encryption key yourself, you specify the key to use, and you have control over when the key is rotated. The master encryption key is stored in the Oracle Cloud Infrastructure Vault service (see [Key Management](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)). The Kubernetes secrets at rest in etcd are encrypted using a data encryption key (a DEK) using the AES-CBC encryption algorithm with PKCS#7 padding. A new DEK is generated for each encryption. The data encryption keys are encrypted using the master encryption key (the MEK), a concept known as envelope encryption. 
Before you can create a cluster for which you want to manage the master encryption key yourself, you have to:
  * create a suitable master encryption key in Vault (or obtain the name and OCID of such a key)
  * create a dynamic group that includes all clusters in the compartment in which you are going to create the new cluster
  * create a policy authorizing the dynamic group to use the master encryption key


Having created the cluster and specified that you want to manage the master encryption key yourself, you can optionally restrict the use of the master encryption key by modifying the dynamic group to include just that cluster.
Note the following:
  * You can only select the option to manage the master encryption key yourself when creating a new cluster in the 'Custom Create' workflow. You cannot choose to manage the master encryption key when creating a new cluster in the 'Quick Create' workflow. And you cannot choose to manage the master encryption keys for clusters you previously created in the 'Custom Create' workflow.


**Caution**
If you select the option to manage the master encryption key yourself, do not subsequently delete the master encryption key in the Vault service. As soon as you schedule a key for deletion in Vault, the Kubernetes secrets stored for the cluster in etcd become inaccessible. If you have already scheduled the key for deletion, it might still be in the Pending Deletion state. If that is the case, cancel the scheduled key deletion (see [Canceling a Master Encryption Key Deletion](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_cancel_the_deletion_of_a_key.htm)) to restore access to the Kubernetes secrets. If you allow the scheduled key deletion operation to complete and the master encryption key to be deleted, the Kubernetes secrets stored for the cluster in etcd are permanently inaccessible. As a result, cluster upgrades will fail. In this situation, you have no choice but to delete and recreate the cluster. 
## Setting Up Master Encryption Key Access 🔗 
If you choose to manage the master encryption key that encrypts Kubernetes secrets in the cluster's etcd key-value store when creating a new cluster in the 'Custom Create' workflow, set up access to the master encryption key:
  1. Log in to the Console.
  2. If you know the OCID of the master encryption key to use to encrypt Kubernetes secrets, go straight to the next step. Otherwise:
     * If a suitable master encryption key already exists in Vault but you're not sure of its OCID, follow the instructions in [Listing Master Encryption Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_view_key_details.htm) and make a note of the master encryption key's OCID.
     * If a suitable master encryption key does not already exist in Vault, follow the instructions in [Creating a Master Encryption Key](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_create_a_new_key.htm) to create one, setting:
       * **Protection Mode** to Software or HSM.
       * **Key Shape: Algorithm** to AES, RSA, or ECDSA.
       * **Key Shape: Length** for AES keys (128, 256) and RSA keys (2048, 3072, 4096), or **Key Shape: Curve ID** for ECDSA keys (NIST_P256, NIST_P384, NIST_P521).
Having created a new master encryption key, make a note of its OCID.
  3. Grant access to the master encryption key in Vault. 
You can grant access to the master encryption key in two ways:
[Create a new IAM policy (recommended)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengencryptingdata.htm)
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Policies**.
    2. Follow the instructions in [To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy), and give the policy a name (for example, `acme-oke-kms-policy`).
    3. Enter a policy statement to give access to the master encryption key, in the format:
```
Allow any-user to use keys in compartment <compartment-name> where ALL {request.principal.type = 'cluster', target.key.id = '<key-ocid>'}

```

where:
       * `<compartment-name>` is the name of the compartment containing the master encryption key.
       * `<key-OCID>` is the OCID of the master encryption key in Vault.
For example:
```
Allow any-user to use keys in compartment acme-kms-key-compartment where ALL {request.principal.type = 'cluster', target.key.id = 'ocid1.key.oc1.iad.annrl______trfg'}

```

    4. Click **Create** to create the new policy.
[Create a new dynamic group, and then create a new IAM policy](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengencryptingdata.htm)
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Under **Identity domain** , select **Dynamic groups**. 
    2. Follow the instructions in [To create a dynamic group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#To), and give the dynamic group a name (for example, `acme-oke-kms-dyn-grp`).
    3. Enter a rule that includes all clusters in the compartment in the format:
Copy
```
ALL {resource.type = 'cluster', resource.compartment.id = '<compartment-ocid>'}
```

where `<compartment-ocid>` is the OCID of the compartment in which you intend to create the new cluster.
For example:
Copy
```
ALL {resource.type = 'cluster', resource.compartment.id = 'ocid1.compartment.oc1..aaaaaaaa23______smwa'}
```

    4. Click **Create Dynamic Group**.
Having created a dynamic group that includes all clusters in the compartment, you can now create a policy to give the dynamic group access to the master encryption key in Vault.
    5. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Policies**.
    6. Follow the instructions in [To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy), and give the policy a name (for example, `acme-oke-kms-dyn-grp-policy`).
    7. Enter a policy statement to give the dynamic group access to the master encryption key, in the format:
Copy
```
Allow dynamic-group <dynamic-group-name> to use keys in compartment <compartment-name> where target.key.id = '<key-OCID>'
```

where:
       * `<dynamic-group-name>` is the name of the dynamic group you created earlier.
       * `<compartment-name>` is the name of the compartment containing the master encryption key.
       * `<key-OCID>` is the OCID of the master encryption key in Vault.
For example:
Copy
```
Allow dynamic-group <acme-oke-kms-dyn-grp> to use keys in compartment acme-kms-key-compartment where target.key.id = 'ocid1.key.oc1.iad.annrl______trfg'
```

    8. Click **Create** to create the new policy.
  4. When you create a new cluster, select the **Encrypt using a key that you manage** option and specify the master encryption key (see [Using the Console to create a Cluster with Explicitly Defined Settings in the 'Custom Create' workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm#create-custom-cluster "Find out how to use the 'Custom Create' workflow to create a Kubernetes cluster with explicitly defined settings and existing network resources using Kubernetes Engine \(OKE\).")).
  5. (Optional) Having created the cluster, for additional security:
    1. Make a note of the OCID of the new cluster you just created.
    2. Restrict the use of the master encryption key:
       * if you simply created an IAM policy, modify the policy statement to explicitly include the OCID of the new cluster, rather than all clusters in the compartment. For example:
```
Allow any-user to use keys in compartment acme-kms-key-compartment where ALL {request.principal.type = 'cluster', target.key.id = 'ocid1.key.oc1.iad.annrl______trfg', request.principal.id = 'ocid1.cluster.oc1.iad.aaaaaaaaaf______yg5q'}

```

       * if you created a dynamic group, modify the dynamic group rule you created earlier to explicitly specify the OCID of the new cluster, rather than all clusters in the compartment. For example:
```
resource.id = 'ocid1.cluster.oc1.iad.aaaaaaaaaf______yg5q'
```



## Rotating the Master Encryption Key 🔗 
If you select the option to manage the master encryption key yourself, you can rotate the master encryption key in the Vault service, creating a new version of the master encryption key (see [Rotating a Vault Key](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys_topic-To_rotate_a_master_encryption_key.htm)). 
In this situation, the master encryption key is not itself deleted (the master encryption key resource continues to exist, with the same OCID), but the master encryption key has a new value. Any new Kubernetes secrets stored for the cluster will be encrypted using the master encryption key's new value. Any existing encrypted Kubernetes secrets will still be accessible, because the original version of the master encryption key is still available in the Vault service. If you want existing Kubernetes secrets to be encrypted using the new version of the master encryption key, you have to rotate the Kubernetes secrets so that they are encrypted again. For example, by running the following command:
Copy
```
kubectl get secrets --all-namespaces -o json | kubectl annotate --overwrite -f - encryption-key-rotation-time="<time>"
```

where `<time>` is a string indicating when to perform the rotation. For example:
Copy
```
kubectl get secrets --all-namespaces -o json | kubectl annotate --overwrite -f - encryption-key-rotation-time="20210909_2135"
```

## Master Encryption Keys in Other Tenancies 🔗 
You can create a cluster in one tenancy that uses a master encryption key in a different tenancy. In this case, you have to write cross-tenancy policies to enable the cluster in its tenancy to access the master encryption key in the Vault service's tenancy. Note that if you want to create a cluster and specify a master encryption key that's in a different tenancy, you cannot use the Console to create the cluster.
For example, assume the cluster is in the ClusterTenancy, and the master encryption key is in the KeyTenancy. Users belonging to a group (OKEAdminGroup) in the ClusterTenancy have permissions to create clusters. A dynamic group (OKEAdminDynGroup) has been created in the cluster, with the rule `ALL {resource.type = 'cluster', resource.compartment.id = 'ocid1.compartment.oc1..<unique_ID>'}`, so all clusters created in the ClusterTenancy belong to the dynamic group.
In the root compartment of the KeyTenancy, the following policies:
  * use the ClusterTenancy's OCID to map ClusterTenancy to the alias OKE_Tenancy 
  * use the OCIDs of OKEAdminGroup and OKEAdminDynGroup to map them to the aliases RemoteOKEAdminGroup and RemoteOKEClusterDynGroup respectively
  * give RemoteOKEAdminGroup and RemoteOKEClusterDynGroup the ability to list, view, and perform cryptographic operations with a particular master key in the KeyTenancy


Copy
```
Define tenancy OKE_Tenancy as ocid1.tenancy.oc1..<unique_ID>
Define dynamic-group RemoteOKEClusterDynGroup as ocid1.dynamicgroup.oc1..<unique_ID>
Define group RemoteOKEAdminGroup as ocid1.group.oc1..<unique_ID>
Admit dynamic-group RemoteOKEClusterDynGroup of tenancy ClusterTenancy to use keys in tenancy where target.key.id = 'ocid1.key.oc1..<unique_ID>'
Admit group RemoteOKEAdminGroup of tenancy ClusterTenancy to use keys in tenancy where target.key.id = 'ocid1.key.oc1..<unique_ID>'
```

In the root compartment of the ClusterTenancy, the following policies:
  * use the KeyTenancy's OCID to map KeyTenancy to the alias KMS_Tenancy
  * give OKEAdminGroup and OKEAdminDynGroup the ability to use master keys in the KeyTenancy
  * allow OKEAdminDynGroup to use a specific master key obtained from the KeyTenancy in the ClusterTenancy


Copy
```
Define tenancy KMS_Tenancy as ocid1.tenancy.oc1..<unique_ID>
Endorse group OKEAdminGroup to use keys in tenancy KMS_Tenancy
Endorse dynamic-group OKEAdminDynGroup to use keys in tenancy KMS_Tenancy
Allow dynamic-group OKEAdminDynGroup to use keys in tenancy where target.key.id = 'ocid1.key.oc1..<unique_ID>'
```

See [Accessing Object Storage Resources Across Tenancies](https://docs.oracle.com/iaas/Content/Object/Concepts/accessingresourcesacrosstenancies.htm) for more examples of writing cross-tenancy policies.
Having entered the policies, you can now run a command similar to the following to create a cluster in the ClusterTenancy that uses the master key obtained from the KeyTenancy:
Command
CopyTry It
```
oci ce cluster create --name oke-with-cross-kms --kubernetes-version v1.16.8 --vcn-id ocid1.vcn.oc1.iad.<unique_ID> --service-lb-subnet-ids '["ocid1.subnet.oc1.iad.<unique_ID>"]' --compartment-id ocid1.compartment.oc1..<unique_ID> --kms-key-id ocid1.key.oc1.iad.<unique_ID>
```

Was this article helpful?
YesNo


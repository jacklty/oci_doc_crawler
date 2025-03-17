Updated 2025-01-15
# Rotating Cluster Credentials
_Find out how to rotate the credentials of clusters you've created using Kubernetes Engine (OKE)._
**Note** You can rotate credentials for clusters with managed nodes, and for clusters with self-managed nodes. Credential rotation is not yet supported for clusters with virtual nodes.
To enable secure TLS (formerly SSL) communication to, from, and within clusters, Kubernetes uses PKI (Public Key Infrastructure) certificates for authentication. For more information about PKI certificates and Kubernetes clusters, see [PKI certificates and requirements](https://kubernetes.io/docs/setup/best-practices/certificates/) in the Kubernetes documentation.
The clusters you create with Kubernetes Engine have PKI root CAs (Certificate Authorities) and private keys for the cluster, the etcd component, and the front-proxy component. These root CAs are used to sign the certificates and private keys used in the cluster. The root CAs, signed certificates, and private keys used in the cluster are collectively known as cluster credentials.
In clusters you create with Kubernetes Engine, the root CAs expire after five years. To continue using a cluster, you have to change (or 'rotate') cluster credentials before the end of the five year period. Additionally, your organization might have security guidelines and policies in place that require you to rotate cluster credentials more frequently (in some cases, much more frequently). Messages informing you of upcoming cluster credential expiry are shown in the Console. You can also use the Console, the CLI, and the API to find out when cluster credentials are due to expire.
When you rotate cluster credentials, you have to update Kubernetes API clients that were using the previous credentials to communicate with the Kubernetes API. Such Kubernetes API clients include kubeconfig files, and pods that communicate directly with the Kubernetes API.
**Note** You can start cluster credential rotation at any time, but you must start credential rotation before the credentials expire.
Note that in an effort to avoid service interruption, if you have not started cluster credential rotation 90 days before the credentials are due to expire, Kubernetes Engine attempts to rotate the cluster credentials automatically. However, we strongly recommend that you rotate cluster credentials yourself, rather than relying on automatic cluster credential rotation. For more information, see [Automatic Cluster Credential Rotation](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengrotatingcredentials.htm#contengrotatingcredentials_topic_automatic_credential_rotation).
Rotating cluster credentials is a three-step process:
  * **Step 1, Initiate the Start Credential Rotation phase:** During the Start Credential Rotation phase, new root CAs, private keys, and certificates are created. You can initiate the Start Credential Rotation phase at any time, but you must start credential rotation before the credentials expire. Starting credential rotation before the credentials expire will also avoid service interruption.
When initiating the Start Credential Rotation phase, you explicitly specify the length of a 'delay period' before the Complete Credential Rotation phase is initiated automatically. The delay period enables you to update Kubernetes API clients (Step 2). During the delay period, both the legacy credentials and the new credentials provide secure communication to, from, and within the cluster. The delay period you specify must be no less than 1 day, and no more than 90 days. You can manually initiate the Complete Credential Rotation phase before the end of the delay period, provided the new credentials are at least 24 hours old and you have successfully completed Step 2.
Do not start Step 2 until the new root CAs, private keys, and certificates have been created.
**Note** When using the CLI or the API to initiate the Start Credential Rotation phase, specify the length of the delay period in the ISO 8601 duration format. For example:
    * use `P5D` to specify five days
    * use `P5DT5H` to specify five days and five hours
    * use `P5DT5H5M` to specify five days, five hours, and five minutes
For more information about the ISO 8601 duration format, search online.
  * **Step 2, Update Kubernetes API clients:** When the new root CAs, private keys, and certificates have been created, and within the delay period you specified (no less than 1 day, and no more than 90 days):
    * Set up new kubeconfig files to enable access to the cluster using both the new credentials and the legacy credentials.
    * Recreate or restart worker nodes hosting pods that communicate directly with the Kubernetes API Server (or to avoid interruption to the worker nodes, simply restart the pods themselves). 
Do not start Step 3 until you have set up new kubeconfig files, and have recreated or restarted worker nodes (or simply restarted the pods).
  * **Step 3, Initiate the Complete Credential Rotation phase:** When you have finished Step 2, and within the delay period you specified (no less than 1 day, and no more than 90 days), you can manually initiate the Complete Credential Rotation phase. During the Complete Credential Rotation phase, the legacy root CAs, private keys, and certificates are retired and removed. Initiate the Complete Credential Rotation phase no sooner than 24 hours after you initiated the Start Credential Rotation phase, and only after you have finished step 2. Provided the new credentials are at least 24 hours old, you can initiate the Complete Credential Rotation phase as soon as you are ready.
If you do not manually initiate the Complete Credential Rotation phase during the delay period you specified (no less than 1 day, and no more than 90 days), the Complete Credential Rotation phase is automatically initiated at the end of the delay period.
When the Complete Credential Rotation phase is complete, we recommend replacing any kubeconfig file created during step 2 (which will contain both legacy credentials and new credentials) with a new kubeconfig file containing only the new credentials.


The Start Credential Rotation phase and Complete Credential Rotation phase are spawned as separate work requests. To track progress of the Start Credential Rotation phase and Complete Credential Rotation phase, view the status of the corresponding work request. See [Viewing Work Requests](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm#contengviewingworkrequests "Find out how to view the operations of Kubernetes Engine \(OKE\) as work requests.").
You can rotate cluster credentials using the Console, the CLI, and the API.
Note the following when rotating cluster credentials:
  * Credential rotation is supported for clusters running Kubernetes version 1.20 or later.
  * Simply upgrading the Kubernetes version on the cluster control plane does not rotate credentials. You have to complete all the steps in the credential rotation process.
  * The Start Credential Rotation phase and Complete Credential Rotation phase can only begin when all worker nodes in the cluster have a status of READY. If the status of one or more worker nodes changes to NOT READY during credential rotation, the credential rotation operations pause for up to 24 hours, waiting for all nodes to again have a status of READY before resuming. If one or more worker nodes still has a status of NOT READY after 24 hours, the credential rotation operations time out.
  * If the Start Credential Rotation phase or the Complete Credential Rotation phase fails for some reason, the legacy credentials continue to work and are not retired until they expire.
  * If you do not manually initiate the Complete Credential Rotation phase within the delay period you specified (no less than 1 day, and no more than 90 days), the Complete Credential Rotation phase is initiated automatically. If you have not updated Kubernetes API clients before the end of the delay period, the cluster will experience service interruption.
  * Credential rotation is supported for clusters with managed nodes, and for clusters with self-managed nodes. Credential rotation is not yet supported for clusters with virtual nodes.


## Required IAM Policies for Rotating Cluster Credentials 🔗 
To rotate cluster credentials, you must belong to a group that has been granted permission to manage the cluster for which you want to rotate the credentials, or be in the tenancy's Adminstrators group.
## Automatic Cluster Credential Rotation 🔗 
Kubernetes Engine monitors your Kubernetes environment to identify clusters with credentials that are approaching their expiry date. When Kubernetes Engine detects a cluster with credentials that are due to expire in 90 days and which you have not started to rotate, Kubernetes Engine attempts to rotate the cluster's credentials automatically in an effort to avoid service interruption. However, note that we strongly recommend that you rotate cluster credentials yourself, rather than relying on Kubernetes Engine to automatically rotate cluster credentials for you.
Kubernetes Engine automatically rotates cluster credentials, regardless of the Kubernetes version running on the cluster. Unlike manual cluster credential rotation, automatic cluster credential rotation does not require clusters to be running Kubernetes version 1.20 or later. 
Also unlike manual cluster credential rotation, Kubernetes Engine automatically rotates cluster credentials regardless of the status of worker nodes in the cluster. Automatic cluster credential rotation does not require worker nodes to have a status of READY during the Start Credential Rotation phase or the Complete Credential phase.
When Kubernetes Engine automatically initiates the Start Credential Rotation phase of credential rotation, it notifies you that automatic cluster credential rotation has started. During the Start Credential Rotation phase, new root CAs, private keys, and certificates are created. When the Start Credential Phase is complete:
  * If cluster credentials have not yet expired, Kubernetes Engine schedules the Complete Credential Rotation phase to start three days before the credential expiration date. You can manually initiate the Complete Credential Rotation phase of credential rotation sooner if you prefer by completing [Step 3, Initiate the Complete Credential Rotation phase](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengrotatingcredentials.htm#contengrotatingcredentials__Step3-InitiateCompleteCredentialRotationphase) (to avoid a service interruption, first complete [Step 2, Update Kubernetes API clients](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengrotatingcredentials.htm#contengrotatingcredentials__Step2-UpdateKubernetesAPIclients)).
  * If cluster credentials have already expired, or are going to expire within three days, Kubernetes Engine initiates the Complete Credential Rotation phase immediately. 


Before the Complete Credential phase is initiated, to avoid a service interruption, it is your responsibility to update Kubernetes API clients to:
  * Set up new kubeconfig files to enable access to the cluster using both the new credentials and the legacy credentials.
  * Recreate or restart worker nodes hosting pods that communicate directly with the Kubernetes API Server (or to avoid interruption to the worker nodes, simply restart the pods themselves). 


Note that if Kubernetes Engine initiates the Complete Credential Rotation phase immediately because cluster credentials have already expired, you do not have an opportunity to update Kubernetes API clients before the legacy credentials are retired. As a result, the cluster will experience a service interruption until you have set up new kubeconfig files to enable access to the cluster using the new credentials, and recreated or restarted worker nodes (or restarted the pods). 
## Using the Console 🔗 
### To check when cluster credentials are due to expire
  1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
  2. Choose a **Compartment** you have permission to work in.
  3. On the **Cluster List** page, click the name of the cluster for which you want to check the credential expiry date.
  4. On the **Cluster** page, review the date beside the **Cluster credentials expire on:** label.


### Step 1: Initiate the Start Credential Rotation Phase 🔗 
  1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
  2. Choose a **Compartment** you have permission to work in.
  3. On the **Cluster List** page, click the name of the cluster for which you want to rotate credentials.
  4. On the **Cluster** page, click **Start Rotation** beside the **Cluster credentials expire on:** label.
  5. In the **Start Credential Rotation** dialog, specify how long to delay the automatic initiation of the Complete Credential Rotation phase. The delay period you specify must be:
     * at least 24 hours after you initiate the Start Credential Rotation phase
     * no more than 90 days after you initiate the Start Credential Rotation phase
  6. Click **Start** to initiate the Start Credential Rotation phase.
  7. To view the progress of the Start Credential Rotation work request, click **Work Requests** under **Resources**.
  8. Only when the status of the Start Credential Rotation work request is **Complete** , move on to updating Kubernetes API clients (see [Step 2: Update Kubernetes API Clients](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengrotatingcredentials.htm#contengrotatingcredentials_topic-Using_the_Console__section-set-up-kubeconfig-file-recreate-nodes-pods)).


### Step 2: Update Kubernetes API Clients 🔗 
When the status of the Start Credential Rotation work request is **Complete** :
  1. Set up new kubeconfig files to access the cluster using the new credentials, using the `oci ce cluster create-kubeconfig` command (see [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.")).
The kubeconfig files contain both the new credentials and the legacy credentials.
  2. Recreate or restart worker nodes hosting pods that communicate directly with the Kubernetes API Server (or to avoid interruption to the worker nodes, simply restart the pods themselves):
     * Recreate or restart worker nodes:
       * Recreate a worker node, by deleting the worker node without scaling down the node pool. A new worker node is created to replace the deleted worker node. See [Deleting Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes.htm#contengdeletingworkernodes "Find out about deleting worker nodes, and notes about setting cordon and drain options, with Kubernetes Engine \(OKE\).").
       * Restart a worker node. See [Rebooting an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/restartinginstance.htm#restart-instance).
     * Restart pods running on the cluster that communicate directly with the Kubernetes API Server.
  3. Only when you have set up new kubeconfig files and recreated or restarted worker nodes or pods, move on to complete credential rotation (see [Step 3: Initiate the Complete Credential Rotation Phase](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengrotatingcredentials.htm#contengrotatingcredentials_topic-Using_the_Console__section-rotate-cluster-credentials)).


### Step 3: Initiate the Complete Credential Rotation Phase 🔗 
When you initiate the Start Credential Rotation phase, you explicitly specify the length of a delay period before the automatic initiation of the Complete Credential Rotation phase. The delay period you specify must be no less than 1 day, and no more than 90 days. During the delay period, both the legacy credentials and the new credentials provide secure communication to, from, and within the cluster. 
If you prefer, rather than waiting for the automatic initiation of the Complete Credential Rotation phase at the end of the delay period, you can initiate the Complete Credential Rotation phase immediately, as follows:
  1. Make sure that:
     * The status of the Start Credential Rotation work request is **Complete**. See [Step 1: Initiate the Start Credential Rotation Phase](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengrotatingcredentials.htm#contengrotatingcredentials_topic-Using_the_Console__section-renew-cluster-credentials).
     * Updated Kubernetes API clients. See [Step 2: Update Kubernetes API Clients](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengrotatingcredentials.htm#contengrotatingcredentials_topic-Using_the_Console__section-set-up-kubeconfig-file-recreate-nodes-pods).
  2. On the **Cluster** page, click **Complete Rotation Now** beside the **Complete credential rotation on:** label.
  3. In the **Complete Rotation** dialog, select the **I have read the above message** option to confirm that you have updated Kubernetes API clients.
  4. Click **Start** to initiate the Complete Credential Rotation phase, during which the legacy root CAs, private keys, and certificates are retired and removed. 
  5. To view the progress of the Complete Credential Rotation work request, click **Work Requests** under **Resources**.
When the status of the Complete Credential Rotation work request is **Complete** , the new credentials are being used for secure communication to, from, and within the cluster. The legacy credentials have been retired and removed.
  6. (Recommended, but not required) Replace any kubeconfig file created during step 2 (which will contain both legacy and new credentials) with a new kubeconfig file containing only the new credentials, using the `oci ce cluster create-kubeconfig` command (see [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.")). 


## Using the CLI 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). For a complete list of flags and options available for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/). 
### Initiating the Start Credential Rotation phase
```
oci ce cluster start-credential-rotation --auto-completion-delay-duration <number-of-days> --cluster-id <cluster-ocid>
```

For example:
```
oci ce cluster start-credential-rotation --auto-completion-delay-duration 'P5D' --cluster-id ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd
```

### Viewing the status of Credential Rotation work requests
```
oci ce cluster credential-rotation-status get --cluster-id <cluster-ocid>
```

For example:
```
oci ce cluster credential-rotation-status get --cluster-id ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd
```

### Initiating the Complete Credential Rotation phase
```
oci ce cluster complete-credential-rotation --cluster-id <cluster-ocid>
```

For example:
```
oci ce cluster complete-credential-rotation --cluster-id ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd
```

## Using the API 🔗 
Run the following operations to rotate cluster credentials:
  * [StartCredentialRotation](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/StartCredentialRotation)
  * [GetCredentialRotationStatus](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/CredentialRotationStatus/GetCredentialRotationStatus)
  * [CompleteCredentialRotation](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/CompleteCredentialRotation)


Was this article helpful?
YesNo


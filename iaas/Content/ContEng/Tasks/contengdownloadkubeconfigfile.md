Updated 2025-02-05
# Setting Up Cluster Access
_Find out about the steps to set up access to the clusters you create using Kubernetes Engine (OKE). Having completed the steps, you can start using kubectl to manage the cluster._
To access a cluster using kubectl, you have to set up a Kubernetes configuration file (commonly known as a 'kubeconfig' file) for the cluster. The kubeconfig file (by default named `config` and stored in the `$HOME/.kube` directory) provides the necessary details to access the cluster. Having set up the kubeconfig file, you can start using kubectl to manage the cluster.
The steps to follow when setting up the kubeconfig file depend on how you want to access the cluster:
  * To access the cluster using kubectl in Cloud Shell, run an Oracle Cloud Infrastructure CLI command in the Cloud Shell window to set up the kubeconfig file.
See [Setting Up Cloud Shell Access to Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#cloudshelldownload). 
  * To access the cluster using a local installation of kubectl:
    * Generate an API signing key pair (if you don't already have one).
    * Upload the public key of the API signing key pair.
    * Install and configure the Oracle Cloud Infrastructure CLI.
    * Set up the kubeconfig file.
See [Setting Up Local Access to Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#localdownload).


## Setting Up Cloud Shell Access to Clusters 🔗 
When a cluster's Kubernetes API endpoint has a public IP address, you can access the cluster in Cloud Shell by setting up a kubeconfig file.
**Note**
To access a cluster with a private Kubernetes API endpoint in Cloud Shell, you can configure a bastion using the Oracle Cloud Infrastructure Bastion service. For more information, see [Setting Up a Bastion for Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm#contengsettingupbastion "Find out how to set up a bastion to access clusters you've created using Kubernetes Engine \(OKE\).").
To set up the kubeconfig file:
[Step 1: Set up the kubeconfig file](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm)
  1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
  2. Choose a **Compartment** you have permission to work in.
  3. On the **Cluster List** page, click the name of the cluster you want to access using kubectl. The **Cluster** page shows details of the cluster.
  4. Click the **Access Cluster** button to display the **Access Your Cluster** dialog box.
  5. Click **Cloud Shell Access**.
  6. Click **Launch Cloud Shell** to display the Cloud Shell window. For more information about Cloud Shell (including the required IAM policy), see [Cloud Shell](https://docs.oracle.com/iaas/Content/API/Concepts/devcloudshellintro.htm).
  7. Run the Oracle Cloud Infrastructure CLI command to set up the kubeconfig file and save it in a location accessible to kubectl. 
For example, enter the following command (or copy and paste it from the **Access Your Cluster** dialog box) in the Cloud Shell window:
Command
CopyTry It
```
oci ce cluster create-kubeconfig --cluster-id ocid1.cluster.oc1.phx.aaaaaaaaae... --file $HOME/.kube/config --region us-phoenix-1 --token-version 2.0.0 --kube-endpoint PUBLIC_ENDPOINT
```

where:
     * `ocid1.cluster.oc1.phx.aaaaaaaaae...` is the OCID of the current cluster. For convenience, the command in the **Access Your Cluster** dialog box already includes the cluster's OCID.
     * `--kube-endpoint PUBLIC_ENDPOINT` specifies to add the public IP address of the cluster's Kubernetes API endpoint to the kubeconfig file. For more information, see [Kubernetes Cluster Control Plane and Kubernetes API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengclustersnodes.htm#processes).
Note that if a kubeconfig file already exists in the location you specify, details about the cluster will be added as a new context to the existing kubeconfig file. The `current-context:` element in the kubeconfig file will be set to point to the newly-added context.
**Tip** For clipboard operations in the Cloud Shell window, Windows users can use Ctrl-C or Ctrl-Insert to copy, and Shift-Insert to paste. For Mac OS users, use Cmd-C to copy and Cmd-V to paste.
  8. If you don't save the kubeconfig file in the default location (`$HOME/.kube`) or with the default name (`config`), set the value of the KUBECONFIG environment variable to point to the name and location of the kubeconfig file. For example, enter the following command in the Cloud Shell window:
Command
CopyTry It
```
export KUBECONFIG=$HOME/.kube/config
```



[Step 2: Verify that kubectl can access the cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm)
Verify that kubectl can connect to the cluster by entering the following command in the Cloud Shell window:
Command
CopyTry It
```
$ kubectl get nodes
```

Information about the nodes in the cluster is shown. 
You can now use kubectl to perform operations on the cluster.
## Setting Up Local Access to Clusters 🔗 
When a cluster's Kubernetes API endpoint does not have a public IP address, you can access the cluster from a local terminal if your network is peered with the cluster's VCN.
**Note**
To access a cluster with a private Kubernetes API endpoint from a local terminal, you can also configure a bastion using the Oracle Cloud Infrastructure Bastion service. For more information, see [Setting Up a Bastion for Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm#contengsettingupbastion "Find out how to set up a bastion to access clusters you've created using Kubernetes Engine \(OKE\).").
To set up the kubeconfig file:
[Step 1: Generate an API signing key pair](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm)
If you already have an API signing key pair, go straight to the next step. If not:
  1. Use OpenSSL commands to generate the key pair in the required PEM format. If you're using Windows, you'll need to install Git Bash for Windows and run the commands with that tool. See [How to Generate an API Signing Key](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#two).
  2. Copy the contents of the public key to the clipboard (you'll need to paste the value into the Console later).


[Step 2: Upload the public key of the API signing key pair](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm)
  1. To view the details: In the navigation bar, select the **Profile** menu and then select **User settings** or **My profile** , depending on the option that you see.
  2. Click **Add Public Key**.
  3. Paste the public key's value into the window and click **Add**.
The key is uploaded and its fingerprint is displayed (for example, d1:b2:32:53:d3:5f:cf:68:2d:6f:8b:5f:77:8f:07:13).


[Step 3: Install and configure the Oracle Cloud Infrastructure CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm)
  1. Install the Oracle Cloud Infrastructure CLI version 2.6.4 (or later). See [Installing the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliinstall.htm). 
  2. Configure the Oracle Cloud Infrastructure CLI. See [Configuring the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliconfigure.htm).


[Step 4: Set up the kubeconfig file](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm)
  1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**. 
  2. Choose a **Compartment** you have permission to work in.
  3. On the **Cluster List** page, click the name of the cluster you want to access using kubectl. The **Cluster** page shows details of the cluster.
  4. Click the **Access Cluster** button to display the **Access Your Cluster** dialog box.
  5. Click **Local Access**.
  6. Create a directory to contain the kubeconfig file. By default, the expected directory name is `$HOME/.kube`. 
For example, on Linux, enter the following command (or copy and paste it from the **Access Your Cluster** dialog box) in a local terminal window:
Copy
```
mkdir -p $HOME/.kube
```

  7. Run the Oracle Cloud Infrastructure CLI command to set up the kubeconfig file and save it in a location accessible to kubectl. 
For example, on Linux, enter the following command (or copy and paste it from the **Access Your Cluster** dialog box) in a local terminal window:
Copy
```
oci ce cluster create-kubeconfig --cluster-id ocid1.cluster.oc1.phx.aaaaaaaaae... --file $HOME/.kube/config --region us-phoenix-1 --token-version 2.0.0 --kube-endpoint PRIVATE_ENDPOINT|PUBLIC_ENDPOINT
```

where:
     * `ocid1.cluster.oc1.phx.aaaaaaaaae...` is the OCID of the current cluster. For convenience, the command in the **Access Your Cluster** dialog box already includes the cluster's OCID.
     * `--kube-endpoint PRIVATE_ENDPOINT|PUBLIC_ENDPOINT` specifies whether to add the private IP address or the public IP address of the cluster's Kubernetes API endpoint to the kubeconfig file. For more information, see [Kubernetes Cluster Control Plane and Kubernetes API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengclustersnodes.htm#processes).
Note that if a kubeconfig file already exists in the location you specify, details about the cluster will be added as a new context to the existing kubeconfig file. The `current-context:` element in the kubeconfig file will be set to point to the newly-added context.
  8. If you don't save the kubeconfig file in the default location (`$HOME/.kube`) or with the default name (`config`), set the value of the KUBECONFIG environment variable to point to the name and location of the kubeconfig file. For example, on Linux, enter the following command (or copy and paste it from the **Access Your Cluster** dialog box) in a local terminal window:
Copy
```
export KUBECONFIG=$HOME/.kube/config
```



[Step 5: Verify that kubectl can access the cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm)
  1. Verify that kubectl is available by entering the following command in a local terminal window:
Copy
```
kubectl version
```

The response shows:
     * the version of kubectl installed and running locally
     * the version of Kubernetes (strictly speaking, the version of the kube-apiserver) running on the cluster's control plane nodes
Note that the kubectl version must be within one minor version (older or newer) of the Kubernetes version running on the control plane nodes. If kubectl is more than one minor version older or newer, install an appropriate version of kubectl. See [Kubernetes version and version skew support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/) in the Kubernetes documentation. 
If the command returns an error indicating that kubectl is not available, install kubectl (see the [kubectl documentation](https://kubernetes.io/docs/tasks/tools/install-kubectl/)), and repeat this step.
  2. Verify that kubectl can connect to the cluster by entering the following command in a local terminal window:
Copy
```
kubectl get nodes
```

Information about the nodes in the cluster is shown. 
You can now use kubectl to perform operations on the cluster.


## Notes about Kubeconfig Files 🔗 
Note the following about kubeconfig files:
  * A single kubeconfig file can include the details for multiple clusters, as multiple contexts. The cluster on which operations will be performed is specified by the `current-context:` element in the kubeconfig file. 
  * A kubeconfig file includes an Oracle Cloud Infrastructure CLI command that dynamically generates an authentication token and inserts it when you run a kubectl command. The Oracle Cloud Infrastructure CLI must be available on your shell's executable path (for example, $PATH on Linux).
  * The authentication tokens generated by the Oracle Cloud Infrastructure CLI command in the kubeconfig file are short-lived, cluster-scoped, and specific to individual users. As a result, you cannot share kubeconfig files between users to access Kubernetes clusters.
  * The Oracle Cloud Infrastructure CLI command in the kubeconfig file uses your current CLI profile when generating an authentication token. If you have defined multiple profiles in different tenancies in the CLI configuration file (for example, in ~/.oci/config), specify which profile to use when generating the authentication token as follows. In both cases, `<profile-name>` is the name of the profile defined in the CLI configuration file:
    * Add `--profile` to the `args:` section of the kubeconfig file as follows:
Copy
```
user:
 exec:
  apiVersion: client.authentication.k8s.io/v1beta1
  args:
  - ce
  - cluster
  - generate-token
  - --cluster-id
  - <cluster ocid>
  - --profile
  - <profile-name>
  command: oci
  env: []
```

    * Set the OCI_CLI_PROFILE environment variable to the name of the profile defined in the CLI configuration file before running kubectl commands. For example:
Command
CopyTry It
```

export OCI_CLI_PROFILE=<profile-name>
```

Command
CopyTry It
```

kubectl get nodes

```

  * The authentication tokens generated by the Oracle Cloud Infrastructure CLI command in the kubeconfig file are appropriate to authenticate individual users accessing the cluster using kubectl. However, the generated authentication tokens are unsuitable if you want other processes and tools to access the cluster, such as continuous integration and continuous delivery (CI/CD) tools. In this case, consider creating a Kubernetes service account and adding its associated authentication token to the kubeconfig file. For more information, see [Adding a Service Account Authentication Token to a Kubeconfig File](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaddingserviceaccttoken.htm#Adding_a_Service_Account_Authentication_Token_to_a_Kubeconfig_File "Find out how to add a service account authentication token to the kubeconfig file of a Kubernetes cluster you've created using Kubernetes Engine \(OKE\).").
  * An IAM policy might have been defined to restrict cluster access to only users that have been verified with multi-factor authentication (MFA). If such a policy exists, you have to add `--profile` and `--auth` arguments to the kubeconfig file to enable an MFA-verified user to access the cluster using kubectl, as follows. In both cases, `<profile-name>` is the name of the MFA-verified user's profile defined in the Oracle Cloud Infrastructure CLI configuration file:
    * Add the following arguments to the `args:` section of the kubeconfig file:
Copy
```

  - --profile
  - <profile-name>
  - --auth
  - security_token
```

For example:
Copy
```
user:
 exec:
  apiVersion: client.authentication.k8s.io/v1beta1
  args:
  - ce
  - cluster
  - generate-token
  - --cluster-id
  - <cluster ocid>
  - --profile
  - <profile-name>
  - --auth
  - security_token
  command: oci
  env: []
```

    * Set the OCI_CLI_PROFILE environment variable to the name of the MFA-verified user's profile defined in the CLI configuration file before running kubectl commands. For example:
Command
CopyTry It
```

export OCI_CLI_PROFILE=<profile-name>
```

Command
CopyTry It
```

kubectl get nodes

```

After updating the kubeconfig file, the user you use to access the cluster must be MFA-verified. If you attempt to access the cluster using a user that has not been MFA-verified, the message `error: You must be logged in to the server (Unauthorized)` is displayed.
For more information about MFA-verified users, see [Managing Multifactor Authentication](https://docs.oracle.com/iaas/Content/Identity/Tasks/usingmfa.htm).


## Upgrading Kubeconfig Files from Version 1.0.0 to Version 2.0.0 🔗 
Kubernetes Engine currently supports kubeconfig version 2.0.0 files, and no longer supports kubeconfig version 1.0.0 files.
Enhancements in kubeconfig version 2.0.0 files provide security improvements for your Kubernetes environment, including short-lived cluster-scoped tokens with automated refreshing, and support for instance principals to access Kubernetes clusters. Additionally, authentication tokens are generated on-demand for each cluster, so kubeconfig version 2.0.0 files cannot be shared between users to access Kubernetes clusters (unlike kubeconfig version 1.0.0 files).
Note that kubeconfig version 2.0.0 files are not compatible with kubectl versions prior to version 1.11.9. If you are currently running kubectl version 1.10.x or older, upgrade kubectl to version 1.11.9 or later. For more information about compatibility between different versions of kubernetes and kubectl, see the [Kubernetes documentation](https://kubernetes.io/docs/setup/release/version-skew-policy/).
Follow the instructions below to determine the current version of kubeconfig files, and how to upgrade any remaining kubeconfig version 1.0.0 files to version 2.0.0.
### Determine the kubeconfig file version
To determine the version of a cluster's kubeconfig file:
1. In a terminal window (the Cloud Shell window or a local terminal window as appropriate), enter the following command to see the format of the kubeconfig file currently pointed at by the KUBECONFIG environment variable:
Command
CopyTry It
```
kubectl config view
```

2. If the kubeconfig file is version 1.0.0, you see a response in the following format:
```
users:
- name: <username>
 user:
  token: <token-value>
```

If you see a response in the above format, you have to upgrade the kubeconfig file. See [Upgrading Kubeconfig Files from Version 1.0.0 to Version 2.0.0](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#upgrading).
3. If the kubeconfig file is version 2.0.0, you see a response in the following format:
```
user:
 exec:
  apiVersion: client.authentication.k8s.io/v1beta1
  args:
  - ce
  - cluster
  - generate-token
  - --cluster-id
  - <cluster ocid>
  command: oci
  env: []
```

If you see a response in the above format, no further action is required.
### Upgrade a kubeconfig version 1.0.0 file to version 2.0.0 🔗 
To upgrade a kubeconfig version 1.0.0 file:
  1. In the case of a local installation of kubectl, confirm that Oracle Cloud Infrastructure CLI version 2.6.4 (or later) is installed by entering:
Command
CopyTry It
```
oci -version
```

If the Oracle Cloud Infrastructure CLI version is earlier than version 2.6.4, upgrade the CLI to a later version. See [Upgrading the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliupgrading.htm).
  2. Follow the appropriate instructions to set up the kubeconfig file for use in Cloud Shell or locally (see [Setting Up Cloud Shell Access to Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#cloudshelldownload) or [Setting Up Local Access to Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#localdownload)). Running the `oci ce cluster create-kubeconfig` command shown in the **Access Your Cluster** dialog box upgrades the existing kubeconfig version 1.0.0 file. If you change the name or location of the kubeconfig file, set the KUBECONFIG environment variable to point to the new name and location of the file.
  3. Confirm the kubeconfig file is now version 2.0.0:
    1. In a terminal window (the Cloud Shell window or a local terminal window as appropriate), enter:
Command
CopyTry It
```
kubectl config view
```

    2. Confirm that that the response is in the following format:
```
user:
 exec:
  apiVersion: client.authentication.k8s.io/v1beta1
  args:
  - ce
  - cluster
  - generate-token
  - --cluster-id
  - <cluster ocid>
  command: oci
  env: []
```



Was this article helpful?
YesNo


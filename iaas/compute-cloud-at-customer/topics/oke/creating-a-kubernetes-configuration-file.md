Updated 2024-12-16
# Creating a Kubernetes Configuration File
On Compute Cloud@Customer, you can set up a Kubernetes configuration file for each OKE cluster that you work with. Your Kubernetes configuration file enables you to access OKE clusters using the `kubectl` command and the Kubernetes Dashboard.
Kubernetes configuration files organize information about clusters, users, namespaces, and authentication mechanisms. You can define contexts to easily switch between clusters and namespaces. The `kubectl` tool uses Kubernetes configuration files to find the information it needs to choose a cluster and communicate with the API server of a cluster.
## Installing the Kubernetes Command Line Tool 🔗 
Install and configure the Kubernetes command line tool `kubectl`. The `kubectl` tool enables you to perform operations on OKE clusters such as deploy applications, inspect and manage cluster resources, and view logs.
To install `kubectl`, see [Kubernetes Install Tools](https://kubernetes.io/docs/tasks/tools/). The `kubectl` version must be within one minor version of the OKE cluster Kubernetes version. For example, a v1.29 client can communicate with v1.28, v1.29, and v1.30 control planes. See [Supported Versions of Kubernetes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/container-engine-for-kubernetes.htm#container-engine-for-kubernetes__k8s-versions).
For more information, including a complete list of `kubectl` operations, see the <https://kubernetes.io/docs/reference/kubectl/> reference page.
## Create a Kubernetes Configuration File 🔗 
Use the CLI to create your Kubernetes configuration file.
**Tip**
The Quick Start button on a cluster details page in the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") shows how to create a Kubernetes configuration file, and provides the OCID of the cluster.
  1. Get the OCID of the cluster: `oci ce cluster list`
  2. Run the [oci ce cluster create-kubeconfig](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/create-kubeconfig.html) command as described to create the configuration file:
The `--cluster-id` option is required.
The default value of the `--file` option is `~/.kube/config`. If you already have a file at the specified location and you want to replace it, use the `--overwrite` option. To maintain more than one configuration file, select a different file by using the `KUBECONFIG` environment variable or the `--kubeconfig` option.
The value of the `--kube-endpoint` option must be `PUBLIC_ENDPOINT`.
If you don't specify the `--profile` option, the current value of your `OCI_CLI_PROFILE` environment variable is used. Best practice is to specify this value.
If provided, the value of the `--token-version` option must be 2.0.0.
**Example:**
Use the following command to configure a Kubernetes configuration file for the specified cluster using the public endpoint:
Copy
```
$ oci ce cluster create-kubeconfig --cluster-id ocid1.cluster.unique_ID \
--file $HOME/.kube/config --kube-endpoint PUBLIC_ENDPOINT --profile profile-name
New config written to the Kubeconfig file /home/username/.kube/config
```

A Kubernetes configuration file includes a CLI command that dynamically generates an authentication token and inserts it when you run a `kubectl` command. By default, the CLI command in the Kubernetes configuration file uses your current CLI profile when generating an authentication token. If you have defined multiple profiles in your CLI configuration file, use one of the following methods to specify which profile to use when generating the authentication token. The value of `**_profile-name_**`is the name of the profile in your CLI configuration file.
     * Ensure that your `OCI_CLI_PROFILE` environment variable is set to the profile for the tenancy where the `ocid1.cluster.unique_ID` resides. This setting is ignored if one of the following methods was used to specify the profile for this cluster in the Kubernetes configuration file.
     * Specify the `--profile` option on the `create-kubeconfig` command line as shown in the preceding example command.
     * Edit the generated configuration file as shown in the following example.
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
  - ** _cluster ocid_**
  - --profile
  - **_profile-name_**
  command: oci
  env: []
```

Use the following command to set your `KUBECONFIG` environment variable to the Kubernetes configuration file that you created or updated in the preceding command:
Copy
```
$ export KUBECONFIG=$HOME/.kube/config
```

The following command shows the content of your new YAML configuration file:
Copy
```
$ kubectl config view
```

If you run the command again with a different cluster OCID, the new information is merged with the existing information. The following message is displayed:
Copy
```
Existing Kubeconfig file found at /home/username/.kube/config and new config merged into it
```



**What's Next:**
[Verify Your Cluster Access](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-kubernetes-configuration-file.htm#creating-a-kubernetes-configuration-file__verify-cluster-access).
## Verify Your Cluster Access 🔗 
Before you run `kubectl` commands, enure that your `OCI_CLI_PROFILE` environment variable is set to the name of the profile that is defined in your OCI configuration file:
Copy
```
$ export OCI_CLI_PROFILE=<profile-name>
```

Run the following command to confirm that you can access your cluster:
Copy
```
$ kubectl cluster-info
```

Every Kubernetes namespace contains at least one ServiceAccount: the default ServiceAccount for that namespace, which is named `default`. If you don't specify a ServiceAccount when you create a Pod, the OKE service automatically assigns the ServiceAccount named `default` in that namespace.
An application running inside a Pod can access the Kubernetes API using automatically mounted service account credentials.
**What's Next:**
[Create a Kubernetes Dashboard](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-kubernetes-configuration-file.htm#creating-a-kubernetes-configuration-file__create-dashboard).
## Create a Kubernetes Dashboard 🔗 
The dashboard helps you manage the cluster and manage and troubleshoot applications running in the cluster.
On the [Kubernetes site](https://kubernetes.io/), see [Deploy and Access the Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)
**What's Next:**
[Creating an OKE Worker Node Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-node-pools.htm#creating-a-worker-node-pools "Learn how to create OKE worker node pools on Compute Cloud@Customer for a workload cluster.")
Was this article helpful?
YesNo


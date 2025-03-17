Updated 2024-08-23
# Accessing a Cluster Using Kubectl
_Find out how to use kubectl to access a Kubernetes cluster you've created using Kubernetes Engine (OKE)._
You can use the Kubernetes command line tool kubectl to perform operations on a cluster you've created with Kubernetes Engine. You can use the kubectl installation included in Cloud Shell, or you can use a local installation of kubectl. In both cases, before you can use kubectl to access a cluster, you have to specify the cluster on which to perform operations by setting up the cluster's kubeconfig file. 
Note the following:
  * An Oracle Cloud Infrastructure CLI command in the kubeconfig file generates authentication tokens that are short-lived, cluster-scoped, and specific to individual users. As a result, you cannot share kubeconfig files between users to access Kubernetes clusters. The generated authentication tokens are also unsuitable if you want other processes and tools to access the cluster, such as continuous integration and continuous delivery (CI/CD) tools. In this case, consider creating a Kubernetes service account and adding its associated authentication token to the kubeconfig file. For more information, see [Adding a Service Account Authentication Token to a Kubeconfig File](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaddingserviceaccttoken.htm#Adding_a_Service_Account_Authentication_Token_to_a_Kubeconfig_File "Find out how to add a service account authentication token to the kubeconfig file of a Kubernetes cluster you've created using Kubernetes Engine \(OKE\).").
  * The version of kubectl you use must be compatible with the version of Kubernetes running on clusters created by Kubernetes Engine. In the case of Cloud Shell, kubectl is regularly updated so it is always compatible with the versions of Kubernetes currently supported by Kubernetes Engine. In the case of a local installation of kubectl, it is your responsibility to update kubectl regularly. For more information about compatibility between different versions of kubernetes and kubectl, see the [Kubernetes documentation](https://kubernetes.io/docs/setup/release/version-skew-policy/).
  * To access a cluster with a private Kubernetes API endpoint using kubectl in Cloud Shell or from a local terminal, you can configure a bastion using the Oracle Cloud Infrastructure Bastion service. For more information, see [Setting Up a Bastion for Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupbastion.htm#contengsettingupbastion "Find out how to set up a bastion to access clusters you've created using Kubernetes Engine \(OKE\).").


## Accessing a Cluster Using kubectl in Cloud Shell 🔗 
To access a cluster using kubectl in Cloud Shell:
  1. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file for use in Cloud Shell, and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See [Setting Up Cloud Shell Access to Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#cloudshelldownload).
  2. In the Cloud Shell window, enter `kubectl` followed by the command for the operation you want to perform on the cluster. For a list of available commands and options, see the [kubectl documentation](https://kubernetes.io/docs/reference/kubectl/overview/).
Note that you must have the appropriate permissions to run the command you enter. See [About Access Control and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutaccesscontrol.htm#About_Access_Control_and_Container_Engine_for_Kubernetes "Find out about the permissions required to access clusters you've created using Kubernetes Engine \(OKE\).").


## Accessing a Cluster Using kubectl Installed Locally 🔗 
To access a cluster using kubectl installed locally:
  1. If you haven't already done so, install kubectl (see the [kubectl documentation](https://kubernetes.io/docs/tasks/tools/install-kubectl/)).
  2. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file for use locally, and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. You might also need to set the OCI_CLI_PROFILE environment variable to the name of the profile defined in the CLI configuration file before running kubectl commands. See [Setting Up Local Access to Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#localdownload).
  3. In a local terminal window, enter `kubectl` followed by the command for the operation you want to perform on the cluster. For a list of available commands and options, see the [kubectl documentation](https://kubernetes.io/docs/reference/kubectl/overview/).
Note that you must have the appropriate permissions to run the command you enter. See [About Access Control and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutaccesscontrol.htm#About_Access_Control_and_Container_Engine_for_Kubernetes "Find out about the permissions required to access clusters you've created using Kubernetes Engine \(OKE\).").


Was this article helpful?
YesNo


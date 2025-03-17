Updated 2025-01-15
# Troubleshooting Network Configuration Issues for Kubernetes Clusters Using Network Path Analysis Tests
_Find out how to use network path analysis tests to help you resolve network connectivity issues with clusters you've created using Kubernetes Engine (OKE)._
For a cluster you create with Kubernetes Engine to function correctly, the network resources specified for the cluster must be configured appropriately. When you create a cluster using the [Quick Create workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Quick_Cluster_with_Default_Settings.htm#create-quick-cluster "Find out how to use the 'Quick Create' workflow to create a Kubernetes cluster with default settings and new network resources using Kubernetes Engine \(OKE\)."), Kubernetes Engine creates and configures new network resources for you, according to the guidelines described in [Network Resource Configuration for Cluster Creation and Deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#Network_Resource_Configuration_for_Cluster_Creation_and_Deployment "Find out how to configure network resources to use Kubernetes Engine \(OKE\)."). However, when you create a cluster using the [Custom Create workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm#create-custom-cluster "Find out how to use the 'Custom Create' workflow to create a Kubernetes cluster with explicitly defined settings and existing network resources using Kubernetes Engine \(OKE\)."), you specify existing network resources for the new cluster to use. These resources must be configured appropriately to enable network communication with the cluster, and to enable different cluster components to communicate with each other. 
Configuring network resources for Kubernetes clusters can become complicated. Kubernetes Engine therefore provides a number of pre-defined network path analysis tests to troubleshoot network configuration issues. These path analysis tests examine virtual network topologies, walk through multiple route tables, and scrutinize security rules in network security groups (NSGs) and security lists. No actual traffic is sent, instead the configuration is examined and used to confirm reachability.
Using the path analysis tests, you can determine whether one OCI resource can reach another OCI resource (unidirectional connectivity from source to destination), and whether two OCI resources can reach each other (bidirectional connectivity). For example, you can use a path analysis test to determine whether a pod in a Kubernetes cluster that uses the VCN-Native Pod Networking CNI plugin can reach OCI services, and vice versa.
When using the Console, you can select the pre-defined path analysis tests from the **Cluster details** screen. For more information about the pre-defined path analysis tests that are available, see [Pre-defined Path Analysis Tests](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtroubleshooting_topic-network_troubleshooting.htm#contengtroubleshooting_topic-network_path_analysis_tests_available_tests).
Each pre-defined path analysis test requires a number of different test parameters. When you run a test, depending on the test you select, default values for some or all of the test parameters are derived from the properties of resources used by the cluster. In some cases, you can change the default values. You have to provide values for test parameters that do not have default values. Having run a pre-defined path analysis test, you can save the results as a JSON file, enabling you to compare test results over time. For more information about running pre-defined path analysis tests for a cluster, see [Running Pre-defined Path Analysis Tests](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtroubleshooting_topic-network_troubleshooting.htm#contengtroubleshooting_topic-network_path_analysis_tests_running).
The path analysis tests are powered by Oracle Cloud Infrastructure Network Path Analyzer (NPA), which identifies virtual network configuration issues that impact connectivity. In addition to the pre-defined path analysis tests available from the **Cluster details** screen, you can also create your own custom path analysis tests using NPA. For more information about NPA, including permissions required to run NPA, and how to create and run path analysis tests with NPA, see [Network Path Analyzer](https://docs.oracle.com/iaas/Content/Network/Concepts/path_analyzer.htm).
## Required IAM Policies for Running Path Analysis Tests 🔗 
To run path analysis tests to verify network paths for a Kubernetes cluster that you have created using Kubernetes Engine, you must belong to a group that has been granted permission to use Network Path Analyzer (NPA). Network Path Analyzer must also have been granted permission to access various network resources.
To find out the permissions to grant, and a recommended IAM policy, see [Required Permissions](https://docs.oracle.com/iaas/Content/Network/Concepts/path_analyzer.htm#path_analyzer__permissions) in the Network Path Analyzer documentation.
## Pre-defined Path Analysis Tests 🔗 
You can use a number of different pre-defined path analysis tests to verify network paths for a Kubernetes cluster that you have created using Kubernetes Engine. In the Console, you can filter the list of path analysis tests by:
  * the type of issue that you want to check for (such as DNS failures, Kubernetes control plane failures, nodes failing to register)
  * paths that are essential, recommended, or optional for the correct functioning of Kubernetes Engine


The tests are grouped into the following broad test categories:
  * **Cluster API tests:** Use to verify that one or more paths are available to allow the cluster's Kubernetes API endpoint to communicate bi-directionally with other cluster components and network locations.
  * **Node tests:** Use to verify that one or more paths are available to allow worker nodes in the Kubernetes data plane to communicate bi-directionally with other cluster components and network locations.
  * **Pod tests:** Use to verify that one or more paths are available to allow pods in the Kubernetes data plane to communicate bi-directionally with other cluster components and network locations. 
  * **Load Balancer tests:** Use to verify that one or more paths are available to allow an OCI load balancer or network load balancer to communicate bi-directionally with other cluster components and network locations.


Cluster components use different paths to communicate with other cluster components and network locations, depending on the cluster's network type (Flannel overlay or VCN-native) and the type of worker nodes the cluster contains (managed and/or virtual). In each test category, there are different path analysis tests to verify these different paths. 
Note that the Console only shows you the path analysis tests that are applicable to the current cluster. For example, if the cluster's network type is Flannel overlay, you can only select path analysis tests that apply to the Flannel overlay network type.
## Running Pre-defined Path Analysis Tests 🔗 
You use the Console to run pre-defined path analysis tests to verify network paths for a Kubernetes cluster that you have created using Kubernetes Engine.
### Using the Console 🔗 
  1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
  2. Choose a **Compartment** you have permission to work in.
  3. On the **Cluster List** page, click the name of the cluster for which you want to run a pre-defined network path analysis test.
  4. Under **Resources** , click **Path analysis tests**.
The pre-defined path analysis tests are grouped into the following broad categories, shown on different test category tabs:
     * **Cluster API tests:** Use to verify that one or more paths are available to allow the cluster's Kubernetes API endpoint to communicate bi-directionally with other cluster components and network locations.
     * **Node tests:** Use to verify that one or more paths are available to allow worker nodes in the Kubernetes data plane to communicate bi-directionally with other cluster components and network locations.
     * **Pod tests:** Use to verify that one or more paths are available to allow pods in the Kubernetes data plane to communicate bi-directionally with other cluster components and network locations. 
     * **Load Balancer tests:** Use to verify that one or more paths are available to allow an OCI load balancer or network load balancer to communicate bi-directionally with other cluster components and network locations.
  5. (Optional) Under **Type of issue that you want to check for** , specify the path analysis tests shown on the test category tabs by selecting the type of issue that you want to check for:
     * **Any issue**
     * **DNS failures**
     * **Kubernetes control plane failures**
     * **Nodes not registering**
  6. (Optional) Under **Filters** , reduce or expand the number of path analysis tests shown on the test category tabs by selecting or de-selecting one or more of the **OKE required** options, as follows:
     * **Yes:** Show those path analysis tests verifying essential paths that must be available in order for Kubernetes Engine to function correctly.
     * **Recommended:** Show those path analysis tests verifying paths that are recommended (but not required) for use by applications running on clusters created by Kubernetes Engine.
     * **No:** Show those path analysis tests verifying paths that are neither required by Kubernetes Engine nor particularly recommended, but which can nonetheless be used by applications running on clusters created by Kubernetes Engine.
If you select all of the OKE required options under **Filters** , all available path analysis tests are shown on the test category tabs. If you deselect all of the OKE required options under **Filters** , no path analysis tests are shown on any of the test category tabs.
  7. Locate the path analysis test you want to run on one of the test category tabs, using the test name and description.
**Tip:** If you can't find the path analysis test you're looking for, or if no path analysis tests are shown, double-check that the **Type of issue that you want to check for** and the **OKE required** options are set correctly. Also double-check that the path analysis test you want to run is applicable to the current cluster. For example, if the cluster's network type is Flannel overlay, you can only select path analysis tests that apply to the Flannel overlay network type.
  8. Click **Launch path analysis** beside the path analysis test you want to run, to display the **Path analysis** page.
If you do not have the correct permissions to run the path analysis test you select, an error message is shown. You have to grant the correct permissions before proceeding. To find out the permissions to grant, and a recommended IAM policy, see [Required Permissions](https://docs.oracle.com/iaas/Content/Network/Concepts/path_analyzer.htm#path_analyzer__permissions) in the Network Path Analyzer documentation.
  9. Depending on the path analysis test you select, change default values or provide values for the source and destination test parameters in the **Path analysis** page.
In many cases, default values for test parameters are derived from the properties of resources used by the cluster. In some cases, you can change the default values. You have to provide values for test parameters that do not have default values.
  10. Click **Run analysis** to run the path analysis test.
  11. Allow the path analysis test to run, which might take up to a minute to complete. 
While the path analysis test is running, traffic is not actually traversing the network. Network configuration information is simply being collected and analyzed to determine how the paths between the source and the destination would function or fail.
After the path analysis test has run, all the possible paths (up to a maximum of eight) that have been identified between the source and the destination are shown on different tabs in the **Discovered paths** section.
Each tab shows the options configured for the path analysis test, along with diagrams visualizing the forward path and (if configured) the return path for traffic between the source and destination, and the status of each path:
     * If the path analysis test determines that network traffic can successfully traverse a particular path, the diagram for that path has a **Path Status** of **Reachable**. A green arrow represents each successful hop between nodes in the overall path.
     * If the path analysis test determines that network traffic cannot successfully traverse a particular path, the diagram for that path has a **Path Status** of **Unreachable**. A green arrow represents any successful hops in the overall path, and a red arrow represents the hop or network segment that is unreachable.
  12. Click **View diagram information** to see more detail about the hops in each path, or click a specific arrow to get details about a particular hop. For example, to determine whether a hop failed because of a misconfiguration in a specific node's routing or security configuration. 
Each hop has a **Routing status** , with one of the following values:
     * **Forwarded:** The relevant route table allows the traffic.
     * **No route:** The route table does not explicitly allow the traffic.
     * **Indeterminate:** The route table cannot be analyzed, because your account does not have the required permissions, or because the node routing information is unavailable for some other reason..
If the node is an OCI resource, the routing information links directly to the relevant route rule.
Each hop has a **Security status** , with one of the following values:
     * **Allowed:** The relevant security list or rule allows the traffic.
     * **Blocked:** The security list or rule blocks the traffic.
     * **Indeterminate:** The security list or rule cannot be analyzed, because your account does not have the required permissions, or because the node security information is unavailable for some other reason. 
If the node is an OCI resource, the security information links directly to the relevant security list or rule.
  13. (Optional) Click **Save as JSON** to save the output of the path analysis test in a JSON file in your default downloads directory.
Saving the path analysis test output as a JSON file enables you to compare test results over time.
  14. Click **Close** to close the **Path analysis** page.


Was this article helpful?
YesNo


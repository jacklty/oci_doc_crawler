Updated 2025-02-18
# Creating a Path Analysis Test
Use the Network Path Analyzer service to create a test that analyzes the configuration of a virtual network. See how the paths between the source and the destination function or fail. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path_analyzer-creating_test.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path_analyzer-creating_test.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path_analyzer-creating_test.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Network Command Center** , select **Network Path Analyzer**.
    2. Select **Create Network Path Analysis**. 
    3. On the **Configure analysis** page, enter the following information: 
       * **Name****:** Enter a descriptive name for the analysis test. It doesn't have to be unique, and it can't be changed later in the Console. Avoid entering confidential information. If you don't enter a name, one is generated for you. 
       * **Create in compartment:** Select the compartment that you want to create the analysis test in. 
       * **Protocol:** Select the type of protocol to use in the test. Common protocols are listed first. You can also specify the source and destination ports later on the page. 
       * **Source:** Select the resource that begins the path that you're testing. 
You can provide the IP address of the source, or you can find an OCI resource to use as the source. The supported OCI resource types are **Subnet IP address** , **VLAN IP address** , **Compute instance (VNIC)** , **VNIC OCID** , **Load balancer** , and **Network load balancer**. After selecting a type, select a specific resource from the list of resources with that type. If necessary, enter the source IPv4 address. 
When you select **Subnet IP address** as the resource type, the specified IP address must belong to one of the subnet CIDRs. The IP address itself doesn't have to be active.
If you enter an on-premises IP address in the **Source IPv4 address** field, select the **This IP address is an on-premises endpoint** checkbox. 
       * **Destination:** Select the resource that ends the path that you're testing. 
You can provide the IP address of the destination, or you can find an OCI resource to use as the destination. The supported OCI resource types are **Subnet IP address** , **VLAN IP address** , **Compute instance (VNIC)** , **VNIC OCID** , **Load balancer** , and **Network load balancer**. After selecting a type, select a specific resource from the list of resources with that type. When select a load balancer or network load balancer as a destination, you must specify the listener to use for the analysis.
If you entered an on-premises IP address in the **Source IPv4 address** field, select the**This IP address is an on-premises endpoint** checkbox.
**Note**
When you use IP addresses to select the source or destination of a path analysis test, the following scenarios might occur because of network configuration. These scenarios can create ambiguity that either prevents the test or creates a test based on an unintended source or destination. 
a. **VCNs with overlapping CIDRs:** In this scenario, if you specify an IP address that belongs to the overlapped part of the CIDR, the network path analyzer can't decide which VCN and VCN subnet the IP address belongs to, so it doesn’t perform the test. To resolve this issue, use the **find resource** option and select the source or destination by specifying its type and selecting from available resources of that type.
b. **VCN and on-premises network with overlapping CIDRs** : In this scenario, one or more VCNs have CIDRs that overlap with an on-premises network. If you select an IP address in the overlapped CIDR, the network path analyzer considers the endpoint as being from an OCI VCN CIDR. If the intended endpoint is to an on-premises network, then you must inform the service by selecting the **This IP address is an on-premises endpoint** checkbox when you enter an on-premises IP address as a source or destination.
       * **Direction:** To test both the forward and reverse paths, select **Bi-directional**. To test the forward path only, select **Uni-directional**
    4. (Optional) **Tags:** To apply one or more tags to the test, select **Show tagging options**. 
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    5. Select **Run analysis**. 
The test that you have configured runs, which might take up to a minute or more (depending on the total number of hops needed) to complete. For details about running tests, see [Running a Path Analysis Test](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/path_analyzer-running_test.htm#top "Use the Network Path Analyzer service to run a test after it has been saved, or immediately after it has been configured."). Because you might not want to save every test you run, you can't save the test yet.
    6. (Optional) After you run the test, select **Save analysis** to save the new analysis parameters. Or, you can select **Cancel** to exit the workflow without saving the test.
  * Use the [path-analyzer-test create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vn-monitoring/path-analyzer-test/create.html) command and required parameters to create a path analyzer test:
Command
CopyTry It
```
oci vn-monitoring path-analyzer-test create --compartment-id compartment_OCID --destination-endpoint file://destination-endpoint.json --protocol protocol --source-endpoint file://source-endpoint.json ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreatePathAnalyzerTest](https://docs.oracle.com/iaas/api/#/en/NetMonitor/latest/PathAnalyzerTest/CreatePathAnalyzerTest) operation to create a path analyzer test.


Was this article helpful?
YesNo


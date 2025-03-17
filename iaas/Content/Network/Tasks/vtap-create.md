Updated 2025-02-18
# Creating a VTAP
Create a Virtual Test Access Point (VTAP) to mirror traffic from a chosen _source_ to a selected _target_ to help troubleshooting, security analysis, and data monitoring.
The resources that serve as the source and target must exist in the same VCN.
For more information and a feature overview, see [Virtual Test Access Points (VTAPs)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap.htm#vtap "A Virtual Test Access Point \(VTAP\) provides a way to mirror traffic from a selected source to a selected target to help in troubleshooting, security analysis, and data monitoring.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-create.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-create.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-create.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Network Command Center** , select **VTAPs**.
    2. Select **Create VTAP**.
    3. Enter the following information:
       * **Name:** Enter a descriptive name for the VTAP. It doesn't have to be unique, and it can't be changed later in the Console (but you can change it with the API).
       * **Compartment:** Select the compartment that you want to create the VTAP in.
       * **VCN:** Select the VCN that contains the resources that you want to use for the source and target for the VTAP. The **Source** and **Target** options show only resources that belong to the VCN you select.
       * **Source:** Select the VTAP's intended source. This source is the interface that the VTAP monitors. Traffic on this interface that matches criteria in the capture filter is mirrored. Source types are as follows: 
         * [Database](https://docs.oracle.com/iaas/Content/Database/home.htm) system
         * [Exadata VM Cluster](https://docs.oracle.com/iaas/Content/Database/home.htm)
         * [Compute](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm) instance VNIC
         * [Load Balancer](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm)
         * [Autonomous Data Warehouse](https://docs.oracle.com/en/cloud/paas/autonomous-data-warehouse-cloud/index.html)
After you select the resource type, use the lists to select the subnet of the current VCN where the resource's IP address or endpoint is located, and the specific resource. 
Traffic from a source can only be mirrored one time.
       * **Target:** Select the resource of the VTAP's intended target. Mirrored traffic from the source is sent to the target. The available target type is [Network Load Balancer](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/home.htm).
After you select the resource type, use the lists to select the subnet of the current VCN where the resource's IP address or endpoint is located, and the specific resource. 
       * **Capture Filter:** Either select an existing capture filter or select to [create a capture filter](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-create.htm#top "Create a capture filter that you can use with a Virtual Test Access Point \(VTAP\) or a VCN flow log."). A new capture filter needs a name, a compartment, and at least one rule.
    4. (Optional) Select **Show advanced options** and provide the following information as needed: 
       * **VXLAN network identifier (VNI):** In this field on the **Settings** tab, enter a VNI to uniquely identify the VXLAN. If you don't select a VNI, one is generated for you.
       * **Max packet size:** Select a maximum packet size between 64 and 9000 bytes. For better performance or efficient ingestion at the target, you can truncate the mirrored packets to a smaller length. 
       * **Priority mode:** Select this option to give equal priority to monitored and mirrored traffic when there is congestion at the source. By default, production traffic is prioritized ahead of VTAP mirrored traffic. When you enable priority mode, monitored traffic and VTAP mirrored traffic are given equal priority. When this option is selected, mirrored traffic might cause some monitored traffic to be dropped whenever the source is congested. If this packet loss is detected, you can either disable priority mode or upgrade the source shapes to accommodate more bandwidth.
       * **Tagging:**
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    5. Select **Create VTAP**.
The VTAP is created and its details page is displayed.
The VTAP is created in the **Stopped** state. Select **Start** to start the VTAP when you're ready.
Traffic from a source can be mirrored only one time. If you start a VTAP and another running VTAP monitors the same source, you might disrupt mirroring on the other VTAP. 
  * When using the CLI, you must [create a capture filter](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-create.htm#top "Create a capture filter that you can use with a Virtual Test Access Point \(VTAP\) or a VCN flow log.") before you create the VTAP.
Use the [vtap create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vtap/create.html) command and required parameters to create a VTAP:
Command
CopyTry It
```
oci network vtap create --capture-filter-id capture_fliter_OCID --compartment-id compartment_OCID
--source-id source_OCID --vcn-id vcn_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * When using the API, you must [create a capture filter](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-create.htm#top "Create a capture filter that you can use with a Virtual Test Access Point \(VTAP\) or a VCN flow log.") before you create the VTAP.
Run the [CreateVtap](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vtap/CreateVtap) operation to create a VTAP.


Was this article helpful?
YesNo


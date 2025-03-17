Updated 2025-02-18
# Viewing a VCN Topology Map
Use Network Visualizer to view a map that shows a visual representation of the topology of a single virtual cloud network (VCN).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/view-vcn-topology-map.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/view-vcn-topology-map.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/view-vcn-topology-map.htm)


  *     1. Open the navigation menu and select **Networking**. Under Network Command Center, select **Network visualizer**. Wait briefly for the network map to generate.
    2. Confirm that you're viewing the region and compartment that contain the VCN that you want to see represented in a map. If necessary, select a different compartment. To see resources in all compartments nested within the selected compartment, select **Include child compartments**.
    3. In the map, select the VCN for which you want view the topology. 
    4. In the **Resource summary** area, select either **View VCN routing map** or **View VCN security map**. While viewing one of these maps, you can switch to the other map by selecting the **Map Mode** option. 
The following elements appear in the control bar above the main map area, from leftmost to rightmost: 
       * **Map** : Displays the selected VCN.
       * **Search bar** : To find a resource by name, enter the name in the search bar. When a match is found and selected, the view in the main map area zooms in to show that resource. 
       * ![Screen Refresh Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_refresh.svg) **Refresh** : Updates the view in the main map area. The view is refreshed every three minutes, but if a change was made since the last refresh, you can manually trigger a refresh of the map.
       * ![Filter Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_filter.svg) **Filter** : **Filter****s** : Displays the filters used in the current view. You can turn them on and off as needed. 
       * ![Download Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_download.svg) **Export Map Data** : **Export map data** : Exports a zip file that contains a high-resolution PNG map of the resources in the current region and compartment, and a PDF file that contains a lower-resolution version of the map plus resource data (such as route tables). The PDF includes only the resource information for the elements shown in the map at the time of export.
       * ![Legend Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_legend.svg) **Map Legend** : Displays the symbols used in the map and their meaning.
The main map area displays the following information and controls:
       * Routable resources in the region but not within the specified VCN are shown on the left side of the map, separated with a dashed line from the resources (such as subnets and VLANs) inside the selected VCN. Gateways and DRG attachments are placed on this dashed line, and you can drag them on the line to make the relationships clearer. Resources that aren't routable from the VCN aren't shown.
       * Use the zoom controls in the lower-right corner of the map to change the view. You can also select the map and pan up, down, left, or right. You can double-click to zoom in 
       * You can dynamically rearrange resources on the map by dragging them. Be aware that these changes are temporary and don't persist if the map is refreshed.
       * Routes that are enabled between resources are shown on the lines that connect the resources. Routes are most often two-way connections but can be one way.
       * Some resources are displayed with both a name and an associated CIDR block. When more than one CIDR block is associated with a resource, a +1 or +2 is added as appropriate (up to +99). The extra CIDR blocks are listed in the summary area for the resource.
       * Any connected elements that you don't have the needed permissions to view are shown with a **no permission** icon: ![Not Visible Icon](https://docs.oracle.com/en-us/iaas/Content/Network/Images/visualization_not-visible.svg). Only the OCID is visible for that resource. 
    5. Select any resource on the map (the resource changes color to indicate the selection) to view basic information for that item in the **Resource summary** area to the right side of the map. The details presented vary depending on the component that you selected. 
For some components, you can also select **View additional resource details** to open a details panel for that component. These details are read-only summaries of the basic components for that resource. Links to that resource's details page are provided in case you want to make edits. 
For subnets and VLANs, you can switch on the **Persist routing information** toggle to maintain the display of the routing information for connections to and from the resource. Using this control, you can display as many or as few routes as you want.
**Tip** To navigate back to the regional network topology map, select the name of the region in the control bar.
  * Use the [vcn-topology get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn-topology/get.html) command and required parameters to get a virtual network topology for a VCN in the current region and specified compartment:
Command
CopyTry It
```
oci network vcn-topology get --compartment-id compartment_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetVcnTopology](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VcnTopology/GetVcnTopology) operation to get a virtual VCN topology for the current region and specified compartment.
The response body will contain a single [VcnTopology](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VcnTopology/) resource, which contains the following resources showing relationships between entities in the VCN:
    * [TopologyEntityRelationship](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/TopologyEntityRelationship)
    * [TopologyContainsEntityRelationship](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/TopologyContainsEntityRelationship)
    * [TopologyAssociatedWithEntityRelationship](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/TopologyAssociatedWithEntityRelationship)


Was this article helpful?
YesNo


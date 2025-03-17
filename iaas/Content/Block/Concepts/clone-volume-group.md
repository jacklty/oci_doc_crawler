Updated 2024-05-13
# Cloning a Volume Group
Clone a volume group in the Block Volume service.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/clone-volume-group.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/clone-volume-group.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/clone-volume-group.htm)


  *     1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Groups**.
    2. In the **Volume Groups** list, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) of the volume group that you want to clone, and then select **Create volume group clone**.
    3. Select the compartment to create the clone in.
    4. (Optional) Select the cluster placement group in which to clone the volume to.
**Note** The **Cluster Placement Group** control only appears in the Console if Cluster Placement Groups are enabled for the tenancy, and you've created and activated a cluster placement group with the capability added for volume resources, see [Cluster Placement Groups for Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/clusterplacementgroups.htm#clusterplacementgroups "Oracle Cloud Infrastructure Cluster Placement Groups lets you create resources in close proximity to one another to support low-latency networking use cases."). 
    5. Enter a name for the new volume group.
    6. Click **Create**.
  * Use the [oci bv volume-group create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/create.html) command and required parameters to clone a volume group from an existing volume group:
Command
CopyTry It
```
oci bv volume-group create --compartment-id <compartment_ID> --availability-domain <external_AD> --source-details <Source_details_JSON>
```

For example:
Command
CopyTry It
```
oci bv volume-group create --compartment-id ocid1.compartment.oc1..<unique_ID> --availability-domain ABbv:PHX-AD-1 --source-details '{"type": "volumeGroupId", "volumeGroupId": "ocid1.volumegroup.oc1.phx.<unique_ID>"}'
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [CreateVolumeGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/CreateVolumeGroup) operation to clone a volume group from an existing volume group.


Was this article helpful?
YesNo


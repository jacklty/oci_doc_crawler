Updated 2024-08-14
# Extending the Root Partition of Worker Nodes
_Find out how to extend the root partition of worker nodes you've created using Kubernetes Engine (OKE)._
When you create and update clusters and node pools, you can specify a custom size for worker node boot volumes. The custom boot volume size you specify must be larger than the default boot volume size of the image you select. When you increase the size of the boot volume, to take advantage of the larger boot volume size, you also need to extend the partition for the boot volume (the root partition).
Oracle Linux platform images include the `oci-utils` package. You can use the `oci-growfs[](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm#oci-growfs)` command from that package to extend the root partition and then grow the file system.
You can use the `oci-growfs[](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm#oci-growfs)` command in a cloud-init script to automatically extend the root partitions of worker nodes when they are created. For an example cloud-init script, see [Example 5: Using a Custom Cloud-init Script and oci-growfs to Increase the Size of the Boot Volume Partition](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingcustomcloudinitscripts.htm#contengusingcustomcloudinitscripts_topic_Examplecloudinitscriptusecases__CustomCloudinitScriptExampleIncreaseBootPartitionSize).
You can use SSH and the `oci-growfs[](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm#oci-growfs)` command to manually extend the root partition of an existing worker node as follows:
  1. Connect to the compute instance hosting the worker node using SSH. For example, by entering `ssh opc@192.0.2.254`
For more information, see [Connecting to Managed Nodes Using SSH](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconnectingworkernodesusingssh.htm#Connecting_to_Worker_Nodes_Using_SSH "Find out how to use SSH to connect to worker nodes in node pools in clusters you've created using Kubernetes Engine \(OKE\).").
  2. (Optional) Confirm the current boot volume size by entering:
```
kubectl describe node <node-id>
```

where `<node-id>` is the name or IP address of the worker node.
The current boot volume size is shown as the value of `ephemeral-storage` under `Allocatable`.
  3. Extend the root partition by entering:
Copy
```
sudo /usr/libexec/oci-growfs -y
```

  4. Restart the kubelet running on the node by entering:
Copy
```
sudo systemctl restart kubelet.service
```

  5. (Optional) Confirm the boot volume size has increased by entering:
```
kubectl describe node <node-id>
```

where `<node-id>` is the name or IP address of the worker node.
The increased boot volume size is shown as the value of `ephemeral-storage` under `Allocatable`.


Was this article helpful?
YesNo


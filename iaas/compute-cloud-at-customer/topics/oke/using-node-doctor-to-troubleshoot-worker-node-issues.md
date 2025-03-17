Updated 2025-02-05
# Using Node Doctor to Troubleshoot Worker Node Issues
On Compute Cloud@Customer, Node Doctor is a script that is included in the latest OKE images.
**Note** If Compute Cloud@Customer has worker nodes that were created before Node Doctor was included in OKE images, you can use node cycling to update older worker node images. See [Node Cycling an OKE Node Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/node-cycling-an-oke-node-pool.htm#node-cycling-an-oke-node-pool "On Compute Cloud@Customer, when you update a node pool, only new nodes that are added during this update or that are added later receive the updates. To replace existing nodes with new nodes that use updated settings, enable the node cycling option.").
If a cluster has a worker node that's in a state other than Active or Running, use the Node Doctor utility to troubleshoot the issues.
Node Doctor scans a worker node and reports the health status of the node. Node Doctor can do the following tasks:
  * Identify potential problem areas and provide references to information to help you address those problem areas. See [Print Troubleshooting Information](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/using-node-doctor-to-troubleshoot-worker-node-issues.htm#using-node-doctor-to-troubleshoot-worker-node-issues__print_info).
  * Collect node system information into a support bundle if you need help from Oracle Support. See [Create a Support Bundle](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/using-node-doctor-to-troubleshoot-worker-node-issues.htm#using-node-doctor-to-troubleshoot-worker-node-issues__support_bundle).


**Important**
Use Node Doctor only on worker nodes. Because Node Doctor is installed on OKE images, Node Doctor is also available on cluster control plane nodes. Don't use Node Doctor on control plane nodes.
## Connect to the Worker Node Using SSH 🔗 
Perform the following steps to connect to the worker node that you want to troubleshoot.
  1. Ensure that you have a private and public SSH key pair.
You must have the private key that goes with the public key that was added to the node when the node was created.
  2. Get the node username. OKE images have the initial username `opc` configured.
  3. Get the IP address of the worker node that you need to troubleshoot.
The IP address is on the Networking tab of the node details page in the Console.
     * If the node has a public IP address, use the public IP address.
     * If the node is on a private IP, then connect to the node through the bastion host.
If a bastion host isn't available, see [Creating a Bastion](https://docs.oracle.com/iaas/Content/Bastion/Tasks/create-bastion.htm).
  4. Enter the following command at a shell prompt on your local system (public IP address) or on the bastion host (private IP address):
Copy
```
ssh -i ** _private_key_file_** **_username_**@**_ip-address_**
```

     * `**_private_key_file_**`. The full path and name of the file that contains the private SSH key that goes with the public key that was added to the node when the node was created.
     * `**_username_**`. The default username for the node. This value probably is`opc`.
     * `**_ip-address_**`. The node IP address that you got in the previous step.
  5. Ensure that you have execute permissions for the following script. You run the script later.
Copy
```
ls -l /usr/local/bin/node-doctor.sh
-rwxr-xr-x 1 user1 user1 6288 Dec 5 2024 usr/local/bin/node-doctor.sh
```



## Print Troubleshooting Information 🔗 
While logged in to the worker node as described in [Connect to the Worker Node Using SSH](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/using-node-doctor-to-troubleshoot-worker-node-issues.htm#using-node-doctor-to-troubleshoot-worker-node-issues__ssh_connect), enter the following command to print information that identifies potential problem areas:
Copy
```
$ sudo /usr/local/bin/node-doctor.sh --check
```

Use the following command to see more options:
Copy
```
$ sudo /usr/local/bin/node-doctor.sh --help
```

## Create a Support Bundle 🔗 
If you can't resolve the issue, use the following command to create a support bundle with relevant information for Oracle Support:
Copy
```
$ sudo /usr/local/bin/node-doctor.sh --generate
```

The support bundle is in the `/tmp` directory as `oke-support-bundle-**_date_**T**_time_**.tar`.
**Note**
Monitor the `/tmp` directory to ensure that it doesn't fill up. Remove old files using the `rm` command, for example.
See the following resources for information about submitting a Support Request and uploading a bundle:
  * [Creating a Support Request](https://docs.oracle.com/iaas/Content/GSG/support/create-incident.htm)
  * [Quick User Guide to Upload Files to My Oracle Support - MOS (Doc ID 1588459.1)](https://support.oracle.com/epmos/faces/DocContentDisplay?id=1588459.1)
  * [How to Upload Files to Oracle Support (Doc ID 1547088.2)](https://support.oracle.com/epmos/faces/DocContentDisplay?id=1547088.2)


Was this article helpful?
YesNo


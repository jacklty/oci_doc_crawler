Updated 2025-01-15
# Troubleshooting Node Issues for Kubernetes Clusters Using the Node Doctor Script
_Find out how to use the Node Doctor script to help you resolve issues with compute instances hosting worker nodes in clusters you've created using Kubernetes Engine (OKE)._
The Node Doctor script is pre-installed on managed node compute instances to help you resolve issues with the instances. Depending on how you run it, the Node Doctor script:
  * Prints troubleshooting output that identifies potential problem areas, with links to documentation to address those areas.
  * Gathers system information into a bundle. My Oracle Support (MOS) provides instructions to upload the bundle to a support ticket.


If you see worker nodes with a **Kubernetes Node Condition** other than "Active", or with a **Node State** other than "Ready", use the Node Doctor script to troubleshoot the issues. 
You can run the Node Doctor script in the following ways: 
  * using SSH
  * using the Run Command feature


The **Worker Node Troubleshooting Guide** is a convenient way to start the Node Doctor script from the Console. The **Worker Node Troubleshooting Guide** provides dynamically populated commands to run the Node Doctor script using either SSH or the Run Command feature. To access the **Worker Node Troubleshooting Guide** , click the **Troubleshoot Nodes** button on the **Node Pool Details** page, select either **SSH Connections** or **Run Command** , and follow the instructions. 
**Note**
  * The Node Doctor script is pre-installed on worker node instances created from July 19, 2021. Worker nodes created before July 19, 2021 do not have the Node Doctor script pre-installed. To find out how to install the Node Doctor script, see [Downloading, Installing, and Updating the Node Doctor Script](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtroubleshooting_topic-node_troubleshooting.htm#contengtroubleshooting_topic_node_troubleshooting_download_node_doctor). Note that to install the Node Doctor script on such nodes, you must have SSH access to them.
  * Oracle releases new versions of the Node Doctor script periodically. Before running the Node Doctor script for the first time (even on worker nodes created after July 19, 2021), follow the instructions in [Downloading, Installing, and Updating the Node Doctor Script](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtroubleshooting_topic-node_troubleshooting.htm#contengtroubleshooting_topic_node_troubleshooting_download_node_doctor) to update the script to the latest version. It's also recommended good practice to update the Node Doctor script from time to time.
  * You can run the Node Doctor script on worker nodes in managed node pools, but not in virtual node pools.


## Using the Run Command Feature to Run the Node Doctor Script 🔗 
You can use the Run Command feature to troubleshoot node issues and generate a support bundle using the Node Doctor script. For more information about using the Run Command feature, see [Running Commands on an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/runningcommands.htm). 
To run the Node Doctor script using the Run Command feature, do one of the following:
  * Use the **Worker Node Troubleshooting Guide**. On the **Node Pool Details** page, click **Troubleshoot Nodes** to display the **Worker Node Troubleshooting Guide** , select **Run Command** , and follow the instructions.
  * Follow the steps in this section.


### Required IAM Policy
For administrators: To write a policy for the Run Command feature, do the following:
  1. Write the following policy to allow any user to use the Run Command feature to issue commands, cancel commands, and view the command output for the instances in a compartment:
Copy
```
Allow any-user to use instance-agent-command-execution-family in compartment id <compartment-ocid> where request.instance.id=target.instance.id
```

  2. If you want to save the output from the Node Doctor script in an Object Storage bucket, write the following policy:
Copy
```
Allow any-user to manage objects in compartment id <compartment-ocid-of-bucket> where all { request.principal.type='instance', request.principal.compartment.id='<compartment-ocid-of-node>', target.bucket.name = '<bucket-name>' }

```

where:
     * `<compartment-ocid-of-bucket>` is the OCID of the compartment to which the Object Storage bucket belongs.
     * `<compartment-ocid-of-node>` is the OCID of the compartment to which the worker node instance belongs.


### Creating the Command to Run the Node Doctor Script
To create the command to run the Node Doctor script on the instance:
  1. On the **Cluster Details** page, click **Node Pools** and click the managed node pool containing the managed node you want to troubleshoot.
  2. Under **Nodes** , click the name of the node you want to troubleshoot, to display the **Instance Details** page.
  3. Under **Resources** , click **Run Command**.
  4. Click **Create Command**.
  5. Enter a name for the command. Avoid entering confidential information.
  6. In the **Timeout in seconds** box, enter the amount of time to give the Compute Instance Run Command plugin to run the command on the instance before timing out. The timer starts when the plugin starts the command. For no timeout, enter 0.
  7. In the **Add script** section, upload the script that you want the Compute Instance Run Command plugin to run on the instance. Select the **Paste script** option and paste one of the following commands in the box:
     * `sudo /usr/local/bin/node-doctor.sh --check` to print troubleshooting output that identifies potential problem areas, with links to documentation to address those areas.
     * `sudo /usr/local/bin/node-doctor.sh --generate &> /dev/null && cat /tmp/oke-support-bundle.tar` to gather system information in a bundle. My Oracle Support (MOS) provides instructions to upload the bundle to a support ticket.
  8. In the **Output type** section, select the location to save the output of the command:
     * **Output as text:** The output is saved as plain text. You can review the output on the Instance Details page.
     * **Output to an Object Storage bucket:** The output is saved to an Object Storage bucket. Select a bucket. In the **Object name** box, enter a name for the output file. Avoid entering confidential information.
     * **Output to an Object Storage URL:** The output is saved to an Object Storage URL. Enter the URL.
  9. Click **Create Command**.


### Viewing the Output of the Node Doctor Script
How to view the output of the Node Doctor script depends on whether the output was saved to an Object Storage location or as a plain text file, as follows:
  1. If the Node Doctor script output was saved to an Object Storage location, do one of the following:
     * [Download the response object from the bucket](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects_topic-To_download_an_object_from_a_bucket.htm) where it was saved.
     * Navigate to the Object Storage pre-authenticated request URL.
  2. If the Node Doctor script output was saved as a plain text file, do the following:
    1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Click the instance that you're interested in.
    3. Under **Resources** , click **Run Command**.
    4. Find the command in the list, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **View Command Details**.


## Using SSH to Run the Node Doctor Script 🔗 
If you have SSH access to a managed node, you can run the Node Doctor script using SSH to troubleshoot node issues and generate a support bundle using the Node Doctor script. 
To run the Node Doctor script using SSH, do one of the following:
  * Use the **Worker Node Troubleshooting Guide**. On the **Node Pool Details** page, click **Troubleshoot Nodes** to display the **Worker Node Troubleshooting Guide** , select **SSH Connections** , and follow the instructions.
  * Follow the steps in this section.


  1. Establish an SSH connection with the worker node instance on which you want to run the Node Doctor script.
For detailed instructions to establish an SSH connection, see [Connecting to Managed Nodes Using SSH](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconnectingworkernodesusingssh.htm#Connecting_to_Worker_Nodes_Using_SSH "Find out how to use SSH to connect to worker nodes in node pools in clusters you've created using Kubernetes Engine \(OKE\)."). At a high level, the steps are:
    1. Find out the IP address of the worker node instance that you want to troubleshoot, and make a note of it. 
For example, on the **Cluster Details** page, click **Node Pools** and then click the node pool containing the worker node. Click **Nodes** , and then click the name of the node you are interested in to display the **Instance Details** page. The instance's IP address is shown on the **Instance Information** tab.
    2. In a terminal window, enter `ssh                 opc@<node_ip_address>` to connect to the worker node, where `<node_ip_address>` is the IP address of the worker node instance that you made a note of earlier. For example, you might enter:```
ssh opc@192.0.2.254
```
If the SSH private key is not stored in the file or in the path that the ssh utility expects (for example, the ssh utility might expect the private key to be stored in ~/.ssh/id_rsa), you must explicitly specify the private key filename and location. For more information, see [Connecting to Managed Nodes Using SSH](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconnectingworkernodesusingssh.htm#Connecting_to_Worker_Nodes_Using_SSH "Find out how to use SSH to connect to worker nodes in node pools in clusters you've created using Kubernetes Engine \(OKE\).").
  2. In the terminal window in which you have established the SSH connection with the worker node instance, enter one of the following commands:
     * `sudo /usr/local/bin/node-doctor.sh --check` to print troubleshooting output that identifies potential problem areas, with links to documentation to address those areas.
     * `sudo /usr/local/bin/node-doctor.sh --generate` to gather system information in a bundle. My Oracle Support (MOS) provides instructions to upload the bundle to a support ticket.


## Downloading, Installing, and Updating the Node Doctor Script 🔗 
Worker nodes created from July 19, 2021 already have the Node Doctor script pre-installed.
Worker nodes created before July 19, 2021 do not have the Node Doctor script pre-installed. To run the Node Doctor script on such a worker node, you must download and install the script. To download and install the Node Doctor script, you must have SSH access to the worker node. 
**Note** Periodically, Oracle releases new versions of the Node Doctor script. Before running the Node Doctor script for the first time (even on worker nodes created after July 19, 2021), follow the final step in the instructions below to update the script to the latest version. It's also recommended good practice to update the Node Doctor script from time to time.
To download, install, and update the Node Doctor script on a managed node:
  1. Establish an SSH connection with the worker node.
For detailed instructions to establish an SSH connection, see [Connecting to Managed Nodes Using SSH](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconnectingworkernodesusingssh.htm#Connecting_to_Worker_Nodes_Using_SSH "Find out how to use SSH to connect to worker nodes in node pools in clusters you've created using Kubernetes Engine \(OKE\)."). At a high level, the steps are:
    1. Find out the IP address of the worker node instance that you want to troubleshoot, and make a note of it. 
For example, on the **Cluster Details** page, click **Node Pools** and then click the node pool containing the worker node. Click **Nodes** , and then click the name of the node to display the **Instance Details** page. The instance's IP address is shown on the **Instance Information** tab.
    2. In a terminal window, enter `ssh opc@<node_ip_address>` to connect to the worker node, where `<node_ip_address>` is the IP address of the worker node that you made a note of earlier. For example, you might enter:```
ssh opc@192.0.2.254
```
If the SSH private key is not stored in the file or in the path that the ssh utility expects (for example, the ssh utility might expect the private key to be stored in ~/.ssh/id_rsa), you must explicitly specify the private key filename and location. For more information, see [Connecting to Managed Nodes Using SSH](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconnectingworkernodesusingssh.htm#Connecting_to_Worker_Nodes_Using_SSH "Find out how to use SSH to connect to worker nodes in node pools in clusters you've created using Kubernetes Engine \(OKE\).").
  2. In the terminal window in which you have established the SSH connection with the worker node, download and install the Node Doctor script in the `/usr/local/bin` directory by entering:```
sudo curl -s -X GET https://objectstorage.<region-name>.oraclecloud.com/n/odx-oke/b/public/o/artifacts/prd/workernode/14d06c9-431/node-doctor --output /usr/local/bin/node-doctor.sh
```

where `<region-name>` is the region in which the cluster is located. For example:
Copy
```
sudo curl -s -X GET https://objectstorage.us-ashburn-1.oraclecloud.com/n/odx-oke/b/public/o/artifacts/prd/workernode/14d06c9-431/node-doctor --output /usr/local/bin/node-doctor.sh
```

Before running the Node Doctor script for the first time, complete the next step. 
  3. When the Node Doctor script has been downloaded and installed on the worker node, get the latest version of the Node Doctor script by entering:
```
sudo /usr/local/bin/node-doctor.sh --update
```

It's recommended good practice to keep the Node Doctor script up-to-date by running the above command from time to time.


You can now use the Node Doctor script to troubleshoot worker node issues.
Was this article helpful?
YesNo


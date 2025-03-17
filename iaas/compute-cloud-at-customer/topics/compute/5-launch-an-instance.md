Updated 2025-01-27
# Task 5: Launch an Instance
In this task, launch an instance with an image and a shape.
A compute instance is a virtual machine (VM), which is an independent computing environment that runs on top of physical hardware. The virtualization makes it possible to run multiple compute instances that are isolated from each other.
A shape describes the instance resources such as the number of CPUs, amount of memory, and network resources. In a production environment, you would select a shape that best suits workload and application requirements for the instance.
For more information about instances and instance components, see these topics:
  * [Images for Compute Cloud@Customer Instances](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/images/images.htm#images "On Compute Cloud@Customer, an image is a template of a virtual hard drive. The image provides the OS and other software for a compute instance. You specify an image to use when you create a compute instance.")
  * [Compute Shapes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/compute-shapes.htm#compute-shapes "A shape is a template that determines the type and amount of resources that are allocated to a compute instance. Compute Cloud@Customer offers a choice between a flexible shape for generic workloads, and dedicated shapes for GPU-accelerated workloads.")
  * [Working with Instances](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/working-with-instances.htm#working-with-instances "On Compute Cloud@Customer, you can create compute instances as needed to meet your compute and application requirements. After you create an instance, you can access it securely from your computer, restart it, attach and detach volumes, and delete it.")


Avoid entering confidential information in names and tags.
  1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
  2. On the **Instances** page, click **Create Instance**.
  3. In the **Launch Instance** dialog box, enter the following information:
     * **Name:** Enter a descriptive name for your compute instance.
     * **Create in Compartment:** Select the Sandbox compartment.
     * **Fault Domain:** Leave the default set to "Automatically select the best fault domain."
     * **Source Image:**
       * **Source Type:** Select Platform Image.
       * **List of images:** Select an Oracle Linux image.
     * **Shape:** Select the VM.PCAStandard.E5.Flex shape, and configure the number of OCPUs and memory. For this temporary instance, set the OCPU value to 1, and memory to 16.
     * **Boot Volume:** Leave the check box empty so that the default boot volume size is created.
     * **Subnet:**
       * **VCN:** Select the VCN you created.
       * **Subnet:** Select the subnet you created.
     * **Public IP Address:** Ensure the check box is checked so that a public IP address is assigned to the instance.
     * **Private IP Address:** Leave the field blank.
     * **Hostname:** You can leave this field blank or enter a hostname.
     * **SSH Keys:** Do one of the following to provide your public SSH key:
       * Click inside the Drag and Drop box to open a file browser and select the file.
       * Drag the file from your file browser listing and drop the file on the Drag and Drop box.
       * Select Paste the public keys, copy your public SSH key text, and paste the text into the field.
     * **Initialization Script:** Leave this area as is.
     * **Network Security Group:** Leave the checkbox clear.
     * **Instance Options:** Don't select **Leave the Legacy Instance Metadata Service Endpoints Disabled**
     * **Availability configuration:** Leave this area as is.
     * **Tagging:** Leave blank. This tutorial doesn't use tags.
  4. Click **Create Instance**.
  5. Monitor the state of the instance.
The state is displayed under the icon of the object. 
Your instance begins in the PROVISIONING state. After the instance is in the RUNNING state, you can connect to it.


**Perform the next task:**
[Task 6: Get the Instance IP Address](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/6-get-the-instance-ip-address.htm#_6-get-the-instance-ip-address "You connect to the instance using SSH with the instance IP address.")
Was this article helpful?
YesNo


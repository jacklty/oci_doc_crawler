Updated 2025-01-23
# Preinstalling the Oracle Cloud Development Kit
Provision a compute instance with the Oracle Cloud Development Kit preinstalled and ready to use.
## What's Included 🔗 
The Oracle Cloud Development Kit template preinstalls the following Oracle Cloud Infrastructure items on the Compute instance: 
  * [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm)
  * [Terraform Provider](https://docs.oracle.com/iaas/Content/dev/terraform/home.htm)
  * [Ansible](https://docs.oracle.com/iaas/Content/API/SDKDocs/ansible.htm) (includes OCI Ansible modules)
  * The following SDKs:
    * [Go](https://docs.oracle.com/iaas/Content/API/SDKDocs/gosdk.htm#SDK_for_Go)
    * [Java](https://docs.oracle.com/iaas/Content/API/SDKDocs/javasdk.htm#SDK_for_Java)
    * [Python](https://docs.oracle.com/iaas/Content/API/SDKDocs/pythonsdk.htm#SDK_for_Python)
  * Git: Use the provided Git command line tool to access any Git-related version control systems, such as Bitbucket, GitHub, and GitLab.


[Instance principal authorization](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/devtools.htm#auth) is set up for installed items and the provisioned Compute instance. An upgrade script is also included.
## Steps for Using the Oracle Cloud Development Kit 🔗 
### To provision an instance with the development kit 🔗 
  1. Launch the **Create stack** page for the Oracle Cloud Development Kit template by selecting this button:
[![Deploy to Oracle Cloud](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Images/deploy-to-oracle-cloud.svg)](https://cloud.oracle.com/resourcemanager/stacks/create?preSelectedSolutionId=oci-dev-tools)
[Alternative steps from the Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/devtools.htm)
    1. On the **Stacks** list page, select **Create stack**. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/list-stacks.htm).
    2. In the **Create stack** page, select **Template**.
    3. Under **Stack configuration** , select **Select template**.
    4. In the **Browse templates** panel, select **Architecture**.
    5. Select **Oracle Cloud development kit**.
**Note** You might need to go to your home region before the template is available for selection.
The focus changes back to the **Create stack** page and the Oracle Cloud Development Kit template is selected.
  2. [Follow the prompts to save your new stack and provision the instance](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/devtools.htm)
    1. In the **Create stack** page, enter a **Name** for the new stack (or accept the default name provided). Avoid entering confidential information.
    2. Optionally enter a **Description**. 
    3. From the **Create in compartment** drop-down, select the compartment where you want to create the stack. 
A compartment from the list scope is set by default.
    4. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    5. Select **Next**. 
The **Configure variables** panel displays the following variables:
       * **Instance Shape** : Select the shape you want to use for the Compute instance.
       * **Auto-generate SSH key pair** : Either generates an SSH key pair or allows you to upload a public key.
         * Enabled (selected): Automatically generates an SSH key pair for accessing the instance. The private key is stored in the Terraform state file. You'll use the private key later to connect to the instance.
**Important** Do not use this option in production. The Terraform state file containing the private key is visible to anyone with access to the created stack.
         * Disabled (cleared): Allows you to upload a public key. No private key is stored. Keep the corresponding private key in a safe location. You'll use the private key later to connect to the instance.
For instructions on generating SSH key pairs, see [Managing Key Pairs on Linux Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/managingkeypairs.htm).
       * **Compute instance to access all resources at tenancy level** : Controls the level used for the [dynamic group policy](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm), which determines what resources are accessible by users of the Compute instance.
         * Enabled (selected): Tenancy level for access to all resources in the tenancy.
         * Disabled (cleared): Compartment level for access to all resources in the same compartment as the instance.
    6. Select **Next**.
    7. In the **Review** panel, verify your stack configuration.
    8. Select the check box for **Run apply**.
This option automatically provisions the instance on stack creation.
    9. Select **Create** to create your stack and automatically provision the instance.
The new stack appears in the Stack Details page. Resource Manager runs the Apply action on the new stack, starting the process to provision the instance.
The new apply job is listed under **Jobs**. Monitor its status: "Succeeded" indicates that the job has completed. While the job runs, or after it finishes, you can [download its log file](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs.htm#top "View console logs for a job in Resource Manager.").
Once the instance is provisioned (indicated by a "Succeeded" status for the apply job), installation of the development kit items begins. The installation process takes a few minutes. If you connect to the instance before the installation finishes, then a warning message indicates that the installation is still in process. Once the items are installed on the instance, you can immediately use them.
    10. To view the Terraform state file (shows the state of your resources after running the job), select the apply job ([get its details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job.htm#top "Get the details of a job in Resource Manager. You can view name, type, status, and other key information about jobs for a specific compartment or stack. For configurations stored in Git, job details include the relevant commit identifier.")) and then select **View state** under **Resources**.
Optionally select **Show changes in this version**.


Congratulations! You have provisioned a Compute instance with the Oracle Cloud Development Kit already installed and ready to use. You can now [connect to the instance](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/devtools.htm#toconnect) and [use the development kit](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/devtools.htm#touse).
[To connect to your newly created instance](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/devtools.htm)
Run the following command:
```
ssh -i <private-key> opc@<compute-instance-public-ip>
```

<private-key> is the private key associated with the instance you provisioned from the stack created using the **Oracle Cloud Developer Tools** template.
<compute-instance-public-ip> is the IP address of the instance. 
[To retrieve the associated private key and IP address](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/devtools.htm)
  1. Go to the **Stack details** page for your newly provisioned instance: 
    1. Open the **navigation menu** and select **Developer Services**. Under **Resource Manager** , select **Stacks**.
    2. Select the name of the stack to display its details page.
  2. Select the **Application information** tab.
  3. Copy the value for **Compute Instance Public IP**.
  4. For the private key, follow the steps that correspond to the key option you selected while creating your stack: 
     * If you enabled **Auto-generate SSH key pair** , then retrieve the generated private key: Copy the value for **Generated Private Key for SSH Access**.
     * If you disabled **Auto-generate SSH key pair** , then reference the full path and name of the file that contains the private key corresponding to the public key that you uploaded while creating the stack. 
**Note** When you connect to your instance, the private key file permissions are validated. For security, your private key must be accessible by the owner only; otherwise, you won't be allowed to connect to the instance. (Owner write permissions are required for you to add the private key to the file.) For Unix or Linux, use the command `chmod 600 (-rw-------)`.


For general information about connecting to Compute instances, see [Connecting to an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/accessinginstance.htm).
Once connected to your instance, you can [use the installed development kit](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/devtools.htm#touse).
[To use the installed development kit](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/devtools.htm)
See the following examples:
  * CLI: See [Using the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#Using_the_CLI)
Usage: See [Easy Provisioning](https://blogs.oracle.com/linux/easy-provisioning-of-cloud-instances-on-oracle-cloud-infrastructure-with-the-oci-cli), [CLI Updates](https://blogs.oracle.com/developers/updates-to-oracle-cloud-infrastructure-cli)
  * [Terraform Provider](https://github.com/oracle/terraform-provider-oci/tree/master/examples)
Usage: See [Terraform Provider](https://docs.oracle.com/iaas/Content/dev/terraform/home.htm).
  * [Ansible](https://github.com/oracle/oci-ansible-collection/tree/master/samples) (includes OCI Ansible modules)
Usage: See [Writing a Sample Playbook](https://docs.oracle.com/iaas/Content/API/SDKDocs/ansiblegetstarted.htm#writeSamplePlaybook).
  * SDKs:
    * [Go](https://github.com/oracle/oci-go-sdk/tree/master/example)
Usage: See <https://godoc.org/github.com/oracle/oci-go-sdk>
    * [Java](https://github.com/oracle/oci-java-sdk/tree/master/bmc-examples)
Usage: See [Concepts](https://docs.oracle.com/iaas/Content/API/SDKDocs/javasdkconcepts.htm).
    * [Python](https://github.com/oracle/oci-python-sdk/tree/master/examples)
Setup and usage: See [Client-Side Encryption](https://docs.oracle.com/iaas/Content/API/SDKDocs/pythonsdk.htm#encryption).
Setup and usage for open source SDKs: See [Open Source SDKs](https://blogs.oracle.com/developers/open-source-sdks-for-oracle-bare-metal-cloud-services)
  * Git: Use the provided Git command line tool to access any Git-related version control systems, such as Bitbucket, GitHub, and GitLab. 
Usage: To get help on using Git, access the terminal on your new Compute instance and run `git --help`.


[To upgrade the installed development kit](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/devtools.htm)
  1. [Connect to the instance that you provisioned from the **Oracle Cloud development kit** template.](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/devtools.htm#toconnect)
  2. Run the upgrade command:
Command
CopyTry It
```
update-kit.sh
```



## Preconfigured Authorization 🔗 
Instance principal authorization is set up for installed development kit items and the provisioned compute instance. The template provides the following preconfiguration:
  * A [dynamic group](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm)
  * An [IAM policy](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm), with all resource access determined by stack configuration (either tenancy or compartment level)
  * Environment variables set in `.bashrc` on the Compute instance for CLI, Terraform, and Ansible


For more information about instance principal authorization, see [Calling Services from an Instance](https://docs.oracle.com/iaas/Content/Identity/callresources/callingservicesfrominstances.htm).
Was this article helpful?
YesNo


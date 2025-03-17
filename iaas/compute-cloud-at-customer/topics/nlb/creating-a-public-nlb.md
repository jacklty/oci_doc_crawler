Updated 2024-08-06
# Creating a Public NLB
On Compute Cloud@Customer, you can create a public Network Load Balancer (NLB) using the Compute Cloud@Customer Console, CLI, or API.
When creating an NLB, you have two main options:
  1. You can provide minimal information, and then assemble the components of the NLB, such as the backend set or other parameters.
  2. You can provide all information during the NLB creation. 


This topic creates a public NLB with minimal information. After creation, assemble other components to complete the NLB configuration. Other components are added by editing the NLB resources.
You must specify a display name for the NLB. It doesn't have to be unique, and you can change it. Avoid entering confidential information.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/creating-a-public-nlb.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/creating-a-public-nlb.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/creating-a-public-nlb.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Network Load Balancers**.
    2. Click **Create Load Balancer**.
    3. Enter the following information:
       * **Name:** Enter a descriptive name for the NLB. Avoid entering confidential information.
       * **Create in Compartment:** Select the compartment in which to create the NLB.
       * **Visibility Type:** Click **Public Load Balancer**. The NLB receives a public IP address accessible from the internet and acts as a frontend for all incoming traffic.
       * **Select Public IP:** You can select the public IP address from the drop-down menu. If the pull-down menu displays None Available, or if you don't select a public IP from the list, a public IP from the configured range is automatically assigned.
       * **Subnet:** Select the name of the VNC and Subnet from the drop-down menus.
       * **Network Security Group:** You can use the default (the **Enable Network Security Groups** box is cleared), or assign an available NSG to the load balancer. If the choices show None Available, you can add an NSG with the +Add Network Security Group option.
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    4. Click **Create Network Load Balancer**.
  * Use the [oci nlb network-load-balancer create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/network-load-balancer/create.html) command and required parameters to create a new public NLB in the specified compartment.
```
oci nlb network-load-balancer create --compartment-id <compartment_OCID> --display-name <name-of-network-load-balancer> --is-private false --subnet-id <subnet_OCID>
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateNetworkLoadBalancer](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/NetworkLoadBalancer/CreateNetworkLoadBalancer) operation to create a new public NLB in the specified compartment.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


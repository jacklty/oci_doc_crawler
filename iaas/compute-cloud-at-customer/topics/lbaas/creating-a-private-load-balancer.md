Updated 2024-01-18
# Creating a Private Load Balancer
On Compute Cloud@Customer, when creating a load balancer (LB), you have two main options: you can provide minimal information when creating the LB and then add other resources later, or you can provide all of the information when creating the LB.
This topic creates a private load balancer with minimal information. You need to assemble other components to complete the LB after creation. These are added by editing the LB resources.
For access control reasons, you must select the compartment where you want the LB to reside. The load balancer doesn't have to be in the same compartment as the VCN or backend set. If you aren't sure which compartment to use, put the load balancer in the same compartment as the VCN.
You must specify a display name for the load balancer. It doesn't have to be unique, and you can change it.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-a-private-load-balancer.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-a-private-load-balancer.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-a-private-load-balancer.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. Click **Create Load Balancer**.
    3. Enter the following information:
       * **Name:** Enter a descriptive name for the LB.
Avoid entering confidential information.
       * **Create in Compartment:** Select the compartment in which to create the LB.
       * **Visibility Type:** Click **Private Load Balance** r. The LB receives a private IP address from the hosting subnet. The LB acts a front end for internal incoming traffic visible only within the VCN.
       * **Subnet:** Select the name of the VNC and Subnet for the LB from the pull-down menus.
       * **Network Security Group:** You can use the Default (**Enable Network Security Groups box** is cleared), or assign an available NSG. If the choices show **None Available** , you can add an NSG with the **+Add Network Security Group** option.
    4. Click **Create Load Balancer**. 
    5. To display the details of the new LB, click view the LB.
  * Use the [oci lb load-balancer create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/load-balancer/create.html) command and required parameters to create a private load balancer.
Copy
```
oci lb load-balancer create --compartment-id  _**compartment_OCID**_ \
--display-name _**name-of-load-balancer**_ --is-private _true_ \ 
--shape-name 400Mbps --subnet-ids _**[subnets_complex_ type]**_
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateLoadBalancer](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/LoadBalancer/CreateLoadBalancer) operation to create a load balancer.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


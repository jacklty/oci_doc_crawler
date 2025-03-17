Updated 2024-01-18
# Creating a Load Balancer Virtual Hostname
On Compute Cloud@Customer, a virtual hostname is associated with a load balancer (LB) and used by one or more listeners. Hostnames associated with a listener correspond to the backend set of that listener. The backend set routes traffic to specific backends which host different applications. 
Virtual hostnames simplify the construction of the hostnames associated with listeners and backend servers because virtual hostnames can use wild card asterisks (*) at the start or end of the hostname. Listeners detect a hostname pattern that matches the virtual hostname patterns created.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-a-load-balancer-virtual-hostname.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-a-load-balancer-virtual-hostname.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-a-load-balancer-virtual-hostname.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of the LB for which you want to create the virtual hostname.
    4. Under **Resources** , click **Hostnames**. 
    5. Click **Create Hostname**.
    6. In the Load Balancer Create Hostname dialog box, enter the following information:
       * **Name:** Enter a name for the virtual hostname. For example, my_virtual_hostname. 
Avoid entering confidential information
       * **Hostname:** Enter the virtual hostname. For example, *example.com.
**Note** Both fields are required.
    7. Click **Create Hostname**. 
  * Use the [oci lb hostname create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/hostname/create.html) command and required parameters to create a virtual hostname associated with a load balancer.
Copy
```
oci lb hostname create --hostname  _**virtual-hostname**_ --load-balancer-id _**load-balancer_OCID**_ \
--name _**virtual-hostname-friendly-name**_
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * This task isn't available in the API. 
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo


Updated 2024-12-16
# Workload Cluster Network CIDR Ranges
Review the example CIDR ranges used for OKE network resources on Compute Cloud@Customer. 
Throughout this documentation, variables are used to represent CIDR ranges for instances in different subnets. The following table lists the CIDR variables and example values. Change these example values as necessary for your environment. The [IP Subnet Calculator on Calculator.net](https://www.calculator.net/ip-subnet-calculator.html) is one tool for finding all available networks for a given IP address and prefix length.
Variable Name |  Description |  Example Value  
---|---|---  
` ** _vcn_cidr_ ** ` |  VCN CIDR range |  172.31.252.0/23  
` ** _worker_cidr_ ** ` |  Worker subnet CIDR |  172.31.253.0/24  
` ** _workerlb_cidr_ ** ` |  Worker load balancer subnet CIDR |  172.31.252.0/25  
` ** _kmi_cidr_ ** ` |  OKE control plane subnet CIDR |  172.31.252.224/28  
` ** _kmilb_cidr_ ** ` |  OKE control plane load balancer subnet CIDR |  172.31.252.240/28  
` ** _kube_client_cidr_ ** ` |  CIDR for clients that are allowed to contact the Kubernetes API server |  10.0.0.0/8  
**What's Next:**
Depending on how you want to create the network resources, see one of the following sections:
  * Use Terraform scripts to automate the creation of the network resources. See [Example Terraform Scripts for Network Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/example-terraform-scripts-for-network-resources.htm#example-terraform-scripts-for-network-resources "On Compute Cloud@Customer, you can use Terraform scripts to automate the creation of OKE network resources.").
  * Begin to create the network resources using the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure."), CLI, or API. See [Configuring OKE Network Resources Individually](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/configuring-network-resources-individually.htm#configuring-network-resources-individually "On Compute Cloud@Customer, you can create the required OKE network resources individually using the Compute Cloud@Customer Console, CLI, or API.").


Was this article helpful?
YesNo


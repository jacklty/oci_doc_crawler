Updated 2024-12-16
# Workload Cluster Network Ports
Learn about the required ports for OKE on Compute Cloud@Customer. 
The following table lists ports that are used by workload clusters. These ports must be available to configure workload cluster networking. You might need to open additional ports for other purposes.
All protocols are TCP. All port states are Stateful. Port 6443 is the port used for the Kubernetes API and is also referred to as `kubernetes_api_port` in this guide.
See also the table in [Network Port and Protocol Matrix](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/security/network-port-and-protocol-matrix.htm#network-port-and-protocol-matrix "Compute Cloud@Customer requires access permissions to be granted for certain IP addresses, ports, and protocols.").
Source IP Address |  Destination IP Address |  Port |  Description  
---|---|---|---  
bastion host: `**_vcn_cidr_**` |  Worker nodes subnet: `**_worker_cidr_**` |  22 |  Outbound connections from the bastion host to the worker CIDR.  
bastion host: `**_vcn_cidr_**` |  Control plane subnet: `**_kmi_cidr_**` |  22 |  Outbound connections from the bastion host to the control plane nodes.  
Worker nodes subnet: `**_worker_cidr_**` |  yum repository |  80 |  Outbound connections from the worker CIDR to external applications.  
Worker nodes subnet: `**_worker_cidr_**` |  Secure yum repository |  443 |  Secure outbound traffic from the worker CIDR to external applications.  
Worker nodes subnet: `**_worker_cidr_**` |  Container registry |  5000 |  Outbound connections from the worker CIDR to the container registry.  
Worker nodes subnet: `**_worker_cidr_**` |  Control plane subnet: `**_kmi_cidr_**` |  6443 |  Outbound connections from the worker CIDR to the Kubernetes API. This is necessary to allow nodes to join through either a public IP address on one of the nodes or the load balancer public IP address.  
Worker nodes subnet: `**_worker_cidr_**` |  Control plane load balancer |  6443 |  Inbound connections from the worker CIDR to the Kubernetes API.  
CIDR for clients: `**_kube_client_cidr_**` |  Control plane load balancer |  6443 |  Inbound connections from clients to the Kubernetes API server.  
Worker nodes subnet: `**_worker_cidr_**` |  Control plane subnet: `**_kmi_cidr_**` |  6443 |  Private outbound connections from the worker CIDR to `kubeapi` on the control plane subnet.  
` ** _kube_client_cidr_ ** ` |  Worker nodes subnet: `**_worker_cidr_**` | 30000-32767 |  Inbound traffic for applications from Kubernetes clients.  
**What's Next:**
Review the example CIDR ranges used in this documentation to configure network resources. See [Workload Cluster Network CIDR Ranges](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/workload-cluster-network-cidr-ranges.htm#workload-cluster-network-cidr-ranges "Review the example CIDR ranges used for OKE network resources on Compute Cloud@Customer.").
Was this article helpful?
YesNo


Updated 2024-12-16
# Configuring SR-IOV for Virtual Networking
On Compute Cloud@Customer, single root I/O virtualization (SR-IOV) technology enables instances to achieve low latency and high throughput simultaneously on 1 or more physical links. 
Compute Cloud@Customer supports up to 127 Virtual Functions (VFs) per compute node. 
This section describes how to configure SR-IOV networking.
  1. Ensure you have the OraclePCA tag networkType VFIO defined on the system. See [Creating OraclePCA Tags](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/creating_oraclepca_tags.htm#creating_oraclepca_tags "On Oracle Compute Cloud@Customer you can use the OraclePCA tag namespace to enable resource attributes that aren't available as CLI options or API attributes.").
**Note** The "networkType": "VFIO" tag can't be changed or removed from a VCN or DRG. The only way to remove this tag is to delete the VCN or DRG.
  2. Create a VCN with SR-IOV functionality enabled.
Create a VCN and add an OraclePCA tag with the following values, see [Creating a VCN](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-vcn.htm#creating-a-vcn "On Compute Cloud@Customer, a virtual cloud network \(VCN\) a virtual, private network that closely resembles a traditional network. VCNs can be further divided into IP subnets. VCNs can communicate with each other through various types of gateways, each type intended for a particular purpose."):
     * _Tag Namespace:_ Enter "OraclePCA"
     * _Key:_ Enter "networkType"
     * _Value:_ Enter "VFIO"
You must create a VCN with SR-IOV support enabled, you can't convert an existing VCN to include SR-IOV functionality.
  3. If you plan to use a DRG in your SR-IOV configuration, you must create a DRG with SR-IOV functionality. Only SR-IOV DRGs can attach to SR-IOV VCNs.
Create a DRG and add an OraclePCA tag with the following values, see [Creating a Dynamic Routing Gateway](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-dynamic-routing-gateway.htm#creating-a-dynamic-routing-gateway "On Compute Cloud@Customer, a DRG is the equivalent of a general purpose router. A DRG is used to connect a VCN to the data center's IP address space. The router is configured separately from the VCNs, at the compartment level and is not required to be in the same compartment as the VCN \(but it typically is\)."):
     * _Tag Namespace:_ Enter "OraclePCA"
     * _Key:_ Enter "networkType"
     * _Value:_ Enter "VFIO"
Attach the SR-IOVs VCNs to the DRG.
  4. Prepare an instance for SR-IOV functionality.
    1. Create and launch an instance. See [Creating an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance.htm#creating-an-instance "On Compute Cloud@Customer, you can create an instance using the Compute Cloud@Customer Console, CLI, and API.").
    2. Create and attach a secondary VNIC to the instance to use as the SR-IOV network interface. The primary VNIC of the instance cannot be the SR-IOV VNIC. See [Creating and Attaching a Secondary VNIC](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-and-attaching-a-secondary-vnic.htm#creating-and-attaching-a-secondary-vnic "On Compute Cloud@Customer, you can add more VNICs to an instance.").
    3. Configure the network bond interfaces, including the secondary IP address on a SR-IOV bond port, using the `configure_vfio` script provided in the Oracle blog _Automating SR-IOV/VFIO bond creation on Private Cloud Appliance and Compute Cloud@Customer_ available at <https://blogs.oracle.com/oracle-systems/>.


Was this article helpful?
YesNo


Updated 2024-10-16
# Network Performance
The content in the sections below apply to Performance 2 Service Level Agreement for Oracle Cloud Infrastructure – Compute within **Section 3.6** of the Oracle PaaS and IaaS Public Cloud Services Pillar documentation. You can download a PDF from the [Oracle Cloud Infrastructure Service Level Agreement (SLA)](https://www.oracle.com/cloud/sla/) page.
Oracle Cloud Infrastructure provides a service-level agreement (SLA) for network throughput between instances in the same availability domain in a Virtual Cloud Network (VCN). You might think of this as a measurement of LAN performance.
**Important** This SLA applies only to bare metal instances. 
If your VCN isn't meeting the bandwidth SLA, ensure that the CPU on the instance isn't loaded heavily with other services or applications. Confirm this using a a utility such as `top` to look at the average CPU utilization. It should be less than one.
To meet the SLA, the network throughput for instances within the same availability domain and VCN must be at least 90% of the stated maximum for at least 99.9% of the billing month. Network throughput is measured in megabits per second (Mbps) or gigabits per second (Gbps).
For information about the average network round-trip latency between regions, see [Inter-Region Latency](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/inter_region_latency.htm#inter_region_latency "View the Inter-Region Latency dashboard in the Console. The dashboard provides the average network round-trip latency \(round-trip time or RTT\) for all pairs of regions in an Oracle Cloud Infrastructure realm. In realms with only one region, the Inter-Region Latency dashboard isn't available.").
## Testing Methodology 🔗 
Launch two bare metal instances in the same availability domain and VCN. Install and run the `iperf3[](https://iperf.fr/)` utility, with one instance as server and the other as client. Look at the `iperf3` bandwidth results to determine your VCN's network throughput.
  1. Launch two bare metal instances in the same availability domain in a single VCN. Designate one as the server and the other as the client. For launch instructions, see [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).
  2. Install `iperf3` on both instances. Example Linux command:
Copy
```
sudo yum install -y iperf3
```

  3. Enable communication to the server instance on TCP port 5201 (for `iperf3`):
    1. For the subnet that the server instance is in, add a rule to the subnet's security list to allow stateless ingress traffic on TCP port 5201 from any source IP address (0.0.0.0/0) and any source port. For instructions, see [Updating Rules in a Security List](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/update-securitylist.htm#update-securitylist "Update the rules used in a security list in a Virtual Cloud Network \(VCN\)."). If you are instead using [network security groups (NSGs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups)) with the instance, add the rule to the instance's NSG.
    2. On the instance itself, open the firewall to allow `iperf3` traffic. Example Linux commands:
**Caution** For instances with an iSCSI boot volume, the following `--reload` command can cause problems. For details and a workaround, see [Instances experience system hang after running firewall-cmd --reload](https://docs.oracle.com/iaas/Content/Compute/known-issues.htm#firewallReload).
Copy
```
sudo firewall-cmd --zone=public --permanent --add-port 5201/tcp
sudo firewall-cmd --reload
```

  4. Start the `iperf3` test:
    1. On the server instance, run `iperf3` in server mode. Example Linux command:
Copy
```
iperf3 -s
```

    2. On the client instance, run `iperf3` in client mode and specify the private IP address of the server instance. Example Linux command:
Copy
```
iperf3 -c <server_instance_private_ip_address>
```

  5. Look at the `iperf3` results on the client instance. The network throughput between the two instances is shown under "Bandwidth" in the last five lines of the client's `iperf3` test output. For example: 
Copy
```
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval     Transfer   Bandwidth    Retr
[ 4] 0.00-10.00 sec XX.YY GBytes NN.NN Gbits/sec 752       sender
[ 4] 0.00-10.00 sec XX.YY GBytes NN.NN Gbits/sec         receiver
iperf Done.

```



### Automated Testing
The script included in [_perf-check.zip_](https://docs.oracle.com/iaas/Content/Resources/Assets/perf-check.zip) automates the commands used in the previous section. To use the script:
  1. Ensure that TCP/UDP port 5201 is open by reviewing the security rules and route tables, making changes if necessary.
  2. Extract the script _perf-check.py_ from the _perf-check.zip_ file.
  3. Start a copy of the script on your server endpoint by entering: 
./perf-check.py server
  4. Start a copy of the script on your client endpoint by entering: 
./perf-check.py client <server address>


The script will produce an archive on both endpoints (default names: _perf-results-client.tar.gz_ and _perf-results-server.tar.gz_). These archives should be provided to Oracle support for further analysis.
**Important** You can use the preceding iperf instructions to test performance between hosts that are not in the same availability domain, or between a host in the VCN and a host in the on-premises network. The instructions can be used to test performance between any two endpoints. For accurate results, when transferring data outside an availability domain, you must add `--parallel 5` at the end of the client connection command. 
Was this article helpful?
YesNo


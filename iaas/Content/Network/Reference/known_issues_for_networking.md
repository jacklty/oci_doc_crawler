Updated 2025-03-10
# Known Issues for Networking
These known issues have been identified in the Networking family of services, including internal connections within a VCN and connectivity to on-premises networks.
See also: [Troubleshooting VCNs and Connectivity](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/troubleshooting.htm#Troubleshooting).
## Active FTP not supported on Windows Instances 🔗  

Details
    The default FTP client provided by Microsoft Windows only supports FTP in active mode, which doesn't work with the Oracle's stateful firewall rules or with instances deployed behind a NAT gateway. 

Workaround
    Oracle recommends that Windows instances use a third-party FTP client running in passive mode.
## CPE Configuration Helper trouble specifying the CPE vendor 🔗  

Details
    
If the following things occur, in the Oracle Console you receive an error that says  _The CPE is missing the vendor information (the device type). Update the CPE and add the vendor information:_
  * You have a CPE that existed before the [CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using_the_CPE_Configuration_Helper) feature was released.
  * You have not yet edited the CPE in the Oracle Console and specified which vendor makes your CPE. 
  * You try to generate the Helper content for the CPE or any IPSec connections that use that CPE.



Workaround
    
Perform the following actions:
  1. In the Oracle Console, view the CPE.
  2. Click **Edit**.
  3. In the **CPE Vendor Information** section, select the vendor that makes your CPE. If you're not sure which vendor makes your CPE, or it's not in the list, select **Other**.
  4. If prompted, select a value for **Platform/Version**. Here are guidelines:
     * Oracle recommends using a route-based configuration if possible.
     * If you do not see your specific CPE platform or version in the list, choose the closest platform/version that predates your CPE version.
  5. Click **Save Changes**. It's important to click this even if you did not change the value for the vendor.


You can then generate the Helper content successfully for the CPE or any IPSec connections that use that CPE.
## Private access issues from your on-premises network to Oracle Analytics Cloud through a service gateway 🔗  

Details
    
If you do _all_ of the following, asymmetric routing can occur for the traffic between your on-premises network and Oracle Analytics Cloud: 
  * Set up your on-premises network with [private access to Oracle services through a service gateway on a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm#Transit_Routing_Private_Access_to_Oracle_Services).
  * Also use the internet or FastConnect public peering for public access to Oracle services.
  * Also use Oracle Analytics Cloud so that it that initiates connection to clients in your on-premises network, and you are not yet using a [Data Gateway](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acmgp/prepare-migrate-oracle-analytics-cloud-classic-instances.html#GUID-F4221878-5446-48D4-A020-48D927FFBD7F) in your network.

_Asymmetric routing_ means that the request traffic and response traffic go over different paths. Here are more details about why asymmetric routing can occur: When Oracle Analytics Cloud initiates connections to clients in your on-premises network, the connection requests must go over a public path (either the internet or FastConnect public peering). However, the response travels over a _private path_ , based on the recommendation in [Routing Preferences for Traffic from An On-premises Network to Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem2.htm#on-prem-to-oracle). 
A workaround is required only if you use Oracle Analytics Cloud so that it initiates connections to clients in your on-premises network, and you are not yet using a Data Gateway in your network. 

Workaround 1 (preferred)
    With Oracle Analytics Cloud, switch from using a Remote Data Connector to a [Data Gateway](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acmgp/prepare-migrate-oracle-analytics-cloud-classic-instances.html#GUID-F4221878-5446-48D4-A020-48D927FFBD7F) .  

Workaround 2
    Configure your customer-premises equipment (CPE) to prefer either an internet or FastConnect public peering path by adding static routes for the [regional source IP address for Oracle Analytics Cloud](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acsom/administer-services-analytics-cloud.html#GUID-736A55EF-A4B2-4A80-B17F-CEB02A37B240). That way, any response traffic to Oracle Analytics Cloud will return on the same path as the incoming connection request. 
## Issues with access to your public instances from Oracle services through a service gateway  🔗  

Details
    
If the route table associated with your public subnet in a VCN includes the following two conflicting route rules, Oracle services might be unable to access your public instances in that subnet. 
  1. Route rule with the **Target Type** set as _internet gateway_.
  2. Route rule with the **Destination Service** set as **All <region> Services in Oracle Services Network** and the **Target Type** set as _service gateway_.

The foregoing two route rules can lead to asymmetric routing when Oracle services initiate connections to public instances in your VCN. Oracle Cloud Infrastructure does not support these rules simultaneously within the same route table. Oracle has updated the service APIs and the Console to disable support for this configuration.  

Workaround
    
We recommend that you remove the route rule that has the **Destination Service** set as **All <region> Services in Oracle Services Network** and the **Target Type** set as _service gateway_. Revert to the configuration you used before adopting the service gateway for Oracle Services Network. With this change, your public instances retain access to all Oracle services through the internet gateway. Oracle services can continue to access your public instances.
However, your instances in the public subnet can continue to access Object Storage through the service gateway. Update the subnet's route table to include a route rule with **Destination Service** set as **OCI <region> Object Storage** and the **Target** set to the VCN's service gateway.
This known issue applies only to public subnets that have access to an internet gateway. Regarding private subnets: you can still configure a private subnet's route table to provide access to**All <region> Services in Oracle Services Network** or to **OCI <region> Object Storage** through the VCN's service gateway.
##  Access issues for instances to Oracle yum services through service gateway 🔗  

Details
     If you want to use a service gateway with your VCN _without also using an internet gateway or NAT gateway for internet access_ , your instances might not have access to the applicable regional Oracle yum server. There are two possible issues: 
  * Instances created before November 2018 might have their repos pointed to URLs that are not accessible through the service gateway
  * Instances that were not able to contact their local region's yum server before may have fallen back to using yum.oracle.com, which is not accessible through the service gateway

    To use either of the following mitigation strategies, you must have one of the following gateways configured so you can reach out to the region's yum server: service gateway, NAT gateway, or internet gateway.  

Workaround 1 (automated)
    
Try the following automated mitigation. If it fails for some reason, use the manual mitigation method that follows.
Copy the following script the to local system and run it. The script disables existing repos and downloads the repo file, which directs the system to the region's local yum servers accessible through the service gateway.
Copy
```
#!/bin/bash
REPODIR='/etc/yum.repos.d'
REPOS=$REPODIR/*
REGION=$(curl -sfm 3 http://169.254.169.254/opc/v1/instance/ | jq -r '.region' | cut -d '-' -f 2)
VERSION=$(egrep '^VERSION_ID' /etc/os-release | cut -d '"' -f 2 | cut -d '.' -f 1)
REPOURL="http://yum-${REGION}.oracle.com/yum-${REGION}-ol${VERSION}.repo"
echo "Disabling existing repos"
for i in $REPOS
do
 if [[ "$i" != *".disabled" ]]; then
  mv $i $i.disabled
  echo "$i disabled"
 else
  echo "$i repofile already disabled"
 fi
done
yum clean all
echo "Pulling new regional repository file"
wget -q $REPOURL -O "$REPODIR/yum-${REGION}-ol${VERSION}.repo"
retval=$?
if [[ "$retval" -ne 0 ]]; then
 echo "Unable to pull repo file, please run manual steps"
 exit 1
fi
yum makecache fast
```


Workaround 2 (manual)
    
If the automated mitigation fails, you can manually mitigate the issue. Here you disable the existing repo files and pull down the latest repo file from your region's yum server. To identify your instance's region key, look at the region list in [Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).
To disable the existing repo files, navigate to the `/etc/yum.repos.d` directory and rename all files present to include `.disabled` at the end of the file name.
Example: 
```
ls /etc/yum.repos.d ksplice-uptrack.repo.disabled public-yum-ol7.repo.disabled
```

Download the repo file for your region to the local system. The following example uses Ashburn (with region key `iad`). **Replace`iad` with the region key applicable to your instance.**
```
cd /etc/yum.repos.d/
wget http://yum-iad.oracle.com/yum-iad-ol7.repo
chown root:root yum-iad-ol7.repo
yum makecache fast

```

Was this article helpful?
YesNo


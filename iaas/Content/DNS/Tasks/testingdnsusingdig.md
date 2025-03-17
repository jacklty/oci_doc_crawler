Updated 2025-03-10
# Testing DNS Using dig
Use BIND'S Domain Information Groper (dig) command line tool to test against the delegation where the domain is hosted. Immediately see whether changes took place without accounting for the cache or TTL (Time to Live) that you have configured.
**Note** Windows users can download the tool from BIND's [website](https://www.isc.org/downloads/). Use Terminal to access dig on Linux and Macintosh systems.
## Using dig 🔗 
Before using BIND's dig tool, you must access or install dig on the system you use. After you have access to dig, you can use dig to test DNS.
[To access dig (Mac)](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/testingdnsusingdig.htm)
  1. From the `Applications` folder, open the `Utilities` folder, and then select **Terminal**.
  2. When the terminal is open, type a [dig command](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/testingdnsusingdig.htm#use-dig) using a hostname you want to look up.


[To install dig (Windows)](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/testingdnsusingdig.htm)
  1. Go to [ISC's website](https://www.isc.org/downloads/) and download the most current, stable version of BIND.
**Note** BIND supports both 32 and 64 bit Windows systems. Confirm which version of Windows you're using and download the correct version of BIND. View Microsoft's [documentation](http://windows.microsoft.com/windows/which-operating-system) to find which version of Windows you're using.
  2. Extract the downloaded file and install BIND in the following directory: `C:\Program Files\ISC BIND 9`. Select the **Tools Only** checkbox.
  3. After BIND is installed, open the **Control Panel** from the **Windows** menu, and then open **System properties**. 
  4. On the **Advanced** tab, select **Environment Variables**. 
  5. Under **System Variables** , select **Path** , and then select **Edit**.
  6. At the end of the path in the **Edit System Variable** window, add `C:\Program Files\ISC BIND 9\bin`, and then select **OK**.
  7. In the Edit Variables window, select **OK**. In the System properties window, select **OK**.


#### To open the Command Prompt
For Windows versions 8 to10:
  1. Select the **Windows** menu icon.
  2. In the **Search** field, type `CMD`.
  3. Select **Command Prompt**.


For Windows version 7:
  1. On the **Start** menu select **Run**.
  2. Enter `CMD`, and then select **OK**.


[To use dig to test DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/testingdnsusingdig.htm)
  1. Open a terminal (Mac and Linux) or command prompt (Windows).
  2. Type `dig <any hostname>`, and then press **Enter**.


The following information is returned:
[![Screenshot showing the output for dns dig](https://docs.oracle.com/en-us/iaas/Content/DNS/images/dig_dns_results.png)](https://docs.oracle.com/en-us/iaas/Content/DNS/images/dig_dns_results.png)
  * **Question section** : The query made to the nameserver. In this example, we asked for the first available A record for the hostname, `oracle.com`.
  * **Answer section** : The first available answer for the query made to the DNS. In this example, we received the A record containing the IP address 137.254.16.101.
  * **Authority section** : The authoritative nameservers from which the answer to the query was received. These nameservers house the zones for a domain.
  * **Additional section** : More information the resolver might need but not the answer to the query.


## dig Commands 🔗 
Command | Description | Example  
---|---|---  
`dig [hostname]` | Returns any A records found within the queried hostname's zone. | `dig oracle.com`  
`dig [hostname] [record type]` | Returns the records of that type found within the queried hostname's zone.  | `dig oracle.com MX`  
`dig [hostname] +short` | Provides a brief answer, often an IP address. | `dig oracle.com +short`  
`dig @[nameserver address] [hostname]` | Queries the nameserver directly instead of the resolver configured in a local system. | `dig @dnsmaster6.oracle.com`  
`dig [hostname] +trace` | Adding `+trace` instructs dig to resolve the query from the root nameserver downwards and to report the results from each query step. | `dig oracle.com +trace`  
`dig -x [IP address]` | Reverse lookup for IP addresses. | `dig -x 108.59.161.1`  
Was this article helpful?
YesNo


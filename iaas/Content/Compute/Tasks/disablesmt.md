Updated 2024-02-23
# Disabling Simultaneous Multithreading
You can disable simultaneous multithreading (SMT) on your instances through the console or by using CLI commands. 
  * For bare metal instances, optionally [configure advanced BIOS settings](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bios-settings.htm#bios-settings "When you create a bare metal compute instance, you can optionally configure advanced BIOS settings that let you optimize performance. For example, you can disable simultaneous multithreading to optimize the NUMA settings."), such as disabling simultaneous multithreading, disabling cores, or optimizing the NUMA settings. Click **Show advanced BIOS settings** , and then select the options that you want to configure. The settings that are available depend on the shape.
  * For virtual machine instances, if you want to disable simultaneous multithreading, click **Show advanced OCPU options** , and then uncheck **Enable simultaneous multithreading (SMT)**. Simultaneous multithreading is enabled by default.
See [Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service.") for more information.


**Confirming SMT Status**
To confirm the status of SMT on your instance, follow the steps outlined below. The threads per core indicate whether SMT is on or off. If there is one thread per core, SMT is off. If there are two threads per core, SMT is on.
To confirm the SMT status for Linux:
  1. SSH into the instance. 
  2. Input the following to get the IP of the instance:```
$ oci compute instance list-vnics --instance-id 
$ instance_id --query ‘data[0].“public-ip”’
$ ssh opc@“public ip returned above”
```

  3. In the shell of the instance, the return should look something like the example below. In this example, SMT is off.```
% lscpu | grep Thread
Thread(s) per core:  1
```



To confirm the SMT status for Windows:
  1. Remote desktop (RDP) into the instance.
  2. In PowerShell, input the following query:```
Get-WmiObject -class win32_processor | ft NumberofCores,NumberofLogicalProcessors
```

  3. The return should look something like the example below. In this example, SMT is off.```
NumberofCores  NumberofLogicalProcessors
1        1
```



Was this article helpful?
YesNo


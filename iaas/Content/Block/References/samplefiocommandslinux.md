Updated 2023-09-26
# Sample FIO Commands for Block Volume Performance Tests on Linux-based Instances
This topic describes sample FIO commands you can use to run performance tests for the Oracle Cloud Infrastructure Block Volume service on instances created from Linux-based images.
## Installing FIO 🔗 
To install and configure FIO on your instances with Linux-based operating systems, run the commands applicable to the operating system version for your instance.
[Oracle Linux and CentOS](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm)
Run the following command to install and configure FIO for your Oracle Linux or CentOS systems.
  * Oracle Autonomous Linux 8.x, Oracle Linux 8.x, and Oracle Linux Cloud Developer 8:
Copy
```
sudo dnf install fio -y
```

  * Oracle Autonomous Linux 7.x, Oracle Linux 6.x, Oracle Linux 7.x, CentOS 7, and CentOS Stream 8:
Copy
```
sudo yum install fio -y
```



[Ubuntu](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm)
Run the following commands to install and configure FIO for your Ubuntu systems:
Copy
```
sudo apt-get update && sudo apt-get install fio -y
```

This applies to Ubuntu 20.04, Ubuntu 18.04, and Ubuntu Minimal 18.04.
## FIO Commands 🔗 
### IOPS Performance Tests
Use the following FIO example commands to test IOPS performance. You can run the commands directly or create a job file with the command and then run the job file. 
[Test random reads](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm)
Run the following command directly to test random reads:
Copy
```
sudo fio --filename= _device name_ --direct=1 --rw=randread --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name=iops-test-job --eta-newline=1 --readonly
```

In some cases you might see more consistent results if you use a job file instead of running the command directly. Use the following steps for this approach.
  1. Create a job file, fiorandomread.fio, with the following:
Copy
```
[global]
bs=4K
iodepth=256
direct=1
ioengine=libaio
group_reporting
time_based
runtime=120
numjobs=4
name=raw-randread
rw=randread
							
[job1]
filename= _device name_
```

  2. Run the job using the following command:
Copy
```
fio randomread.fio
```



[Test file random read/writes](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm)
Run the following command against the mount point to test file read/writes:
Copy
```
sudo fio --filename=/ _custom mount point_/_file_ --size=500GB --direct=1 --rw=randrw --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name=iops-test-job --eta-newline=1
```

Add both the read IOPS and the write IOPS returned.
[Test random read/writes](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm)
**Caution** Do not run FIO tests with a write workload (`readwrite`, `randrw`, `write`, `trimwrite`) directly against a device that is in use. 
Run the following command to test random read/writes:
Copy
```
sudo fio --filename= _device name_ --direct=1 --rw=randrw --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name=iops-test-job --eta-newline=1
```

Add both the read IOPS and the write IOPS returned.
In some cases you might see more consistent results if you use a job file instead of running the command directly. Use the following steps for this approach.
  1. Create a job file, fiorandomreadwrite.fio, with the following:
Copy
```
[global]
bs=4K
iodepth=256
direct=1
ioengine=libaio
group_reporting
time_based
runtime=120
numjobs=4
name=raw-randreadwrite
rw=randrw
							
[job1]
filename= _device name_
```

  2. Run the job using the following command:
Copy
```
fio randomreadwrite.fio
```



[Test sequential reads](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm)
For workloads that enable you to take advantage of sequential access patterns, such as database workloads, you can confirm performance for this pattern by testing sequential reads.
Run the following command to test sequential reads:
Copy
```
sudo fio --filename= _device name_ --direct=1 --rw=read --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name=iops-test-job --eta-newline=1 --readonly
```

In some cases you may see more consistent results if you use a job file instead of running the command directly. Use the following instructions for this approach:
  1. Create a job file, fioread.fio, with the following:
Copy
```
[global]
bs=4K
iodepth=256
direct=1
ioengine=libaio
group_reporting
time_based
runtime=120
numjobs=4
name=raw-read
rw=read
							
[job1]
filename= _device name_
```

  2. Run the job using the following command:
Copy
```
fio read.fio
```



### Throughput Performance Tests 🔗 
Use the following FIO example commands to test throughput performance.
[Test random reads](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm)
Run the following command to test random reads:
Copy
```
sudo fio --filename= _device name_ --direct=1 --rw=randread --bs=256k --ioengine=libaio --iodepth=64 --runtime=120 --numjobs=4 --time_based --group_reporting --name=throughput-test-job --eta-newline=1 --readonly
```

In some cases you might see more consistent results if you use a job file instead of running the command directly. Use the following steps for this approach.
  1. Create a job file, fiorandomread.fio, with the following:
Copy
```
[global]
bs=256K
iodepth=64
direct=1
ioengine=libaio
group_reporting
time_based
runtime=120
numjobs=4
name=raw-randread
rw=randread
							
[job1]
filename= _device name_
```

  2. Run the job using the following command:
Copy
```
fio randomread.fio
```



[Test file random read/writes](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm)
Run the following command against the mount point to test file read/writes:
Copy
```
sudo fio --filename=/ _custom mount point_/_file_ --size=500GB --direct=1 --rw=randrw --bs=64k --ioengine=libaio --iodepth=64 --runtime=120 --numjobs=4 --time_based --group_reporting --name=throughput-test-job --eta-newline=1 
```

Add both the read MBPs and the write MBPs returned.
[Test random read/writes](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm)
**Caution** Do not run FIO tests with a write workload (`readwrite`, `randrw`, `write`, `trimwrite`) directly against a device that is in use. 
Run the following command to test random read/writes:
Copy
```
sudo fio --filename= _device name_ --direct=1 --rw=randrw --bs=256k --ioengine=libaio --iodepth=64 --runtime=120 --numjobs=4 --time_based --group_reporting --name=throughput-test-job --eta-newline=1
```

Add both the read MBPs and the write MBPs returned.
In some cases you might see more consistent results if you use a job file instead of running the command directly. Use the following steps for this approach.
  1. Create a job file, fiorandomread.fio, with the following:
Copy
```
[global]
bs=256K
iodepth=64
direct=1
ioengine=libaio
group_reporting
time_based
runtime=120
numjobs=4
name=raw-randreadwrite
rw=randrw
							
[job1]
filename= _device name_
```

  2. Run the job using the following command:
Copy
```
fio randomreadwrite.fio
```



[Test sequential reads](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm)
For workloads that enable you to take advantage of sequential access patterns, such as database workloads, you can confirm performance for this pattern by testing sequential reads.
Run the following command to test sequential reads:
Copy
```
sudo fio --filename= _device name_ --direct=1 --rw=read --bs=256k --ioengine=libaio --iodepth=64 --runtime=120 --numjobs=4 --time_based --group_reporting --name=throughput-test-job --eta-newline=1 --readonly
```

In some cases you might see more consistent results if you use a job file instead of running the command directly. Use the following steps for this approach.
  1. Create a job file, fioread.fio, with the following:
Copy
```
[global]
bs=256K
iodepth=64
direct=1
ioengine=libaio
group_reporting
time_based
runtime=120
numjobs=4
name=raw-read
rw=read
							
[job1]
filename= _device name_
```

  2. Run the job using the following command:
Copy
```
fio read.fio
```



### Latency Performance Tests 🔗 
Use the following FIO example commands to test latency performance. You can run the commands directly or create a job file with the command and then run the job file. 
[Test random reads for latency](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm)
Run the following command directly to test random reads for latency:
Copy
```
sudo fio --filename= _device name_ --direct=1 --rw=randread --bs=4k --ioengine=libaio --iodepth=1 --numjobs=1 --time_based --group_reporting --name=readlatency-test-job --runtime=120 --eta-newline=1 --readonly
```

In some cases you might see more consistent results if you use a job file instead of running the command directly. Use the following steps for this approach.
  1. Create a job file, fiorandomreadlatency.fio, with the following:
Copy
```
[global]
bs=4K
iodepth=1
direct=1
ioengine=libaio
group_reporting
time_based
runtime=120
numjobs=1
name=readlatency-test-job
rw=randread
							
[job1]
filename= _device name_
```

  2. Run the job using the following command:
Copy
```
fio fiorandomreadlatency.fio
```



[Test random read/writes for latency](https://docs.oracle.com/en-us/iaas/Content/Block/References/samplefiocommandslinux.htm)
**Caution** Do not run FIO tests with a write workload (`readwrite`, `randrw`, `write`, `trimwrite`) directly against a device that is in use. 
Run the following command directly to test random read/writes for latency:
Copy
```
sudo fio --filename= _device name_ --direct=1 --rw=randrw --bs=4k --ioengine=libaio --iodepth=1 --numjobs=1 --time_based --group_reporting --name=rwlatency-test-job --runtime=120 --eta-newline=1
```

In some cases you might see more consistent results if you use a job file instead of running the command directly. Use the following steps for this approach.
  1. Create a job file, fiorandomrwlatency.fio, with the following:
Copy
```
[global]
bs=4K
iodepth=1
direct=1
ioengine=libaio
group_reporting
time_based
runtime=120
numjobs=1
name=rwlatency-test-job
rw=randrw
							
[job1]
filename= _device name_
```

  2. Run the job using the following command:
Copy
```
fio fioradomrwlatency.fio
```



Was this article helpful?
YesNo


Updated 2023-08-28
# Configuring Object Storage with Flume
Configure Flume to store data from various sources such as TCP, file, stream, and so on to persist in Object Storage.
  1. [Access](https://docs.oracle.com/en-us/iaas/Content/bigdata/hadoop-odh-open.htm#cluster-ambari) Apache Ambari.
  2. From the side toolbar, under **Services** click **Flume**.
  3. Click **Configs**.
  4. Update **flume-conf** with the following parameters:
Copy
```
#list hdfs sources
hdfs_agent.sources = nc_source
hdfs_agent.channels = memchannel
hdfs_agent.sinks = hdfs_write
 
# configure hdfs-agent source
hdfs_agent.sources.nc_source.type = netcat
hdfs_agent.sources.nc_source.bind = 0.0.0.0
hdfs_agent.sources.nc_source.port = 33333
 
# properties of hdfs-Cluster1-sink
hdfs_agent.sinks.hdfs_write.type = hdfs
hdfs_agent.sinks.hdfs_write.hdfs.path = oci://<compartment>@<tenancy>/new
hdfs_agent.sinks.hdfs_write.hdfs.roll.Interval = 30
hdfs_agent.sinks.hdfs_write.hdfs.writeFormat = Text
hdfs_agent.sinks.hdfs_write.hdfs..fileType = DataStream
 
hdfs_agent.channels.memchannel.capacity = 100000
hdfs_agent.channels.memchannel.type = memory
 
hdfs_agent.sources.hdfs_source.channels = memchannel
hdfs_agent.sinks.hdfs_write.channel = memchannel
hdfs_agent.sinks.hdfs_write.hdfs.kerberosPrincipal = flume/<hostname>@<realm>
hdfs_agent.sinks.hdfs_write.hdfs.kerberosKeytab = /etc/security/keytabs/flume.service.keytab
```

  5. Run:
Copy
```
head -n 5 log.txt | nc <hostname> <hdfs_agent.sources.nc_source.port>
```

Flume persists the data from netcat source to Object Storage under the new bucket as configured.


Was this article helpful?
YesNo


Updated 2023-08-28
# Configuring Object Storage with Flink
Flink uses Object Storage as sink for persisting data, which can be achieved by using HDFS connector.
  1. [Access](https://docs.oracle.com/en-us/iaas/Content/bigdata/hadoop-odh-open.htm#cluster-ambari) Apache Ambari.
  2. From the side toolbar, under **Services** click **HDFS**.
  3. Click **Configs**.
  4. View the relevant HDFS connector properties in **core-site.xml** , and then restart HDFS.
  5. To write stream data to Object Storage, run:
Copy
```
export HADOOP_CLASSPATH=`hadoop classpath`;
sudo /usr/odh/current/flink/bin/flink run-application -t yarn-application -yD 
classloader.check-leaked-classloader=false 
-yD security.kerberos.login.keytab=/etc/security/keytabs/smokeuser.headless.keytab 
-yD security.kerberos.login.principal=<ambari-qa-principal> 
/usr/odh/current/flink/bin//../examples/streaming/WordCountStreaming.jar 
--input <object_storage_input_file_location> --output <object_storage_output_file_location>

```

  6. To set Object Storage as sink in Batch mode, run:
Copy
```
export HADOOP_CLASSPATH=`hadoop classpath`;
sudo /usr/odh/current/flink/bin/flink run-application -t yarn-application 
-yD classloader.check-leaked-classloader=false 
-yD security.kerberos.login.keytab=/etc/security/keytabs/smokeuser.headless.keytab 
-yD security.kerberos.login.principal=<ambari-qa-principal> 
/usr/odh/current/flink/bin//../examples/batch/WordCount.jar --input 
<object_storage_input_file_location> --output 
<object_storage_output_file_location> 
```

  7. To use Object Storage for storing savepoints, configure <object_storage_file_location> for the `state.savepoints.dir` parameter.
  8. To use Object Storage for storing checkpoints, configure in the client with specific interval and path to Object Storage,


Was this article helpful?
YesNo


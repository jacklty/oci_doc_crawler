Updated 2023-08-28
# Configuring Object Storage with Kafka
Configure Kafka connect with Object Storage using S3 connector.
  1. Download the [S3 sink connector](https://www.confluent.io/hub/confluentinc/kafka-connect-s3).
  2. Start Kafka connect, ad then copy the zip file to the cluster where kafka-connect is installed.
  3. Extract the zip file to `/usr/odh/current/kafka-broker/plugins`.
  4. Provide access to Kafka user for plugins folder.
  5. Create a properties file (for example, `connect.properties`) with the `connect` parameter.
  6. Update the `plugin.path` parameter with plugins path, `/usr/odh/current/kafka-broker/plugins`.
  7. Create `connect-log4j.properties` under `/usr/odh/current/kafka-broker/config`.
    1. Create new API keys from the OCI Console. See [Creating an Object Storage API Key for a Cluster](https://docs.oracle.com/en-us/iaas/Content/bigdata/integrated-services-os-create.htm#os-create-key "Create an API key to connect a Big Data Service cluster to Object Storage.").
    2. Generate the access key and secret keys. See [Create Secret Keys](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm#create-secret-key).
  8. Copy the access and secret keys.
  9. Export the following env variables required to access Object Storage.
     * `export AWS_SECRET_KEY=<secret key>`
     * `export AWS_ACCESS_KEY=<access key>`
  10. Start the connect server:
Copy
```
sudo -u kafka sh /usr/odh/current/kafka-broker/bin/connect-distributed.sh /usr/odh/current/kafka-broker/config/connect.properties --bootstrap.servers <broker_hostname>:6667
```

  11. Add the Object Storage server:
`curl`
  12. Verify the connector is running:
Copy
```
source /usr/odh/current/kafka-broker/config/kafka-env.sh ; sudo -u kafka sh /usr/odh/current/kafka-broker/bin/kafka-console-producer.sh --broker-list <broker_hostname>:6667 --topic hdfs-kafka --producer.config /usr/odh/current/kafka-broker/config/server.properties 
```

  13. Create a message and file in Object Storage.


Was this article helpful?
YesNo


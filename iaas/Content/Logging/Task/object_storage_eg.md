Updated 2023-01-04
# Object Storage Example
The following is a logging command example related to Object Storage.
**To create a log group and create a log in Object Storage**
Command
CopyTry It
```
oci logging log-group create --compartment-id <compartment_OCID> 
 --display-name CLITestLogGroup
oci logging log create --display-name object_log_write --log-group-id <log_group_OCID>
 --log-type SERVICE --is-enabled true --configuration file://~/.oci/objectstorage_configuration.json
```

objectstorage_configuration.json:
```
{
 "archiving": {
  "isEnabled": true
 },
 "compartmentId": "ocid1.compartment.oc1..<unique_ID>",         
 "source": [
  {
   "category":"write",
   "parameters": null,
   "resource": "bucket-cli-sample",  
   "service": "objectstorage",    
   "sourceType": "OCISERVICE"
  }
 ]
}
```

Was this article helpful?
YesNo


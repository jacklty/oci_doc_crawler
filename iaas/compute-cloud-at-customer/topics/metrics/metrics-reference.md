Updated 2024-03-19
# Compute Cloud@Customer Metrics Reference
See a list of metrics emitted by Compute Cloud@Customer using the `oci_ccc` metric namespace.
Each metric includes the following dimensions:
  * **RESOURCEID** : The OCID of the Compute Cloud@Customer infrastructure
  * **RESOURCENAME** : The name of the Compute Cloud@Customer infrastructure


Metric Name | Metric Display Name | Unit | Description  | Collection Frequency (minutes) | Dimensions  
---|---|---|---|---|---  
`ComputeOCPUsTotal` | OCPU Total | integer | Total number of OCPUs in the infrastructure | 15  |  `resourceId` `resourceName` `faultDomain` `computeNode`  
`ComputeOCPUsAvailable` | OCPU Available | integer | Number of available OCPUs | 15  |  `resourceId` `resourceName` `faultDomain` `computeNode`  
`ComputeMemoryTotal` | Memory Total | GB | Total amount of compute memory in the infrastructure | 15  |  `resourceId` `resourceName` `faultDomain` `computeNode`  
`ComputeMemoryAvailable` | Memory Available | GB | Amount of available compute memory | 15  |  `resourceId` `resourceName` `faultDomain` `computeNode`  
`StorageSpaceTotal` | Storage Total | GB | Total storage capacity in the infrastructure  | 15  |  `resourceId` `resourceName` `storageNode`  
`StorageSpaceAvailable` | Storage Available | GB | Amount of available storage capacity  | 15  |  `resourceId` `resourceName` `storageNode`  
Was this article helpful?
YesNo


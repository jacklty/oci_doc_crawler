Updated 2024-08-21
# Details for Health Checks
Review advanced details for writing policies to control access to the Health Checks service.
## Resource-Types 🔗 
### Aggregate Resource-Type 🔗 
`health-check-family`
The `health-check-family` aggregate resource-type covers these individual resource-types:
  * `health-check-monitor`
  * `health-check-results`
  * `on-demand-probe`
  * `vantage-points`


### Individual Resource-Types 🔗 
`health-check-monitor`
`health-check-results`
`on-demand-probe`
`vantage-points`
## Supported Variables 🔗 
Health Checks supports all the general variables (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm "Use the following general variables for all requests")), plus the variables listed here. Values in the list can be any valid test type, such as HTTP, HTTPS, and ICMP.
Variable | Variable Type | Comments  
---|---|---  
`target.health-check-monitor.test-type` | String  
`target.on-demand-probe.test-type` | String  
`target.health-check-results.test-type` | String  
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
For example, the `use` verb for the `health-check-monitor` resource-type covers no extra permissions or API operations compared to the `read` verb.
[health-check-monitor](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/healthcheckpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  HEALTH_CHECK_MONITOR_INSPECT |  `ListHttpMonitors` `ListPingMonitors` | none  
read |  _INSPECT +_ HEALTH_CHECK_MONITOR_READ |  `GetHttpMonitor` `GetPingMonitor` | none  
use |  _READ +_ no extra | none | none  
manage |  _USE +_ HEALTH_CHECK_MONITOR_MANAGE HEALTH_CHECK_MONITOR_MOVE |  `CreateHttpMonitor` `DeleteHttpMonitor` `UpdateHttpMonitor` `CreatePingMonitor` `DeletePingMonitor` `UpdatePingMonitor` `ChangeHttpMonitorCompartment` `ChangePingMonitorCompartment` | none  
[health-check-results](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/healthcheckpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  HEALTH_CHECK_RESULTS_INSPECT |  `ListHttpProbeResults` `ListPingProbeResults` | none  
read |  _INSPECT +_ no extra | none | none  
use |  _READ +_ no extra | none | none  
manage |  _USE +_ no extra | none | none  
[vantage-points](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/healthcheckpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | VANTAGE_POINTS_INSPECT | `ListHealthChecksVantagePoints` | none  
read |  _INSPECT +_ no extra | none | none  
use |  _READ +_ no extra | none | none  
manage |  _USE +_ no extra | none | none  
[on-demand-probe](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/healthcheckpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | none | none | none  
read |  _INSPECT +_ no extra | none | none  
use |  _READ +_ no extra | none | none  
manage |  _USE +_ ON_DEMAND_PROBE_MANAGE |  `CreateOnDemandHttpProbe` `CreateOnDemandPingProbe` | none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/permissions.htm#permissions "Permissions are the atomic units of authorization that control a user's ability to perform operations on resources. Oracle defines all the permissions in the policy language.").
API Operation | Permissions Required to Use the Operation  
---|---  
`ListHealthChecksVantagePoints` | VANTAGE_POINTS_INSPECT  
`ChangeHttpMonitorCompartment` | HEALTH_CHECK_MONITOR_MOVE  
`CreateHttpMonitor` | HEALTH_CHECK_MONITOR_MANAGE  
`DeleteHttpMonitor` | HEALTH_CHECK_MONITOR_MANAGE  
`GetHttpMonitor` | HEALTH_CHECK_MONITOR_READ  
`UpdateHttpMonitor` | HEALTH_CHECK_MONITOR_MANAGE  
`ListHttpMonitors` | HEALTH_CHECK_MONITOR_INSPECT  
`CreateOnDemandHttpProbe` | ON_DEMAND_PROBE_MANAGE  
`ListHttpProbeResults` | HEALTH_CHECK_RESULTS_INSPECT  
`ChangePingMonitorCompartment` | HEALTH_CHECK_MONITOR_MOVE  
`CreatePingMonitor` | HEALTH_CHECK_MONITOR_MANAGE  
`DeletePingMonitor` | HEALTH_CHECK_MONITOR_MANAGE  
`GetPingMonitor` | HEALTH_CHECK_MONITOR_READ  
`UpdatePingMonitor` | HEALTH_CHECK_MONITOR_MANAGE  
`ListPingMonitors` | HEALTH_CHECK_MONITOR_INSPECT  
`CreateOnDemandPingProbe` | ON_DEMAND_PROBE_MANAGE  
`ListPingProbeResults` | HEALTH_CHECK_RESULTS_INSPECT  
Was this article helpful?
YesNo


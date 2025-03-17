Updated 2023-03-21
# Process Overview for Calling Services from Compute Instances
Process flow for setting up and using Compute instances.
The following steps summarize the process flow for setting up and using Compute instances as principals. The subsequent sections provide more details.
  1. Create a [dynamic group](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm#Managing_Dynamic_Groups). In the dynamic group definition, you provide the matching rules to specify which Compute instances you want to allow to make API calls against services. 
  2. Create a policy granting permissions to the dynamic group to access services in your tenancy (or compartment).
  3. A developer in your organization configures the application built using the Oracle Cloud Infrastructure SDK to authenticate using the instance principals provider. The developer deploys the application and the SDK to all the Compute instances that belong to the dynamic group.
  4. The deployed SDK makes calls to Oracle Cloud Infrastructure APIs as allowed by the policy (without needing to configure API credentials).
  5. For each API call made by an instance, the [Audit service](https://docs.oracle.com/iaas/Content/Audit/Concepts/auditoverview.htm) logs the event, recording the OCID of the instance as the value of `principalId` in the event log.


Was this article helpful?
YesNo


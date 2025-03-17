Updated 2024-08-06
# Using Schedule-Based Autoscaling
On Compute Cloud@Customer, 
Autoscaling instance pools enables you to effectively manage instance resource use.
An instance pool can have an autoscaling configuration and policies that scale the instance pool in the following ways according to a schedule:
  * Scale out: add instances
  * Scale in: remove instances
  * Lifecycle or power action: stop, start, or reboot instances


When an instance pool scales out or scales in, instances are created or terminated as described in [Updating an Instance Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-an-instance-pool.htm#updating-an-instance-pool "On Compute Cloud@Customer, when you update an instance pool, you can change the name of the pool, the size of the pool, the instance configuration that's used to create new instances, the fault domains, VCN, and subnet.").
Policies define the schedule for autoscaling and the specific actions to take. An autoscaling configuration can have up to 50 schedule-based autoscaling policies, each with a different schedule and target pool size or lifecycle action. An instance pool can have only one autoscaling configuration.
If you manually change the pool size or lifecycle state as described in [Updating an Instance Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-an-instance-pool.htm#updating-an-instance-pool "On Compute Cloud@Customer, when you update an instance pool, you can change the name of the pool, the size of the pool, the instance configuration that's used to create new instances, the fault domains, VCN, and subnet.") and [Stopping and Starting Instances in an Instance Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/stopping-and-starting-instances-in-an-instance-pool.htm#stopping-and-starting-instances-in-an-instance-pool "On Compute Cloud@Customer, performing operations such as reset or stop on the pool object performs that operation on all instances that are members of the pool. Performing these operations on an individual instance that's a member of the pool doesn't affect any other member instances."), autoscaling resets the pool size or lifecycle state to the value that is set in the policy the next time the scheduled autoscaling policy runs.
**Note**
To use autoscaling, ensure that you have installed CLI 3.15.1 or newer and Oracle Cloud Infrastructure Python SDK 2.80.0 or newer.
Was this article helpful?
YesNo


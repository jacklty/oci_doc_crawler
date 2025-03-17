Updated 2023-08-15
# Working with Instance Pools
On Compute Cloud@Customer, instance pools simplify the management of compute instances. An instance pool defines a set of compute instances that's managed as a group. Managing instances as a group enables you to efficiently provision instances and manage the state of instances.
Creating an instance pool requires an instance configuration and a placement configuration. If you update the instance configuration or placement configuration, existing instances aren't affected. New instances that are added to the pool use the new instance and placement configurations.
**Caution**
When you delete an instance pool, the resources that were created by the pool are permanently deleted, including associated instances, attached boot volumes, and block volumes.
You can define an autoscaling configuration and policies that scale the instance pool in (remove instances) or out (add instances) or stop, start, or reboot the instances according to a schedule. Autoscaling a pool enables you to use resources even more effectively by stopping or removing instances when demand is lower and starting or adding instances when demand is higher. You can use instance pool autoscaling along with network load balancing by defining the backend set of servers to be an autoscaled instance pool. 
When working with compute instance configurations and compute instance pools, keep the following points in mind:
  * You can't delete a compute instance configuration if it's associated with at least one compute instance pool. 
  * You can use the same compute instance configuration for multiple compute instance pools. However, a compute instance pool can have only one compute instance configuration associated with it.
  * If you modify the compute instance configuration for a compute instance pool, existing compute instances that are part of that pool don't change. Any new compute instances that are created after you modify the compute instance configuration will use the new compute instance configuration. New compute instances will not be created unless you have increased the size of the compute instance pool or terminate existing compute instances.
  * If you decrease the size of a compute instance pool, the oldest compute instances are deleted first.


Was this article helpful?
YesNo


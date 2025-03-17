Updated 2024-12-11
# Notes about OCI Native Ingress Controller Version 1.4.0
_Find out about the changes in OCI native ingress controller version 1.4.0, and the preparatory steps that you might have to perform before upgrading to version 1.4.0._
OCI native ingress controller version 1.4.0 introduces the following new features:
  * Support for the preservation of a load balancer for an `IngressClass`, when the `IngressClass` itself is deleted.
  * Support for network security groups.
  * Support for defined tags and free-form tags.


If you have been using earlier versions of the OCI native ingress controller, you might have to perform some preparatory steps before upgrading to version 1.4.0 to retain existing network security group and tag associations. For more information, see:
  * [Notes about existing load balancers that have already been added to network security groups](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-140migrationnotes.htm#contengsettingupnativeingresscontroller_114migrationnotes__nic-140-notes-nsg-migration)
  * [Notes about existing load balancers to which tags have already been applied](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-140migrationnotes.htm#contengsettingupnativeingresscontroller_114migrationnotes__nic-140-notes-tag-migration)


Because you might have to perform some preparatory steps, Oracle does not automatically update the OCI native ingress controller cluster add-on to version 1.4.0, even if you have selected the **Automatic updates** option. For more information, see, [Notes about automatically updating the OCI Native Ingress Controller Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-140migrationnotes.htm#contengsettingupnativeingresscontroller_114migrationnotes__nic-140-notes-auto-update)
## Notes about existing load balancers that have already been added to network security groups 🔗 
OCI native ingress controller version 1.4.0 introduces support for adding load balancers to network security groups.
If you have manually added load balancers that were created by (or managed by) an OCI native ingress controller version earlier than version 1.4.0 to network security groups, note that those associations will not be retained when you upgrade to OCI native ingress controller version 1.4.0 or later.
Therefore, before you upgrade from an earlier version of the OCI native ingress controller, use the `oci-native-ingress.oraclecloud.com/network-security-group-ids` annotation to specify the network security groups to which you want to add the load balancer.
## Notes about existing load balancers to which tags have already been applied 🔗 
OCI native ingress controller version 1.4.0 introduces support for defined tags and free-form tags on load balancers.
If defined tags or free-form tags have already been applied to a load balancer created by (or managed by) an OCI native ingress controller version earlier than version 1.4.0, note that those existing tags will not be retained when you upgrade to OCI native ingress controller version 1.4.0 or later.
Therefore, before you upgrade from an earlier version of the OCI native ingress controller, use the `oci-native-ingress.oraclecloud.com/defined-tags` and `oci-native-ingress.oraclecloud.com/freeform-tags` annotations to specify values for existing defined tags or free-form tags.
When you upgrade to version 1.4.0, the OCI native ingress controller applies the defined tags and free-form tags specified by the annotations to the load balancer.
Note that to enable the OCI native ingress controller to apply defined tags to a load balancer, a suitable IAM policy must exist to enable the OCI native ingress controller to use the appropriate tag namespace. 
For more information, see [Applying Tags to the Load Balancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller_addingtags).
## Notes about automatically updating the OCI Native Ingress Controller Add-on 🔗 
Oracle does not automatically update the OCI native ingress controller cluster add-on to version 1.4.0, even if you have selected the **Automatic updates** option, because you might have to perform some preparatory steps to retain existing network security group and tag associations. For more information about the preparatory steps, see:
  * [Notes about existing load balancers that have already been added to network security groups](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-140migrationnotes.htm#contengsettingupnativeingresscontroller_114migrationnotes__nic-140-notes-nsg-migration)
  * [Notes about existing load balancers to which tags have already been applied](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-140migrationnotes.htm#contengsettingupnativeingresscontroller_114migrationnotes__nic-140-notes-tag-migration)


After performing any preparatory steps, you have to manually update the OCI native ingress controller cluster add-on to version 1.4.0 using the Console, the CLI, or the API (see [Updating a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-add-on.htm#update-add-on "Find out how to update a cluster add-on using Kubernetes Engine \(OKE\).")). Having manually updated the add-on to version 1.4.0, you can then select the **Automatic updates** option if you want Oracle to automatically update the OCI native ingress controller cluster add-on in future.
Was this article helpful?
YesNo


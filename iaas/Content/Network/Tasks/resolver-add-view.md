Updated 2023-05-30
# Adding a Private View to a Resolver
You can create and attach a view to a resolver in addition to the default view, so that their zones are resolvable in the VCN. 
Each VCN-dedicated resolver has a protected default view. You can add your own zones to the default view, but there are restrictions on zone names to avoid collisions with protected zones. If a resolver is deleted, and its default view contains non-protected zones, then the default view will be converted to a non-protected view instead of being deleted. You can create and attach a view to a resolver in addition to the default view, so that their zones are resolvable in the VCN.
See [Private DNS resolvers](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-Private-resolver.htm#Private_resolver "A private DNS resolver answers DNS queries for a VCN per a configuration you create.") for more information and a feature overview.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-add-view.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-add-view.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/resolver-add-view.htm)


  *     1. From the **Virtual Cloud Network Details** screen for your VCN, look in the VCN Information tab and click the name of the DNS resolver for the VCN. The **Private Resolver Details** screen appears.
    2. From the **Private Resolver Details** screen, click **Manage Private Views**. The **Manage Private Views** screen appears.
    3. Select a previously created private view from the drop down menu in the numbered **Private view** list. 
    4. To associate another view, click **Additional Private View** select another view.
    5. When you are finished, click **Save Changes**.
Views created automatically by Oracle are available in addition to views you create.
  * Use the [resolver update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/resolver/update.html) command and required parameters to add a private view to a resolver:
Command
CopyTry It
```
oci dns resolver update --resolver-id resolver_OCID --attached-views '[{"view-id":"view_ocid"}]' ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateResolver](https://docs.oracle.com/iaas/api/#/en/dns/latest/Resolver/UpdateResolver) operation to add a private view to a resolver. Include the `AttachedViews` attribute.


Was this article helpful?
YesNo


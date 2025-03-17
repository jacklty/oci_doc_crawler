Updated 2024-11-23
# Allowing My Oracle Cloud Support to Access Client Log Files
Give consent to My Oracle Cloud Support to access your Microsoft AD bridge client log files.
When My Oracle Cloud Support are diagnosing AD bridge issues, they might need access to the AD bridge client log files.
The default behavior is that My Oracle Cloud Support can't access the client log files, which are on a machine at your premises. You have to add them to the support request. You can give your consent so that My Oracle Cloud Support can fetch the logs directly when they need to be analyzed to resolve an issue. This can reduce the time it takes for the support request to be resolved.
Learn about the scope of consent, what it covers, and how long it lasts:
  * **How long does consent last?**
After you have given your consent, it remains effective until you remove your consent, or remove the AD bridge domain.
  * **Do I need to give separate consent for every AD bridge?**
No. Your consent applies at Microsoft Active Directory domain level. If you have more than one bridge under the same Microsoft Active Directory domain, the consent applies to all of them.
  * **Do I need to provide consent for each Microsoft Active Directory domain?**
If you have more than one Microsoft Active Directory domain, a separate consent is needed for each one.
  * **Can Oracle fetch any file from the windows machine where the Microsoft Microsoft Active Directory bridge client is installed?**
No. Only Microsoft Microsoft Active Directory bridge log files are fetched.
  * **When is the log file fetched from the client machine?**
Oracle only fetches logs files if they're needed so they can be analyzed as part of resolving a service request that you have raised. If you raise a service request and there's no need for the AD bridge client log file to be examined, then it's not fetched.
  * **Where are the log files stored?**
They're uploaded to tenant Oracle cloud storage.
  * **Do the log files stay in cloud storage indefinitely?**
No. They'll be removed from cloud storage after 24 hours, after Oracle has analyzed the logs. An automated purge job deletes all log files that are older than 24 hours.


Was this article helpful?
YesNo


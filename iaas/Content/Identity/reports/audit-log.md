Updated 2025-03-13
# Audit Log Report
The audit log captures system activity such as successful and failed sign ins, user creation, update and deletion, and so on. Many event types are captured, and you can search for specific types of event, or by date.
To find out more about retrieving data from OCI Audit, see:
  * [Implement multi cloud security using OCI Audit to capture events from OCI Identity and Access Management](https://docs.oracle.com/en/learn/oci-iam-multicloud-security/#introduction)
  * [Generate Identity and Access Management Reports from Oracle Cloud Infrastructure Audit](https://docs.oracle.com/en/learn/generating-iam-reports-from-oci-audit/index.html#introduction)


This report returns data for the last 14 days. You can use the [OCI Audit service](https://docs.oracle.com/iaas/Content/Audit/home.htm) for older data (up to 365 days).
## Data
The audit log report shows: 
  * The date and time of an event.
  * The signed-in user or client who caused the event.
  * The event id.
  * A description of the event.
  * The target of the event.


## More Details
For each row in the report, you can select > to expand details for that entry. The additional information for each row is: 
  * The Execution Context Id
  * Client IP
  * SSO Comments
  * SSO Browser
  * Matched Sign-On Policy Rule
  * Authentication Level
  * User's device information, also called the device fingerprint
  * Protected resource
  * SSO Policy Obligation


## Filtering the Results
You can filter the audit log report to show: 
  * Results from a specific date range. Audit log events are only kept for 90 days, so you can't search from earlier than 90 days ago.
  * The signed in user or client. This is case-sensitive and you must enter the username exactly as it appears on the system.
  * The description of the event. Start typing the name of the description, or choose from the list.


## Audit Log Events
The following events are reported in the Audit Log:
  * Application access failed
  * Application accessed
  * Application activated
  * Application created
  * Application deactivated
  * Application deleted
  * Application granted
  * Application revoked
  * Application updated
  * Bypasscode created
  * Group deleted
  * IAM group created
  * MFA factor enrolled
  * Notification delivered
  * Notification not delivered
  * Password changed
  * Password policy created
  * Password policy updated
  * Password reset
  * Password reset by Admin
  * SSO policy created
  * SSO policy rule created
  * SSO policy rule updated
  * SSO policy updated
  * User activated
  * User added to group
  * User created
  * User deactivated
  * User deleted
  * User login
  * User login failed
  * User logout
  * User removed from group
  * User updated


Was this article helpful?
YesNo


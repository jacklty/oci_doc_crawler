Updated 2024-02-13
# Understanding Adaptive Security
Adaptive Security provides strong authentication capabilities for users based on their historical behavior in an identity domain in IAM.
Adaptive Security analyzes a user's risk profile based on their historical behavior, such as too many unsuccessful sign-on attempts and too many unsuccessful MFA attempts. To evaluate the user's behavior across other systems with which IAM isn't directly involved, Adaptive Security allows you to configure existing risk providers to obtain the user's risk score from third-party risk providers, such as Symantec CloudSOC Cloud Access Security Broker (CASB). With this context and risk information, Adaptive Security profiles each user, and arrives at its own risk score and an overall consolidated risk level (High, Medium, Low). 
These scores and risk levels can be used with policies to enforce a remediation action, such as allowing or denying the user from accessing IAM and its protected applications and resources, requiring the user to provide a second factor to authenticate into IAM. 
Administrators can also view how the user's risk profile trended over time, and drill down to see details associated with each event.
Was this article helpful?
YesNo


Updated 2024-05-30
# Understanding Risk Providers
Identity domain administrators and security administrators use identity domain risk providers to configure various contextual and threat events to be analyzed within an identity domain in IAM. An identity domain can also consume user risk scores from third-party risk providers.
## Default Risk Provider
An identity domain includes a default risk provider with a list of supported contextual and threat events, such as too many unsuccessful login attempts or too many unsuccessful MFA attempts. Administrators can enable events of interest, and specify weighting or severity for each of these events. The system uses the configured weighting to compute the user's risk score. 
You can configure the following events for a risk provider: 
  * Access from an unknown device
  * Too many unsuccessful login attempts
  * Too many unsuccessful MFA attempts
  * Access from suspicious IP addresses
  * Access from an unfamiliar location
  * Impossible travel between locations

As an example, if a user uses a new (unknown) device to sign in, the system won't recognize the device, and will the trigger the **Access from an unknown login device** event.
Administrators can assign weighting to events that correspond to risk ranges. Consider the weighting for each of the risks as follows: 
  * low risk range (0-25)
  * medium risk range (26-75)
  * high risk range (76-100)

If the administrator wants to consider the user login from an unknown device to be of low risk, then the administrator sets the weighting for that event to be less than 25. If the administrator wants to consider the same event to be of medium risk, then the administrator sets the weighting for that event to be from 26 through 75. Any value set greater than 75 for that event is considered as high risk. If the user violates more than one event, then the risk score is a combination of two weightings and corresponds to the appropriate risk level. The user's risk scores are evaluated continuously and are reduced based on the remediation actions that are taken by the user, such as successful logins and password resets.
## Third-Party Risk Providers
Administrators can create risk providers to obtain a user's risk score from the Symantec third-party risk engine. This risk engine provides additional intelligence on the user's behavior across heterogeneous systems with which IAM isn't directly involved.
To provide a consolidated risk profile of the user at any time, IAM takes the highest level of the risk scores of both the default IAM risk provider and the configured third-party risk providers, and qualifies the user as a high-risk, medium-risk, or low-risk user. For example, if a user's risk score from the default risk provider is within the Low range, but the risk score from a third-party risk provider is within the Medium range, then the user's consolidated risk level is set to Medium.
Administrators can then use the identity domain risk score, third-party risk score, or consolidated user risk level as conditions that can be used with identity domain sign-on policies to enforce a remediation action, such as allowing or denying the user from accessing an identity domain and its protected applications and resources, requiring the user to provide a second factor to authenticate into an identity domain, and so on.
Was this article helpful?
YesNo


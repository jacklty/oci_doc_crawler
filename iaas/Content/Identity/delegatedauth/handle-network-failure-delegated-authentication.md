Updated 2025-01-14
# Handle Network Failure in Delegated Authentication
Handle a network failure in a delegated authentication.
Most organizations still rely on Microsoft Active Directory (AD) for managing their user accounts, and users rely on Active Directory for authentication and access to various systems. If for some reasons, users are not be able to authenticate themselves with Active Directory credentials. This has a huge impact on the daily operations and business of the organizations.
To avoid situations like these, IAM provides you with a network failure handling functionality. This functionality helps users to sign in with Active Directory credentials even when IAM is not able to reach the Active Directory (AD) Bridge.
You configure delegated authentication for an AD domain in IAM so that a user can use their Active Directory password to authenticate into IAM.
If the AD Bridge is not reachable, then users are unable to validate their credentials with Active Directory and therefore cannot sign in into IAM. Your Active Directory is not reachable for several reasons. This could be because of network connectivity between AD Bridge and IAM is down.
To avoid this situation, IAM provides the local password caching functionality to perform local authentication in case AD Bridge is not reachable. This functionality helps delegated users to sign in into IAM even if AD Bridge is not reachable. For security reasons, this password is stored in hashed form in IAM.
Ensure that the lifetime of this cache password in IAM is limited. You can configure the maximum duration (5 days) you set to cache the password on IAM. For example, if your network connectivity is down and you have set the cache password duration to 2 days, then it enables users to sign in to IAM for only 2 days. However, if Active Directory is still not reachable for longer than the specified duration, then you cannot sign in to IAM.
To guard against the possibility that someone can use brute force attacks to access your account, you can limit the number of unsuccessful password attempts during password caching in IAM. After several failed attempts, IAM locks your user account. There is a limit of 5 which is configurable.
You cannot perform the following operations while the network connectivity is down:
  * A user cannot change their own password
  * A user cannot reset their own password by validating the token
  * A user cannot change their own email address
  * An administrator cannot change a user's password to a known value
  * An administrator cannot reset a user's password whose password is authenticated by Active Directory


However, if you recently changed a password in Active Directory, then you can sign in to IAM with that password while connectivity is down, provided you have already login to IAM while Active Directory was available.
**Note**
Sometimes, you might encounter a system error even if you provide a correct password. This is either because the password cache is empty or because the password has expired.
## Activating Local Password Caching 🔗 
You must activate the local password caching functionality to enable delegated authentication users to sign in into IAM in case Microsoft Active Directory is not reachable.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. On the domain details page, click **Security**.
  3. Select **Delegated authentication**.
  4. Expand the node to the right of the AD Bridge for which you want to activate password cache.
  5. Turn **On** the **Activate password cache** switch.
  6. Set the duration you want to cache this password in **Cache password duration (days)**.
  7. Select how many unsuccessful password attempts that you want during password caching in **Number of unsuccessful passwords attempts during password caching**.
  8. Select **Save**.


Was this article helpful?
YesNo


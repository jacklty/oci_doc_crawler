Updated 2024-12-18
# IAM Database Password Lockouts
A user's account gets locked if the user encounters 10 consecutive failed sign-in attempts.
IAM database and Console users are locked out after 10 consecutive failed sign-in attempts (total for both passwords). Only an IAM administrator can unlock your user account.
  * If you fail to sign in to IAM or the database after 10 consecutive attempts (total for both), your account is locked and you cannot sign in to either your database or the Console.
  * When you are locked out, an IAM administrator must explicitly unlock your account.
  * IAM does not support automatic unlocking.
  * A failed login count is tracked centrally across all regions in a realm. Failed logins are recorded in your home region and replicated to their subscribed regions.


## **Failed login attempts** 🔗 
Was this article helpful?
YesNo


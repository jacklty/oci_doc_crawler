Updated 2024-12-18
# User Password
Users are prompted to change their passwords the first time they sign in.
When the user signs in to the Console the first time, they'll be immediately prompted to change the password. If the user waits more than 7 days to initially sign in and change the password, it will expire and an administrator will need to reset the password for the user.
After the user successfully signs in to the Console, they can use Oracle Cloud Infrastructure resources according to permissions they've been granted through policies. 
**Note**
A user automatically has the ability to change their password in the Console. An administrator does not need to create a policy to give a user that ability.
## Changing a Password 🔗 
Users can change their password, after it has been assigned, from the Console.
If a user wants to change their own password _sometime after_ they change their initial one-time password, they can do it in the Console. Remember that a user can automatically change _their own_ password; an administrator does not need to create a policy to give the user that ability. 
For more information, see [Unblocking a User](https://docs.oracle.com/en-us/iaas/Content/Identity/access/to_unblock_a_user.htm#unblock_user "Unblock a user as an administrator."). 
## If a User Needs Their Console Password Reset 🔗 
If a user forgets their password, they can use the Console's **Forgot Password** link to reset the password.
If a user forgets their Console password and also has no access to the API, they can use the Console's **Forgot Password** link to have a reset password link sent to the email address configured for the user account. (All user profiles require an email address.)
Users can also ask an administrator to reset their password for them. All administrators (and anyone else who has permission to the tenancy) can reset Console passwords. The process of resetting the password generates and sends a reset password email. The user will need to change their password before the link expires and before they can sign in to the Console again.
If you're an administrator who needs to reset a user's Console password, see [Unblocking a User](https://docs.oracle.com/en-us/iaas/Content/Identity/access/to_unblock_a_user.htm#unblock_user "Unblock a user as an administrator.").
## If a User Is Blocked from Signing In to the Console 🔗 
If a user tries to sign in to the Console and is unsuccessful more times in a row than is allowed by the identity domain's password policy, they will be automatically blocked from further attempts.
If automatic account unlock is not enabled for the identity domain by the password policy, the user must contact an administrator to get unblocked (see [Unblocking a User](https://docs.oracle.com/en-us/iaas/Content/Identity/access/to_unblock_a_user.htm#unblock_user "Unblock a user as an administrator.")).
Was this article helpful?
YesNo


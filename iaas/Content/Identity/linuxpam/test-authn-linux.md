Updated 2023-05-31
# Testing Authentication into Linux Using IAM
Test authentication on Linux using a user in IAM.
**Before you begin:** Ensure that configured your Confidential Application and that it only contains the following roles: 
  * **Me**
  * **POSIX Viewer**
  * **Signin**

**Identity Domain Administrator** or **User Administrator** should not be listed. See [Configuring a Confidential Application](https://docs.oracle.com/en-us/iaas/Content/Identity/linuxpam/configure-confidential-application.htm#configure-confidential-application "To register the IAM Linux PAM as a client application in IAM, you create a confidential application with the POSIX Viewer role.") for additional information.
  1. SSH into your Linux environment where the Linux Pluggable Authentication Module (PAM) is installed.
  2. When prompted enter the password for the IAM user:
For example:
```
# ssh userPosix@host.example.com
password:
Last login: Thur Mar 28th 12:14:04 2019 from host.example.com
[userPosix@host ~]$ 
```


You should be logged in successfully.
Was this article helpful?
YesNo


Updated 2024-09-30
# Working with SMTP Credentials
Simple Mail Transfer Protocol (SMTP) credentials are needed in order to send email through the Email Delivery service.
Each user is limited to a maximum of two SMTP credentials. If more than two are required, they must be generated on other existing users or additional users must be created.
**Note**
You can't change your SMTP username or password to a string of your own choice. The credentials are always Oracle-generated strings.
Each user created in the IAM service automatically has the ability to create and delete their own SMTP credentials in the Console or the API. An administrator does not need to create a policy to give a user those abilities. Administrators (or anyone with permission to the tenancy) also have the ability to manage SMTP credentials for other users. 
**Tip** Although each user can create and delete their own credentials, it is a security best practice to create a new user and generate SMTP credentials on this user rather than generating SMTP credentials on your Console user that already has permissions assigned to it.
SMTP credentials don't expire. Each user can have up to two credentials at a time. To get SMTP credentials in the Console, see [Generating SMTP Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/access/to_generate_SMTP_credentials.htm#generate-smtp-credentials "Use the Console to generate SMTP credentials."). 
For information about using the Email Delivery service, see [Overview of the Email Delivery Service](https://docs.oracle.com/iaas/Content/Email/Concepts/overview.htm).
Was this article helpful?
YesNo


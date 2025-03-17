Updated 2025-01-14
# Constructing a Self-Registration URL
After creating a self-registration profile in IAM, you must create a self-registration URL.
  1. On the **Self registration** page, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the profile you want to update, and select **Edit** to edit the profile.
  2. On the **Edit self-registration profile** page, copy the **Profile ID** to construct a URL exactly like the following example:
```
https://[instancename.idcs.internal.oracle.com:port]/ui/v1/signup?profileid=[ProfileID]
```

If the URL isn't constructed properly, you receive an error stating that your profile wasn't found. Verify that the syntax of the URL is correct.
This URL gives the user access to the self-registration page. After the user completes self-registration and clicks **Submit** , they are presented with a success page. The user must then select the link **Select here to continue** to go to the **My Apps** page. If the user doesn't select the link within 1 hour, the token expires and user is presented with the **Login** page again.


Was this article helpful?
YesNo


Updated 2023-06-08
# Testing the SSO Using a Previously Oracle E-Business Suite Bookmarked URL
You can use the Oracle E-Business Suite URL that you have bookmarked to verify the integration and ensure that the SSO works.
  1. Open a browser and enter one of the Oracle E-Business Suite URLs that you have bookmarked (for example, the Self-Service Reports page - P11D Reports):
```
https://ebsasserter.example.com:7002/ebs?requestUrl=http%3A%2F%2Febs.example.com%3A8000%2FOA_HTML%2FRF.jsp%3Ffunction_id%3D1023615%26resp_id%3D54745%26resp_appl_id%3D800%26security_group_id%3D0%26lang_code%3DUS%26oas%3DZGSSqTllSAVkI4tpzTqoZw..%26params%3DYQiYllX3TGJSmdkebayqm4plh8uddwPMseD54DE-G-c
```

  2. The IAM **Sign In** page appears. Use the user name and password of the previously created user to sign in.
  3. Upon successful authentication, the user is redirected to the Oracle E-Business Suite page passed as a parameter to the E-Business Suite Asserter URL in the `requestUrl` parameter.
  4. Log out from Oracle E-Business Suite. The browser is redirected to the IAM **Sign In** page.


Was this article helpful?
YesNo


Updated 2023-06-08
# Testing the SSO Using the E-Business Suite Asserter Direct URL with a Redirect Parameter
You can use the URL for the E-Business Suite Asserter with a redirect parameter to verify the integration and ensure that the SSO works.
  1. Open a browser and enter the URL for the E-Business Suite Asserter along with the `requestUrl` parameter. In the following example, the parameter value points to one of the Oracle E-Business Suite pages (for example, Self-Service Reports page - P11D Reports).
```
_https://ebsasserter.example.com:7002_/ebs?requestUrl=http%3A%2F%2Febs.example.com%3A8000%2FOA_HTML%2FRF.jsp%3Ffunction_id%3D1023615%26resp_id%3D54745%26resp_appl_id%3D800%26security_group_id%3D0%26lang_code%3DUS%26oas%3DZGSSqTllSAVkI4tpzTqoZw..%26params%3DYQiYllX3TGJSmdkebayqm4plh8uddwPMseD54DE-G-c
```

The `requestUrl` parameter value must match one of the `whitelist.urls` and must be URL encoded. 
  2. The IAM **Sign In** page appears. Use the username and password of the previously created user to sign in.
  3. Upon successful authentication, the user is redirected to the page passed as a parameter to the E-Business Suite Asserter URL in the `requestUrl` parameter.
  4. Log out from Oracle E-Business Suite. The browser is redirected to the IAM Sign In page.


Was this article helpful?
YesNo


Updated 2023-06-08
# Logging in with Non-US English Language
Identity Cloud Service EBS Asserter supports the language configuration of a user provided in EBS. If the `FND_OVERRIDE_SSO_LANG` profile option is enabled for a user in EBS, Asserter creates an EBS session based on the value of the `ICX_LANGUAGE` profile option of this user.
For a given EBS deployment, if there is no such configuration for a user in EBS, the language can be controlled using the `langCode` parameter or `base.lang` can be set in the `bridge.properties`.
You can sign in to the EBS Home Page in a different language by specifying the code for the language in the login URL: 
```
https://_apps.example.com_/OA_HTML/AppsLogin?langCode=_language
      code_>
```

Was this article helpful?
YesNo


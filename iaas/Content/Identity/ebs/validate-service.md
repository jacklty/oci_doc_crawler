Updated 2023-06-08
# Validating the Service
You can validate the Asserter configuration, E-Business Suite configuration, and IAM Application setup using the Validation Service.
**Note** This validation service is only available for EBS Asserter 20.1.3 onwards.
Access the validation service using the endpoint `app.url/validate` for example, `_https://ebsasserter.example.com:7002_/ebs/validate`.
The validation result of each configuration is one of `Success`, `Failure`, `Undetermined`.
If the result is `Failure` or `Undetermined`, the response body suggests the expected configuration. Reconfigure EBS Asserter or the Oracle E-Business Suite or IAM Application as appropriate.
Was this article helpful?
YesNo


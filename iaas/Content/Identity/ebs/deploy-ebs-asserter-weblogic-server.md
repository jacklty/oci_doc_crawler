Updated 2025-01-14
# Deploying the E-Business Suite Asserter on Oracle WebLogic Server
You must deploy the E-Business Suite Asserter to the Administration Server instance of Oracle WebLogic Server to perform end-to-end testing of the integration.
  1. Copy the E-Business Suite Asserter war file (`ebs.war`) to the working folder in the Oracle WebLogic Server `/opt/ebssdk`.
  2. Enter the following URL in a web browser, replacing `host:port` with the host name and port for the Oracle WebLogic Server Administration Console:
```
http://wls_host:wls_port/console
```

For example, `https://ebsasserter.example.com:7002/console`.
  3. Sign in to the WebLogic console as an administrator.
  4. In the **Change Center** , select the **Lock & Edit** button.
  5. Under Domain Structure, select **Deployments**.
  6. On the right, under **Deployments** , select the **Install** button. 
  7. Enter the path for the E-Business Suite Asserter war file as `/opt/ebssdk`.
  8. Select the `ebs.war` file and select **Next**.
  9. Select **Install this deployment as an application** , and then select **Next**.
  10. Select the target server (for example, **EBSAsserter_server**) and then select **Next**.
  11. Accept the default values and select **Finish**.
  12. Select **Activate Changes**.


Was this article helpful?
YesNo


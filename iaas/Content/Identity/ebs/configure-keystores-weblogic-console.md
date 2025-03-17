Updated 2025-01-14
# Configuring Keystores in WebLogic Console
Using If you are using Custom Trust Store in WebLogic for asserter deployment, instead of using Custom Identity and Custom Trust Store with WebLogic server, use Custom Identity and Java Trust Store. With this configuration, you do not need to import IAM certificate.
  1. Start the Oracle WebLogic Server Administration Console by entering `http://wls_host:wls_port/console` in the URL line of a web browser. For example, `https://ebsasserter.example.com:7002/console`.
  2. Sign in to WebLogic console as an administrator.
  3. In the left panel, select **Lock & Edit**, expand **Environment** , select **Servers**.
  4. Select the name of the target server where you want to configure the keystore.
  5. Select **Keystores** under the **Configuration** tab.
  6. In the left panel, select **Lock & Edit** to make the changes.
  7. Select **Custom Identity and Java Trust Store**.
  8. Select **Save** and **Activate Changes**.
  9. Restart the WebLogic server.


Was this article helpful?
YesNo


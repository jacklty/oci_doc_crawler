Updated 2025-01-14
# Configuring Hostname Verification in WebLogic Console
You can configure the hostname verification in Oracle WebLogic Server Administration Console.
  1. Start the Oracle WebLogic Server Administration Console by entering `http://wls_host:wls_port/console` in the URL line of a web browser. For example, `https://ebsasserter.example.com:7002/console`.
  2. Sign in to WebLogic console as an administrator.
  3. In the left panel, select **Lock & Edit**, expand **Environment** , select **Servers**.
  4. Select the name of the target server where you want to deploy the EBS Asserter. In this example, **AdminServer**.
  5. Select the **SSL** tab. Scroll down and expand the **Advanced** section.
  6. Update the **Hostname Verification** parameter with the value **None** , and then select **Save**.
  7. Select **Activate Changes**.
  8. Restart the servers.


Was this article helpful?
YesNo


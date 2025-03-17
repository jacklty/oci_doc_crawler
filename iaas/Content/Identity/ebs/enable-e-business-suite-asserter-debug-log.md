Updated 2025-01-14
# Enabling the E-Business Suite Asserter Debug Log
To send logs to a file, add `FileHandler` to the `handlers` property in the `logger.properties` file. This enables file logging globally.
  1. Create a `logger.properties` file with entries as follows:
```
handlers = java.util.logging.FileHandler, java.util.logging.ConsoleHandler
java.util.logging.FileHandler.pattern = %h/ebsasserter.log
java.util.logging.FileHandler.formatter = java.util.logging.SimpleFormatter
java.util.logging.FileHandler.level=ALL
java.util.logging.ConsoleHandler.formatter = java.util.logging.SimpleFormatter
java.util.logging.ConsoleHandler.level=ALL
com.oracle.ebs.sso.level=ALL
oracle.apps.fnd.ext.level=ALL
oracle.security.jps.idcsbinding.level=ALL
```

  2. Add the option `-Djava.util.logging.config.file=<logger.properties                         file created above>` in Oracle WebLogic Server:
    1. Using a browser, access the Oracle WebLogic Server Administration Console.
    2. In the Oracle WebLogic Server Administration Console, select **servers** under **Environment** in the **Domain Structure**.
    3. In the **Servers** table, select the name of the server instance where the E-Business Suite Asserter is deployed.
    4. From the **WebLogic Server** menu, select **Administration** , then select **Server Start**.
    5. From the **Server Start** page, you can add the option `-Djava.util.logging.config.file=<logger.properties                          file created above>` in the **Arguments** field.
    6. Select **Save**.
  3. Restart the Oracle WebLogic Server where the E-Business Suite Asserter is deployed.
The E-Business Suite Asserter debug log file is in `<HOME DIR>/ebsasserter.log`.


Was this article helpful?
YesNo


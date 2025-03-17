Updated 2025-01-14
# Defining the Data Source
In the Oracle WebLogic Server where E-Business Suite Asserter is deployed, you must configure database connectivity by adding data sources to your WebLogic domain. WebLogic Java Database Connectivity (JDBC) data sources provide database access and database connection management.
  1. Enter the following URL in a web browser, replacing `host:port` with the host name and port for the WebLogic Administration Console:
```
http://wls_host:wls_port/console
```

For example, `https://ebsasserter.example.com:7002/console`.
  2. Sign in to WebLogic console as an administrator.
  3. In the administration console under **Domain Structure** , expand **Services** and then select **Data Sources**.
  4. Under the **Data Sources** table heading, select the **New** list, and select **Generic Data Source**.
  5. In the **JDBC Data Source Properties** section, specify the following values, and then select **Next** :
     * **Name** : `visionDS`
     * **JNDI Name** : `visionDS`
     * **Database Type** : `oracle`
The value of the **Name** parameter must match the `ebs.ds.name` parameter in the E-Business Suite Asserter configuration file.
  6. Select a database driver, and then select **Next**.
     * If you are using an XA data source, select `*Oracle's Driver               (Thin XA) for Instance connections; Versions:any`.
     * If you are using a non-XA data source, select `*Oracle's Driver               (Thin) for Instance connections; Versions:Any`.
  7. In the **Transaction Options** section, perform one of the following, and select **Next** :
     * For a non-XA data source, uncheck the **Supports Global Transactions** checkbox.
     * For an XA data source, leave the checkbox checked.
  8. In the **Connection Properties** section, specify the following appropriate values and then select **Next**.
     * **Database Name** : `EBSDB`
     * **Host Name** : `ebs.example.com`
     * **Port** : `1521`
     * **Database Username** : Enter the username you created earlier in [Creating an Application User on Oracle E-Business Suite](https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/create-app-user-ebs.htm#create-app-user-ebs "You must create a specific application user that is authorized to connect to the Oracle E-Business Suite database. The Apps Schema Connect role determines the authorization to connect to the Oracle E-Business Suite database. A user that has this role is authorized to connect to the Oracle E-Business Suite database.").
     * **Password** : Enter the password for the username.
  9. In the **Driver Class Name** field, enter one of the following:
     * `oracle.apps.fnd.ext.jdbc.datasource.AppsDataSource` if you use a non-XA data source.
     * `oracle.apps.fnd.ext.jdbc.datasource.AppsXADataSource` if you are using an XA data source.
Optionally, you can use the `oracle.jdbc.OracleDriver` driver instead, but you need to provide administrative database credentials during this value. If you don't want to expose administrative database credentials to WebLogic administrators, use one of the two values provided for **Driver Class Name** in this task.
  10. In the **Properties** text box, keep the current value for `user`, add a new line, and enter the path to the `dbc` file as shown in this example:
```
user=IDENTITYADMIN
dbcFile=/opt/ebssdk/EBSDB_ebsasserter.example.com.dbc
```

**Note** This field is case sensitive. Ensure the name of the file is correctly written with the correct uppercase and lowercase letters.
  11. Review the data source properties values, confirm that the database is running, and select **Test Configuration**.
Ensure your network doesn't block communication between the E-Business Suite Asserter's WebLogic server machine and the Oracle E-Business Suite database through the port number you provided in the datasource.
  12. When you see the **Connection test succeeded** message, then select **Next**.
  13. In the **Select Targets** section, select the target server (for example, **EBSAsserter_server**), and select **Finish**.
  14. In the **Change Center** , select the **Activate Changes** button. 


Was this article helpful?
YesNo


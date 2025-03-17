Updated 2023-06-08
# Configure the E-Business Suite Asserter in Oracle E-Business Suite
Register the E-Business Suite Asserter application server with Oracle E-Business Suite.
## Registering the E-Business Suite Asserter with Oracle E-Business Suite 🔗 
To establish communication with Oracle E-Business Suite, the E-Business Suite Asserter uses the application server ID in the database connection file. The database connection file is generated while registering the E-Business Suite Asserter application server with Oracle E-Business Suite.
  1. Sign in to the Oracle E-Business Suite application server machine. Don't use the root user. Use the user that installed and ran the WebLogic Server.
  2. Run the commands `echo $JAVA_HOME` and `echo $WL_HOME`, and then make note of the value that is set for each:
     * `JAVA_HOME`: `/usr/java/jdk1.7.0_201`
     * `WL_HOME`: `/u01/oracle/wlserver`
If the values of the commands `$JAVA_HOME` and `$WL_HOME` aren't set, request that the WebLogic administrator set them. The `$WL_HOME` value is only needed if you use a version of Oracle E-Business Suite greater than 12.2.
The values for the `$JAVA_HOME` and `$WL_HOME` might differ from your environment. Update the fields with the correct values for your environment.
  3. Run the following command to create a working folder:
```
cd /opt
mkdir ebssdk
cd ebssdk
```

  4. Extract the `fndext.jar` file, which is in the `WEB-INF/lib` folder inside the `ebs.war` file that you have downloaded from the IAM Console. 
  5. Copy the `fndext.jar` file to the working folder you created in the previous step and also to the E-Business Suite Asserter WebLogic `$DOMAIN_HOME/lib` folder.
The name of the `fndext.jar` file might vary depending on the current version.
  6. Locate your Oracle E-Business Suite environment file (in this example, `/u01/install/VISION/EBSapps.env`) and run the following command:
```
source /u01/install/VISION/EBSapps.env
```

The path to the `.env` file might vary depending on your environment.
  7. Locate the `.dbc` file that is associated with your Oracle E-Business Suite instance in the following folder: `$FND_SECURE/EBSDB.dbc`.
If your database instance name is `EBSDB`, the file has a name like `EBSDB.dbc`. Make a note of the full path of the `.dbc` file (including the file name itself): `/u01/install/VISION/fs1/inst/apps/EBSDB_ebs/appl/fnd/12.0.0/secure/EBSDB.dbc.`
  8. Run the following command to register the E-Business Suite Asserter application server with Oracle E-Business Suite:
```
cd /opt/ebssdk
java oracle.apps.fnd.security.AdminDesktop apps/_apps_ CREATE NODE_NAME=_ebsasserter.example.com_ DBC=_/u01/install/VISION/fs1/inst/apps/EBSDB_ebs/appl/fnd/12.0.0/secure/EBSDB.dbc_
```

**Note** The value of `CREATE NODE_NAME` is the asserter hostname. Use the value that is correct for your setup.
  9. Run the following command:
```
cat _EBSDB___ebsasserter.example.com_.dbc
```

The resulting file name might be in all uppercase letters. Make a note of the `APPL_SERVER_ID` value.
  10. Copy the `_EBSDB___ebsasserter.example.com_.dbc`file to the EBS Asserter's WebLogic Server machine under the`/opt/ebssdk` folder. Create the folder if the folder doesn't exist.


Was this article helpful?
YesNo


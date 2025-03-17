Updated 2023-07-06
# Log Files
Understand how to manage the log files created by the bridge between Microsoft Active Directory and an IAM identity domain, and how to let Oracle access them on demand for support.
## Creating and Managing Log Files for the Microsoft Active Directory Bridge 🔗 
After you install and configure the AD bridge, you may want to access the log files for troubleshooting purposes. You can locate these files in the `%ProgramData%\Oracle\IDBridge\logs` directory.
To modify the log level of the log files for the AD bridge:
  1. Navigate to the `%ProgramFiles%\Oracle\IDBridge` directory.
  2. Using a text editor, open the `log4net.config` file.
  3. In the file, locate the following line of code: `<level value="info" />`
  4. Change the value of the `level value` parameter to one of the following log levels:
Log Level | Description  
---|---  
`all` | Capture all events.  
`debug` | Capture fine-grained informational events that are most useful to debug the AD Bridge.  
`error` | Capture error events that might still allow the AD bridge to continue running.  
`fatal` | Capture severe error events that will result in the AD bridge no longer running.  
`info` | Capture informational events that highlight the progress of the AD bridge at a coarse-grained level.  
`off` | Turn off logging.  
`trace` | Capture finer-grained informational events than the `debug` log level.  
`warn` | Capture potentially harmful situations to the AD bridge.  
  5. Save and close the `log4net.config` file.


**Note** You must restart the AD bridge for the change you made to the log level to take effect. See [Restarting the Microsoft Active Directory Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/maintain-microsoft-active-directory-ad-bridge.htm#restart-microsoft-active-directory-ad-bridge).
Was this article helpful?
YesNo


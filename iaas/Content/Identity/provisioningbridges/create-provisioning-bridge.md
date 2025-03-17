Updated 2025-01-14
# Creating a Provisioning Bridge
Create a provisioning bridge in an identity domain to link your on-premises apps with IAM.
Part of creating a provisioning bridge is installing the client for the bridge. The machine where you install this client must meet the following prerequisites:
  * Java 8 installed
  * Administrative rights to access the client network that the provisioning bridge uses to communicate with the apps that you want to monitor
  * Permissions to run the scripts that are used to install and start the provisioning bridge
  * Permissions to create, manage, and run commands in the folders associated with the machine where you install the client for the provisioning bridge
  * Permissions to manage log files associated with the provisioning bridge
  * The ability to communicate with both the identity domain server and the servers associated with the target apps (for example, the Oracle Internet Directory or Oracle E-Business Suite servers) 
  * Low network latency with these target servers

To create the provisioning bridge, follow these steps:
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. Select **Settings** and then select **Provisioning bridges**.
  4. If this is the first bridge you're creating, then select **Create Provisioning Bridge**.
  5. In the **Create provisioning bridge** panel, enter a name and description for the provisioning bridge. Then, select **Add**.
  6. In the **Provisioning bridge info** page, make a note of the identity domain URL, client ID, and client secret.
The URL contains the name and port number for the identity domain. The client ID and client secret are used by the provisioning bridge to access IAM as an administrator.
**Note** The client secret is encrypted (for security purposes). To see the secret in clear text, select **Show Secret**. To regenerate the secret for the bridge, select **Regenerate**.
  7. Select the link to the **Downloads** page.
The **Downloads** page opens.
  8. In the **Identity Cloud Service Provisioning Bridge** tile, select **Download**.
The Console downloads the client for the provisioning bridge to the folder that you choose.
  9. Verify that a **Success** message is displayed to show that the download is successful.
  10. Start the Windows or generic machine where you want to install the client for the provisioning bridge.
**Important** Ensure that you have administrative rights for this machine. Also, this machine communicates with the client network that the provisioning bridge uses to access the apps that you want to monitor.
  11. On this machine, create a folder, and then unzip the file that you downloaded into this folder. This zip file contains the client that you are to install for the provisioning bridge.
After you unzip the file, the following folders are created:
     * `bin:` This folder contains the `crossplatform.jar` file. This file is used by the installer to install, start, and stop the provisioning bridge.
     * `bundle_home:` This folder contains the connector JAR files that Oracle ships with the bridge. These files are used by the bridge to communicate with the apps.
     * `conf:` This folder contains two properties files:
       * `BridgeRuntimeConfigurations` contains properties associated with the provisioning bridge communicating with the identity domain and the target apps. Oracle recommends that you don't modify the contents of this file.
       * `log4j` contains properties associated with logging operations that the provisioning bridge performs.
     * `dependencies:` This folder contains the script files that the provisioning bridge uses to communicate with Oracle E-Business Suite for synchronization and provisioning purposes.
     * `logs:` This is the default folder is where all log files for the provisioning bridge are stored. You can change this folder and path by modifying the `log4j.properties` file.
The following files are also created:
     * `startup.bat:` Use this file to start the client for the provisioning bridge on a Windows (`.bat`) machine.
     * `startup.sh:` Use this file to start the client on a generic (`.sh`) machine.
     * `FileInfo.json:` This file contains version information about the zipped file that you downloaded. Oracle strongly recommends that you don't modify the contents of this file.
**Tip** While you're installing the client, IAM generates log files for the provisioning bridge automatically, and stores them in the `logs` folder.
  12. If you're installing the provisioning bridge on a generic machine, then open a Terminal window, navigate to the folder that you created in the previous step, and run the `./startup.sh install` command.
  13. If you're installing the provisioning bridge on a Windows machine, then open Windows Explorer, navigate to the folder that you created in the previous step, and double-click the `startup.bat` file.
  14. At the **Enter a password for Oracle Wallet** prompt, enter an Oracle Wallet password.
The wallet is a file that's used to store sensitive information such as the identity domain URL, client ID, and client secret securely.
**Note** After you install the provisioning bridge, a `wallet` folder is created, and the wallet you create is stored in this folder. When you start the provisioning bridge, instead of providing the identity domain URL, client ID, and client secret, you only have to supply the password for the Oracle Wallet.
  15. When prompted, enter this password again.
**Important** There's no mechanism to recover an Oracle Wallet password if you forget it. If this happens, delete the `wallet` folder and install the provisioning bridge again.
  16. At the next set of prompts, enter the URL, client ID, and client secret.
**Tip** These credentials appear on the provisioning bridge details page of the Console.
  17. If your organization has a firewall in place and requires communication to be handled using an HTTP proxy server, then when prompted, enter the full path (or address) of the proxy server, the port number reserved for this server, and the administrator credentials for connecting to the server.
If your organization doesn't require communication to be handled using an HTTP Proxy Server, then press **Enter** after each prompt to skip the prompt.
The bridge attempts to connect to the identity domain server.
If a connection can be established, then information about the bridge you created appears. This information includes the name, description, version number, URL of the identity domain, and the locations of the `log4j.properties` file and `bundle_home` folder.
Otherwise, you receive an error message, indicating that you entered an incorrect URL, client ID, or client secret. Modify the incorrect values, and try again. If the problem persists, then delete the Oracle Wallet you created, and repeat steps 12 or 13.


Was this article helpful?
YesNo


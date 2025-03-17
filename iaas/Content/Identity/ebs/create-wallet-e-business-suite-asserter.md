Updated 2023-06-08
# Creating a Wallet for the E-Business Suite Asserter
For security purposes, the E-Business Suite Asserter component uses a wallet to register the client ID, client secret, and IAM URL as parameters.
  1. Sign in to the E-Busine ss Suite Asserter application server machine, and navigate to the `/opt/ebssdk` folder.
Ensure the user has enough privileges to perform the following actions.
  2. Access the folder where the `idcs-wallet-<version>.jar` file is located.
  3. Run the command `java -jar                         idcs-wallet-<version>.jar`, and then provide the following values when prompted:
     * `Enter Client ID:` Enter the client ID generated while registering and activating the E-Business Suite Asserter in IAM.
     * `Enter Client Secret:` Enter the client secret for the client ID.
     * `Enter IDCS base URL:` Enter IAM base URL. For example: `https://**MYTENANT**.identity.oraclecloud.com`.
The command line creates a wallet file named `cwallet.sso` in the provided path.

Make note of the path of the `cwallet.sso` file.
Was this article helpful?
YesNo


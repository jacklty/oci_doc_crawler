Updated 2025-01-14
# Configuring FIDO Authenticator
Configure Fast ID Online (FIDO) authentication in an identity domain in IAM so that users can authenticate with an external authentication device such as a YubiKey, or an internal device such as Windows Hello or Mac Touch ID.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. On the domain details page, select **Security**.
  4. On the **Security** page, select **Two-factor authentication**.
  5. Select the **FIDO authenticator** tab.
  6. Configure the FIDO authenticator settings:
     * **Time-out (milliseconds):** The length of time in which the user must act. If the user doesn't act within this period, authentication fails. The default is 60,000 milliseconds (6 seconds).
     * **Attestation:** This is a key pair that belongs to the device and is assigned during manufacture. It's specific to the device model and used when the device is registered to prove the specific model. 
       * **None:** indicates that the relying party isn't interested in authenticator attestation.
       * **Indirect:** indicates that the relying party allows for anonymized attestation data.
       * **Direct:** indicates that the relying party wants to receive the attestation data from the authenticator.
     * **Authenticator selection attachment:** Controls the authenticator type a user registers with.
       * **Platform:** Select to use Windows Hello and Mac Touch ID.
       * **Cross-Platform:** Select to use a cross-platform authenticator such as YubiKey.
       * **Both:** This value is the default.
     * **Authenticator selection resident key:** Chooses whether support for a resident key is enabled and how.
       * **None:** (default) indicates that the private key is encrypted and stored on the server.
       * **Required:** indicates the relying party requires a client-side discoverable credential, and is prepared to receive an error if a client-side discoverable credential can't be created.
       * **Preferred:** indicates the relying party prefers creating a client-side discoverable credential, but would accept a server-side credential.
       * **Discouraged:** indicates the relying party prefers creating a server-side credential, but would accept a client-side discoverable credential.
     * **Authenticator selection user verification:** The relying party's requirements regarding user verification during registration.
       * **Required:** indicates that the relying party requires user verification for the operation or the operation fails.
       * **Preferred:** (default) indicates that the relying party prefers user verification for the operation if possible.
       * **Discouraged:** indicates that the relying party doesn't want user verification used during the operation.
     * **Public key types:** The cryptographic algorithm used to generate a public key pair during registration. IAM only certifies ES256 (the default), RS1, and RS256.
     * **Exclude credentials:** (disabled by default). Used by relying parties to limit the creation of multiple credentials for the same account on a single authenticator.
  7. Select **Save changes**.
  8. Confirm the changes when prompted.

FIDO authentication is now an additional sign-in factor
Was this article helpful?
YesNo


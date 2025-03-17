Updated 2023-08-02
# Upgrading App Gateway for Cloud Gate
Troubleshoot the upgrade path for high-availability with multiple App Gateways.
These are errors you might see if the Cloud Gate deployment mixes incompatible releases, for example, patching directly to R2, or to R3, without patching first to R1. In each case, the solution is to rollback and apply the patches in the correct order.
See [Upgrade Path for High Availability Deployments Using App Gateway Docker Image](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/upgrade-for_cloudgate.htm#upgrade-cloudgate "Upgrade path for deployments using App Gateway Docker Image.").
## Login Loop after Upgrade 🔗 
If there is an existing Cloud Gate Session, or IAM SSO session, or both, you may see a login loop similar to the loop caused by Cloud Gate Session cookies being too large.
When Cloud Gate cannot decrypt the existing Cloud Gate Session cookie, it will redirect to IAM to kick off authentication (see the `/oauth2/v1/authorize` request). 
The initial request to `/smoke/test/oauth/echo` goes to a Cloud Gate node that hasn't been patched to R1. As it cannot detect a valid Cloud Gate Session, the unpatched Cloud Gate redirects to IAM to log in. 
The Cloud Gate callback goes to the R2 Cloud Gate node. As the R2 release supports both Block Cipher modes of operation, it is able to decrypt the Cloud Gate State cookie and create a new Cloud Gate Session (encrypted using the new Block Cipher mode of operation).
The /smoke/test/oauth/echo replay request goes to the unpatched Cloud Gate node. And, again, it fails to decrypt the Cloud Gate Session cookie.
This is the login loop.
**Sample Logging from cg-trace-main.log**```
# The login loop is caused by the Cloud Gate Session cookie ( ORA_OCIS_CG_SESSION_ ) failing to decrypt:
[2022-04-07T20:10:04.971799+00:00] [trace3] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [SessionKeyManager.cpp] [357] [decryptSessionData] [] decryptSessionData: using default regional session key
[2022-04-07T20:10:04.971815+00:00] [trace3] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [SessionKeyManager.cpp] [628] [logSessionKey] [] SESSIONKEY(REGION-CRYPTO) - - TUPLE: attempting decrypt with keys
[2022-04-07T20:10:04.971823+00:00] [trace3] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [SessionKeyManager.cpp] [643] [logSessionKey] [] SESSIONKEY(REGION-CRYPTO) - - prevSHA256=9E30456BA34D76BD5CCBFF74DBF03C734EF4097B1A8725B146E76E99000984B0
[2022-04-07T20:10:04.971832+00:00] [trace3] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [SessionKeyManager.cpp] [645] [logSessionKey] [] SESSIONKEY(REGION-CRYPTO) - - currSHA256=9E30456BA34D76BD5CCBFF74DBF03C734EF4097B1A8725B146E76E99000984B0
[2022-04-07T20:10:04.971840+00:00] [trace3] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [SessionKeyManager.cpp] [647] [logSessionKey] [] SESSIONKEY(REGION-CRYPTO) - - nextSHA256=321846513AE2657C6E0AA36EDDE38AFE8BD1B10169D204CF495EDFFE50F1AEC2
[2022-04-07T20:10:04.971853+00:00] [trace3] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [SessionKeyManager.cpp] [649] [logSessionKey] [] SESSIONKEY(REGION-CRYPTO) - - expiry-loc-svr=2022-08-05 17:39:05
[2022-04-07T20:10:04.971871+00:00] [trace3] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [SessionKeyManager.cpp] [651] [logSessionKey] [] SESSIONKEY(REGION-CRYPTO) - - expiry-loc-fix=2022-08-05 17:39:05
[2022-04-07T20:10:04.971879+00:00] [trace3] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [SessionKeyManager.cpp] [653] [logSessionKey] [] SESSIONKEY(REGION-CRYPTO) - - expiry-loc-pad=2022-08-05 17:41:06
[2022-04-07T20:10:04.971887+00:00] [trace3] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [SessionKeyManager.cpp] [390] [decryptSessionData] [] decryptSessionData: using explicit crypto key
[2022-04-07T20:10:04.971978+00:00] [crit] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [SessionKeyManager.cpp] [628] [logSessionKey] [] CRITICAL - SESSIONKEY(REGION-CRYPTO) - - TUPLE: all keys failed (may be expected if old data)
[2022-04-07T20:10:04.971988+00:00] [crit] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [SessionKeyManager.cpp] [643] [logSessionKey] [] CRITICAL - SESSIONKEY(REGION-CRYPTO) - - prevSHA256=9E30456BA34D76BD5CCBFF74DBF03C734EF4097B1A8725B146E76E99000984B0
[2022-04-07T20:10:04.971996+00:00] [crit] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [SessionKeyManager.cpp] [645] [logSessionKey] [] CRITICAL - SESSIONKEY(REGION-CRYPTO) - - currSHA256=9E30456BA34D76BD5CCBFF74DBF03C734EF4097B1A8725B146E76E99000984B0
[2022-04-07T20:10:04.972004+00:00] [crit] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [SessionKeyManager.cpp] [647] [logSessionKey] [] CRITICAL - SESSIONKEY(REGION-CRYPTO) - - nextSHA256=321846513AE2657C6E0AA36EDDE38AFE8BD1B10169D204CF495EDFFE50F1AEC2
[2022-04-07T20:10:04.972027+00:00] [crit] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [SessionKeyManager.cpp] [649] [logSessionKey] [] CRITICAL - SESSIONKEY(REGION-CRYPTO) - - expiry-loc-svr=2022-08-05 17:39:05
[2022-04-07T20:10:04.972034+00:00] [crit] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [SessionKeyManager.cpp] [651] [logSessionKey] [] CRITICAL - SESSIONKEY(REGION-CRYPTO) - - expiry-loc-fix=2022-08-05 17:39:05
[2022-04-07T20:10:04.972041+00:00] [crit] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [SessionKeyManager.cpp] [653] [logSessionKey] [] CRITICAL - SESSIONKEY(REGION-CRYPTO) - - expiry-loc-pad=2022-08-05 17:41:06
[2022-04-07T20:10:04.972050+00:00] [fail] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [SessionKeyManager.cpp] [438] [decryptSessionData] [ORA_CG_2302 ORA_CG_2650 ORA_CG_1621] decryptSessionData: FAIL - all keys failed - SESSIONKEY(REGION-CRYPTO) dataKeyID=9E30456BA34D76BD5CCBFF74DBF03C734EF4097B1A8725B146E76E99000984B0
[2022-04-07T20:10:04.972062+00:00] [fail] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [EncodingEncryptor.cpp] [104] [decrypt] [ORA_CG_2302 ORA_CG_2650 ORA_CG_1621 ORA_CG_1664] decrypt failed (bad key/data?)
[2022-04-07T20:10:04.972067+00:00] [trace3] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [EncodingEncryptor.cpp] [108] [decrypt] [] decrypt: b64=3174 cry=2380 out=0 bytes
[2022-04-07T20:10:04.972074+00:00] [trace2] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [CookieBase.cpp] [117] [initializeFromRequest] [] Cookie decryption failed [name=ORA_OCIS_CG_SESSION_cgdev-tenant1_cgdev-tenant1.cgdevcloud.test]
[2022-04-07T20:10:04.972087+00:00] [trace2] [P:290] [T:0] [E:1.ae9c054fa6fe4419bc5e1857e94958ed;kXjE] [CookieManager.cpp] [41] [createCookie] [] Added cookie [name=ORA_OCIS_CG_SESSION_cgdev-tenant1_cgdev-tenant1.cgdevcloud.test] [type=SESSION] [initialized=0] [existsInRequest=1] [valid=0] [last-status=ERR_Decrypt_Failed] to CookieManager
```

## Cross-Domain Log out Failure 🔗 
The cross-domain logout flow may fail when the following conditions are met:
  * Third party cookies are disabled.
  * There is a Cloud Gate NGINX server which has been patched to R2.
  * There are two Cloud Gate NGINX servers which haven't been patched.


When the R2 server initiates logout, the unpatched nodes fail to decrypt the `LOGOUT_DATA` post body submitted to Cloud Gate by IAM.
The cg-trace-main.log file notes decryption failures, such as:
  * `all keys failed (may be expected if old data)`
  * `decrypt failed (bad key/data?)`


## Failed Login after Upgrade 🔗 
After successfully signing into IAM, the Cloud Gate callback (`cloudgate/v1/oauth2/callback`) returns 401 if Cloud Gate is unable to decrypt the State cookie.
**Sample Logging from cg-trace-main.log**
```
# First, the Cloud Gate State cookie ( ORA_OCIS_CG_ST_ ) will fail to decrypt:
[2022-04-07T18:42:34.618617+00:00] [trace3] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [SessionKeyManager.cpp] [390] [decryptSessionData] [] decryptSessionData: using explicit crypto key
[2022-04-07T18:42:34.618693+00:00] [crit] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [SessionKeyManager.cpp] [628] [logSessionKey] [] CRITICAL - SESSIONKEY(REGION-CRYPTO) - - TUPLE: all keys failed (may be expected if old data)
[2022-04-07T18:42:34.618705+00:00] [crit] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [SessionKeyManager.cpp] [643] [logSessionKey] [] CRITICAL - SESSIONKEY(REGION-CRYPTO) - - prevSHA256=9E30456BA34D76BD5CCBFF74DBF03C734EF4097B1A8725B146E76E99000984B0
[2022-04-07T18:42:34.618713+00:00] [crit] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [SessionKeyManager.cpp] [645] [logSessionKey] [] CRITICAL - SESSIONKEY(REGION-CRYPTO) - - currSHA256=9E30456BA34D76BD5CCBFF74DBF03C734EF4097B1A8725B146E76E99000984B0
[2022-04-07T18:42:34.618722+00:00] [crit] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [SessionKeyManager.cpp] [647] [logSessionKey] [] CRITICAL - SESSIONKEY(REGION-CRYPTO) - - nextSHA256=321846513AE2657C6E0AA36EDDE38AFE8BD1B10169D204CF495EDFFE50F1AEC2
[2022-04-07T18:42:34.618733+00:00] [crit] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [SessionKeyManager.cpp] [649] [logSessionKey] [] CRITICAL - SESSIONKEY(REGION-CRYPTO) - - expiry-loc-svr=2022-08-05 17:39:05
[2022-04-07T18:42:34.618741+00:00] [crit] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [SessionKeyManager.cpp] [651] [logSessionKey] [] CRITICAL - SESSIONKEY(REGION-CRYPTO) - - expiry-loc-fix=2022-08-05 17:39:05
[2022-04-07T18:42:34.618748+00:00] [crit] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [SessionKeyManager.cpp] [653] [logSessionKey] [] CRITICAL - SESSIONKEY(REGION-CRYPTO) - - expiry-loc-pad=2022-08-05 17:41:06
[2022-04-07T18:42:34.618758+00:00] [fail] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [SessionKeyManager.cpp] [438] [decryptSessionData] [ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621 ORA_CG_1664 ORA_CG_2652 ORA_CG_2656 ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621 ORA_CG_1664 ORA_CG_2652 ORA_CG_2656 ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621] decryptSessionData: FAIL - all keys failed - SESSIONKEY(REGION-CRYPTO) dataKeyID=9E30456BA34D76BD5CCBFF74DBF03C734EF4097B1A8725B146E76E99000984B0
[2022-04-07T18:42:34.618786+00:00] [fail] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [EncodingEncryptor.cpp] [104] [decrypt] [ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621 ORA_CG_1664 ORA_CG_2652 ORA_CG_2656 ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621 ORA_CG_1664 ORA_CG_2652 ORA_CG_2656 ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621 ORA_CG_1664] decrypt failed (bad key/data?)
[2022-04-07T18:42:34.618793+00:00] [trace3] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [EncodingEncryptor.cpp] [108] [decrypt] [] decrypt: b64=547 cry=410 out=0 bytes
[2022-04-07T18:42:34.618801+00:00] [trace2] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [CookieBase.cpp] [117] [initializeFromRequest] [] Cookie decryption failed [name=ORA_OCIS_CG_ST_cgdev-tenant1_cgdev-tenant1.cgdevcloud.test]
[2022-04-07T18:42:34.618815+00:00] [trace2] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [CookieManager.cpp] [41] [createCookie] [] Added cookie [name=ORA_OCIS_CG_ST_cgdev-tenant1_cgdev-tenant1.cgdevcloud.test] [type=REQUEST_STATE] [initialized=0] [existsInRequest=1] [valid=0] [last-status=ERR_Decrypt_Failed] to CookieManager
 
# Next, the ID Token from IDCS will fail to decrypt:
[2022-04-07T18:42:34.624873+00:00] [trace3] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [OAuthFlows.cpp] [3398] [getIdTokenInImplicitFlow] [] IDCS_CG_ENC isSecretKey=1
[2022-04-07T18:42:34.625048+00:00] [trace3] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [SessionKeyManager.cpp] [628] [logSessionKey] [] SESSIONKEY(REGION-SECRET) - - TUPLE: attempting decrypt with keys
[2022-04-07T18:42:34.625061+00:00] [trace3] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [SessionKeyManager.cpp] [637] [logSessionKey] [] SESSIONKEY(REGION-SECRET) - - currSHA256=
[2022-04-07T18:42:34.625069+00:00] [trace3] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [SessionKeyManager.cpp] [395] [decryptSessionData] [] decryptSessionData: using explicit regional secret
[2022-04-07T18:42:34.625154+00:00] [crit] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [SessionKeyManager.cpp] [628] [logSessionKey] [] CRITICAL - SESSIONKEY(REGION-SECRET) - - TUPLE: all keys failed (may be expected if old data)
[2022-04-07T18:42:34.625168+00:00] [crit] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [SessionKeyManager.cpp] [637] [logSessionKey] [] CRITICAL - SESSIONKEY(REGION-SECRET) - - currSHA256=
[2022-04-07T18:42:34.625177+00:00] [fail] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [SessionKeyManager.cpp] [438] [decryptSessionData] [ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621 ORA_CG_1664 ORA_CG_2652 ORA_CG_2656 ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621 ORA_CG_1664 ORA_CG_2652 ORA_CG_2656 ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621 ORA_CG_1664 ORA_CG_2652 ORA_CG_2656 ORA_CG_2641 ORA_CG_2642 ORA_CG_1621] decryptSessionData: FAIL - all keys failed - SESSIONKEY(REGION-SECRET) dataKeyID=28C0F2CE5E3B385F9F28E7BED8EC26C5B171E1D65E66FCD2400112EB6B743EAD
[2022-04-07T18:42:34.625220+00:00] [fail] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [EncodingEncryptor.cpp] [104] [decrypt] [ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621 ORA_CG_1664 ORA_CG_2652 ORA_CG_2656 ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621 ORA_CG_1664 ORA_CG_2652 ORA_CG_2656 ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621 ORA_CG_1664 ORA_CG_2652 ORA_CG_2656 ORA_CG_2641 ORA_CG_2642 ORA_CG_1621 ORA_CG_1664] decrypt failed (bad key/data?)
[2022-04-07T18:42:34.625225+00:00] [trace3] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [EncodingEncryptor.cpp] [108] [decrypt] [] decrypt: b64=2748 cry=2061 out=0 bytes
[2022-04-07T18:42:34.625233+00:00] [trace1] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [OAuthFlows.cpp] [3421] [getIdTokenInImplicitFlow] [ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621 ORA_CG_1664 ORA_CG_2652 ORA_CG_2656 ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621 ORA_CG_1664 ORA_CG_2652 ORA_CG_2656 ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621 ORA_CG_1664 ORA_CG_2652 ORA_CG_2656 ORA_CG_2641 ORA_CG_2642 ORA_CG_1621 ORA_CG_1664 ORA_CG_2551] id_token decode-and-decryption failed
[2022-04-07T18:42:34.625246+00:00] [trace1] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [OAuthFlows.cpp] [3683] [completeOauthBrowserFlow] [ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621 ORA_CG_1664 ORA_CG_2652 ORA_CG_2656 ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621 ORA_CG_1664 ORA_CG_2652 ORA_CG_2656 ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621 ORA_CG_1664 ORA_CG_2652 ORA_CG_2656 ORA_CG_2641 ORA_CG_2642 ORA_CG_1621 ORA_CG_1664 ORA_CG_2551 ORA_CG_2534] Could not get ID token
 
# Cloud Gate will attempt to retry the login flow, but this fails as the State cookie failed to decrypt:
[2022-04-07T18:42:34.625251+00:00] [trace1] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [OAuthFlows.cpp] [3686] [completeOauthBrowserFlow] [] Retrying /authorize
[2022-04-07T18:42:34.625255+00:00] [trace2] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [OAuthFlows.cpp] [3314] [retryOauthBrowserFlow] [] Entry
[2022-04-07T18:42:34.625263+00:00] [trace1] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [OAuthFlows.cpp] [3276] [validateStateCookie] [ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621 ORA_CG_1664 ORA_CG_2652 ORA_CG_2656 ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621 ORA_CG_1664 ORA_CG_2652 ORA_CG_2656 ORA_CG_2302 ORA_CG_2650 ORA_CG_2653 ORA_CG_2651 ORA_CG_1621 ORA_CG_1664 ORA_CG_2652 ORA_CG_2656 ORA_CG_2641 ORA_CG_2642 ORA_CG_1621 ORA_CG_1664 ORA_CG_2551 ORA_CG_2534 ORA_CG_2539] State cookie invalid
[2022-04-07T18:42:34.625268+00:00] [trace2] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [OAuthFlows.cpp] [3347] [retryOauthBrowserFlow] [] Second retry
[2022-04-07T18:42:34.625272+00:00] [trace2] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [OAuthFlows.cpp] [3354] [retryOauthBrowserFlow] [] Exit, success=0
[2022-04-07T18:42:34.625284+00:00] [trace3] [P:290] [T:0] [E:1.0448b21d2f58bc605049585de68f149d;kXjE] [PlatformUtil.cpp] [602] [addResponseHeader] [] www-authenticate: Bearer error="invalid_session", error_description="Authentication Failure"
```

Was this article helpful?
YesNo


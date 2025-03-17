Updated 2024-04-02
# Client/User JWT Assertion
An assertion is a package of information that facilitates the sharing of identity and security information across security domains. An assertion typically contains information about a subject or principal, information about the party that issued the assertion and when it was issued. It also contains information about the conditions under which the assertion is to be considered valid, such as when and where it can be used. The intent is to provide an alternative client authentication mechanism. Clients can build client assertions and use them as credentials rather than using the client ID and client secret in an OAuth token request.
Identity domains support the use of client and user assertions for authentication. The following information defines the format of the client assertion and the user assertion, including standard and custom claims. Names with (*) are proprietary to Oracle.
## Client/User Assertion Headers 🔗 
Name | Value  
---|---  
`kid` | Key identifier. Used to identify the trusted third-party certificate to validate the assertion signature. The `x5t` or `kid` claim must be present in the JWT assertion header.  
`type` | Type. Identifies the type of assertion, which is always `JWT`.  
`alg` | Algorithm. Identifies the specific type of JWT signing algorithm. This is a required header for the JWT assertion. Identity domains support RS256.  
`x5t` | Base64 URL encoded X.509 certificate sha1 thumbprint. This is used to identify specific certificates. The `x5t` or `kid` claim must be present in the JWT assertion header.  
## JWT Body/Claims 🔗 
Name | Value  
---|---  
`sub` | Subject. The principal that's the subject of the JWT: For client assertions, the client ID value must be the identity domain App `name` attribute. For user assertions, the claim value must be the username.  
`iss` | Issuer. The Client that's generating the assertions (identity domain App `name` attribute). This is a required claim for the assertion.  
`aud` | Audience. Identifies the recipients for which the JWT is intended. The identity domain URL (`https://<domainURL>`) must be one of the `aud` claim values.  
`exp` | Expiration. The time (UNIX epoch time) when the JWT assertion expires. This is a required claim for the assertion.  
`iat` | Issued at. The date when the assertion was issued.   
**Sample JWT Client Assertion**
```
{ 
  "kid": "SampleOAuthClient_1",
  "typ": "JWT",
  "alg": "RS256",
  "x5t": "fa4c3b48128f0a88cb8e3c37fbcd02d341080e4f33f081dc546886e7f4bc26aa"
}
{ 
"aud": ["https://<domainURL>/"],
    "sub": "60da13c1-6f27-41e2-bc4e-9cdbccbb4251",
    "iss": "60da13c1-6f27-41e2-bc4e-9cdbccbb4251",
    "exp": "1598229425738",
    "iat": "1440549425738",
    "jti": "bbd28459-5ba9-4dfb-bfeb-8141eca853c4"
}
```

**Sample JWT User Assertion**
```
{
 "kid": "SampleOAuthClient_1",
 "typ": "JWT",
 "alg": "RS256",
 "x5t": "fa4c3b48128f0a88cb8e3c37fbcd02d341080e4f33f081dc546886e7f4bc26aa"
}
{
 "aud": ["https://<domainURL>/"],
 "sub": "test@oracle.com",
 "iss": "60da13c1-6f27-41e2-bc4e-9cdbccbb4251",
 "exp": "1598229425738",
 "iat": "1440549425738",
 "jti": "bbd28459-5ba9-4dfb-bfeb-8141eca853c4"
}
```

## Generating User and Client Assertions Using a Signing Key 🔗 
**Before You Begin**
Ensure that you have the following installed.
  1. GlassFish javax.json-1.0.4 library
  2. JDK 8 to perform the base64 encoding/decoding.


**Note:** It's not necessary to generate a signed client assertion if the client can authenticate using client ID & client secret. You need to decide how to authenticate the client by using the client ID/client secret or by using PKI.
**Assertion Generator Lightweight JDK8**
```
import java.io.ByteArrayInputStream;
import java.nio.charset.StandardCharsets;
import java.security.InvalidKeyException;
import java.security.KeyFactory;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.Signature;
import java.security.SignatureException;
import java.security.cert.CertificateEncodingException;
import java.security.cert.CertificateException;
import java.security.cert.CertificateFactory;
import java.security.cert.X509Certificate;
import java.security.interfaces.RSAPrivateKey;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.PKCS8EncodedKeySpec;
import java.util.Arrays;
import java.util.Base64;
import java.util.Date;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import javax.json.Json;
import javax.json.JsonArrayBuilder;
import javax.json.JsonObject;
import javax.json.JsonObjectBuilder;
 
/**
 *
 * Sample class to generate assertions suitable for IDCS jwt-bearer style OAuth
 * Requires JDK8 in order to perform the Base64 encoding/decoding
 *
 * JSON dependency is javax.json-1.0.4.jar
 * http://central.maven.org/maven2/org/glassfish/javax.json/1.0.4/javax.json-1.0.4.jar
 *
 * Assumptions - self-signed keypair generated using something like ..
 *
 * KEY_ALG=RSA
 * SIG_ALG=SHA256withRSA
 *
 * ${JAVA_HOME}/bin/keytool -genkeypair -v -keystore .... -storetype PKCS12 -storepass .... \
 * -keyalg ${KEY_ALG} -keysize 2048 -sigalg ${SIG_ALG} -validity 1825 \
 * -alias ... -keypass .... -dname ...."
 *
 * Using client and user assertion output from this class, obtain access token using something like ....
 *
 * grant_type='urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer'
 * user_assertion='XXXXXXX.YYYYYYY.ZZZZZZZZ'
 * client_assertion_type='urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer'
 * client_assertion='AAAAAAA.BBBBBBB.CCCCCCCC'
 * client_id='31282cbe9858409ab5b5a6020e85ccb6'
 * scope='urn:opc:entitlementid=999999999urn:opc:resource:consumer::all'
 *
 * oauth_payload="grant_type=${grant_type}&assertion=${user_assertion}&client_assertion_type=${client_assertion_type}&client_assertion=${client_assertion}&client_id=${client_id}&scope=${scope}"
 *
 * oauth_url='https://idcs-XXXXXXXXXXXX.YYYYYY.com/oauth2/v1/token'
 *
 * curl -i
-H "Content-Type:application/x-www-form-urlencoded;charset=UTF-8" --request POST ${oauth_url} -d ${oauth_payload}
 */
public class AssertionGeneratorLightweightJdk8
{
  // Client certificate in raw form - obtained from the Generate Self-Signed Keypair section
  static String CLIENT_CERT =
    "MIIDtzCCAp+gAwIBAgIENeogPjANBgkqhkiG9w0BAQsFADCBizELMAkGA1UEBhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExFzAVBgNVBAcTDlJlZHdvb2QgU2hvcmVzMRswGQYDVQQKExJPcmFjbGUgQ29ycG9yYXRpb24xDDAKBgNVBAsTA0lETTEjMCEGA1UEAxMac2xleHRjb21wMTMgQ0VDUyBBc3NlcnRpb24wHhcNMTgwODE1MTAyMDQ1WhcNMjMwODE0MTAyMDQ1WjCBizELMAkGA1UEBhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExFzAVBgNVBAcTDlJlZHdvb2QgU2hvcmVzMRswGQYDVQQKExJPcmFjbGUgQ29ycG9yYXRpb24xDDAKBgNVBAsTA0lETTEjMCEGA1UEAxMac2xleHRjb21wMTMgQ0VDUyBBc3NlcnRpb24wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCT+xQU6S+KzjunLPFuvfpy86BxNcUJp8EppGORDR3VrjNH69G3hVF18gV9J/XAVtPApP4n+ZRRQvaFuzwjaXHf3vZ10wEu/N0RIE3zIq98CBMyRp2C8orTYuboN1pQGjieAEBHe2kp7Y1Jkc2UtircRHSpOBDp7KwuwLlHmlBXC4clF6nzFq8UZ9hg4UkA5+lDR70esRAEgrDxJpnSjp27cJFhZHP8oaLQ+ai4wvg9UReUns/mTcNwc6Acv/HPK+d9m9AEzj7ItAVYhnfhQVZ4fUr/AiAvAT43Pv0ZqEHlyByjqauIYp8O+kvtCC68A4mGMHDUNxvVq10Bs7SozaWzAgMBAAGjITAfMB0GA1UdDgQWBBT8O+7161UPiGFbrsEh0Rua0JJezTANBgkqhkiG9w0BAQsFAAOCAQEAAoh+ThSg3Jk4el/RHCOOJZ1pbSMKjmmzWC46Ca8tpjdJ4iaOYrXe+QQmyUvfp/hGcKdvbvex/Ot19d4TxMwNHxapxPfllKDd8WYzMdBc1th8JLxeGXHYfRhk1ImHQWDW9B1K2x2JC/03Wtg/d+Ipno97ydnzcz1+Ef1HEuG4A8WmXS2GBppldZxIeI4XMqi9nKxyDZX+WQPi6RgbpLkizY3krcHUbdwsuWKoc2JATST8XgUx5hw2znlFezt60+7uXnFbfU72WgYrzwrr8NWiR6d9LLP9t5R9odY2Q4WoifwzljkslpYZ0hjWFuvRdLK/XLzb0hLiU0m15oZz9kQWqw==";
 
  // PKCS8 version of the private key in raw form - obtained from the Generate Self-Signed Keypair section
  
static String CLIENT_PRIVATE_KEY =
    "MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCT+xQU6S+KzjunLPFuvfpy86BxNcUJp8EppGORDR3VrjNH69G3hVF18gV9J/XAVtPApP4n+ZRRQvaFuzwjaXHf3vZ10wEu/N0RIE3zIq98CBMyRp2C8orTYuboN1pQGjieAEBHe2kp7Y1Jkc2UtircRHSpOBDp7KwuwLlHmlBXC4clF6nzFq8UZ9hg4UkA5+lDR70esRAEgrDxJpnSjp27cJFhZHP8oaLQ+ai4wvg9UReUns/mTcNwc6Acv/HPK+d9m9AEzj7ItAVYhnfhQVZ4fUr/AiAvAT43Pv0ZqEHlyByjqauIYp8O+kvtCC68A4mGMHDUNxvVq10Bs7SozaWzAgMBAAECggEARy0C0bP/HAJqCtTBI4TZC6VGzG0SYrx/WiopgcEPUpHBNJymeGD1d4d7QGGSAHtCymwRmuSehB9zN4uBN38mOImjfbSJ4zHYmr4w//r08PFpWktAw5UpVNdDPPoyxEh4Zvaz9C3VvUb3KCWq/hZIsz1x51qCOCGQB8TG2TvN3K+BP0zzB0IPRqI7b3ydxLFJ8Hn9Y1HRd/8fi11wiPlHtVwMhKXrqnTiaZTayUW9ARPgLK4ZajtUM5FNC8PRTZqxkMge9qC4Q8067zuIMZhHeRR8bLS/5MHSae6/uR0vZOg9nWmRj6Zq33tlflaPcSer/RWlAY5AygQGFveVJc8fQQKBgQDN5jJQPyPcHN+mopJxO5P0c5f69sv8J4hG05qC1I66P5w+TkZZJQYJGMJbazrDmgHigcrbNdUnjYhrNyOipzaYaSye8FRrmgpTZY1nwlY5qj5HHi5GNjbMq/OJKbs46mBu3aSl3K1d0ujAv+rxUofd9PwNjmBMyfNr95h3Jmew0QKBgQC3/Qv02c0e4RrdWVfpi71AiUqmMQ/nKj1SVQ54XQU6FY0y9RTYENN7+b6mFYHJm9B9CkQPx4NsScmQK/ucvE1ZxZANeFaOENAiq06A+0tj31FGoDBIihVYUkHnrupiJz8ug+9c4jwUoho95V6/iLVnRu4a70Wc97N1LnGeG/QvQwKBgH7GXfRK7Cl7HbncH47YwCCji9BaZP682IvDfj9P4RGMWQeD6oy43x56wDDJtUT6bm6ou959JuFTo8tgB/D+Q/9TwsWZ9GDMV89Bl+9rGOwohnADhTp15wfeV/T8XOqOZRHeJqJ5XcWHNwh3IpGz3zQqw4cVQvYE4nx31siGPRIBAoGAIgDSRN472okfvejVJoR85YB6G1zV45Ma4ix2ECig3qs8/T3uLEBv1WnCok83PVtenL1Y9tGYqFq6tbprNfxXD1BD3zluRbM1xDKEv7GxrTOIgdT5F27tovUQ2RCqoJlARAh+JFxrXiTXVLkfWaaaYAvr1W6DHw9oSy/aL65a4qECgYB85lE4sKn2g97W7i51w7rNZwRPr0WcwDz2ecuXOFaURw9g/+8duD9Cq4zMcxwNSjc/kPbxNrY3PKcbZm2Guq6KSiF6Svg8valbMuEadOar/4CZeGyHy8tfYHRGxHP5w2Bh1HbCVQvjC3IzAZJi6pjknz7HuIdOkuhCcSRGjLhurQ==";
 
static String KEY_ID = "cecsassertionkey"; // the alias/key we registered the public certificate under
 
static String CLIENT_ID = "31282cbe9858409ab5b5a6020e85ccb6"; // the trusted client ID
 
static String USER_NAME = "abc@xyz.com"; // the user whom we want to assert identity for
 
static List<String> AUDIENCE_LIST = Arrays.asList("<domainURL>/");
 
  // JSON Web Token Claims ...
  private static final String ISSUER_CLAIM = "iss";
  private static final String SUBJECT_CLAIM = "sub";
  private static final String AUDIENCE_CLAIM = "aud";
  private static final String EXPIRATION_TIME_CLAIM = "exp";
  private static final String NOT_BEFORE_CLAIM = "nbf";
  private static final String ISSUED_AT_CLAIM = "iat";
  private static final String JWT_ID_CLAIM = "jti";
 
  // JSON Web Token Header Parameters
  private static final String ALGORITHM_HEADER = "alg";
  private static final String KEY_ID_HEADER = "kid";
  private static final String X509CERT_SHA1_HEADER = "x5t";
  private static final String X509CERT_SHA256_HEADER = "x5t#S256";
 
  public static void main(String[] args) throws Exception
  {
    Date now = new Date();
 
    Date expirationTime = new Date((60 * 60 * 1000) + now.getTime()); // (1 hour from current time)
 
    JsonObject clientClaims = buildJWTClaims(CLIENT_ID, CLIENT_ID, AUDIENCE_LIST, expirationTime, now, now,
      UUID.randomUUID().toString());
 
    System.out.println(clientClaims.toString());
 
    // Call the method to generate the assertions for both client and user assertions
    String clientAssertion = generateAndSignJWTAssertion(CLIENT_PRIVATE_KEY, CLIENT_CERT, KEY_ID, clientClaims);
 
    System.out.println("Trusted Client Signed Client Assertion:" + clientAssertion);
 
    JsonObject userClaims = buildJWTClaims(CLIENT_ID, USER_NAME, AUDIENCE_LIST, expirationTime, now, now,
      UUID.randomUUID().toString());
    System.out.println(userClaims.toString());
 
    String userAssertion = generateAndSignJWTAssertion(CLIENT_PRIVATE_KEY, CLIENT_CERT, KEY_ID, userClaims);
 
    System.out.println("Trusted Client Signed User Assertion: " + userAssertion);
  }
 
  // Builds JsonObject with the list of claims
  static JsonObject buildJWTClaims(
    String issuer,
    String subject,
    List<String> audience,
    Date expirationTime,
    Date notBefore,
    Date issuedAt,
    String jwtId
  )
  {
    Map<String, Object> claims = new LinkedHashMap<>();
 
    claims.put(ISSUER_CLAIM, issuer);
    claims.put(SUBJECT_CLAIM, subject);
    claims.put(AUDIENCE_CLAIM, audience);
    claims.put(EXPIRATION_TIME_CLAIM, expirationTime);
    claims.put(NOT_BEFORE_CLAIM, notBefore);
    claims.put(ISSUED_AT_CLAIM, issuedAt);
    claims.put(JWT_ID_CLAIM, jwtId);
 
    return createJsonObjectFromMap(claims);
  }
 
public static String generateAndSignJWTAssertion(
    final String base64EncodedPrivateKey,
    final String base64EncodedCertificate,
    final String keyID,
    final JsonObject claims
) throws CertificateException, NoSuchAlgorithmException, InvalidKeySpecException, InvalidKeyException,
    SignatureException
{
  // Get the certificate from certificate factory
    CertificateFactory certificateFactory = CertificateFactory.getInstance("X.509");
    X509Certificate certificate = (X509Certificate) certificateFactory.generateCertificate(
      new ByteArrayInputStream(Base64.getDecoder().decode(base64EncodedCertificate)));
 
    KeyFactory keyFactory = KeyFactory.getInstance("RSA");
    RSAPrivateKey privateKey = (RSAPrivateKey) keyFactory.generatePrivate(
      new PKCS8EncodedKeySpec(Base64.getDecoder().decode(base64EncodedPrivateKey)));;
 
    // NOTE returned Strings may be padded at end with potentially 0, 1, or 2 trailing '=' signs.
    String base64X5TUrl = getCertificateDigestAsURLSafeBase64EncodedString(certificate, "SHA-1");
 
    String base64X5T256Url = getCertificateDigestAsURLSafeBase64EncodedString(certificate, "SHA-256");
 
    // Populate the header for signing
    Map<String, Object> headers = new LinkedHashMap<>();
 
    headers.put(ALGORITHM_HEADER, "RS256");
    headers.put(KEY_ID_HEADER, keyID);
    headers.put(X509CERT_SHA1_HEADER, base64X5TUrl);
    headers.put(X509CERT_SHA256_HEADER, base64X5T256Url);
 
    JsonObject header = createJsonObjectFromMap(headers);
    System.out.println(header.toString());
 
    String signingInput = toBase64URLSafe(header.toString().getBytes(StandardCharsets.UTF_8), true) + '.'
      + toBase64URLSafe(claims.toString().getBytes(StandardCharsets.UTF_8), true);
 
    Signature signer = Signature.getInstance("SHA256withRSA");
    signer.initSign(privateKey);
    signer.update(signingInput.getBytes(StandardCharsets.UTF_8));
 
    String signature = toBase64URLSafe(signer.sign(), true);
 
    String assertion = signingInput + '.' + signature;
 
    return assertion;
}
 
static JsonObject buildJWTHeader(
    String issuer,
    String subject,
    List<String> audience,
    Date expirationTime,
    Date notBefore,
    Date issuedAt,
    String jwtId
)
{
    Map<String, Object> claims = new LinkedHashMap<>();
 
    claims.put(ISSUER_CLAIM, issuer);
    claims.put(SUBJECT_CLAIM, subject);
    claims.put(AUDIENCE_CLAIM, audience);
    claims.put(EXPIRATION_TIME_CLAIM, expirationTime);
    claims.put(NOT_BEFORE_CLAIM, notBefore);
    claims.put(ISSUED_AT_CLAIM, issuedAt);
    claims.put(JWT_ID_CLAIM, jwtId);
 
    return createJsonObjectFromMap(claims);
}
 
private static JsonObject createJsonObjectFromMap(Map<String, Object> map)
{
    JsonObjectBuilder builder = Json.createObjectBuilder();
 
    for (Map.Entry<String, Object> claim : map.entrySet())
    {
      String key = claim.getKey();
      Object value = claim.getValue();
      if (value == null)
      {
        continue;
      }
 
      if (value instanceof String)
      {
        builder.add(key, (String) value);
      }
      else if (value instanceof Date)
      {
        builder.add(key, Long.valueOf(((Date) value).getTime() / 1000L)); // seconds since epoch
      }
      else if (value instanceof List)
      {
        List<String> list = (List<String>) value;
        if (list.size() == 0)
        {
          continue;
        }
        else if (list.size() == 1)
        {
          String listVal = list.get(0);
          if (listVal != null)
          {
            builder.add(key, list.get(0));
          }
        }
        else
        {
          JsonArrayBuilder arrayBuilder = Json.createArrayBuilder();
          for (String listVal : list)
          {
            if (listVal != null)
            {
              arrayBuilder.add(listVal);
            }
          }
 
          builder.add(key, arrayBuilder);
        }
      }
    }
 
    return builder.build();
}
 
public static String getCertificateDigestAsURLSafeBase64EncodedString(
    X509Certificate certificate,
    String hashAlg
) throws NoSuchAlgorithmException, CertificateEncodingException
{
    // hash algorithm "SHA-1" or "SHA-256"
    byte[] certificateEncoded = certificate.getEncoded();
 
    byte[] digest = MessageDigest.getInstance(hashAlg).digest(certificateEncoded);
 
    return toBase64URLSafe(digest, true);
}
 
public static String toBase64URLSafe(byte[] bytes, boolean removePadding)
{
    String base64URLSafeString = Base64.getUrlEncoder().encodeToString(bytes);
 
    return removePadding
      ? trimTrailingBase64Padding(base64URLSafeString)
      : base64URLSafeString;
}
 
public static String trimTrailingBase64Padding(String b64EncodedString)
{
    if (b64EncodedString != null)
    {
      if (b64EncodedString.endsWith("=="))
      {
        return b64EncodedString.substring(0, b64EncodedString.length() - 2);
      }
      else if (b64EncodedString.endsWith("="))
      {
        return b64EncodedString.substring(0, b64EncodedString.length() - 1);
      }
    }
 
    return b64EncodedString;
  }
}

```

## Sample Output and Decoding from Assertion Java Code 🔗 
**Trusted Client Signed User Assertion** ```
eyJhbGciOiJSUzI1NiIsImtpZCI6ImNlY3Nhc3NlcnRpb25rZXkiLCJ4NXQiOiJ4YWhmUG1xOXJqaGlya3V5YldzMXJra1oxZW8iLCJ4NXQjUzI1NiI6InFXbS12X251b3JsNDM3Nlk1LWlTY3hPd3lwVXp5bDB4Y1NsS0Nucm5xX0kifQ.eyJpc3MiOiIzMTI4MmNiZTk4NTg0MDlhYjViNWE2MDIwZTg1Y2NiNiIsInN1YiI6InNoYXVuLmxpbkBvcmFjbGUuY29tIiwiYXVkIjoiaHR0cHM6Ly9pZGVudGl0eS5vcmFjbGVjbG91ZC5jb20vIiwiZXhwIjoxNTM0NDc5ODU0LCJuYmYiOjE1MzQ0NzYyNTQsImlhdCI6MTUzNDQ3NjI1NCwianRpIjoiNmZhOWE3MGYtNTU4Yy00YzkzLWJhYzctYzZhNjcyYTA1OTkyIn0.hCTvkcA_wwSCTAM1mHa4Bib2bcdbyGBdTnJpGJ9oXqh3Tp60Jh5izwvv1Pj3GwUm1QmeAIW-GwKlwZWLuCWOEmj53FByial14E9_4_ZJGc870MGlmCTx-WzvuEMk-wWaRhtjichtYC4ofyl00qzg3Cw3WljfN-Zm4EkLJmgkjL8YflFB7qRwmFfi_X_AMjq_FSI8QPIRZqf9HOcLGLXkSqYLsDh1sEv9Og3PbGkmwRA2Zaq6waP7Izzx0ge5IfQdBIotv76IPJ0cyIVUbfhCc-TO71WqrWlfCA2dZxC7nCE0y01NBYPpaMm8kGj71lWHrIn0yfULJgYS0-lPOiAMYg
```

**Trusted Client Signed Client Assertion** ```
eyJhbGciOiJSUzI1NiIsImtpZCI6ImNlY3Nhc3NlcnRpb25rZXkiLCJ4NXQiOiJ4YWhmUG1xOXJqaGlya3V5YldzMXJra1oxZW8iLCJ4NXQjUzI1NiI6InFXbS12X251b3JsNDM3Nlk1LWlTY3hPd3lwVXp5bDB4Y1NsS0Nucm5xX0kifQ.eyJpc3MiOiIzMTI4MmNiZTk4NTg0MDlhYjViNWE2MDIwZTg1Y2NiNiIsInN1YiI6IjMxMjgyY2JlOTg1ODQwOWFiNWI1YTYwMjBlODVjY2I2IiwiYXVkIjoiaHR0cHM6Ly9pZGVudGl0eS5vcmFjbGVjbG91ZC5jb20vIiwiZXhwIjoxNTM0NDc5ODU0LCJuYmYiOjE1MzQ0NzYyNTQsImlhdCI6MTUzNDQ3NjI1NCwianRpIjoiYTliZGVjZGQtNWNjZS00ZjJkLTk3MTAtMjY2MWYxMGFhYmQxIn0.JvzZaeD1pS2KMrrh2CzdQk61oj04XeRXZOlMfSDDEpmaw6gSys1DrbiOWa4IPircHMRGskQ-SbGTH3IdZ_UqPgPmjDL46EpGg_1i90l-GUepnFpoUTwuUX0uDWGijrpxIF-n0DyyxipVbwVBNbduPm4vd4Gzz2r59O_0xh46DWF1KnIHyKUXiEQBwZl269ZpoFUiPPhaswOzWphYttMixUGzcsvSijPMOdPmbaSrGKXk0vBlxJqJnzQInQ_Kyj4MnP6LTHpsF3mqTnNmtnVkDy1AtShTp9xrjQGJaWLfwpswSwmBZAceMjsGIvJ3g84WJl2XcyoEEDlSR0A8z6Dyxg
```

**Decoding User Assertion**
Header |  ```
{
  "alg": "RS256",
  "kid": "cecsassertionkey",
  "x5t":
    "xahfPmq9rjhirkuybWs1rkkZ1eo",
  "x5t#S256":
    "qWm-v_nuorl4376Y5-iScxOwypUzyl0xcSlKCnrnq_I"
 }
```
  
---|---  
Payload |  ```
{
  "iss": "31282cbe9858409ab5b5a6020e85ccb6",
  "sub":
    "abc@xyz.com",
  "aud": "https://<domainURL>/",
  "exp": 1534479854,
  "nbf": 1534476254,
  "iat":
    1534476254,
  "jti": "6fa9a70f-558c-4c93-bac7-c6a672a05992"
}
```
  
**Decoding Client Assertion**
Header |  ```
{
  "alg": "RS256",
  "kid": "cecsassertionkey",
  "x5t":
    "xahfPmq9rjhirkuybWs1rkkZ1eo",
  "x5t#S256":
    "qWm-v_nuorl4376Y5-iScxOwypUzyl0xcSlKCnrnq_I"
}
```
  
---|---  
Payload |  ```
{
  "iss": "31282cbe9858409ab5b5a6020e85ccb6",
  "sub":
    "31282cbe9858409ab5b5a6020e85ccb6",
  "aud": "https://<domainURL>/",
  "exp": 1534479854,
  "nbf": 1534476254,
  "iat":
      1534476254,
  "jti": "a9bdecdd-5cce-4f2d-9710-2661f10aabd1"
}
```
  
## Example Token Requests Using User Assertions 🔗 
**Example Request Using Authorization Header and User Assertion**```
  curl -i
  -H 'Authorization: Basic <base64Encoded clientid:secret>'
  -H 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8'
  --request POST https://<domainURL>/oauth2/v1/token
  -d 'grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer&assertion=<Base64 encoded user-assertion-value>&scope=<scope value>'
```

**Example Request Using User Assertion and Client Assertion**```
  curl -i
  -H 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8'
  --request POST https://<domainURL>/oauth2/v1/token
  -d 'grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer&assertion=<Base64 encoded user-assertion-value>&scope=<scope value>' \
  -d 'client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&client_assertion=<Base64 encoded client-assertion-value>'
```

Was this article helpful?
YesNo


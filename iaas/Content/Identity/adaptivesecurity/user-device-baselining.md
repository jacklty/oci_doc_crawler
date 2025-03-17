Updated 2024-05-30
# User Device Baselining
Enable this feature to automatically baseline a user's device the first time they sign in to OCI.
The first time a user signs in to OCI a baseline is created for the user's device. When a user signs in from this device, they don't receive an email notification. If a user accesses their account using an unknown device, then the user receives an email notifying them that a new device was used to sign in to their account.
## Enabling Device Baselining
To enable device baselining:
  1. Enable Adaptive Security, see [Activating Adaptive Security](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/activate-adaptive-security.htm#activate-adaptive-security "Activate adaptive security for an identity domain in IAM to evaluate contextual and threat event analysis, and obtain user risk scores from the configured third-party risk providers.").
  2. Enable `deviceBaseliningEnabled` flag in `SsoSettings`.```
PUT /admin/v1/SsoSettings/SsoSettings
```

**Note** Include the following attribute in the body of the API command: `deviceBaseliningEnabled = true`


## Getting the Baseline Status of a Device
The tenant administrator can use the following endpoint to retrieve the device details associated with a user: ```
POST /admin/v1/UserDevices?attributeSets=all&filter=owner.userName eq "{{UserName of the user}}" 
```

`isBaselined`: If the value of this attribute is `true`, then this particular device is baselined for the user. Sample response:```
     {
      "owner": {
        "value": "bacxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "userName": "user@abccorp.com",
        "display": "user abc"
      },
      "id": "blcxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "isBaselined": true,
      "deviceType": "Mac",
      "verified": true,
      "deviceFingerPrint": "cn2ayxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "dfp": "36bacesaxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "schemas": [
        "urn:ietf:params:scim:schemas:oracle:idcs:UserDevice"
      ]
    }
```

## Deleting a User Device
To delete a user device, use the following endpoint:```
DELETE /admin/v1/UserDevices/{{id}}
```

Was this article helpful?
YesNo


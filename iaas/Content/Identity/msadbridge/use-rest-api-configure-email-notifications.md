Updated 2023-07-06
# Use REST API to Configure Email Notifications
Using the REST API, administrators can configure who receives email notifications when connectivity is broken and restored.
The administrator can provide a comma separated list of emails IDs to which to send the notifications using `PATCH /admin/v1/Settings/Settings`.
Example payload: ```
{
  "schemas":[    
   "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations":[
    {
      "op": "replace",
      "path":     "contactEmails",
      "value": [       
    "admin@oracle.com",       
    "<emailid>@gmail.com"       
   ]
    }
     
       ]
}
```

Was this article helpful?
YesNo


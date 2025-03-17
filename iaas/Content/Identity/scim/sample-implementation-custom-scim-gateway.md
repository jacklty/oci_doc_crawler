Updated 2024-02-13
# Sample Implementation of a Custom SCIM Gateway
Oracle provides a sample application that conforms to SCIM specifications, and which you can use to develop a custom SCIM gateway to integrate it with your custom application.
You can download the sample implementation `idcs-scim-gateway-app` from <https://github.com/oracle-samples/idm-samples/tree/master/idcs-scim-gateway-app>.
This custom gateway exposes HTTP endpoints to enable operations such as creating, searching for, updating, and deleting users. The custom gateway stores information about the users locally in the `db.json` file. This file has the `JSON` format.
[![A custom SCIM gateway exposing HTTP endpoints to enable operations such as searching, creating, updating, and deleting users](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-sample-app-architecture.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-sample-app-architecture.png)
Item | Description  
---|---  
![Callout 2](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable1.png) |  GET http(s)://<scimgatehost:port>/scimgate/Users GET http(s)://<scimgatehost:port>/scimgate/Users/<id>  
![Callout 2](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable2.png) |  POST http(s)://<scimgatehost:port>/scimgate/Users PUT http(s)://<scimgatehost:port>/scimgate/Users/<id> DELETE http(s)://<scimgatehost:port>/scimgate/Users/<id>  
The sample application uses express and body-parser packages. The `server.js` file implements a route for users' endpoints:
```
"...
var express = require('express')
var app = express()
var bodyParser = require('body-parser');
app.use(bodyParser.json());
var config = require('./config.js');
..."
```

The `routes/users.js` file defines the SCIM REST API endpoints, and maps each endpoint to the corresponding JavaScript function:
```
"...
//Get operation for /Users endpoint
app.get('/scimgate/Users', users.findAll);
//Get operation for /Users/:id endpoint
app.get('/scimgate/Users/:id', users.findOne);
//Put operation for /Users endpoint
app.post('/scimgate/Users', users.create);
//Put operation for /Users endpoint
app.put('/scimgate/Users/:id', users.update);
//Delete operation for /Users endpoint
app.delete('/scimgate/Users/:id', users.delete);
..."
```

The `user.controller.js` file implements JavaScript functions to create, read, update, and delete users in the local user store, represented by the `userdb.json` file:
```
"...
exports.findAll = function(req, res){
console.log('Entering findAll function.');
...
};
exports.findOne = function(req, res) {
console.log('Entering findOne function.');
...
};
exports.create = function(req, res){ console.log('Entering create function.');
...
};
exports.update = function(req, res){
console.log('Entering update function.');
...
};
exports.delete = function(req, res){ console.log('Entering delete function.');
...
};
..."
```

The `userdb.json` file contains an array of users, and the structure of each user entry follows the SCIM specification standard, using a subset of the user attributes:
```
{
 "resources": [
  {
   "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
   ],
   "id": "1",
   "externalId": "1",
   "userName": "user1@example.com",
   "name": {
    "formatted": "User 1 Name",
    "familyName": "Name",
    "givenName": "User 1"
   },
   "displayName": "User 1 DisplayName",
   "active": true,
   "password": "User1Password",
   "emails": [
    {
     "value": "user1@example.com",
     "type": "work",
     "primary": true
    }
   ]
  }
 ]
}
```

To authorize the client to make HTTP requests, the sample SCIM gateway application uses two environment variables that you must set before running the application: `ADMINUSER` and `ADMINPASS`. These variables represent the administrator's user name and password for your API authentication service. You provide values for these variables by setting up the `run.sh` shell script for UNIX or Mac environments, or the `run.bat` batch script for Windows environments.
IAM sends these administrative credentials in the form of an authorization header for all requests to authenticate the administrator's credentials, and then accesses the custom SCIM gateway using the `basic` grant type.
You can modify the sample application's source code and implement other types of authentication methods to match your requirements.
You can also change the sample application's source code so that instead of contacting the local user store (represented by the `userdb.json` file), the new sample application contacts your application's identity store to create, read, update, and delete users.
Was this article helpful?
YesNo


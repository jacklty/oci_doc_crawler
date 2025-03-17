Updated 2025-01-10
# Known Issues for Container Registry
Known issues have been identified in Container Registry.
## Use Tenancy Namespace instead of Tenancy Name in image tags and Docker login credentials on or before September 30, 2019 🔗  

Details
    
Up to now, you might have been using either the tenancy name or the tenancy namespace when logging in to Oracle Cloud Infrastructure Registry and when performing operations on images in the Container Registry.
After September 30, 2019, you will have to use the tenancy namespace rather than the tenancy name when using Oracle Cloud Infrastructure Registry. 

Background
    
After September 30, 2019, you will not be able to:
  * Specify the tenancy name when logging in to Oracle Cloud Infrastructure Registry.
  * Perform operations on images that include tenancy name in the repository path.


Instead, you will have to use the tenancy namespace rather than the tenancy name when using Oracle Cloud Infrastructure Registry.
A tenancy namespace is an auto-generated and immutable random string of alphanumeric characters. For example, the namespace of the acme-dev tenancy might be ansh81vru1zp. You can see the tenancy namespace on the Container Registry page of the Console. 
Note that for some older tenancies, the tenancy namespace might be the same as the tenancy name. If that is the case, no action is required.
On or before September 30, 2019, if the tenancy namespace and the tenancy name are different, you must:
  * Start specifying the tenancy namespace when logging in to Oracle Cloud Infrastructure Registry, instead of the tenancy name.
  * Start specifying the tenancy namespace when pushing new images to Oracle Cloud Infrastructure Registry, instead of the tenancy name.
  * Migrate any existing images in Oracle Cloud Infrastructure Registry that include the tenancy name in the path.


The following workarounds and examples assume:
  * tenancy name is acme-dev
  * tenancy namespace is ansh81vru1zp
  * username is jdoe@acme.com



Workaround for logging into Oracle Cloud Infrastructure Registry
    
Previously, when you logged in to Oracle Cloud Infrastructure Registry and were prompted for a username, you could have entered it in the format `<tenancy-name>/<username>`.
For example:
```
$ docker login phx.ocir.io
Username: acme-dev/jdoe@acme.com
Password:
```

On or before September 30, 2019, you must start using the tenancy namespace instead of the tenancy name when logging in to Oracle Cloud Infrastructure Registry. When you are prompted for username, enter it in the format `<tenancy-namespace>/<username>`.
For example:
```
$ docker login phx.ocir.io
Username: ansh81vru1zp/jdoe@acme.com
Password:
```


Workaround for pushing new images to Oracle Cloud Infrastructure Registry
    
Previously, when you pushed a new image to Oracle Cloud Infrastructure Registry, you could have specified the tenancy name as part of the repository path in the `docker push` command. You could have entered the command in the format:
```
$ docker push <region-key>.ocir.io/<tenancy-name>/<image-name>:<tag>
```

For example:
```
$ docker push phx.ocir.io/acme-dev/helloworld:latest
```

On or before September 30, 2019, you must start using the tenancy namespace instead of the tenancy name in the `docker push` command when you push new images. Enter the command in the format:
```
$ docker push <region-key>.ocir.io/<tenancy-namespace>/<image-name>:<tag>
```

For example:
```
$ docker push phx.ocir.io/ansh81vru1zp/helloworld:latest
```


Workaround for existing images in Oracle Cloud Infrastructure Registry that include the tenancy name in the repository path
    
If you have previously pushed images to Oracle Cloud Infrastructure Registry, those existing images could have included the tenancy name as part of the repository path. For example, `phx.ocir.io/acme-dev/helloworld:latest`.
After September 30, 2019, you will not be able to perform operations on existing images in the Container Registry that include the tenancy name in the repository path.
So on or before September 30, 2019, for every existing image that contains the tenancy name in the repository path, you must replace tenancy name with tenancy namespace.
To replace tenancy name with tenancy namespace in the repository path of an existing image:
  1. Pull the image by entering:
```
$ docker pull <region-key>.ocir.io/<tenancy-name>/<image-name>:<tag>
```

For example:
```
$ docker pull phx.ocir.io/acme-dev/helloworld:latest
```

  2. Use the `docker tag` command to change the repository path by entering:
```
$ docker tag <region-key>.ocir.io/<tenancy-name>/<image-name>:<tag> <region-key>.ocir.io/<tenancy-namespace>/<image-name>:<tag>
```

For example:
```
$ docker tag phx.ocir.io/acme-dev/helloworld:latest phx.ocir.io/ansh81vru1zp/helloworld:latest
```

  3. Push the image with the new repository path to the Container Registry by entering:
```
$ docker push <region-key>.ocir.io/<tenancy-namespace>/<image-name>:<tag>
```

For example:
```
$ docker push phx.ocir.io/ansh81vru1zp/helloworld:latest
```

  4. Repeat the above steps for every existing image that has tenancy name in the repository path.


Was this article helpful?
YesNo


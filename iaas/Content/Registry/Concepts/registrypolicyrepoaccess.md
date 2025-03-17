Updated 2025-01-10
# Policies to Control Repository Access
_Find out how to set up policies to control access to repositories in Container Registry, along with some examples of common policies._
You have fine-grained control over the operations that users are allowed to perform on repositories in Oracle Cloud Infrastructure Registry (also known as Container Registry). 
A user's permissions to access repositories comes from the groups to which they belong. The permissions for a group are defined by identity policies. Policies define which actions the members of a group can perform. Users access repositories and perform operations based on the policies set for the groups they are members of. Identity policies to control repository access can be set at the tenancy and at the compartment level. See [Details for Container Registry](https://docs.oracle.com/iaas/Content/Identity/Reference/registrypolicyreference.htm).
Before you can control access to repositories, you must have already created users and already placed them in appropriate groups (see [Managing Users](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingusers.htm) and [Managing Groups](https://docs.oracle.com/iaas/Content/Identity/Tasks/managinggroups.htm)). You can then create policies and policy statements to control repository access (see [Managing Policies](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm)).
Note that users in the tenancy's Administrators group can perform any operation on any repository in Container Registry that belongs to the tenancy.
## Common Policies 🔗 
**Note**
The policies in this section use example group names, as follows:
  * acme-viewers: A group that you want to limit to just viewing a list of repositories.
  * acme-pullers: A group that you want to limit to pulling images.
  * acme-pushers: A group that you want to allow to push and pull images.
  * acme-managers: A group that you want to allow to push and pull images, delete repositories, and edit repository metadata (for example, to make a private repository public).


Make sure to replace the example group names with your own group names.
[Enable users to view a list of all the repositories belonging to the tenancy or to a compartment](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registrypolicyrepoaccess.htm)
**Type of access:** Ability to see a list of all repositories in Container Registry belonging to the tenancy (or to a particular compartment). Users will not be able to:
  * view the images or layers in a repository
  * push or pull images from or to a repository


**Where to create the policy:**
  * In the tenancy. For example:
Copy
```
Allow group acme-viewers to inspect repos in tenancy
```

  * In the tenancy or in a compartment. For example:
Copy
```
Allow group acme-viewers to inspect repos in compartment acme-compartment
```



[Enable users to pull images from any repository belonging to the tenancy or to a compartment](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registrypolicyrepoaccess.htm)
**Type of access:** Ability to pull images (layers and manifests) from any repository in Container Registry that belongs to the tenancy (or to a particular compartment).
**Where to create the policy:**
  * In the tenancy. For example:
Copy
```
Allow group acme-pullers to read repos in tenancy
```

  * In the tenancy or in a compartment. For example:
Copy
```
Allow group acme-pullers to read repos in compartment acme-compartment
```



[Enable users to pull images from specific repositories in the tenancy or in a compartment](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registrypolicyrepoaccess.htm)
**Type of access:** Ability to pull images (layers and manifests) from any repository in Container Registry that has a name starting with "acme-web-app" and that belongs to the tenancy (or that belongs to a particular compartment).
**Where to create the policy:**
  * In the tenancy. For example:
Copy
```
Allow group acme-pullers to read repos in tenancy where all { target.repo.name=/acme-web-app*/ }
```

  * In the tenancy or in a compartment. For example:
Copy
```
Allow group acme-pullers to read repos in compartment acme-compartment where all { target.repo.name=/acme-web-app*/ }
```



[Enable users to push images to any repositories (and create new repositories if necessary) in the tenancy or in a compartment](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registrypolicyrepoaccess.htm)
**Type of access:** Ability to push images (layers and manifests) to any repository in Container Registry that belongs to the tenancy or to a particular compartment. 
Users always require the `REPOSITORY_READ` and `REPOSITORY_UPDATE` permissions to push images. If the specified repository doesn't exist yet, users also require the `REPOSITORY_CREATE` permission to create a new repository in the tenancy's root compartment when they push the image. For more information about this unusual scenario, see [Creating a Repository](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrycreatingarepository.htm#top "Find out how to create a repository in Container Registry.").
**Where to create the policy:**
  * In the tenancy. For example:
Copy
```
Allow group acme-pushers to manage repos in tenancy
```

If you consider the previous example too permissive (since it includes the `REPOSITORY_MANAGE` and `REPOSITORY_DELETE` permissions, which are not required to push images), you can restrict the permissions to explicitly specify the permissions you do want to give. For example:
Copy
```
Allow group acme-pushers to manage repos in tenancy where ANY {request.permission = 'REPOSITORY_READ', request.permission = 'REPOSITORY_UPDATE', request.permission = 'REPOSITORY_CREATE'}
```

  * In the tenancy or in a compartment. For example, in a compartment:
Copy
```
Allow group acme-pushers to manage repos in compartment acme-compartment
```

Note that if you create the policy in a compartment other than the root compartment as shown above, users cannot push an image to a repository that doesn't exist yet. That's because the above policy does not give users permission to create a new repository in the tenancy's root compartment. For more information about this unusual scenario, see [Creating a Repository](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrycreatingarepository.htm#top "Find out how to create a repository in Container Registry.").


[Enable managers to perform any operation on any repository belonging to the tenancy or to a compartment](https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registrypolicyrepoaccess.htm)
**Type of access:** Ability to perform any operation on any repository in Container Registry that belongs to the tenancy (or to a particular compartment), including:
  * Pull an image from any repository.
  * Push an image to any repository.
  * Create a new repository. That is, either to create an empty repository in any compartment, or to create a repository in the tenancy's root compartment when pushing an image for which no repository exists yet. Note that if you create the policy in a compartment other than the root compartment, users cannot push an image to a repository that doesn't exist yet. That's because the policy does not give users permission to create a new repository in the root compartment. For more information about this unusual scenario, see [Creating a Repository](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrycreatingarepository.htm#top "Find out how to create a repository in Container Registry.").
  * Delete a repository.
  * Change a public repository to a private repository, or a private repository to a public repository.


**Where to create the policy:**
  * In the tenancy. For example:
Copy
```
Allow group acme-managers to manage repos in tenancy
```

  * In the tenancy or in a compartment. For example:
Copy
```
Allow group acme-managers to manage repos in compartment acme-compartment
```

Note that if you create the above policy in a compartment other than the root compartment, users cannot push an image to a repository that doesn't exist yet. That's because the policy does not give users permission to create a new repository in the root compartment. For more information about this unusual scenario, see [Creating a Repository](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrycreatingarepository.htm#top "Find out how to create a repository in Container Registry.").


Was this article helpful?
YesNo


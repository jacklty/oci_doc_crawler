Updated 2024-02-13
# Setting Permissions to Synchronize Users, Groups, and Group Membership
Set permissions for your AD bridge service account so that you can synchronize users, groups, or OUs between Microsoft Active Directory and IAM.
  1. Use your domain administrator credentials to sign in to the machine that contains your Microsoft Active Directory server.
  2. Open a command window.
  3. Set the **Generic Read** permissions for the users, groups, and organizational units (OU) in the Microsoft Active Directory domain that you want to import into Identity Domains:
```
dsacls <AD_Domain_Name> /I:T /g "<AD_Domain_Name>\<User/Group_Name>:GR"
```

**Note**
`<AD_Domain_Name>` is the name of the domain that you're associating with IAM and `<User/Group_Name>` is the username of your domain administrator account.
`/I:T`: This parameter specifies the objects to which you are applying the permissions. T is the default, which means you can propagate inheritable permissions to this object and child objects down to one level only.
`/g`: This parameter grants the permissions that you specify to the user or group. For example, `/g {<user> | <group>}:<permissions>`. 
`<permissions>`: This parameter specifies the type of permissions that you are applying.
     * `GR`: Generic Read
     * `GW`: Generic Write
     * `LC`: List the child objects of the object
     * `RP`: Read Property
  4. Set the **List Children** and **Read** properties for the **cn=Deleted Objects** container with inheritance. This container is also in the Microsoft Active Directory domain that you're associating with IAM.
`dsacls "cn=deleted objects,<AD_Domain_Name>" /takeOwnership`
`dsacls "cn=deleted objects,<AD_Domain_Name>" /I:T /g "<AD_Domain_Name>\<User/Group_Name>:LCRP"`
**Note** If you don't have these permissions, then the AD bridge won't be able to synchronize deleted users, groups, or OUs between Microsoft Active Directory and IAM. This causes inconsistencies between Microsoft Active Directory and IAM.


Was this article helpful?
YesNo


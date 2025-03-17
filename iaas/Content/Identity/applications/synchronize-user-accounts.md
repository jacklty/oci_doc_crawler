Updated 2023-06-28
# Synchronizing Users
After synchronizing your SaaS app with an identity domain, you will see the result of the import including the number of users created, deleted, and updated. You can do a general search based on account name, user e-mail, or username. You can also filter and search the results based on Situation and Synchronization Status. Select values from the respective lists to view users matching the search criteria. These are helpful when you have to find a set of users based on their situation or status from a huge number of results.
The **Import** page provides you with the overall status information, whether the last import succeeded, failed, or is still running. If the import succeeded, then the result is listed as follows: 
  * **Start date** is the date and time you started the import job. 
  * **End date** determines date and time the import job finished.
  * **Accounts created** shows the number of identity domain accounts that got created during the import based on your synchronization settings.
  * **Accounts deleted** lists the number of identity domain accounts that got deleted during the import based on your synchronization settings.
  * **Accounts updated** notes the number of identity domain accounts that got changed during the import.


  1. This table summarizes the result of successfully running an import. For each SaaS app account, it shows whether there exists a matching identity domain user and the action that you need to perform to link the SaaS user account to an identity domain user.
Column | Description  
---|---  
**Account** |  Shows the name of the SaaS app user account.  
**Situation** |  Lists whether a matching identity domain user exists or doesn't exist based on your synchronization configuration:
     * **No match is found** indicates that you need to manually select which action to take.
     * **Exact match is found** indicates that an identity domain user exists that matches the synchronization criteria that you configured.
     * **Multiple matches are found** indicates that there are multiple matches found for a user. You need to manually select one of the available actions.
     * **Manually linked** is the result of any action that you performed to link this SaaS app account to an identity domain user.  
**User** |  Shows the email address and username of the identity domain user.  
**Action** |  If there's no matching identity domain user, you need to select the appropriate action from the list:
     * **Assign existing user** : The **Assign user** page lists all existing identity domain users and allows you to select the one that you want to link with this SaaS app account.
     * **Create new user and link** : The **Add user** page allows you to create a new identity domain user.  
**Status** |  Lists the status or whether you need to confirm linking the SaaS app account to the identity domain user.  
  2. Take the appropriate action to link your SaaS users with identity domain accounts.


Was this article helpful?
YesNo


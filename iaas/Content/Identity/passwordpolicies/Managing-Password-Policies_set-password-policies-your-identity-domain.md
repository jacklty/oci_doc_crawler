Updated 2025-02-28
# Creating a Password Policy
Create up to ten password policies in an identity domain in IAM, assign relative priorities to them, and attach them to groups. A group can't be assigned to more than one password policy.
  1. On the **Password policy** list page, select **Add**. If you need help finding the list page, see [Listing Password Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordpolicies/listing-password-policies.htm#untitled1 "Retrieve a list of password policies.").
  2. Enter a name and a description for the policy.
  3. Enter a value for **Priority**.
The priority can be any integer between 1 and 10, where 1 is highest priority and 10 is lowest. If an existing password policy has the same that you enter, that policy moves down to the next priority number. For example, if there's a password policy with a priority of 2 and another with a priority of 3, and you create a policy with a priority of 2, the existing policy priorities are reset to 3 and 4.
  4. To add one or more groups to the password policy, select **Add** , select the groups, and then select **Add**.
Each group can have only one policy assigned to it.
If a user is assigned to more than one group, then the password policy with the highest priority is the password policy enforced for the user.
  5. Select the type of policy that you want to set for this identity domain: **Simple** , **Standard** , or **Custom**.
If you select **Simple** or **Standard** , the criteria for the selected policy are displayed. You can't change the criteria for these policies. 
If you select **Custom** , you can customize the following criteria:
     * **Password length (minimum):** The minimum number of characters that the password must contain.
     * **Password length (maximum):** The maximum number of characters allowed for the password. A password can't exceed 500 characters.
     * **Expires after (days):** The number of days until the password expires. Setting this option to 0 means that the password never expires.
     * **Account lock threshold:** The number of consecutive, unsuccessful login attempts into the identity domain after which the user account is locked. If you enter 0, then the user's account is never be locked.
     * **Enable automatic account unlock:** Automatically unlocks locked user accounts after the configured amount of time has passed.
     * **Automatically unlock account after (minutes):** The amount of time (in minutes), after which locked user accounts unlock automatically. You can set a value ranging between 5 minutes and 24 hours.
     * **Previous passwords remembered:** The number of unique new passwords that a user must use before a previously used password can be reused.
     * **Alphabetic (minimum):** The number of alphabetic characters that the password must contain.
     * **Numeric (minimum):** The number of alphabetic characters that the password must contain.
     * **Special (minimum):** The number of numeric characters that the password must contain.
     * **Lowercase (minimum):** The number of lowercase characters that the password must contain.
     * **Uppercase (minimum):** The number of uppercase characters that the password must contain.
     * **Unique (minimum):** The number of unique characters that the password must contain. Increasing the number of unique characters in a password can increase password strength by avoiding repetitive sequences that are easily guessed.
     * **Repeated (maximum):** The number of repeated characters that are allowed for the password. Limiting the use of repeating characters in a password provides extra security by preventing users from specifying passwords that are easy to guess, such as the same character repeated several times.
     * **Starts with an alphanumeric character:** To force the first character of all passwords to be an alphanumeric character, select this checkbox.
     * **Required characters:** The alphanumeric or special characters that the password must contain, separated by commas.
     * **Password must not contain: The user's first name:** Prevents the user's first name from being used as all or part of the password
     * **Password must not contain: The user's last name:** Prevents the user's last name from being used as all or part of the password.
     * **Password must not contain: The user's username:** Prevents the user's username from being used as all or part of the password
     * **Characters not allowed:** The alphanumeric or special characters that aren't allowed in the password, separated by commas.
     * **Whitespaces:** Prevents whitespace characters from being used as part of a password, A whitespace character is a character that represents horizontal space. For example, for the display name of John Smith, the space between "John" "Smith" is a whitespace character
     * **Dictionary words:** Screens all passwords for words that can be found in a custom dictionary. The custom dictionary contains a set of words derived from the OWASP top passwords list, including common substitutions ('@' for 'a', '$' for 's'), and prohibits those words.
  6. When you're finished, select **Add**.


Was this article helpful?
YesNo


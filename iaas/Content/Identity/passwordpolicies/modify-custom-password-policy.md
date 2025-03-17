Updated 2025-02-28
# Modifying the Custom Password Policy
Adjust the strength of the custom password policy in an identity domain in IAM to meet the business and security requirements for your enterprise applications.
  1. On the **Password policy** list page, select the name of the policy you want to change. If you need help finding the list page, see [Listing Password Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordpolicies/listing-password-policies.htm#untitled1 "Retrieve a list of password policies.").
  2. To change the description and priority of the password policy, select **Edit password policy** , make your changes, and then select **Save changes**.
  3. To change the password rules, select **Edit password rules** , and proceed with the rest of the steps.
  4. Select **Custom** and edit the criteria in the following list:
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
  5. Select **Save changes**.
  6. (Recommended): In the **Save password policy** dialog box, select **Force all users to set a new password on their next login**. 
Do this to ensure that existing users set passwords to meet the criteria for the policy before their next sign in to the identity domain. If you don't select this option, the password policy applies to users only when they're created or when they reset their passwords.
  7. Select **Save changes**.


Was this article helpful?
YesNo


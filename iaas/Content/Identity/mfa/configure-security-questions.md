Updated 2025-01-14
# Configuring Security Questions
Configure security questions settings, select the security questions that a user may use as a second verification method during sign-in, and add custom security questions for access to an in an identity domain in IAM. 
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. On the domain details page, select **Security**.
  4. On the **Security** page, select **Two-factor authentication**.
  5. Select the **Security questions** tab.
  6. Under **Security questions settings** , set options for answer length and the number of questions a user is asked.
The minimum number of security questions that a user must set up is three.
**Note** This value can't be changed using the user interface. If you need to change this number, you must use the `/SecurityQuestionSettings` API endpoint.
     * **Minimum answer length (characters):** The minimum number of characters that must be contained in each security question answer. Enter a value between 1 and 8.
     * **Number of security questions a user is asked:** Set the number of questions a user is asked. Enter a value between 1 and 5.
  7. Under **Manage security questions** , select the checkboxes for the preconfigured questions that you want to use.
To disable a default security question, clear the checkbox for that question.
  8. Select the **Language** in which you want to view the questions.
  9. To add a custom security question, select **Add question** and then follow these steps:
    1. In the **Add a security question** panel, enter the custom security question in the _Default language_ field. Optionally, enter the translated question text into the appropriate language row. When you view the custom security questions in a different language, those questions appear in your default language if you don't provide translated question text.
A good security question should be a memorable piece of information that only the user would know. It should not be easily discoverable.
Good example: What was the name of your second pet?
Bad example: What was your high school mascot?
    2. Select **Add**.
    3. Confirm the changes.
The custom question is added at the bottom of the user-defined **Questions** list.
  10. To remove a custom question, follow these steps:
    1. Find the custom question in the **User defined questions** list.
    2. Select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) of the question and select **Remove**.
    3. Select **Remove** in the confirmation dialog box.
  11. When you're done configuring security questions, select **Save changes**.


Was this article helpful?
YesNo


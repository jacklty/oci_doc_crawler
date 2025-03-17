Updated 2025-01-14
# Creating a Hosted Sign-In Page
Create a Hosted Sign In page in IAM to customize the look and feel of the identity domain sign-in experience by using style classes, custom HTML, and translation support.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. On the domain details page, select **Settings**.
  4. On the **Settings** page, select **Hosted sign in**.
  5. Select **Enable hosted sign in**. 
  6. Edit the **Custom HTML**.
A limited set of HTML tags is available.
     * div
     * img
     * label
     * input
     * h1
     * h2
     * h3
     * span
A limited set of style properties is available.
     * align-items: 
     * background-color: 
     * background: 
     * border-radius: 
     * border: 
     * box-shadow: 
     * content:
     * display: 
     * height: 
     * justify-content: 
     * left: 
     * margin-top: 
     * margin: 
     * max-height: 
     * max-width: 
     * min-height: 
     * padding-left: 
     * padding-right: 
     * padding: 
     * position: 
     * text-align: 
     * top: 
     * width:
Properties can be applied inline. In the following example, the sign-in page background has been customized by setting the style property to `style="background-color:lightblue"`
```
<div class="oj-flex oj-sm-flex-direction-column">
 <div id="idcs-app-shell-signin-background" class="oj-idaas-signin-app-shell oj-idaas-signin-app-shell-background">
  <div class="oj-flex oj-idaas-signin-app-shell-wrapper oj-idaas-signin-app-shell-wrapper-background" style="background-color:lightblue">
   <div class="oj-flex-item oj-sm-12 oj-idaas-signin-app-shell-padding-left oj-idaas-signin-app-shell-padding-right">
    <div class="oj-idaas-signin-app-shell-branding-logo-wrapper">
     <img id="custom-idaas-signin-branding-logo" class="oj-idaas-signin-app-shell-branding-logo" />
    </div>
    <oj-idaas-signin-section id="custom-idaas-signin-section"></oj-idaas-signin-section>
   </div>
   <div class="oj-flex-item oj-sm-12 oj-idaas-signin-app-shell-content-wrapper">
    <oj-idaas-signin-message id="custom-idaas-signin-message"></oj-idaas-signin-message>
    <div class="oj-idaas-signin-app-shell-padding-left oj-idaas-signin-app-shell-padding-right">
     <oj-bind-slot name="content"></oj-bind-slot>
    </div>
   </div>
  </div>
 </div>
</div>
```

**Tip** Need to start over? You can revert to the default HTML values by selecting **Restore default HTML**.
  7. Specify translations.
The following existing elements can be customized in the sign-in page. To customize the existing elements, the following reserve IDs must be used.
     * Element: `username label`
     * Reserve ID: `idcs-username-label`
     * Element: `username placeholder` (help text inside the username field)
     * Reserve ID: `idcs-username-placeholder`
     * Element: `password label`
     * Reserve ID: `idcs-password-label`
     * Element: `password placeholder` (help text inside the username field)
     * Reserve ID: `idcs-password-placeholder`
**Tip** Need to start over? You can clear the translations pane by selecting **Restore default translations**.
  8. Select **Preview sign in** to view changes without saving them.
  9. Select **Save changes**.


Was this article helpful?
YesNo


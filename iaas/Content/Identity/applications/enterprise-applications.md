Updated 2023-04-14
# Enterprise Applications
Enterprise applications are web applications that require App Gateway to integrate with IAM for authentication and authorization purposes.
Enterprise applications work similarly to confidential applications if you configure the **Client configuration** and **Resource server configurations** section under OAuth configuration tab.
To configure an enterprise application to work with App Gateway for authentication and authorization purposes, you need to know the following information about your web application:
  * The web application's base URL. For example, if a known URL of your application is `http://myapp.internal.example.com:3266/myapp/private/home`, then the base URL is `http://myapp.internal.example.com:3266`.


  * The list of resources of your web application. For example, if your web application exposes the following URLs: functionalities A to Z in the following format `/myapp/private/funcA` to `/myapp/private/funcZ`, a home page `/myapp/private/home`, a logout URL `/myapp/logout`, an about page `myapp/public/about`, and an index page `/myapp/index`, then the list of all resources of your web application is:
    * URLs from `/myapp/private/funcA` to `/myapp/private/funcZ`
    * `/myapp/private/home`
    * `/myapp/logout`
    * `/myapp/public/about`
    * `/myapp/index`


  * For each resource, define which resources require the user to be authenticated, which don't require user authentication, and which resource represents the log out action. Below are examples of authenticated and non-authenticated resources:
    * Resources from `/myapp/private/funcA` to `/myapp/private/funcZ`, and `/myapp/private/home` require the user to be authenticated.
    * `/myapp/logout` logs out the user.
    * Both `myapp/public/about` and `/myapp/index` are public resources and don't require the user to be authenticated.


  * For each resource, define who can access which resource and which HTTP Method will be allowed or denied access. For example, you can define that all members of group **Employees** are allowed access to make `GET` and `POST` HTTP requests to resource `/myapp/private/home`, only members of group **MyGroupA** can access `/myapp/private/funcA`, and only users accessing from within network perimeter **IntranetIPs** can access resources from `/myapp/private/funcB` to `/myapp/private/funcZ`.


  * Identify URL patterns that apply to your list of resources. In the previous example, the URL pattern `/myapp/private/.*` matches all the application's functionality URLs and the home page URL. All these URLs may require the same kind of authentication and authorization.


Was this article helpful?
YesNo


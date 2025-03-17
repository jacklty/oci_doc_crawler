Updated 2023-05-31
# Creating a Wallet on Linux
Configure a wallet on your Linux environment to store the client_id and client_secret of the confidential application with the POSIX Viewer role. This lets the Linux PAM to communicate securely with the confidential application.
On the Linux environment, run the following commands as the root user:
  * `walletMgr add <wallet_location> client_id                 <client_id>`
  * `walletMgr add <wallet_location> client_secret                 <client_secret>`


For example: ```
$ walletMgr add /etc/opc-wallet/ client_id b6d001f65da542c38ceb284ea8a05926
wallet initialized successfully.
key client_id is added successfully in wallet.
```
```
$ walletMgr add /etc/opc-wallet/ client_secret fea39433-5115-4050-b486-138cce381fb2
wallet initialized successfully.
key client_secret is added successfully in wallet.
```

Was this article helpful?
YesNo


Updated 2023-08-15
# Guidelines for Securing the Hardware
After installation of Compute Cloud@Customer, secure the hardware by restricting access to the hardware. You must ensure that nobody, other than authorized Oracle personnel, access or open the Compute Cloud@Customer rack. 
We recommend the following practices to restrict access: 
  * Have the Compute Cloud@Customer and related equipment installed in a locked, restricted-access room. 
  * Store any site-located spare parts in a locked cabinet. Restrict access to the locked cabinet to authorized personnel.
  * Limit SSH listener ports to the management and private networks. Use SSH protocol 2 (SSH-2) and FIPS 140-2 approved ciphers.
  * Limit SSH allowed authentication mechanisms. Inherently insecure methods are disabled.


Was this article helpful?
YesNo


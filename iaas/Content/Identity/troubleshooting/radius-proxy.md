Updated 2023-01-04
# RADIUS Proxy
Learn how to troubleshoot common RADIUS Proxy issues.
## /sbin/service idcs_radius is Stopped 🔗 
When you see that the status of `/sbin/service idcs_radiusd` is stopped, use the following steps.
  1. Check that the radius agent is running by using the following Python command:`<radius_proxy_installer_location>/oracle_radius_proxy/radius_agent/scripts/src/radius_agent.py status `
  2. If the status is running, check the agent logs at: `<radius_proxy_installer_location>/oracle_radius_proxy/radius_agent/logs/agent.log`
  3. If you see the following exception in the RADIUS Proxy logs (`<radius_proxy_installer_location>/oracle_radius_proxy/radius_proxy/log/radius_proxy.log`), ensure that the host entry is correct in the RADIUS Proxy listener: `Exception in thread "main" java.net.BindException: Cannot assign requested address at sun.nio.ch.Net.bind0(Native Method)`


Was this article helpful?
YesNo


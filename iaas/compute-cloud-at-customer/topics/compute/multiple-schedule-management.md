Updated 2023-08-15
# Multiple Schedule Management
On Compute Cloud@Customer, 
When you create and enable an autoscaling configuration, the Autoscaling service evaluates the schedule rules in the policies in the configuration.
If multiple policies in the same configuration run at the same time, only one lifecycle state policy and one pool size policy run. The lifecycle state policy runs first.
If multiple lifecycle state policies in the same configuration run at the same time, the policy with the highest priority action runs. The following list shows actions in priority order from highest to lowest priority:
  1. Force Reboot
  2. Reboot
  3. Start
  4. Force Stop


If multiple pool size policies in the same configuration run at the same time, the policy that specifies the largest pool size runs.
Was this article helpful?
YesNo


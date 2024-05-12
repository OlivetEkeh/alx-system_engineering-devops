Issue Summary:

Duration of the outage: 
Start time: April 25, 2024, 10:00 AM WAT
End time: April 25, 2024, 3:00 PM WAT

Impact:
During the outage, the web server hosting our primary application was completely inaccessible. Users attempting to access the application encountered HTTP errors or timeouts. Approximately 100% of our users were affected by this outage.

Root Cause:
The root cause of the outage was traced back to a misconfiguration during a software purge operation on the server. While attempting to remove a non-essential software package, a critical dependency required by the web server stack was inadvertently removed, leading to the server's inability to serve web requests.


Timeline:

- 10:00 AM WAT: The issue was detected when users reported being unable to access the application. Additionally, automated monitoring alerts triggered indicating a high volume of HTTP errors.

- 10:15 AM WAT: Engineers on-call began investigating the issue. Initial assumption was that the problem might be related to network connectivity issues or a potential DDoS attack due to the sudden spike in HTTP errors.

- 10:30 AM WAT: Network connectivity and DDoS attack were ruled out after further investigation. Focus shifted to the web server stack configuration as a potential root cause.

- 11:00 AM WAT: Misleading investigation paths were taken when engineers attempted to roll back recent changes to the server configuration, assuming a recent deployment might have caused the issue. However, this did not resolve the problem.

- 11:30 AM WAT: The incident was escalated to the DevOps team lead and the system administrator for further assistance.

- 12:00 PM WAT: System administrator identified the misconfiguration during the software purge operation as a potential cause of the issue. 

- 1:00 PM WAT: The root cause was confirmed after restoring the critical dependency that was inadvertently removed during the purge operation.

- 3:00 PM WAT: The incident was resolved after restoring the server to a previous known good state and ensuring that all services were functioning properly.



Root Cause:

The root cause of the outage was traced back to a misconfiguration that occurred during a software purge operation on the server. While attempting to remove a non-essential software package, a critical dependency required by the web server stack was inadvertently removed. Specifically, a crucial library required by the Apache web server was deleted, leading to the server's inability to serve web requests.

Resolution:

To resolve the issue, the critical dependency that was inadvertently removed during the purge operation needed to be restored. The system administrator identified the missing library and reinstalled it on the server. Additionally, steps were taken to ensure that proper testing procedures were implemented to prevent similar misconfigurations in the future. After restoring the missing dependency and verifying the server's functionality, the application was brought back online, and users were able to access it without any further issues.

With the root cause identified and the necessary steps taken to address it, the server was restored to a stable state, and normal operations resumed.

Corrective and Preventative Measures:

Improvements and Fixes:
1. Implement Strict Change Control: Establish a formal change control process to carefully review and approve all server configuration changes before implementation. This will help prevent accidental misconfigurations and minimize the risk of similar incidents in the future.

2. Enhanced Monitoring and Alerting: Enhance monitoring systems to provide more granular visibility into server health and performance metrics. Implement proactive alerts for critical dependencies and services to detect and address issues before they impact users.

3. Automated Configuration Management: Invest in automated configuration management tools such as Ansible or Chef to streamline server configuration and ensure consistency across environments. Automate routine tasks such as software installations and updates to reduce the likelihood of manual errors.

4. Regular Disaster Recovery Testing: Conduct regular disaster recovery testing exercises to validate backup and restoration procedures. Ensure that backups are regularly tested and can be quickly restored in the event of a critical failure or outage.

Tasks to Address the Issue:
- Restore Missing Dependency: Reinstall the critical library required by the Apache web server that was inadvertently removed during the software purge operation. Verify that all necessary dependencies are properly installed and configured.

- Review Configuration Changes: Conduct a thorough review of recent configuration changes to identify any other potential misconfigurations or dependencies that may have been affected. Document lessons learned and update procedures to prevent similar incidents in the future.

- Implement Change Control Process: Establish a formal change control process to review and approve all server configuration changes before implementation. Define roles and responsibilities for change management and ensure that changes are properly documented and communicated.

- Enhance Monitoring and Alerting: Enhance monitoring systems to provide real-time visibility into server health and performance metrics. Configure proactive alerts for critical dependencies and services to detect issues early and minimize downtime.

- Automate Configuration Management: Invest in automated configuration management tools to streamline server configuration and ensure consistency across environments. Automate routine tasks such as software installations and updates to reduce manual errors and improve efficiency.

- Conduct Disaster Recovery Testing: Schedule regular disaster recovery testing exercises to validate backup and restoration procedures. Test backups regularly to ensure they are reliable and can be quickly restored in the event of a critical failure.

By implementing these corrective and preventative measures, we can mitigate the risk of similar incidents in the future and improve the overall reliability and stability of our server infrastructure.







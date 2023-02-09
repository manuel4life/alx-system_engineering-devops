Increase Nginx Open Files

This script will increase the number of open files allowed by Nginx on a Unix-based system.
Prerequisites

Before running this script, make sure that you have the following:

    A Unix-based system
    Nginx installed
    Root or sudo privileges

What the script does

The script does the following:

    Edits the /etc/security/limits.conf file to increase the number of open files allowed by Nginx

    Restarts the Nginx service to apply the changes

Conclusion

This script is a quick and easy way to increase the number of open files allowed by Nginx. This can be useful when you encounter errors such as "too many open files" or when you need to increase the maximum number of open files for performance reasons.

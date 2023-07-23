#Command line for the win Background Context CMD CHALLENGE is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

This project is NOT mandatory at all. It is 100% optional. Doing any part of this project will add a project grade of over 100% to your average. Your score won’t get hurt if you don’t do it, but if your current average is greater than your score on this project, your average might go down. Have fun

To establish an SFTP connection to the sandbox environment, you'll need the following information:

Hostname: This is the IP address or domain name of the server where the sandbox environment is hosted.
Username: The username you've been provided to log in to the sandbox environment.
Password: The password associated with the provided username.
Assuming you have the necessary credentials, follow these steps to connect via SFTP using the command-line:

Open a terminal or command prompt on your computer.

Use the sftp command followed by the username and hostname to initiate the connection. Replace USERNAME and HOSTNAME with the actual credentials provided to you:

bash
Copy code
sftp USERNAME@HOSTNAME
If you're connecting to this host for the first time, it might ask you to verify the server's fingerprint. Type yes and press Enter to continue.

After that, it will prompt you for the password associated with the provided username. Enter the password and press Enter. Note that when you type the password, nothing will appear on the screen for security reasons, but it is being entered.

If the provided credentials are correct, you should now be connected to the sandbox environment via SFTP. You will see an SFTP prompt similar to this:

shell
Copy code
sftp>
You can now use various SFTP commands like ls, get, put, etc., to list directories, download files from the server, upload files to the server, and manage your files and directories.

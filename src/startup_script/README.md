# RadioHead
Startup script for automating the scanning process.

Open the Dash and search for "Startup Applications".

click on Add and give in the command to run the application. (It is possible to run python scripts with Startup Applications)

Advanced users may want to put a .desktop file in ~/.config/autostart to run applications after a user login. 
This may have following content:
'''
[Desktop Entry]
Type=Application
Name=<Name of application as displayed>
Exec=<command to execute>
Icon=<full path to icon>
Comment=<optinal comments>
X-GNOME-Autostart-enabled=true
'''

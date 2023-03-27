# Stash-tray-icon

Generates stash tray icon.

1. Download stash-linux from https://github.com/stashapp/stash/releases.

2. You need to add a config.txt file to your stash folder which should be placed in /home/$USER_NAME/Applications/Stash/. If you want to place your stash folder in different place you need to edit a python line number 90.

3. Inside the config file you need to specify a path to icon (i.e. /home/$USER_NAME/Applications/Stash/stash.png) and specify port number (default 9999). Then copy an icon.png file from the repo.

4. You need add location of stash-linux binary either to PATH or copy stash-linux to PATH location (i.e. /usr/bin) so python script can run it from terminal.
Bash
https://phoenixnap.com/kb/linux-add-to-path 
[archive] https://archive.is/brU9G
Zsh
https://stackoverflow.com/questions/11530090/adding-a-new-entry-to-the-path-variable-in-zsh
[archive] https://archive.ph/quobn

5. Run main.py with command python main.py and your default browser should start now and connect to a port 9999 on localhost. Plase exit with an "Quit" option in a tray icon as exiting with ctrl+c does not kill process yet and an icon stays.

# Stash-tray-icon

Generates stash tray icon.

1. Download [stash-linux](https://github.com/stashapp/stash/releases). 

2. You need to add a config.txt file to your stash folder which should be placed in /home/$USER_NAME/Applications/Stash/. If you want to place your stash folder in different place you need to edit a python line number 90.

3. Inside the config file you need to specify a path to icon (i.e. /home/$USER_NAME/Applications/Stash/stash.png) and specify port number (default 9999). Then copy an icon.png file from the repo.

4. You need add location of stash-linux binary either to PATH or copy stash-linux to PATH location (i.e. /usr/bin) so python script can run it from terminal.
[Bash](https://phoenixnap.com/kb/linux-add-to-path),
[archive.is](https://archive.is/brU9G),
[Zsh](https://stackoverflow.com/questions/11530090/adding-a-new-entry-to-the-path-variable-in-zsh),
[archive.is](https://archive.ph/quobn).

5. Run main.py with command python main.py and your default browser should start now and connect to a port 9999 on localhost. Plase exit with an "Quit" option in a tray icon as exiting with ctrl+c does not kill process yet and an icon stays. Alternatively you can download .desktop file (and add your username) and .bin file nad just run it like normal program. You need to download .bin file [from here](https://github.com/Giger22/Stash-tray-icon-Linux/releases/tag/0.1) or create .bin file yourself with nuitka3.

| Algorithm        | Hash           |
| ------------- |:-------------:|
| sha-512| d57f87609269177b95c1b69bf2a15c1fbdd44b25de9e069a0e10adeba3d3532bca51f4b7423a97d7b078ea540bd5eca0d0fe959638440279ef22719e10d095fd|
| sha-256| c8aaf4d2f68c43766162f020ce0be2f184428a9eae3f5b919103740f903f1441|
| sha-1| ca8e49712bae29e22c391c7215b95b2a6971bb81|
| md5| ce1694a89b54ec70b2c3fb3fe247fcbb|

I created the .bin file with nuitka3 and I had to comment line 98 because for some reason a .desktop file opened two tabs but when executing .bin file or running main.py with pyton it opens only one.

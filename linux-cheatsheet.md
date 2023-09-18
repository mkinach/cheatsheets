# Linux Cheatsheet

### GNU Screen

Useful aliases
```
alias sc='screen -q -S 1'  # create a screen
alias sls='screen -ls'     # list all screens
alias sr='screen -d -RR'   # reattach most recent screen, or named screen
```

Screen navigation
* `ctrl+a c` to create a new window
* `ctrl+a "` to list all windows
* `ctrl+a A` to rename current window
* `ctrl+a n` to go to next window
* `ctrl+a p` to go to previous window
* `ctrl+a d` to detach from current screen
* `ctrl+a k` to kill current screen
* `ctrl+a :sessionname mySessionName` to rename entire session


### Miscellaneous

Display shared library dependencies of a binary
```
ldd executable         # for trusted binaries
objdump -p executable  # for untrusted binaries
```

Remove `apt` packages
```
sudo apt remove <package>   # keep config files
sudo apt purge <package>    # purge config files
sudo apt clean              # clear the cache
sudo apt autoremove         # remove unneeded dependencies
```

Generate and push SSH keys
```
ssh-keygen -t rsa
ssh-copy-id -i ~/.ssh/id_rsa.pub user@remoteserver
```

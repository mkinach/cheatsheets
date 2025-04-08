# Linux Cheatsheet

#### Index:

[Docker](#docker)<br>
[GNU Screen](#gnu-screen)<br>
[Miscellaneous](#miscellaneous)<br>

---

### Docker

Basic commands
```
docker ps -a         # list all containers
docker ps            # list only running containers

docker images        # list all images

docker start <ID>    # start a stopped container
docker stop  <ID>    # stop a running container
docker restart <ID>  # stop and restart a running container

docker volume ls              # list volumes
docker volume create <name>   # create a volume
docker volume inspect <name>  # print volume mount point
docker volume rm <name>       # remove a volume

docker run <options> <ID>     # create and start a new container from a specified image
docker run -d <ID>            # run in detached mode
docker run -it <ID>           # run in interactive mode

docker attach <ID>            # attach to an interactive container

docker rm <ID>     # remove a stopped container
docker rm -v <ID>  # remove a stopped container and associated volumes
docker rmi <ID>    # remove an image

docker logs <ID>  # view container logs

docker exec -it <ID> <command>  # execute command in a running container

docker cp /path/to/local/file <ID>:/path/to/container/file  # copy files to container
docker exec <ID> chmod -R 644 /path/to/container/file  # fix permissions
```

Create a temporary interactive Ubuntu container
```
docker pull ubuntu:latest
docker run -it --rm ubuntu:latest
docker rmi ubuntu:latest
```

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

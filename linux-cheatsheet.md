# Linux Cheatsheet

### ComputeCanada Clusters

Get the specs of a particular Graham/Cedar node
```
scontrol show node gra1261
```

Get the specs of all nodes
```
sinfo --Node --long
```

Check available space for your group
```
diskusage_report
```

Cancel one job
```
scancel <jobid>
```

Cancel all (pending) jobs for a user
```
scancel -u <username>
```

View jobs in the queue for a user
```
squeue --user=mikin
```

View details about one specific job
```
scontrol show job -dd <jobid>
```

Monitor currently running jobs for a user
```
alias jobmon='squeue -i 60 --user=mikin -o "%.8i %.5C  %.7m  %.19V %.19S %.11l %.5M "'
```

Check memory usage of a completed or running job
```
sstat
sacct  # see man page for relevant format statements
```

Alias for getting stats for completed job (assuming Slurm output is in cwd)
```
stats() {
jobID=`ls | grep [0-9]*out | awk -F. '{print $1}'`
seff ${jobID}
}
```

Slurm file for submitting a serial job on a node
```
#! /bin/bash

# First compile, then submit via sbatch

#SBATCH --account=def-matt
#SBATCH --job-name=wave
#SBATCH --mem-per-cpu=3G
#SBATCH --time=01:00:00

# Fix for RNPL code
echo $PATH
export PATH=$PATH:$(pwd)
echo $PATH

srun ./w1dcn id0
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

# Git Cheatsheet

Configuring Git on a new machine
```
git config --list
git config --global user.name "User Name"
git config --global user.email "user@domain.com"
git config --global core.editor "vim"
```

For email privacy
```
git config --global user.email "user@users.noreply.github.com"
```

Basic repository commands
```
git add <file>
git add <directory-with-files>  # add subdirectory files all at once

git diff
git diff HEAD <file>            # compare with most recent commit
git diff HEAD~1 <file>          # compare with most recent commit before last
git diff [--staged]             # diff added but not-yet-committed files
git diff f22b25e <file>         # diff using last few chars of some commit ID

git show [HEAD~n] <file>        # show file contents from specific commit

git checkout -b <newbranch>        # create and switch to a new branch
git switch <branch>                # change to a different branch
git branch -m <newname>            # rename the current branch
git branch -m <oldname> <newname>  # rename a non-head branch

git checkout [HEAD~n] <file>    # restore file
git checkout f22b25e            # detach HEAD state for some commit ID
git checkout main               # reattach your HEAD
git checkout -- <file>          # revert file back to previous commit
git checkout f22b25e -- <file>  # revert file back to specific commit

git commit --amend              # add to most recent commit & edit commit msg
```

Stash both staged and unstaged changes (basically, temporarily revert to last commit)
```
git stash
git stash list
git stash pop  # restore
```

Create a temporary branch from a past commit
```
git checkout -b temp-branch 56a4e5c08
git log --oneline --decorate --graph --all  # see where branch pointers are pointing
git checkout main                           # change back
git branch -a                               # show branch structure
git branch -d temp-branch                   # delete temp branch
```

Ignoring files and subdirectories
```
echo *.dat >> .gitignore
echo results/ >> .gitignore    # an entire directory
echo !final.dat >> .gitignore  # except final.dat
git add .gitignore
git add -f <file>              # override .gitignore to explicitly include a file
git rm --cached <file>         # untrack (but do not delete) a file previously committed
git status --ignored
```

Connect to remote repository for the first time
```
git remote add origin https://github.com/path
git remote -v
```

Push/pull changes from remote repository
```
git push origin main
git pull origin main
```

Rename, remove files, etc.
```
git mv <file1> <file2>
git rm <file1>
git rm --cached <file>  # stop tracking file but keep it on disk
```

Undo most recent commit, but leave all files on disk unchanged
```
git reset HEAD~
```

Undo every change in cwd since last commit
```
git reset HEAD --hard  # BE CAREFUL
git clean -fd          # remove untracked files & directories
```

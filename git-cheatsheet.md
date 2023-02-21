# Git Cheatsheet

Configuring Git on a new machine
```
git config --list
git config --global user.name "User Name"
git config --global user.email "user@domain.com"
git config --global core.editor "vim"
git config --global diff.guitool kdiff3
git config --global merge.tool kdiff3 
```

For email privacy
```
git config --global user.email "user@users.noreply.github.com"
```

Basic repository commands
```
git add <directory-with-files>  # add all contents of a subdirectory

git diff HEAD <file>                  # compare with most recent commit
git diff HEAD~1 <file>                # compare with most recent commit before last
git diff <commitID> <file>            # diff against a specific commit
git diff --staged                     # diff added but not-yet-committed files
git difftool <commitID1> <commitID2>  # diff using GUI tool

git show <commitID> <file>            # show file contents from specific commit
git show [HEAD~n] <file>

git switch -c <newbranch>             # create and switch to a new branch
git switch -c <newbranch> <commitID>  # create a branch based on an old commit
git branch -m <newname>               # rename the current branch
git branch -m <oldname> <newname>     # rename a non-HEAD branch
git branch -a                         # list all branches
git branch -d                         # delete a branch

git checkout -- <file>                # revert file back to previous commit
git checkout <commitID> <file>        # revert file back to specific commit
git checkout [HEAD~n] <file>

git commit --amend         # add to most recent commit & edit commit msg
git commit -a              # automatically stage all changes and commit them
git commit -m <message>    # specify the commit message from the command line

git stash                  # save uncommited changes to the stash stack
git stash list             # list contents of the stash stack
git stash drop <stashID>   # delete a specific stash from the stash stack
git stash apply <stashID>  # apply a specific stash to the working directory
git stash pop              # apply most recent stash, then delete it

git log --oneline --decorate --graph --all  # pretty print branch structure
```

Ignoring files and subdirectories
```
echo *.dat >> .gitignore
echo results/ >> .gitignore      # ignore an entire directory
echo !final.dat >> .gitignore    # except final.dat
git add -f <file>                # override .gitignore to explicitly include a file
git rm --cached <file>           # untrack (but do not delete) a file previously added or committed 
git status --ignored             # list files which are untracked or ignored
git ls-tree -r HEAD --name-only  # list all files being tracked on current branch
```

Connect to remote repository for the first time
```
git remote add origin https://github.com/path
git remote -v
```

Undo most recent commit, but leave all files on disk unchanged
```
git reset --soft HEAD~1  # reset but leave the changes staged
```

Undo every change in working directory since last commit
```
git reset --hard HEAD  # BE CAREFUL
git clean -fd          # remove untracked files & directories
```

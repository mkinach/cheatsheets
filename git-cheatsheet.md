# Git Cheatsheet

Configuring Git on a new machine
```
git config --list
git config --global user.name "User Name"
git config --global user.email "user@domain.com"
git config --global core.editor "vim"
git config --global diff.guitool kompare  # could also use kdiff3
git config --global merge.tool kompare    # could also use kdiff3 
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
git show [HEAD~n] <file>              # show file contents from n commits ago

git switch -c <newbranch>             # create and switch to a new branch
git switch -c <newbranch> <commitID>  # create a branch based on an old commit
git branch -m <newname>               # rename the current branch
git branch -m <oldname> <newname>     # rename a non-HEAD branch
git branch -a                         # list all branches
git branch -d <branch>                # delete a branch

git checkout -- <file>                # revert file back to previous commit
git checkout <commitID> <file>        # revert file back to specific commit
git checkout [HEAD~n] <file>          # revert file back to version n commits ago

git tag                            # list all tagged versions
git tag <tag>                      # add a tag to current version
git tag -d <tag>                   # delete a tag
git checkout <tag>~<n>             # checkout relative to a tagged version
git checkout -b <newbranch> <tag>  # create and switch to a new branch based on tag

git clone --bare <repo> <repo>.git  # create a bare repo

git commit --amend         # add to most recent commit and edit commit msg
git commit -a              # automatically stage all changes and commit them (but not untracked files)
git commit -m <message>    # specify the commit message from the command line

git stash                  # save uncommited changes to the stash stack
git stash list             # list contents of the stash stack
git stash drop <stashID>   # delete a specific stash from the stash stack
git stash apply <stashID>  # apply a specific stash to the working directory
git stash pop              # apply most recent stash, then delete it

git log --max-count=<n>                      # display the last n commits
git log --since='<n> minutes ago'            # display commits made in the last n minutes
git log --until='<n> minutes ago'            # display commits made before the last n minutes
git log --author=<name>                      # list all commits made by a specific author
git log --oneline --decorate --graph --all   # pretty print branch structure
git log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short  # pretty print with specific formatting

git hist --all  # show any commits deleted by "git reset" (at least until garbage collection occurs)
```

Remote repositories
```
git remote -v   # list remote repos

git remote add origin https://github.com/<path>  # add new remote repo

git branch --track <branch> <remote>  # create local tracking branch which follows remote branch

git fetch <remote> <branch>  # fetch changes from remote repo but do not merge
git pull  <remote> <branch>  # fetch changes from remote repo and auto-merge (git fetch + git merge)
git push  <remote> <branch>  # push local commits from specified branch to the specified remote repo
```

Ignoring files and subdirectories
```
echo *.dat >> .gitignore         # ignore files matching pattern
echo results/ >> .gitignore      # ignore an entire directory
echo !final.dat >> .gitignore    # exclude final.dat from .gitignore
git add -f <file>                # override .gitignore to explicitly include a file
git rm --cached <file>           # untrack (but do not delete) a file previously added or committed 
git status --ignored             # list files which are untracked or ignored
git ls-tree -r HEAD --name-only  # list all files being tracked on current branch
```

Undoing commits
```
git revert HEAD  # create new commit which undoes changes in most recent commit

git reset --soft HEAD~1  # reset to last commit but leave the changes staged and keep files on disk

git reset --hard HEAD  # discard changes in working directory and staging area since last commit
git clean -fd          # permanently remove untracked files and directories
```

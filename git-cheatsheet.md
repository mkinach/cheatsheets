# Git Cheatsheet
#### References: [1](https://swcarpentry.github.io/git-novice/07-github/index.html)

Configuring Git on a new machine:
```
git config --list
git config --global user.name "User Name"
git config --global user.email "user@domain.com"
git config --global core.editor "vim"
```

For email privacy:
```
git config --global user.email "user@users.noreply.github.com"
```

Basic repository commands:
```
git init
git add <file>
git add <directory-with-files>  # add subdirectory files all at once
git diff HEAD~1 <file>  # compare with most recent commit before last
git diff
git diff [--staged]  # diff added but not-yet-committed files
git diff f22b25e <file>  # diff using last few chars of some commit ID
git show [HEAD~n] <file>
git checkout [HEAD~n] <file>  # restore file
git checkout f22b25e  # detach HEAD state for some commit ID
git checkout master   # reattach your HEAD
git status
git commit
git log
git commit --all
```

Ignoring files and subdirectories:
```
echo *.dat >> .gitignore
echo results/ >> .gitignore
echo !final.dat >> .gitignore  # except final.dat
git add .gitignore
git add -f <file>  # override .gitignore to explicitly include file
git status --ignored
```

Connect to remote repository for the first time:
```
git remote add origin https://github.com/path
git remote -v
```

Push/pull changes from remote repository:
```
git push origin master
git pull origin master
```

Rename files:
```
git mv <file1> <file2>
```

Undo most recent commit, but leave all files on disk unchanged:
```
git reset HEAD~
```

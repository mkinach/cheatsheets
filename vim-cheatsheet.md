# Vim Cheatsheet

[Code Folding](#Code Folding)  
[Marks](#Marks)
[Miscellaneous](#Miscellaneous)
[Netrw](#Netrw)
[Screen Splitting](#Screen Splitting)
[Search](#Search)
[Spellcheck](#Spellcheck)

### Code Folding

* choose the folding mode:
`:set foldmethod=indent`
`:set foldmethod=syntax`
`:set foldmethod=manual`
* `zc` to fold code, `zo` to open code by one level at the cursor
* `za` will toggle open/close fold by one level at the cursor
* capital letters (`zC`, `zO`, `zA`) will apply opening/closing to ALL levels of folding for the current focused group
* `zm` increases the fold level by one (globally)
* `zr` decreases the fold level by one (globally)
* `zM` closes all open folds to deepest level (globally)
* `zR` opens all closed folds (globally)
* `zf` to define a fold from visual selection (if `foldmethod=manual`)

### Marks

* `ma` (where `a` is any letter) to create local bookmark at current line
* `mA` (where `A` is any CAPITAL letter) to create global bookmark on current line
* `'a` or `'A` to return to the start of a bookmarked line
* ```a`` or ```A`` to return to a bookmarked line *and* position
* `:marks` to list all marks
* `:delmarks aB` to delete mark `a`, `B`
* `:delmarks a-d` to delete mark `a`, `b`, `c`, `d`
* `:delmarks!` to delete all lowercase marks in current buffer (`a` to `z`)

### Miscellaneous

* `:sh` to open a shell from Vim instance (`exit` to go back)
* `:! cmd` to run shell command `cmd` from Vim instance (does not work with aliases)
* `:! cmd %` to run shell command `cmd` from Vim instance with current file (`%`) as parameter
* `:r! cmd` to put output of shell command `cmd` into current buffer
* `:r file` to dump contents of `file` into current buffer
* `q:` brings up command history
* `q/` brings up search history
* `"+` to access system clipboard (must have Vim compiled with +clipboard; e.g. vim-gtk)
* `:reg` to list all registers
* `:wv` to write registers to `.viminfo` (to be accessed globally) 
* `:rv` to reload registers from `.viminfo`
* `ctrl-a` to increment highlighted number, `ctrl-x` to decrement
* `o` to move to other corner of block (when in visual mode)
* `gv` to re-select last visual selection 
* `ctrl+o` take you back to previous jump locations (including files), `ctrl+i` takes you forward

### Netrw

* `Enter` to open a file/window or enter a directory
* `-` to go up to parent directory
* `gh` to toggle hidden files
* `%` to create a new file
* `d` to create a new directory
* `R` to rename a file or directory
* `D` to delete a file or empty directory
* `x` to open in default system application
* `mf` to mark a file
* `mF` to unmark a file
* `mt` to assign target
* `mc` to copy marked files to target
* `mm` to move marked files to target
* `md` to diff marked files (up to 3)
* `mb` to create a bookmark
* `gb` to go to most recent bookmark
* `qb` to list bookmarked files
* `ctrl+o` to go back to Netrw from opened file 

### Screen Splitting

* `:sp [filename]` to open _filename_ (null for same file) with a horizontal (top/bottom) split
    * `ctrl+ws` to split current buffer horizontally
* `:vsp [filename]` to open _filename_ (null for same file) with a vertical (left/right) split
    * `ctrl+wv` to split current buffer vertically
* `ctrl-w` then `>` or `<` to resize a vertical split (or `ctrl-w n` to resize _n_ lines at once)
* `ctrl-w` then `+` or `-` to resize a horizontal split (or `ctrl-w n` to resize _n_ lines at once)
* `:set scrollbind` in both windows to scroll multiple split windows at once

### Search

* `*` to search for word under cursor
* `n` to search forward, `N` to search backwards
* `ggn` to jump to first match, `GN` to jump to last
* `*` to search forward on EXACT word at cursor, `#` to search backwards
* `g*` to search forward on NON-EXACT word at cursor, `g#` to search backwards
* `:%s/pattern//gn` to count number of matches of a word
* `:%s///gn` to repeat count occurrences of work last last search for
* `:10,50s/pattern//gn` to count number of matches between lines 10 and 50
* `:%s/old/new/gc` to search-and-replace, but confirm before making each change
* `:'<,'>s/\%Vold/new/g` to search-and-replace inside visual block (note the `\%V`)

### Spellcheck

* `setlocal spell spelllang=en_CA` to enable spellcheck
* `:set nospell` to disable spellcheck
* `]s` to move to next misspelled word, `[s` to move to previous
* `z=` over misspelled word to select an alternative
* `zg` to add word to dictionary
* `zw` to mark a word spelling as incorrect

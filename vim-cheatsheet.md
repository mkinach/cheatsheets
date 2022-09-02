# Vim Cheatsheet

### Miscellaneous

* `:sh` to open a shell from Vim instance (`exit` to go back)
* `:! cmd` to run shell command `cmd` from Vim instance (does not work with aliases)
* `:! cmd %` to run shell command `cmd` from Vim instance with current file (`%`) as parameter
* `:r! cmd` to put output of shell command `cmd` into current buffer
* `:r file` to dump contents of `file` into current buffer
* `%` to move to matching character: (), {}, []
* `zz` to center screen about cursor
* `q:` brings up command history
* `q/` brings up search history
* `g;` to jump to last edit location
* `R` in normal mode to mass-replace text (replace mode)
* `"+` to access system clipboard (must have Vim compiled with +clipboard; e.g. vim-gtk)
* `:reg` to list all registers
* `:wv` to write registers to `.viminfo` (to be accessed globally) 
* `:rv` to reload registers from `.viminfo`
* `ctrl-a` to increment highlighted number, `ctrl-x` to decrement

### Visual Mode

* `o` to move to other corner of block (when in visual mode)
* `gv` to re-select last visual selection 
* `ab` to select current text surrounded by `()`
* `aB` to select current text surrounded by `{}`
* `ib` to select current text surrounded by `()`, excluding the `(` and `)`
* `iB` to select current text surrounded by `{}`, excluding the `{` and `}`

### Marks

* `ma` (where `a` is any letter) to create local bookmark at current line
* `mA` (where `A` is any CAPITAL letter) to create global bookmark on current line
* `'a` or `'A` (where `a` or `A` is any letter) to return to a bookmarked position
* `:marks` to list all marks
* `:delmarks aB` to delete mark `a`, `B`
* `:delmarks a-d` to delete mark `a`, `b`, `c`, `d`
* `:delmarks!` to delete all lowercase marks in current buffer (`a` to `z`)
* `'.` to jump to last change in current buffer
* `''` to jump to line in current buffer where jumped from
* `ctrl+o` take you back to previous jump locations (including files), `ctrl+i` takes you forward

### Search-In-Text

* `*` to search for word under cursor
* `n` to search forward, `N` to search backwards
* `ggn` to jump to first match, `GN` to jump to last
* `*` to search forward on EXACT word at cursor, `#` to search backwards
* `g*` to search forward on NON-EXACT word at cursor, `g#` to search backwards
* `ctrl+o` jumps back to original cursor after searching, then `ctrl+i` takes you forward again
* `:%s/pattern//gn` to count number of matches of a word
* `:%s///gn` to repeat count occurrences of work last last search for
* `:10,50s/pattern//gn` to count number of matches between lines 10 and 50
* `:%s/old/new/gc` to search-and-replace, but confirm before making each change

### Screen Splitting

* `:sp [filename]` to open _filename_ (null for same file) with a horizontal (top/bottom) split
    * `ctrl+ws` to split current buffer horizontally
* `:vsp [filename]` to open _filename_ (null for same file) with a vertical (left/right) split
    * `ctrl+wv` to split current buffer vertically
* `ctrl-w` then `>` or `<` to resize a vertical split (or `ctrl-w n` to resize _n_ lines at once)
* `ctrl-w` then `+` or `-` to resize a horizontal split (or `ctrl-w n` to resize _n_ lines at once)
* `:set scrollbind` in both windows to scroll multiple split windows at once

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

### Spellcheck

* `setlocal spell spelllang=en_CA` to enable spellcheck
* `:set nospell` to disable spellcheck
* `]s` to move to next misspelled word, `[s` to move to previous
* `z=` over misspelled word to select an alternative
* `zg` to add word to dictionary
* `zw` to mark a word spelling as incorrect

# Vim Cheatsheet

### Miscellaneous

* `R` in normal mode to mass-replace text (replace mode)

* `"+` to access system clipboard (must have vim compiled with +clipboard; e.g. vim-gtk)

* Ctrl-A to increment highlighted number, Ctrl-X to decrement

* `:sh` to open a shell from Vim instance (`exit` to go back)
* `:! cmd` to run shell command `cmd` from Vim instance (does not work with aliases)
* `:! cmd %` to run shell command `cmd` from Vim instance with current file (`%`) as parameter
* `:r! cmd` to put output of shell command `cmd` into current buffer
* `:r file` to dump contents of `file` into current buffer

* `ma` (where `a` is any letter) to bookmark current cursor positon
* `mA` (where `a` is any CAPITAL letter) to create global bookmark
* ``a` or ``A` (where `a` or `A` is any letter) to return to a bookmarked position

### Search-In-Text

* `*` to search for word under cursor

* `n` to search forward, `N` to search backwards

* `ggn` to jump to first match, `GN` to jump to last

* `*` to search forward on EXACT word at cursor, `#` to search backwards

* `g*` to search forward on NON-EXACT word at cursor, `g#` to search backwards

* after searching, `Ctrl+o` jumps back to original cursor, then `Ctrl+i` takes back to cursor of word found in search 

* `:%s/pattern//gn` to count number of matches of a word

* `:%s///gn` to repeat count occurances of work last last search for

* `:10,50s/pattern//gn` to count number of matches between lines 10 and 50


### Screen Splitting

* `:sp [filename]` to open _filename_ (null for same file) with a horizontal (top/bottom) split

* `:vsp [filename]` to open _filename_ (null for same file) with a vertical (up/down) split

* `Ctrl-w` then `>` or `<` to resize a vertical split (or `Ctrl-w n` to resize _n_ lines at once)
 
* `Ctrl-w` then `+` or `-` to resize a horizontal split (or `Ctrl-w n` to resize _n_ lines at once)


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

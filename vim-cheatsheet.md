# Vim Cheatsheet

### Miscellaneous

* `R` in normal mode to mass-replace text


### Search-In-Text

* `*` to search for word under cursor

* `n` to search forward, `N` to search backwards

* `ggn` to jump to first match, `GN` to jump to last

* `*` to search forward on EXACT word at cursor, `#` to search backwards

* `g*` to search forward on NON-EXACT word at cursor, `g#` to search backwards

* after searching, `Ctrl+o` jumps back to original cursor, then `Ctrl+i` takes
  back to cursor of word found in search 

* `:%s/pattern//gn` to count number of matches of a word

* `:%s///gn` to repeat count occurances of work last last search for

* `:10,50s/pattern//gn` to count number of matches between lines 10 and 50


### Screen Splitting

* `:sp filename` to open with a horizontal (top/bottom) split

* `:vsp filename` to open with a vertical (up/down) split


### Code Folding

* choose the folding mode:
`:set foldmethod=indent`
`:set foldmethod=syntax`
`:set foldmethod=manual`

* `zc` to fold code, `zo` to open code by one level at the cursor

* `za` will toggle open/close fold by one level at the cursor

* capital letters (`zC`, `zO`, `zA`) will apply opening/closing to all
  levels of folding for the current focused group

* `zm` increases the fold level by one (globally)

* `zr` decreases the fold level by one (globally)

* `zM` closes all open folds to deepest level (globally)

* `zR` opens all closed folds (globally)

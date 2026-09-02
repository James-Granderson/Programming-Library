# `less`

**Concept:** Shell  
**Action:** Display  
**Object:** `less`  
**Classification:** Command  
**Environment:** Shell  
**Path Type:** N/A  
**Tags:** command

---

### What It Is

A terminal pager used to view text one screen at a time.

### What It Does

Displays file or command output interactively without requiring the entire input to fit on the screen.

### How to Use

Run `less` followed by a file or pipe input into it.

### Requirements

Shell

### Representation

```sh
less file.txt

```

Example:

```sh
less large-file.txt

```

This opens `large-file.txt` in an interactive view. Use the arrow keys or `Page Up` and `Page Down` to move through the file. Press `q` to exit.

`less` can also receive output from another command:

```sh
cat large-file.txt | less

```

This sends the output of `cat` into `less`, allowing it to be viewed one screen at a time.

### Flags

```text
-N — Show line numbers.

    Example:
    less -N file.txt

    Displays the line number alongside each line of the file.

-S — Chop long lines instead of wrapping them.

    Example:
    less -S file.txt

    Long lines remain on a single line and extend horizontally.
    Use the left and right arrow keys to view the portions that
    extend beyond the screen.

-i — Make searches case-insensitive unless the search pattern
     contains uppercase characters.

    Example:
    less -i file.txt

    Searching for "error" also matches "Error" and "ERROR".
    An uppercase character in the search pattern can make the
    search case-sensitive.

-F — Exit immediately when the entire content fits on one screen.

    Example:
    less -F file.txt

    If the file is short enough to fit on one screen, `less`
    exits instead of opening the interactive pager.

-X — Prevent the terminal from being cleared when `less` exits.

    Example:
    less -X file.txt

    Leaves the displayed content on the terminal after exiting.

```

### Notes

`less` is a **pager**, meaning its primary purpose is controlling how large amounts of text are viewed interactively.

Unlike a command such as `cat`, `less` does not simply dump the entire file into the terminal:

```sh
cat large-file.txt

```

prints the entire file at once, while:

```sh
less large-file.txt

```

opens an interactive view that allows the user to move through the content.

The same applies when piping command output:

```sh
some-command | less

```

The output of `some-command` becomes the input to `less`.

Common interactive commands include:

```text
Space — Move forward one screen.
b — Move backward one screen.
↑ / ↓ — Move one line.
/pattern — Search forward for a pattern.
?pattern — Search backward for a pattern.
n — Move to the next search match.
N — Move to the previous search match.
g — Go to the beginning.
G — Go to the end.
q — Quit.

```

Flags can also be combined:

```sh
less -NS file.txt

```

This shows line numbers while preventing long lines from wrapping.


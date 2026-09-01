# `EOF`

**Concept:** Shell
**Action:** Reference
**Object:** EOF
**Classification:** Shell Concept
**Environment:** Shell
**Path Type:** N/A
**Tags:** shell
---

---

---

### What It Is

EOF means **End Of File**.

It represents the point where a file or input stream has no more data to provide.

In a shell here-document, `EOF` is also commonly used as the name of a delimiter that marks where the input block ends.

### What It Does

When reading a file or input stream, EOF tells the program that there is no more input to read.

In a here-document, the `EOF` delimiter tells the shell where the supplied input ends.

### How to Use

EOF is encountered when a program reaches the end of an input source.

For a here-document, put a delimiter after `<<` and place the same delimiter by itself on a later line.

### Requirements

Shell

### Representation

End of input:

```text
data
data
data
EOF
````

Here-document:

```sh
cat <<'EOF'
hello
world
EOF
```

The first `EOF` names the delimiter.

The second `EOF` ends the input block.

`EOF` is only a conventional delimiter name. You can use another name:

```sh
cat <<'END'
hello
world
END
```

### Notes

The `EOF` in a here-document is **not the end of a file itself**. It is simply a marker chosen by the shell script to indicate the end of the here-document.

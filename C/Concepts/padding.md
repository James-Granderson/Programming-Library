# `Padding`
**Concept:** C
**Action:** Represent
**Object:** Padding
**Classification:** Programming Concept
**Environment:** Any C compiler
**Path Type:** N/A
**Tags:** keyword

---

### What It Is

Extra bytes inserted into an object's memory layout so that its members are stored at properly aligned addresses.

### What It Does

Moves a member to the next address that satisfies its alignment requirement.

The order of members can change how much padding is needed.

### How to Use

Padding is added automatically by the compiler when it lays out a `struct`.

### Requirements

None.

### Representation

Assume these example sizes and alignment requirements:

```text
double    = 8 bytes
long long = 8 bytes
int       = 4 bytes
short     = 2 bytes
char      = 1 byte

```

A well-ordered structure:

```c
struct Good {
    double a;
    long long b;
    int c;
    short d;
    char e;
};

```

can be laid out without padding between its members:

```text
address

0   ┌───────────────┐
    │    double     │  8 bytes
8   ├───────────────┤
    │   long long   │  8 bytes
16  ├───────────────┤
    │      int      │  4 bytes
20  ├───────────────┤
    │     short     │  2 bytes
22  ├───────────────┤
    │     char      │  1 byte
23  └───────────────┘

```

Now reverse the order:

```c
struct Bad {
    char a;
    double b;
    int c;
    short d;
};

```

After the `char`, the next address is `1`. If the `double` must begin at an address divisible by 8, the compiler needs padding:

```text
address

0   ┌───────────────┐
    │     char      │
1   ├───────────────┤
    │    padding    │
    │    padding    │
    │    padding    │
    │    padding    │
    │    padding    │
    │    padding    │
    │    padding    │
8   ├───────────────┤
    │    double     │  8 bytes
16  ├───────────────┤
    │      int      │  4 bytes
20  ├───────────────┤
    │     short     │  2 bytes
22  └───────────────┘

```

The padding exists because the `double` could not begin at address `1`. It had to be moved to the next properly aligned address, `8`.

### Notes

Padding takes up real memory, but it is not a member of the `struct`.

The compiler determines the layout based on the alignment requirements of the target implementation. Changing the order of members can therefore change the amount of memory the `struct` occupies.

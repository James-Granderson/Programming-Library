# `Time Complexity`
**Concept:** Algorithms
**Action:** Measure
**Object:** Time Complexity
**Classification:** Algorithm
**Environment:** Language-independent
**Path Type:** N/A
**Tags:** algorithm

---

### What It Is

A measure of how the amount of work an algorithm performs changes as the input gets larger.

### What It Does

Describes how an algorithm scales with input size.

The input size is commonly represented by `n`.

### How to Use

Identify how the amount of work changes as `n` increases, then describe that growth using Big-O notation.

### Requirements

Input size `n` // Represents how much data the algorithm is working with.

### Representation

#### O(1) — Constant

The amount of work stays the same regardless of the input size.

```text
array = [4, 8, 2, 9, 1]

access array[2]

1 operation

```

Whether the array contains 5 elements or 5,000,000 elements, accessing a known index takes the same number of operations.

```text
n = 5,000,000
     ↓
    O(1)

```

---

#### O(log n) — Logarithmic

The algorithm reduces the remaining work by a constant factor, commonly by half.

Binary search:

```text
[1, 2, 4, 8, 9, 12, 15, 20]

          ↓
      check middle
          ↓
    eliminate half
          ↓
    eliminate half
          ↓
        found

```

The search space is repeatedly divided:

```text
n = 16
 ↓
8
 ↓
4
 ↓
2
 ↓
1

```

This is:

```text
O(log n)

```

---

#### O(n) — Linear

The amount of work grows directly with the input size.

Linear search:

```text
[4, 8, 2, 9, 1]

4 → 8 → 2 → 9 → 1

```

If there are `n` elements, the algorithm may check all `n` elements.

```text
n = 5       → up to 5 checks
n = 100     → up to 100 checks
n = 1,000   → up to 1,000 checks

```

This is:

```text
O(n)

```

---

#### O(n log n) — Linearithmic

The algorithm performs logarithmic work for each of `n` elements.

A common example is merge sort.

Conceptually, the array is repeatedly divided:

```text
[8, 4, 2, 9, 1, 7, 5, 3]

          ↓ divide

[8, 4, 2, 9]    [1, 7, 5, 3]

          ↓ divide

[8, 4] [2, 9]    [1, 7] [5, 3]

          ↓ divide

[8] [4] [2] [9]  [1] [7] [5] [3]

```

The divisions create about `log n` levels, and each level processes all `n` elements.

```text
n × log n
   ↓
O(n log n)

```

---

#### O(n²) — Quadratic

The amount of work grows with the square of the input size.

For example, comparing every element with every other element:

```text
[ A  B  C ]

A → B
A → C
B → A
B → C
C → A
C → B

```

With `n` elements, the work can grow approximately as:

```text
n × n
  ↓
 n²
  ↓
O(n²)

```

For example:

```text
n = 10     → about 100 operations
n = 100    → about 10,000 operations
n = 1,000  → about 1,000,000 operations

```

---

#### O(2ⁿ) — Exponential

The amount of work doubles as the input gains another element.

For example, an algorithm that explores every possible subset of a set has:

```text
n = 1 → 2 possibilities
n = 2 → 4 possibilities
n = 3 → 8 possibilities
n = 4 → 16 possibilities
n = 5 → 32 possibilities

```

The growth is:

```text
2 × 2 × 2 × ... × 2
          n times

```

which is:

```text
O(2ⁿ)

```

As `n` becomes large, the amount of work grows extremely quickly.

### Common Time Complexities

```text
O(1)       constant
O(log n)   logarithmic
O(n)       linear
O(n log n) linearithmic
O(n²)      quadratic
O(2ⁿ)      exponential

```

From slower growth to faster growth:

```text
O(1)
  ↓
O(log n)
  ↓
O(n)
  ↓
O(n log n)
  ↓
O(n²)
  ↓
O(2ⁿ)

```

### Notes

Time complexity describes **how the amount of work grows as the input grows**.

Big-O notation focuses on the growth rate rather than exact operation counts.

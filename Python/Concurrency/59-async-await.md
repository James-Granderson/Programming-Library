# `Async and Await`

**Concept:** Cooperative Concurrency
**Action:** Suspend
**Object:** `Coroutine`
**Classification:** Asynchronous Execution
**Environment:** Python Runtime
**Path Type:** Direct
**Tags:** async, await, coroutine, asyncio

---

### What It Is

async def creates a coroutine function and await suspends a coroutine while an awaitable progresses.

### What It Does

It enables cooperative concurrency, especially for I/O-bound programs.

### How to Use

Use asyncio and await non-blocking operations rather than blocking the event loop.

### Requirements

A coroutine must be driven by an appropriate runner or event loop.

### Representation

```python
async def fetch():
    result = await client.get()
|Async is concurrency by cooperation, not automatically parallel CPU execution.
```

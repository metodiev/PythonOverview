# Introduction to AsyncIO
## Goal

Learn how to write asynchronous code in Python using asyncio to handle tasks concurrently without threads.

## Concept

Python normally runs code synchronously, meaning each operation blocks the next.

AsyncIO lets you:

Define coroutines that can pause (await)

Run multiple coroutines concurrently in a single thread

Handle I/O-bound tasks efficiently (network calls, file I/O, etc.)
```bash
## Basic Syntax
import asyncio

async def say_hello(delay, name):
    await asyncio.sleep(delay)  # non-blocking sleep
    print(f"Hello, {name} after {delay} seconds!")

async def main():
    # Schedule multiple coroutines concurrently
    await asyncio.gather(
        say_hello(2, "Alice"),
        say_hello(1, "Bob"),
        say_hello(3, "Charlie")
    )

# Run the main coroutine
asyncio.run(main())


Output (order may vary based on delay):

Hello, Bob after 1 seconds!
Hello, Alice after 2 seconds!
Hello, Charlie after 3 seconds!
```

## Exercise

- Write an async function fetch_data(name, delay) that prints “Fetching {name}…” after a given delay.
- Create a main() coroutine that runs 3–5 fetches concurrently using asyncio.gather().
- Experiment: change delays and see how the order of completion changes.
- Try running await fetch_data(...) without asyncio.gather() — what happens to execution?

## Reflection

- How does asyncio differ from threads for concurrency?
- Why is await required inside async functions?
- When would async I/O be better than multithreading or multiprocessing?
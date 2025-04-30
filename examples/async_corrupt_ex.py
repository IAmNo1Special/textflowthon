import asyncio
from textflow import TextFlow
import sys

async def main():
    tc = TextFlow(fg="magenta", cursor="_")
    await tc.async_corrupt(
        "ASYNC CORRUPTION IN PROGRESS!",
        file=sys.stdout,
        cycles=5,
        corrupt_sections=4,
        corrupt_duration=0.18,
        symbols="@#$%&*?!"
    )

if __name__ == "__main__":
    asyncio.run(main())

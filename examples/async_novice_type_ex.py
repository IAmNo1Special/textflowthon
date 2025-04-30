import asyncio
from textflowthon import TextFlowThon
import sys

async def main():
    tc = TextFlowThon(fg="yellow", cursor="_")
    await tc.async_novice_type(
        "Async novice typewriter demo!",
        file=sys.stdout,
        error_rate=0.2,
        max_mistakes=3,
        correction_delay=0.4,
        backspace_delay=0.04
    )

if __name__ == "__main__":
    asyncio.run(main())

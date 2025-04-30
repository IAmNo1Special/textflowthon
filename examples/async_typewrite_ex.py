"""
Example: Asynchronous TextFlow Usage
------------------------------------
This script demonstrates how to use TextFlow's async typewriter animation.
"""
import asyncio
from textflow.core import TextFlow

async def main():
    tc = TextFlow(width=50, delay=0.04, fg="magenta", cursor="█")
    await tc.async_typewrite("This is an async typewriter animation (async).\nUse it in chatbots, agents, or any async Python app!")

if __name__ == "__main__":
    asyncio.run(main())

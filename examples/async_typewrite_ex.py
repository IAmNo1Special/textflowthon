"""
Example: Asynchronous TextFlowThon Usage
------------------------------------
This script demonstrates how to use TextFlowThon's async typewriter animation.
"""
import asyncio
from textflowthon.core import TextFlowThon

async def main():
    tc = TextFlowThon(width=50, delay=0.04, fg="magenta", cursor="█")
    await tc.async_typewrite("This is an async typewriter animation (async).\nUse it in chatbots, agents, or any async Python app!")

if __name__ == "__main__":
    asyncio.run(main())

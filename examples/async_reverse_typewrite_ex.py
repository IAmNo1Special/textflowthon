"""
Example: Reverse Typewriter Effect (Async)

This script demonstrates the right-to-left typewriter animation in TextFlowThon (async).
"""
import asyncio
from textflowthon import TextFlowThon

def main():
    tc = TextFlowThon(fg="deep_sky_blue1", bg="black", delay=0.03, cursor="<")
    asyncio.run(tc.async_reverse_typewrite("This is a textflowthon effect test for reverse typewriter (async)"))

if __name__ == "__main__":
    main()

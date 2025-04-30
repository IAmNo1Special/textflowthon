"""
Example: Reverse Typewriter Effect (Async)

This script demonstrates the right-to-left typewriter animation in TextFlow (async).
"""
import asyncio
from textflow import TextFlow

def main():
    tc = TextFlow(fg="deep_sky_blue1", bg="black", delay=0.03, cursor="<")
    asyncio.run(tc.async_reverse_typewrite("This is a textflow effect test for reverse typewriter (async)"))

if __name__ == "__main__":
    main()

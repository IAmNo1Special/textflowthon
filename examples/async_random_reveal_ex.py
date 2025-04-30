"""
Example: Async Random Reveal Effect with TextFlowThon

This script demonstrates the async random reveal animation, where characters are revealed in random order asynchronously.
"""
import asyncio
from textflowthon import TextFlowThon

def main():
    tc = TextFlowThon(fg="bright_cyan", bg="black", delay=0.04, cursor="*")
    asyncio.run(tc.async_random_reveal("This is a textflowthon effect test for random reveal (async)", mask="*"))

if __name__ == "__main__":
    main()

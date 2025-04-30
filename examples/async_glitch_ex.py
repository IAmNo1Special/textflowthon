"""
Example: Glitch Effect (Async)

This script demonstrates the async glitch animation, where characters rapidly flicker through random symbols before settling on the correct letter.
"""
import asyncio
from textflowthon import TextFlowThon

def main():
    tc = TextFlowThon()
    asyncio.run(tc.async_glitch("This is a textflowthon effect test for glitch! (async)", steps=12, delay=0.04))

if __name__ == "__main__":
    main()

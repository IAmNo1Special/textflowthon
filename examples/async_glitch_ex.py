"""
Example: Glitch Effect (Async)

This script demonstrates the async glitch animation, where characters rapidly flicker through random symbols before settling on the correct letter.
"""
import asyncio
from textflow import TextFlow

def main():
    tc = TextFlow()
    asyncio.run(tc.async_glitch("This is a textflow effect test for glitch! (async)", steps=12, delay=0.04))

if __name__ == "__main__":
    main()

"""
Example: Using a FIGlet/ASCII font with TextFlowThon (Async)

This script demonstrates how to animate text in the terminal using a custom FIGlet font asynchronously.
Requires: pyfiglet
"""
import asyncio
from textflowthon import TextFlowThon

def main():
    tc = TextFlowThon(font="slant", fg="spring_green3", bg="black", delay=0.01)
    asyncio.run(tc.async_typewrite("This is a textflowthon effect test for figlet fonts (async)"))

if __name__ == "__main__":
    main()

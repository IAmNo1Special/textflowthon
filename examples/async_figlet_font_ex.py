"""
Example: Using a FIGlet/ASCII font with TextFlow (Async)

This script demonstrates how to animate text in the terminal using a custom FIGlet font asynchronously.
Requires: pyfiglet
"""
import asyncio
from textflow import TextFlow

def main():
    tc = TextFlow(font="slant", fg="spring_green3", bg="black", delay=0.01)
    asyncio.run(tc.async_typewrite("This is a textflow effect test for figlet fonts (async)"))

if __name__ == "__main__":
    main()

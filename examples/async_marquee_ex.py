import sys
import asyncio
from textflowthon import TextFlowThon

tc = TextFlowThon()

async def main():
    await tc.async_marquee(
        "TYPECAST MARQUEE EFFECT!",
        file=sys.stdout,
        width=40,
        delay=0.07,
        padding=40,
        loop=2,
        fg="red",
        bounce=True,
        pad_char="-"
    )

if __name__ == "__main__":
    asyncio.run(main())

import sys
import asyncio
from textflowthon import TextFlowThon

tc = TextFlowThon()

async def main():
    await tc.async_boot_sequence(
        message="ASYNC BOOT: WELCOME TO TYPECAST OS!",
        file=sys.stdout,
        delay=0.08,
        highlight_color="bright_green",
        bios_color="bright_white",
        mem_color="cyan",
        error_color="bright_red",
        boot_ok=True
    )

if __name__ == "__main__":
    asyncio.run(main())

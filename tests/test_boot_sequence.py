import sys
from textflow import TextFlow
import asyncio

def test_boot_sequence_sync_runs():
    tc = TextFlow()
    # Should not raise
    tc.boot_sequence(
        message="TEST BOOT SEQUENCE SYNC",
        file=sys.stdout,
        delay=0.001,
        highlight_color="green",
        bios_color="white",
        mem_color="cyan",
        error_color="red",
        boot_ok=True
    )

def test_boot_sequence_sync_error():
    tc = TextFlow()
    # Should not raise
    tc.boot_sequence(
        message="ERROR BOOT SYNC",
        file=sys.stdout,
        delay=0.001,
        boot_ok=False
    )

async def _test_async_boot_sequence():
    tc = TextFlow()
    await tc.async_boot_sequence(
        message="TEST BOOT SEQUENCE ASYNC",
        file=sys.stdout,
        delay=0.001,
        highlight_color="green",
        bios_color="white",
        mem_color="cyan",
        error_color="red",
        boot_ok=True
    )

async def _test_async_boot_sequence_error():
    tc = TextFlow()
    await tc.async_boot_sequence(
        message="ERROR BOOT ASYNC",
        file=sys.stdout,
        delay=0.001,
        boot_ok=False
    )

def test_boot_sequence_async_runs():
    asyncio.run(_test_async_boot_sequence())

def test_boot_sequence_async_error():
    asyncio.run(_test_async_boot_sequence_error())

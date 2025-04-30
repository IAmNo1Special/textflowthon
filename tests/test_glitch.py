import io
from textflowthon import TextFlowThon
import pytest
import asyncio
import sys

def test_glitch_typewrite_basic():
    tc = TextFlowThon(delay=0, fg="green")
    buf = io.StringIO()
    tc.glitch("GLITCH TEST", file=buf)
    output = buf.getvalue()
    assert "GLITCH TEST" in output

def test_async_glitch_typewrite_basic():
    tc = TextFlowThon(delay=0, fg="green")
    buf = io.StringIO()
    asyncio.run(tc.async_glitch("ASYNC GLITCH TEST", file=buf))
    output = buf.getvalue()
    assert "ASYNC GLITCH TEST" in output

def test_glitch_basic(monkeypatch):
    tc = TextFlowThon()
    buf = io.StringIO()
    # Patch time.sleep to speed up tests
    monkeypatch.setattr("time.sleep", lambda x: None)
    tc.glitch("GlitchTest", file=buf, steps=5, delay=0)
    output = buf.getvalue()
    assert isinstance(output, str)
    assert "GlitchTest" in output
    lines = [line for line in output.splitlines() if line.strip()]
    assert lines[-1] == "GlitchTest"

def test_async_glitch_basic(monkeypatch):
    tc = TextFlowThon()
    buf = io.StringIO()
    # Patch asyncio.sleep to speed up tests
    async def dummy_sleep(x):
        return None
    monkeypatch.setattr("asyncio.sleep", dummy_sleep)
    asyncio.run(tc.async_glitch("AsyncGlitchTest", file=buf, steps=5, delay=0))
    output = buf.getvalue()
    assert isinstance(output, str)
    assert "AsyncGlitchTest" in output
    lines = [line for line in output.splitlines() if line.strip()]
    assert lines[-1] == "AsyncGlitchTest"

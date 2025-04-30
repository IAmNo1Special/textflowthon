import io
import pytest
from textflow.core import TextFlow
import asyncio

def test_novice_type_basic():
    tc = TextFlow(fg="yellow")
    buf = io.StringIO()
    tc.novice_type("hello world", file=buf, error_rate=0.5, max_mistakes=2, correction_delay=0.01, backspace_delay=0.001)
    output = buf.getvalue()
    assert "hello world" in output
    assert len(output.replace(" ", "")) >= len("hello world")  # Should type at least the correct text

def test_novice_type_no_mistakes():
    tc = TextFlow(fg="yellow")
    buf = io.StringIO()
    tc.novice_type("no mistakes", file=buf, error_rate=0.0, max_mistakes=1)
    output = buf.getvalue()
    assert "no mistakes" in output

def test_novice_type_iterative():
    tc = TextFlow(fg="yellow")
    buf = io.StringIO()
    tc.novice_type("demo test", file=buf, error_rate=0.3, max_mistakes=2, correction_delay=0.01, backspace_delay=0.001)
    output = buf.getvalue()
    assert "demo test" in output
    assert output.strip().endswith("demo test")

def test_async_novice_type_basic():
    tc = TextFlow()
    buf = io.StringIO()
    async def run():
        await tc.async_novice_type("async test", file=buf, error_rate=0.5, max_mistakes=2, correction_delay=0.01, backspace_delay=0.001)
    asyncio.run(run())
    output = buf.getvalue()
    assert "async test" in output

def test_async_novice_type_iterative():
    tc = TextFlow()
    buf = io.StringIO()
    async def run():
        await tc.async_novice_type("async demo", file=buf, error_rate=0.3, max_mistakes=2, correction_delay=0.01, backspace_delay=0.001)
    asyncio.run(run())
    output = buf.getvalue()
    assert "async demo" in output
    assert output.strip().endswith("async demo")

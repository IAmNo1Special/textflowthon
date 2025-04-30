import io
import asyncio
from textflowthon.core import TextFlowThon

# --- Synchronous Reverse Typewriter Test ---
def test_reverse_typewrite_basic(monkeypatch):
    tc = TextFlowThon(delay=0, fg="orange1", cursor="<", bg=None)
    buf = io.StringIO()
    monkeypatch.setattr(tc, "_clear_line", lambda out_console: None)
    tc.reverse_typewrite("ReverseMe", file=buf)
    output = buf.getvalue()
    assert isinstance(output, str)
    assert "ReverseMe" in output
    # Final line should be the full text (right to left built up)
    lines = [line for line in output.splitlines() if line.strip()]
    final_line = lines[-1]
    assert final_line.rstrip("< ") == "ReverseMe"

# --- Asynchronous Reverse Typewriter Test ---
def test_async_reverse_typewrite_basic(monkeypatch):
    tc = TextFlowThon(delay=0, fg="deep_sky_blue1", cursor="<", bg=None)
    buf = io.StringIO()
    monkeypatch.setattr(tc, "_clear_line", lambda out_console: None)
    asyncio.run(tc.async_reverse_typewrite("AsyncReverse", file=buf))
    output = buf.getvalue()
    assert isinstance(output, str)
    assert "AsyncReverse" in output
    lines = [line for line in output.splitlines() if line.strip()]
    final_line = lines[-1]
    assert final_line.rstrip("< ") == "AsyncReverse"

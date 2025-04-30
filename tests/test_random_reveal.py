import io
import asyncio
from textflow.core import TextFlow

# --- Synchronous Random Reveal Test ---
def test_random_reveal_basic(monkeypatch):
    tc = TextFlow(delay=0, fg="yellow", cursor="_", bg=None)
    buf = io.StringIO()
    monkeypatch.setattr(tc, "_clear_line", lambda out_console: None)
    tc.random_reveal("RevealMe", file=buf, mask="*")
    output = buf.getvalue()
    assert isinstance(output, str)
    assert "RevealMe" in output
    # Only the final frame (last non-empty line) should be mask-free
    lines = [line for line in output.splitlines() if line.strip()]
    final_line = lines[-1]
    assert "*" not in final_line

# --- Asynchronous Random Reveal Test ---
def test_async_random_reveal_basic(monkeypatch):
    tc = TextFlow(delay=0, fg="cyan", cursor="_", bg=None)
    buf = io.StringIO()
    monkeypatch.setattr(tc, "_clear_line", lambda out_console: None)
    asyncio.run(tc.async_random_reveal("AsyncReveal", file=buf, mask="#"))
    output = buf.getvalue()
    assert isinstance(output, str)
    assert "AsyncReveal" in output
    lines = [line for line in output.splitlines() if line.strip()]
    final_line = lines[-1]
    assert "#" not in final_line

# --- Mask Character Edge Case ---
def test_random_reveal_mask(monkeypatch):
    tc = TextFlow(delay=0, fg="green")
    buf = io.StringIO()
    monkeypatch.setattr(tc, "_clear_line", lambda out_console: None)
    tc.random_reveal("MaskTest", file=buf, mask="-")
    output = buf.getvalue()
    assert "MaskTest" in output
    lines = [line for line in output.splitlines() if line.strip()]
    final_line = lines[-1]
    assert "-" not in final_line

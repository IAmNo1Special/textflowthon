import io
from textflow.core import TextFlow

# --- FIGlet/ASCII Font Tests ---
def test_typewrite_with_figlet_font(monkeypatch):
    tc = TextFlow(font="slant", delay=0)
    buf = io.StringIO()
    monkeypatch.setattr(tc, "_clear_line", lambda out_console: None)
    tc.typewrite("TestFont", file=buf)
    output = buf.getvalue()
    assert isinstance(output, str)
    assert len(output.splitlines()) > 1
    # The output should not be the same as the input (i.e., ASCII art was applied)
    assert "TestFont" not in output.replace(" ", "")
    # Optionally: check for typical ASCII art chars
    assert any(c in output for c in "_/\\|")

def test_async_typewrite_with_figlet_font(monkeypatch):
    tc = TextFlow(font="standard", delay=0)
    buf = io.StringIO()
    monkeypatch.setattr(tc, "_clear_line", lambda out_console: None)
    import asyncio
    asyncio.run(tc.async_typewrite("AsyncFont", file=buf))
    output = buf.getvalue()
    assert isinstance(output, str)
    assert len(output.splitlines()) > 1
    assert "AsyncFont" not in output.replace(" ", "")
    assert any(c in output for c in "_/\\|")

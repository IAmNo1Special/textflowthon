import asyncio
from textflow.core import TextFlow
import io

# --- Synchronous Tests ---
def test_typewrite_basic(monkeypatch):
    tc = TextFlow(width=20, delay=0, fg="green", cursor="*")
    buf = io.StringIO()
    # Monkeypatch _clear_line to avoid writing ANSI codes to StringIO
    monkeypatch.setattr(tc, "_clear_line", lambda out_console: None)
    tc.typewrite("Hello world!", file=buf)
    output = buf.getvalue()
    assert "Hello world!" in output
    assert isinstance(output, str)

# --- Asynchronous Tests ---
def test_async_typewrite_basic(monkeypatch):
    tc = TextFlow(width=20, delay=0, fg="red", cursor="|")
    buf = io.StringIO()
    monkeypatch.setattr(tc, "_clear_line", lambda out_console: None)
    asyncio.run(tc.async_typewrite("Async test!", file=buf))
    output = buf.getvalue()
    assert "Async test!" in output

# --- Frames Generator ---
def test_frames_generator():
    tc = TextFlow(width=10)
    frames = list(tc.frames("abc"))
    assert frames[0] == "a|"
    assert frames[1] == "ab|"
    assert frames[2] == "abc|"
    assert frames[3] == "abc"
    # Should yield the final string without cursor
    assert frames[-1].endswith("abc")

# --- Style Helper ---
def test_get_style_fg_only():
    tc = TextFlow(fg="blue")
    style = tc._get_style()
    assert "blue" in style

def test_get_style_fg_bg():
    tc = TextFlow(fg="yellow", bg="magenta")
    style = tc._get_style()
    assert "yellow" in style and "on magenta" in style

# --- Dynamic Attribute Change ---
def test_dynamic_style_change(monkeypatch):
    tc = TextFlow()
    tc.fg = "red"
    tc.bg = "white"
    tc.delay = 0
    buf = io.StringIO()
    monkeypatch.setattr(tc, "_clear_line", lambda out_console: None)
    tc.typewrite("Dynamic!", file=buf)
    output = buf.getvalue()
    assert "Dynamic!" in output

# --- Output to File-Like ---
def test_output_to_file_like(monkeypatch):
    tc = TextFlow()
    buf = io.StringIO()
    monkeypatch.setattr(tc, "_clear_line", lambda out_console: None)
    tc.typewrite("File-like test", file=buf)
    output = buf.getvalue()
    assert "File-like test" in output

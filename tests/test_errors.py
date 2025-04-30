import io
from textflowthon.core import TextFlowThon

# --- Error Handling Tests ---
def test_typewrite_invalid_font(monkeypatch):
    tc = TextFlowThon(font="not_a_real_font", delay=0)
    buf = io.StringIO()
    monkeypatch.setattr(tc, "_clear_line", lambda out_console: None)
    tc.typewrite("Should fallback", file=buf)
    output = buf.getvalue()
    # Should fallback to normal text (not crash)
    assert "Should fallback" in output

# No pytest.mark.asyncio here, this is not an async function
def test_async_typewrite_invalid_font(monkeypatch):
    tc = TextFlowThon(font="not_a_real_font", delay=0)
    buf = io.StringIO()
    monkeypatch.setattr(tc, "_clear_line", lambda out_console: None)
    import asyncio
    asyncio.run(tc.async_typewrite("Should fallback async", file=buf))
    output = buf.getvalue()
    assert "Should fallback async" in output

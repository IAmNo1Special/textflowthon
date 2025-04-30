import io
import re
from textflowthon import TextFlowThon
import asyncio

ANSI_ESCAPE = re.compile(r'\x1b\[[0-9;]*m')

def strip_ansi(s):
    return ANSI_ESCAPE.sub('', s)

def test_matrix_rain_basic():
    tc = TextFlowThon()
    buf = io.StringIO()
    tc.matrix_rain(width=10, height=5, delay=0.001, duration=0.1, file=buf)
    output = buf.getvalue()
    # Output should contain at least some matrix rain characters
    assert any(c in output for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*+-")

def test_matrix_rain_final_reveal():
    tc = TextFlowThon()
    buf = io.StringIO()
    msg = "HELLO\nWORLD"
    tc.matrix_rain(text=msg, width=10, height=5, delay=0.001, duration=0.1, file=buf)
    output = buf.getvalue()
    # The message should appear embedded in the last N lines of rain output
    N = 10
    lines = [line for line in output.splitlines() if line.strip()]
    found = False
    for line in lines[-N:]:
        if "HELLO" in strip_ansi(line):
            found = True
            break
    assert found, f'HELLO not found in last {N} lines: {lines[-N:]}'
    found = False
    for line in lines[-N:]:
        if "WORLD" in strip_ansi(line):
            found = True
            break
    assert found, f'WORLD not found in last {N} lines: {lines[-N:]}'

def test_async_matrix_rain_basic():
    tc = TextFlowThon()
    buf = io.StringIO()
    asyncio.run(tc.async_matrix_rain(width=10, height=5, delay=0.001, duration=0.1, file=buf))
    output = buf.getvalue()
    assert any(c in output for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*+-")

def test_async_matrix_rain_final_reveal():
    tc = TextFlowThon()
    buf = io.StringIO()
    msg = "HELLO\nWORLD"
    asyncio.run(tc.async_matrix_rain(text=msg, width=10, height=5, delay=0.001, duration=0.1, file=buf))
    output = buf.getvalue()
    # The message should appear embedded in the last N lines of rain output
    N = 10
    lines = [line for line in output.splitlines() if line.strip()]
    found = False
    for line in lines[-N:]:
        if "HELLO" in strip_ansi(line):
            found = True
            break
    assert found, f'HELLO not found in last {N} lines: {lines[-N:]}'
    found = False
    for line in lines[-N:]:
        if "WORLD" in strip_ansi(line):
            found = True
            break
    assert found, f'WORLD not found in last {N} lines: {lines[-N:]}'

def test_async_matrix_rain_colors():
    tc = TextFlowThon()
    buf = io.StringIO()
    msg = "HELLO\nWORLD"
    # Use a custom fg and msg_fg
    asyncio.run(tc.async_matrix_rain(text=msg, width=10, height=5, delay=0.001, duration=0.1, fg="blue", msg_fg="yellow", file=buf))
    output = buf.getvalue()
    # The output should contain the message somewhere in the last N lines
    N = 20
    lines = [line for line in output.splitlines() if line.strip()]
    found_hello = any("HELLO" in strip_ansi(line) for line in lines[-N:])
    found_world = any("WORLD" in strip_ansi(line) for line in lines[-N:])
    assert found_hello and found_world, f'HELLO/WORLD not found in last {N} lines: {lines[-N:]}'
    # Output should contain some blue and yellow ANSI codes
    plain_output = strip_ansi(output)
    assert "HELLO" in plain_output and "WORLD" in plain_output
    # Check for ANSI color codes (blue/yellow)
    assert "\x1b[" in output

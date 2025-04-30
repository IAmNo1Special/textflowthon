# Integration Tips

TextFlow can be integrated with other libraries and tools for powerful terminal experiences.

---

## Integrating with Rich Progress Bars
```python
from rich.progress import Progress
from textflow import TextFlow

progress = Progress()
progress.start()
tc = TextFlow()
tc.typewrite("Starting a long task...")

with progress:
    for i in progress.track(range(10), description="Working..."):
        # Do some work
        pass

tc.typewrite("Task complete!")
```

## Using TextFlow in Chatbots or Agents
```python
import asyncio
from textflow import TextFlow

async def bot_message():
    tc = TextFlow(fg="yellow")
    await tc.async_typewrite("Bot: Hi! How can I help?")

asyncio.run(bot_message())
```

## Logging Animated Output
```python
import io
from textflow import TextFlow

buf = io.StringIO()
tc = TextFlow()
tc.typewrite("Logging this animation!", file=buf)
# Now buf.getvalue() contains the animated output
```

---

For more, see the [usage guide](usage_guide.md) or [advanced](advanced.md) topics.

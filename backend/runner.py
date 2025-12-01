import asyncio
from google.genai import types
from google.adk.runners import InMemoryRunner
from .orchestrator import coordinator_agent
from .memory import MemoryBank

memory = MemoryBank()

runner = InMemoryRunner(agent=coordinator_agent, app_name="nutri_app")

session = None

async def init_session():
    global session
    session = await runner.session_service.create_session(
        user_id="user",
        app_name="nutri_app"
    )

asyncio.run(init_session())


async def ask_backend(query: str):
    memory.remember("user", {"user": query})

    msg = types.Content(role="user", parts=[types.Part.from_text(text=query)])


    full = ""
    async for event in runner.run_async(
        user_id="user",
        session_id=session.id,
        new_message=msg
    ):
        if event.content.parts:
            text = event.content.parts[0].text
            if text is not None:
                full += text

    memory.remember("user", {"assistant": full})
    return full

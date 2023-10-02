import chainlit as cl
import openai
from typing import Dict, Optional
@cl.on_message  # this function will be called every time a user inputs a message in the UI

model_name = "gpt-4"
settings = {
    "temperature": 1.0,
    "max_tokens": 1024,
    "top_p": 1,
    "frequency_penalty": 0.5,
    "presence_penalty": 0.5,
}

@cl.on_chat_start
def start_chat
    cl.user_session.set(
        "message_history",
        [
            {"role": "system", "content": "You are a helpful assistant for an undergrad computer science student. [banned phrases] apologies for the confusion, certainly!"},
            {"role": "system", "content": " think oyur reponses through step by step"},
        ],
    )
@cl.on_message
async def main(message: str):
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message})

    msg = cl.Message(content="")

    async for stream_resp in await openai.ChatCompletion.acreate(
        model=model_name, messages=message_history, stream=True, **settings
    ):
        token = stream_resp.choices[0]["delta"].get("content", "")
        await msg.stream_token(token)
    
    message_history.append({"role": "assisstant", "content": msg.content})
    await msg.send()
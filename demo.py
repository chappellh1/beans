import os
import openai
import chainlit as cl

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")
@cl.on_message
async def main(message: str):
    chat_completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "system", "content": "speak like a jar jar binks"},{"role": "user", "content": message}])
    
    response_message = chat_completion["choices"][0]["message"]["content"]
    await cl.Message(author="Diddy", content=f" { response_message}", indent=1).send()
    # send back the final answer
    await cl.Message(content=f"Walken: {response_message}").send()
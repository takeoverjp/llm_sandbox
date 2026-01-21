# To demonstrate your familiarity with OpenAI API, and also Ollama, build a tool that takes a technical question,
# and responds with an explanation. This is a tool that you will be able to use yourself during the course!

# imports
# If these fail, please check you're running from an 'activated' environment with (llms) in the command prompt

import os
import json
from dotenv import load_dotenv
from openai import OpenAI


# constants

MODEL_GPT = 'gpt-4o-mini'
MODEL_LLAMA = 'llama3.2'

# set up environment

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if api_key and api_key.startswith('sk-proj-') and len(api_key)>10:
    print("API key looks good so far")
else:
    print("There might be a problem with your API key? Please visit the troubleshooting notebook!")

SYSTEM_PROMPT = """
あなたは優秀なプログラミング講師です。与えられたプログラムの内容を初心者にもわかりやすく説明してください。
"""

USER_PROMPT = """
yield from {book.get("author") for book in books if book.get("author")}
"""

openai = OpenAI()

stream = openai.chat.completions.create(
    model=MODEL_GPT,
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT}
    ],
    stream=True,
)
response = ""
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)

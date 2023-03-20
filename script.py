import sys
import os
import openai
import pyperclip

def get_api_key(var):
    key = os.environ.get(var)
    if key is None:
        raise ValueError("Environment variable not set")
    return key

openai.api_key = get_api_key("OPENAI_KEY")

model_engine = "text-davinci-003"
temperature = 0.5
max_tokens = 200

while True:

    user_input = input("> ")
    if user_input == "q":
        break

    response = openai.Completion.create(
        engine = model_engine,
        prompt = user_input.strip(),
        temperature = temperature,
        max_tokens = max_tokens,
        n = 1,
        stop = None,
        frequency_penalty = 0,
        presence_penalty = 0
    )

    generated_text = response.choices[0].text.strip()
    print(generated_text)
    pyperclip.copy(generated_text)

sys.exit()
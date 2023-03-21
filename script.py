import sys
import os
import openai
import pyperclip

def get_api_key(var):
    key = os.environ.get(var)
    if key is None:
        raise ValueError("Environment variable not set")
    return key

def concatenate_strings(strings):
    strings = strings[1:]
    
    concatenated_string = " ".join(strings)

    return concatenated_string

openai.api_key = get_api_key("OPENAI_KEY")

model_engine = "text-davinci-003"
temperature = 0.7
max_tokens = 200

def api_call(user_input):
    response = openai.Completion.create(
        engine = model_engine,
        prompt = user_input,
        temperature = temperature,
        max_tokens = max_tokens,
        n = 1,
        stop = None,
        frequency_penalty = 0,
        presence_penalty = 0
    )

    return response.choices[0].text.strip()


if (len(sys.argv) > 1):
    prompt = concatenate_strings(sys.argv)
    generated_text = api_call(prompt)
    print(generated_text)
    pyperclip.copy(generated_text)
    sys.exit()


while True:

    user_input = input("> ")
    if user_input == "q":
        break

    generated_text = api_call(user_input.strip())

    print(generated_text)
    pyperclip.copy(generated_text)

sys.exit()
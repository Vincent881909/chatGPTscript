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

# Change these settings specific to your use case
model_engine = "text-davinci-003"
temperature = 0.5
max_tokens = 150

def chatGPT_API(user_input):
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
    user_input = concatenate_strings(sys.argv)
    generated_text = chatGPT_API(user_input)
    print(generated_text)
    pyperclip.copy(generated_text)
    sys.exit()


while True:

    user_input = input("> ")
    if user_input == "q":
        break

    generated_text = chatGPT_API(user_input.strip())
    print(generated_text)
    pyperclip.copy(generated_text)

sys.exit()

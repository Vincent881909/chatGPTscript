# chatGPTscript
A straight-forward python script to communicate with openAI API using a command line interface to retrieve responses from the text-davinci-003 model.

## Install

In order to use this program make sure to clone this repository into your desired directory using `gh repo clone Vincent881909/chatGPTscript`.
Cotinue to install the necessary libraries by running:

````bash
pip install -r requirements.txt
````
Make sure to set your API key as a environment variable called OPENAI_KEY. This serves for confidentiality reasons. In order to generate a API key visit [this link](https://platform.openai.com/account/api-keys). We also want to to create an alias in order to run the script from anywhere in the terminal to allow for quick access. To set a environment variable and creating a alias (depedning on your shell) write to .zshrc or .bashrc file. Run `nano ~/.zshrc` to open the editor and then export your API key and create an alias:

````bash
export OPENAI_KEY='INSERT_YOUR_KEY_HERE'
alias chatgpt='python3 PATH/TO/YOUR/SCRIPT.py'
````

Make sure to save the changes with control + o to write to the file and press enter to confirm. Exit the editor with control + x. To execute the content of the file run `source ~/.zshrc`. Now you will be able to run the program from any directory. Refer to Usage to get an indea on how to use it. 

## Usage

You have two options when it comes to providing the program with your prompt:
- Single response by providing your prompt as a program argument
- Loop that continously asks for your input

If you provide a prompt as a program argument the program will return a single response and exit. You can run `chatgpt YOUR_PROMPT` and the program will return your single response and exit. Note here, that your prompt cannot contain a '?' since the character is a special character in the terminal. It is used to signify a wildcard character, which means it can be used to represent any character or set of characters in a string. Therefore, it cannot be used as a program argument. This script adjusted the response tokens so it works well with short responses. For example, if you want to know how to write to a file in the terminal you could run `chatgpt How do I write to a file in the terminal`. Or perhaps you want to create a function to convert a string to lowercase. You could run `chatgpt Create a function in c++ that converts a string to all lowercase` .

If no program arguments are provided, the program will continue to ask for your input until you hit 'q' which will exit the program. Please also note that the generated response will be copied to your clipboard in case you need to quickly paste it elsewhere.

Please bare in mind that the openAI API is not free and has limited usage before you get billed. Refer to [openai](https://platform.openai.com/docs/introduction) for more info.

# chatGPTscript
A straight-forward python script to communicate with openAI API to retrieve responses from their text-davinci-003 model.

## Install

In order to use this program make sure to pull this repository into your desired directory using `gh repo clone Vincent881909/chatGPTscript`.
Cotinue to install the necessary libraries by running:

````bash
pip install -r requirements.txt
````
Make sure to set your API key as a environment variable called OPENAI_KEY. This serves for confidentiality reasons. In order to generate an API key visit [this link](https://platform.openai.com/account/api-keys). To set an envornment variable (depedning on your shell) write to .zshcr or .bashcr file. Run `nano ~/.zshrc` to open the editor and then export your API key:

````bash
export OPENAI_KEY='INSERT_YOUR_KEY_HERE'
````

Make sure to save the changes with ctr + o to write to the file and press enter to confirm. Exit the editor with ctrl + x. To executes the content of the file run `source ~/.zshrc`.

At this stage you will be able to run the script within your directory. If you wish to create an alias in order to run your script from anywhere in your terminal you need make another change to the .zshcr file (or .bashcr depending on your shell). To do this open the text edtir again using `nano ~/.zshrc`
and create an alias by typing 

````bash
alias chatgpt='python3 PATH/TO/YOUR/SCRIPT.py'
`````

Save the changes and exit the text editor and apply the changes again by running `source ~/.zshrc`.

## Usage

You have two options when it comes to providing the program with your prompt:
- Single response by providing your prompt as a program argument
- Loop that continuesly asks for your input


If you provide a prompt as a program argument the program will return a single response and exit. You can run `chatgpt YOUR_PROMPT` and the program will return your single response and exit. Note here, that your prompt cannot contain a '?' since the character is a special character in the terminal. It is used to signify a wildcard character, which means it can be used to represent any character or set of characters in a string. Therefore, it cannot be used as a program argument.

If no program arguments are provided, the program will continue to ask for your input until you hit 'q' which will exit the program. Please also note that the generated response will be copied to your clipboard in case you need to quickly paste it elsewhere.

Please bare in mind that the openAI API is not free and has limited usage before you get billed. Refer to [openai](https://platform.openai.com/docs/introduction) for more info.

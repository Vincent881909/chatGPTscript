# chatGPTscript
A straight-forward python script to communicate with openAI API to retrieve responses from their text-davinci-003 model.

## Install

In order to use this program make sure to pull this repository into your desired directory using `gh repo pull Vincent881909/chatGPTscript`.
Cotinue to install the necessary libraries by running:

````bash
pip install -r requirements.txt
````
Make sure to set your API key as a environment variable called OPENAI_KEY. This serves for confidentiality reasons. To do this run you need to (depedning on your shell) write to .zshcr or .bashcr file. Run `nano ~/.zshrc` to open the editor and then export your API key:

````bash
export OPENAI_KEY='INSERT_YOUR_KEY_HERE'
````

Make sure to save the changes with ctr + o to write to the file and press enter to confirm. Exit the editor with ctrl + x. To executes the content of the file run `source ~/.zshrc`.




If you provide a prompt as a program argument the program will return a single response and exit. Note here, that your prompt cannot contain a '?' since the character is a special character in the terminal. It is used to signify a wildcard character, which means it can be used to represent any character or set of characters in a string. Therefore, it cannot be used as a program argument.

If no program arguments are provided, the program will continue to ask for your input until you hit 'q'.
Please bare in mind that the openAI API is not free and has limited usage before you get billed. Refer to openai.com for more info.

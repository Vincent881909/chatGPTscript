# chatGPTscript
A straight-forward python script to communicate with openAI API to retrieve responses from their text-davinci-003 model. Make sure to set your API key in as a environment variable called OPENAI_KEY. This serves for confidentiality reasons.
If you provide a prompt as a program argument the program will return a single response and exit.Note here, that your prompt cannot contain a '?' since the character is a special character in the terminal. It is used to signify a wildcard character, which means it can be used to represent any character or set of characters in a string. Therefore, it cannot be used as a program argument. 
If no program arguments are provided, the program will continue to ask for your input until you hit 'q'.
Please bare in mind that the openAI API is not free and has limited usage before you get billed. Refer to openai.com for more info.

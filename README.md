# Jarvis_AI
An AI assistant which can answer any questions, capable of answering follow-up questions and much more. Built using ChatGPT API and uses GPT 3.5 turbo model.

# About

This Python script uses the speechRecognition module to recognize the message or the prompt said by the user and converts it into text. This text is then sent as a prompt to
the GPT AI model(```gpt-3.5-turbo``` in this case). The prompt is sent by the means of Open AI API and the response text given by the model is sent through the same API to the user. The python script again convets this text data into speech and gives it out using the pyttsx3 module.

The previous conversation(one command-response block) is fed to the gpt model as the context thus providing the ability to answer follow up questions effectively. One drawback is it has context of the immediate previous conversation and not the ones which were done few iterations back. You will have to provide the whole context again. 

# Usage

Clone this repository by running the command below in the terminal:
```
git clone https://github.com/aneeshkp246/Jarvis_AI.git
```
Then change the directory

```
cd Jarvis_AI
```
Get an Open AI API key from [here](https://platform.openai.com/account/api-keys). Then paste it in the space provided in between the double quotes. Afterwards, save the changes. 

Then run the Python file using the below command:

```
python assistant.py

```

Now give the prompt to the AI assistant through your voice clearly using a quality microphone. It will recognize it as accurate as possible and give the prompt to the AI model. As soon as the response is generated, it converts the text data into speech and reads the response aloud.

# License

MIT ©️ aneeshkp246

import speech_recognition as sr
import pyttsx3
import openai

openai.api_key = "your_openai_api_key_here"

engine = pyttsx3.init()


def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except Exception as err:
        print(f"Skipping unknown error {err}")


def generate_response(prompt, previous_resp):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": previous_resp},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=20,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        n=1,
        stop=["\n"],
    )

    return response["choices"][0]["message"]["content"]


def speak_text(text):
    engine.say(text)
    engine.runAndWait()


previous_response = "You are a helpful assistant."


def main():
    global previous_response
    while True:
        print('Say \"Jarvis\" to start recording your question')
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "jarvis":
                    filename = 'input.wav'
                    print("Please Say your question")

                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())
                            text = transcribe_audio_to_text(filename)

                            if text:
                                print(f"You said: \"{text}\"")
                                response = generate_response(text, previous_response)
                                print(f'Jarvis says:  \"{response}\"')
                                speak_text(response)
                                previous_response = text

            except Exception as err:
                print(f"An error occurred {err}")


if __name__ == '__main__':
    main()

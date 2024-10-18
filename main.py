import pyttsx3
import webbrowser
import musicLibrary
from krutrim_cloud import KrutrimCloud
# Initialize the text-to-speech engine
engine = None


# Function to initialize pyttsx3 engine
def init_speech_engine():
    global engine
    if engine is None:
        engine = pyttsx3.init()


def speak(text):
    init_speech_engine()
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    client = KrutrimCloud(api_key="gGc8MsOhBTCwkdy3o5dXFA")

    # Create a completion request to KrutrimCloud's chat model
    completion = client.chat.completions.create(
        model="Meta-Llama-3-8B-Instruct",
        messages=[
            {"role": "system",
             "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google   pyaragraph  write a song for her "},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content


def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open_new_tab("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open_new_tab("https://www.youtube.com")
    elif "open stackoverflow" in c.lower():
        webbrowser.open_new_tab("https://www.stackoverflow.com")


    elif "open github" in c.lower():
        webbrowser.open_new_tab("https://github.com")
        #play songs
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open_new_tab(link)

    else:
        output = aiprocess(c)
        print(output)
        speak(output)


# def close_engine():
#     global engine
#     if engine is not None:
#         engine.stop()  # Stop the engine properly
#         engine = None  # Clear the engine reference


if __name__ == "__main__":
    try:
        speak("Initializing Bappa...")

        while True:
            # Take input from the keyboard
            command = input("Enter your command (type 'exit' to quit): ")
            if command.lower() == "hello":
                speak("Hello Yogiii")
                print("Bappa hearing U..........")

            if command.lower() == "exit":
                print("Goodbye!")
                speak("Goodbye!")
                break



            processcommand(command)

    except Exception as e:
        print(f"Error during initialization: {e}")

    # finally:
    #     # Ensure the engine is properly closed at the end
    #     close_engine()

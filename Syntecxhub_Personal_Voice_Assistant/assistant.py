import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import datetime
import os
import sys

engine = pyttsx3.init()
engine.setProperty("rate", 170)

voices = engine.getProperty("voices")
if voices:
    engine.setProperty("voice", voices[0].id)


def speak(text):
    """Convert text to speech."""
    print(f"\nAssistant: {text}")
    engine.say(text)
    engine.runAndWait()


recognizer = sr.Recognizer()


def listen():
    """Listen to microphone and convert speech to text."""
    with sr.Microphone() as source:

        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)

            print("Recognizing...")
            command = recognizer.recognize_google(audio)

            print("You:", command)

            return command.lower()

        except sr.WaitTimeoutError:
            speak("No speech detected.")
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I could not understand you.")
            return ""

        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
            return ""

        except Exception as e:
            speak("An unexpected error occurred.")
            print(e)
            return ""


def open_application(command):

    try:

        if "notepad" in command:
            subprocess.Popen("notepad")
            speak("Opening Notepad")

        elif "calculator" in command:
            subprocess.Popen("calc")
            speak("Opening Calculator")

        elif "paint" in command:
            subprocess.Popen("mspaint")
            speak("Opening Paint")

        elif "command prompt" in command:
            subprocess.Popen("cmd")
            speak("Opening Command Prompt")

        elif "file explorer" in command:
            subprocess.Popen("explorer")
            speak("Opening File Explorer")

        else:
            return False

        return True

    except Exception as e:
        speak("Unable to open application.")
        print(e)
        return True


def search_web(command):

    try:

        query = command.replace("search", "").replace("google", "").strip()

        if query == "":
            speak("Please say what you want to search.")
            return

        url = f"https://www.google.com/search?q={query}"

        webbrowser.open(url)

        speak(f"Searching Google for {query}")

    except Exception as e:
        speak("Unable to search the web.")
        print(e)


def open_website(command):

    try:

        if "youtube" in command:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")
            return True

        elif "google" in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")
            return True

        elif "github" in command:
            webbrowser.open("https://github.com")
            speak("Opening GitHub")
            return True

        return False

    except Exception as e:
        speak("Unable to open website.")
        print(e)
        return True


def tell_time():

    current = datetime.datetime.now().strftime("%I:%M %p")

    speak(f"The current time is {current}")


def show_help():

    print("\nSAMPLE COMMANDS: \n")

    commands = [
        "Open Notepad",
        "Open Calculator",
        "Open Paint",
        "Open Command Prompt",
        "Open File Explorer",
        "Open YouTube",
        "Open Google",
        "Open GitHub",
        "Search Python Programming",
        "Search Artificial Intelligence",
        "What is the time",
        "Help",
        "Exit"
    ]

    for c in commands:
        print("•", c)

    print()


def process_command(command):

    if command == "":
        return

    if "exit" in command or "quit" in command or "stop" in command: # Exit

        speak("Goodbye.")
        sys.exit()

    elif "help" in command:

        show_help()
        speak("The command list has been displayed.")

    elif "time" in command:

        tell_time()

    elif "search" in command:

        search_web(command)

    elif "open" in command:

        if open_application(command):
            return

        if open_website(command):
            return

        speak("I don't recognize that application or website.")

    else:

        speak("Sorry, I don't know that command.")


def main():

    print("=" * 50)
    print("      PERSONAL VOICE ASSISTANT")
    print("=" * 50)

    show_help()

    speak("Hello! I am your personal voice assistant.")

    while True:

        command = listen()

        process_command(command)

if __name__ == "__main__":

    main()
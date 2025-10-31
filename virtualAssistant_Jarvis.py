import os
import datetime
import random
import wikipedia
import webbrowser
import speech_recognition as sr
import pyttsx3
import pyautogui
import psutil
import pyjokes
from dotenv import load_dotenv
import google.generativeai as genai

# ========== CONFIG ==========
load_dotenv()
genai.configure(api_key=os.getenv("JARVIS_API_KEY"))
MODEL = "gemini-2.0-flash"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 165)

# ========== SPEAK ==========
def speak(text):
    print(f"🤖 Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

# ========== GREETING ==========
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning Sir!")
    elif hour < 18:
        speak("Good afternoon Sir!")
    else:
        speak("Good evening Sir!")
    speak("I am Jarvis, your desktop assistant. How can I help you today?")

# ========== LISTEN ==========
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"🧑 You: {query}")
    except Exception:
        speak("Sorry, could you please repeat that?")
        return "none"
    return query.lower()

# ========== GEMINI AI ==========
def ask_gemini(prompt):
    try:
        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(prompt)
        reply = response.text.strip()
        return "\n".join(reply.split("\n")[:3])
    except Exception as e:
        return f"⚠️ Error: {e}"

# ========== SYSTEM CONTROL ==========
def systemControl(query):
    if "screenshot" in query:
        filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        pyautogui.screenshot(filename)
        speak(f"Screenshot taken and saved as {filename}")

    elif "shutdown" in query:
        speak("Shutting down the system. Goodbye sir.")
        os.system("shutdown /s /t 1")

    elif "restart" in query:
        speak("Restarting your computer.")
        os.system("shutdown /r /t 1")

    elif "sleep" in query:
        speak("Putting your system to sleep.")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    elif "battery" in query:
        battery = psutil.sensors_battery()
        speak(f"Your system is at {battery.percent} percent charge.")

    elif "volume up" in query:
        pyautogui.press("volumeup")
        speak("Volume increased.")

    elif "volume down" in query:
        pyautogui.press("volumedown")
        speak("Volume decreased.")

    elif "mute" in query:
        pyautogui.press("volumemute")
        speak("Volume muted.")

# ========== MAIN ==========
if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand()

        if "none" in query:
            continue

        # --- Wikipedia ---
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia:")
                speak(results)
            except:
                speak("I couldn’t find anything on Wikipedia.")

        # --- Websites ---
        elif "open youtube" in query:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube...")

        elif "open google" in query:
            webbrowser.open("https://google.com")
            speak("Opening Google...")

        elif "search" in query:
            speak("What should I search for?")
            topic = takeCommand()
            if topic != "none":
                webbrowser.open(f"https://www.google.com/search?q={topic}")
                speak(f"Here are the results for {topic}")

        elif "open stackoverflow" in query:
            webbrowser.open("https://stackoverflow.com")
            speak("Opening Stack Overflow...")

        # --- Music ---
        elif "play music" in query or "song" in query:
            music_dir = "D:\\Music"
            try:
                songs = os.listdir(music_dir)
                a = random.choice(songs)
                os.startfile(os.path.join(music_dir, a))
                speak("Playing your song, sir.")
            except:
                speak("Music folder not found.")

        # --- Time & Date ---
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "date" in query:
            today = datetime.date.today()
            speak(f"Today’s date is {today.strftime('%B %d, %Y')}")

         # --- Open any desktop application like Notepad ---
        elif "open notepad" in query:
            path = "C:\\Windows\\System32\\notepad.exe"
            speak("Opening Notepad...")
            os.startfile(path)

        # --- Open Visual Studio Code ---
        elif "open code" in query:
            codePath = "C:\\Users\\alisa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening Visual Studio Code...")
            os.startfile(codePath)

        # --- Jokes ---
        elif "joke" in query:
            speak(pyjokes.get_joke())

        # --- System Control ---
        elif any(word in query for word in ["screenshot", "shutdown", "restart", "sleep", "volume", "battery", "mute"]):
            systemControl(query)

        # --- Quit ---
        elif "quit" in query or "exit" in query:
            speak("Goodbye sir, shutting down systems.")
            break

        # --- Default to Gemini ---
        else:
            reply = ask_gemini(query)
            speak(reply)


# 🤖 JARVIS AI DESKTOP ASSISTANT

## 🧠 What is Jarvis?
Jarvis is your **talking computer friend**! It can **listen to you**, **talk back**, and **do tasks** for you — like opening websites, telling jokes, playing music, and answering questions using **Google Gemini AI**.

It’s just like *Iron Man’s Jarvis*, but on your computer! 💻✨

---

## 🎯 What Jarvis Can Do

| 💡 Feature | 💬 What It Does |
|-------------|----------------|
| 🎤 **Listens to You** | Understands your voice using your microphone. |
| 🔊 **Talks Back** | Replies with a robotic voice. |
| 🌍 **Opens Websites** | Opens Google, YouTube, Stack Overflow, etc. |
| 📚 **Wikipedia Search** | Reads short summaries about anything. |
| 💡 **AI Brain (Gemini)** | Answers smart questions using Google Gemini AI. |
| 🧩 **Controls Computer** | Takes screenshots, restarts, shuts down, etc. |
| 🎵 **Plays Music** | Plays songs from your computer. |
| 😂 **Tells Jokes** | Makes you laugh with funny tech jokes. |
| ⏰ **Tells Time & Date** | Says the current time and date. |

---

## 🧰 Tools & Libraries Used

| 🧩 Library | 💬 What It Does |
|-------------|----------------|
| `speech_recognition` | Listens and understands your speech. |
| `pyttsx3` | Lets Jarvis talk. |
| `webbrowser` | Opens websites. |
| `wikipedia` | Searches Wikipedia. |
| `pyautogui` | Takes screenshots and controls system volume. |
| `psutil` | Checks battery and system info. |
| `pyjokes` | Tells random jokes. |
| `dotenv` | Loads API keys safely. |
| `google.generativeai` | Connects Jarvis to Google Gemini AI. |

---

## 🪜 Step-by-Step Setup Guide

### 🧩 1. Clone the Repository

If the project is on GitHub, you can download (clone) it using:
```bash
git clone https://github.com/yourusername/Jarvis-AI-Assistant.git
```
Then go into the folder:
```bash
cd Jarvis-AI-Assistant
```

Or you can just **create a folder** manually called `Jarvis` on your desktop.

---

### ⚙️ 2. Install Python
If you don’t have Python yet, download it from [https://python.org/downloads](https://python.org/downloads)

Make sure it’s added to your PATH.

---

### 📦 3. Install Required Packages
Open the terminal or command prompt and type:
```bash
pip install speechrecognition pyttsx3 wikipedia pyautogui psutil pyjokes python-dotenv google-generativeai
```

---

### 🔐 4. Add Your Gemini API Key
Create a new file named `.env` in the same folder as your `jarvis.py` file and paste this inside it:
```
JARVIS_API_KEY=your_gemini_api_key_here
```
👉 You can get your Gemini API key from **Google AI Studio**.

---

### ▶️ 5. Run Jarvis
In the command prompt, go to your project folder and type:
```bash
python jarvis.py
```

Jarvis will greet you and start listening to your commands! 🎤

---

## 💬 Example Conversation

**Jarvis:** Good evening Sir! I am Jarvis, your desktop assistant. How can I help you today?  
**You:** What’s the time?  
**Jarvis:** Sir, the time is 8:45 PM.  
**You:** Open YouTube.  
**Jarvis:** Opening YouTube...  
**You:** Tell me a joke.  
**Jarvis:** Why do programmers prefer dark mode? Because light attracts bugs! 😂  

---

## 💡 How Jarvis Works (Simple Version)

1. 🎧 **Listens to You** → Uses microphone to hear you.  
2. 🧠 **Understands You** → Changes your voice into text.  
3. ⚙️ **Decides What to Do** → Figures out what you want.  
4. 💻 **Does the Task** → Opens a website or tells you something.  
5. 🔊 **Talks Back** → Replies to you using its robotic voice.  

If Jarvis doesn’t know the answer, it asks **Google Gemini AI** for help! 🌐

---

## 🧾 Folder Structure

```
Jarvis_AI_Desktop_Assistant_PoweredBy_GoogleGemini/
│
├── jarvis.py                                   ← Main Python file
├── requirements.txt                            ← All dependencies
├── README.md                                   ← This file
├── .env                                        ← Stores Gemini API key (private)
├── .gitignore                                  ← Keeps .env & cache files safe
└── Jarvis_AI_Desktop_Assistant_Documentation.docx ← Full project documentation

```

---

## ⚠️ Important Notes

- 🎙️ Speak clearly and slowly for better accuracy.  
- 🌐 Internet is needed for Wikipedia and Gemini AI.  
- ⚠️ Be careful when using “shutdown” or “restart” commands!  
- 🗂️ Update file paths (like your music or VS Code) to match your computer.  

---

## 👨‍💻 Developer Info

**Developer:** Mohd Saif Ali Ansari  
**Language:** Python  
**AI Engine:** Google Gemini API  
**Version:** 1.0  
**Goal:** To make computers talk like humans! 💬🤖

---

## 🌟 Future Ideas

| Feature | Description |
|----------|-------------|
| 🧠 Memory | Jarvis remembers your name and choices. |
| 💬 Chat History | Keeps a record of your past chats. |
| 🧏 Offline Mode | Works without internet. |
| 🎨 GUI Interface | Adds buttons and a nice window to use Jarvis easily. |

---

⭐ *Jarvis isn’t just a program — it’s your personal assistant powered by Python and AI!*  
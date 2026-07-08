# Automated Personal Voice Assistant

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/Artificial%20Intelligence-Project-blueviolet?style=for-the-badge)
![Speech Recognition](https://img.shields.io/badge/Speech-Recognition-success?style=for-the-badge)
![TTS](https://img.shields.io/badge/Text--to--Speech-pyttsx3-orange?style=for-the-badge)
![Internship](https://img.shields.io/badge/Syntecxhub-AI%20Internship-FF6B00?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

An interactive, multi-threaded offline desktop Voice Assistant engineered using Python. The application implements automated speech-to-text signal capture, rule-based command processing, and real-time text-to-speech (TTS) responses.

Developed as **Task 4** during my **Artificial Intelligence Internship** at **Syntecxhub**.

---

## 📌 Project Overview

This application transforms live microphone input into executable system commands. It dynamically adjusts for ambient noise, converts speech into text using Google's Speech Recognition service, and executes predefined commands such as launching desktop applications, searching the web, and announcing the current time.

---

##  Core Features

-  **Offline Text-to-Speech:** Uses `pyttsx3` for fast, offline voice responses.
-  **Ambient Noise Calibration:** Adjusts to background noise before listening for commands.
-  **Rule-Based Command Processing:** Matches spoken commands with predefined actions.
-  **Desktop Application Control:** Launches applications such as:
  - Notepad
  - Calculator
  - Paint
  - File Explorer
  - Command Prompt
-  **Web Automation:** Opens Google, YouTube, GitHub, or performs Google searches directly from voice commands.
-  **Time Announcement:** Speaks the current system time.
-  **Exception Handling:** Handles speech recognition errors, microphone timeouts, and internet connectivity issues gracefully.

---

##  Technologies Used

- Python 3
- SpeechRecognition
- pyttsx3
- subprocess
- webbrowser
- datetime

---

##  Project Structure

```text
Syntecxhub_Task4_Voice_Assistant/
│
├── assistant.py          # Main application source code
├── requirements.txt      # Project dependencies
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

---

##  How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/AqsaAliRazaJamali/Syntecxhub_Personal_Voice_Assistant.git
```

### 2. Navigate to the Project Directory

```bash
cd Syntecxhub_Voice_Assistant
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Voice Assistant

```bash
python assistant.py
```

---

##  Application Workflow

```text
Microphone Input
        │
        ▼
Ambient Noise Calibration
        │
        ▼
Speech Recognition
        │
        ▼
Command Processing
        │
        ▼
Execute System Command / Web Search / Speak Response
```

---

## 📋 Sample Voice Commands

###  System Applications

- Open Notepad
- Open Calculator
- Open Paint
- Open File Explorer
- Open Command Prompt

###  Browser Commands

- Open Google
- Open YouTube
- Open GitHub

###  Search Commands

- Search Python Programming
- Search Artificial Intelligence

###  Utility Commands

- What is the time
- Help
- Exit
- Quit
- Stop

---

## ⚠️ Exception Handling

The assistant safely handles common runtime exceptions, including:

- `WaitTimeoutError` – No speech detected.
- `UnknownValueError` – Speech could not be recognized.
- `RequestError` – Speech recognition service unavailable due to network issues.

These safeguards ensure the application continues running without unexpected crashes.

---

## 🎓 Internship Information

This project was completed as **Task 4** of the **Artificial Intelligence Internship** offered by **Syntecxhub**.

---

## 👩‍💻 Author

**Aqsa Jamali**

GitHub: https://github.com/AqsaAliRazaJamali

---

## 📄 License

This project was developed for educational and internship purposes as part of the Syntecxhub AI Internship Program.

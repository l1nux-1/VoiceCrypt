# 🎙️ VoiceCrypt
Encrypt your voice using Caesar cipher with a sleek Python GUI.

**VoiceCrypt** is a voice-powered Caesar cipher encryption app built with Python. It listens to your voice (in Turkish), converts it to text using speech recognition, and then encrypts the resulting text using a classic Caesar cipher with a shift of 3. The interface is built using `customtkinter` with a modern dark theme for a sleek and simple user experience.

## ✨ Features

- 🎤 **Speech Recognition**: Converts spoken Turkish into text in real-time.
- 🔐 **Caesar Cipher Encryption**: Applies a classic Caesar cipher with a shift of 3.
- 💻 **Modern GUI**: Built with `customtkinter`, featuring dark mode and smooth design.
- 🧪 **Offline Operation**: Except for the speech recognition API, the app works offline.

---

## 📦 Requirements

To run this project, you’ll need:

- Python 3.8+
- pip (Python package installer)

### Python Libraries

Install dependencies with:

If PyAudio causes issues (common on Windows), try installing it with pipwin:

pip install pipwin
pipwin install pyaudio

git clone https://github.com/l1nux-1/voicecrypt.git
cd voicecrypt

python voicecrypt.py


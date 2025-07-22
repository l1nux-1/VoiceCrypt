import customtkinter as ctk
import speech_recognition as sr

def caesar_cipher(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            ascii_start = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - ascii_start + shift) % 26 + ascii_start)
        else:
            encrypted += char
    return encrypted

def listen_and_encrypt():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            status_label.configure(text=" Listening...")
            app.update()
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            status_label.configure(text=" Recognizing...")
            app.update()

            text = recognizer.recognize_google(audio, language="tr-TR")  # Still listening in Turkish
            input_text.set(text)

            encrypted = caesar_cipher(text, 3)
            encrypted_text.set(encrypted)

            status_label.configure(text=" Encryption complete.")
        except sr.UnknownValueError:
            status_label.configure(text=" Could not understand audio.")
        except sr.RequestError:
            status_label.configure(text=" Internet connection error.")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Voice Caesar Cipher")
app.geometry("500x400")

input_text = ctk.StringVar()
encrypted_text = ctk.StringVar()

ctk.CTkLabel(app, text="Spoken Text", font=ctk.CTkFont(size=16), text_color="#e0ffff").pack(pady=10)
ctk.CTkEntry(app, textvariable=input_text, width=400, text_color="light green").pack(pady=5)

ctk.CTkLabel(app, text="Encrypted Text", font=ctk.CTkFont(size=16), text_color="#e0ffff").pack(pady=10)
ctk.CTkEntry(app, textvariable=encrypted_text, width=400, text_color="light green").pack(pady=5)

ctk.CTkButton(app, text="🎤 Speak and Encrypt", command=listen_and_encrypt, fg_color="#7f00bf").pack(pady=20)

status_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=12))
status_label.pack(pady=5)

app.mainloop()

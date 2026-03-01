import speech_recognition as sr
import pyttsx3
from datetime import datetime

# TTS engine init
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # কথা বলার speed adjust
engine.setProperty('volume', 1.0)  # volume 0.0 to 1.0

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Voice recognition init
r = sr.Recognizer()

speak("হ্যালো boss, আমি Jarvis। বলো কী করতে চাও।")

while True:
    with sr.Microphone() as source:
        print("শুনছি...")
        # Ambient noise adjust
        r.adjust_for_ambient_noise(source, duration=2)

        # Retry loop
        for attempt in range(3):
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=10)
                command = r.recognize_google(audio, language='bn-BD,en-US')
                print("তুমি বলেছো:", command)

                # Basic commands
                if "কেমন আছো" in command:
                    speak("আমি ভালো আছি boss, তুমি কেমন আছো?")
                elif "সময়" in command:
                    now = datetime.now().strftime("%H:%M")
                    speak(f"এখন সময় {now}")
                elif "প্রস্থান " in command or "আউট " in command or "যাও" in command or "বন্ধ হও" in command or "ক্লোস" in command or "যাও এখন" in command:
                    speak("ঠিক আছে boss, আমি বন্ধ হচ্ছি।")
                    exit()
                else:
                    speak("দুঃখিত boss, আমি বুঝতে পারিনি।")

                break  # success হলে retry loop থেকে বের হবে

            except sr.UnknownValueError:
                print("বুঝতে পারিনি, আবার বলো।")
                if attempt == 2:
                    speak("দুঃখিত boss, আমি বুঝতে পারিনি।")
            except sr.WaitTimeoutError:
                print("কিছু বলোনি, আবার চেষ্টা করো।")
                if attempt == 2:
                    speak("দুঃখিত boss, তুমি কিছু বলোনি।")

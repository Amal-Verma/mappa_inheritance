import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()

    engine.setProperty('rate', 150)  
    engine.setProperty('volume', 1) 

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    text = "mappa is nice"
    text_to_speech(text)
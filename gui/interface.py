import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
import speech_recognition as sr

# hotwork is hello not mappa

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hotword Activated GUI")
        self.setGeometry(575, 350, 400, 300)
        
        # Status label for debugging
        self.status_label = QLabel("Status: Waiting for hotword...")
        
        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_status(self, message):
        self.status_label.setText(f"Status: {message}")
        QApplication.processEvents()  # Force UI update

    def listen_for_hotword(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.update_status("Listening for hotword...")
            print("Say the hotword...")

            try:
                audio = recognizer.listen(source)
                print("Audio captured for hotword")
                hotword = recognizer.recognize_google(audio).lower()
                print(f"Recognized hotword: {hotword}")

                if "hello" in hotword:
                    self.update_status("Hotword detected! Listening for command...")
                    print("Hotword detected. Listening for commands...")
                    self.listen_for_command()
                else:
                    self.update_status("Hotword not detected, try again.")
            except sr.UnknownValueError:
                self.update_status("Could not understand audio (hotword)")
                print("Could not understand audio")
            except sr.RequestError as e:
                self.update_status(f"Error with recognition service: {e}")
                print(f"Error with recognition service: {e}")

    def listen_for_command(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.update_status("Listening for command...")
            print("Say the command...")

            try:
                audio = recognizer.listen(source)
                print("Audio captured for command")
                command = recognizer.recognize_google(audio).lower()
                print(f"Recognized command: {command}")

                if "open terminal" in command:
                    self.update_status("Opening terminal...")
                    print("Opening terminal...")
                    subprocess.run(["wt"]) 
                if "open browser" in command:
                    self.update_status("Opening terminal...")
                    print("Opening terminal...")
                    subprocess.run(["edge.exe"])  
                else:
                    self.update_status("Command not recognized")
                    print("Command not recognized")
            except sr.UnknownValueError:
                self.update_status("Could not understand audio (command)")
                print("Could not understand audio")
            except sr.RequestError as e:
                self.update_status(f"Error with recognition service: {e}")
                print(f"Error with recognition service: {e}")

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.listen_for_hotword()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()

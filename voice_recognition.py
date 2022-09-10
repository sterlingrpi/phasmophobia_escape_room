import speech_recognition as sr
r = sr.Recognizer()
r.dynamic_energy_threshold = False

class Voice():
    def __init__(self, timeout=5.0):
        self.timeout = timeout
        self.text = None

    def get_text(self):
        try:
            with sr.Microphone() as source:
                audio_text = r.listen(source, timeout=self.timeout)
            self.text =  r.recognize_google(audio_text)
        except:
            self.text = None

        return self.text

if __name__ == '__main__':
    while True:
        voice = Voice()
        text = voice.get_text()
        print(text)
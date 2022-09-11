import speech_recognition as sr

class Voice():
    def __init__(self, timeout=5.0):
        self.r = sr.Recognizer()
        self.r.dynamic_energy_threshold = False
        self.timeout = timeout
        self.text = None

    def get_text(self):
        try:
            with sr.Microphone() as source:
                audio_text = self.r.listen(source, timeout=self.timeout)
            self.text =  self.r.recognize_google(audio_text)
        except:
            self.text = None

        return self.text

if __name__ == '__main__':
    voice = Voice()
    print('say something')
    while True:
        text = voice.get_text()
        if text:
            print(text)
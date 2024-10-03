import pyttsx3
import requests

class Speaking:
    def speak(self, audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()

class Try:
    def Dictionary(self):
        speak = Speaking()
        speak.speak("Which word do you want to find the meaning of, sir?")
        
        # Taking the string input
        query = input()
        meaning = self.get_meaning(query)

        if meaning:
            print("Meaning:", meaning)
            speak.speak("The meaning is " + meaning)
        else:
            speak.speak("Sorry, I couldn't find the meaning for that word.")

    def get_meaning(self, word):
        # Use a different dictionary API here
        # Replace with your API endpoint and key
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            return data[0]['meanings'][0]['definitions'][0]['definition']
        else:
            return None

if __name__ == '__main__':
    gfg_instance = Try()
    gfg_instance.Dictionary()

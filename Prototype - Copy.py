import nltk
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("Voices", voices[0].id)


def speak(audio):
    if engine._inLoop:
        engine.endLoop()
        engine.say(audio)
        print(audio)
        engine.runAndWait()
    else:
        engine.say(audio)
        print(audio)
        engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    user = ""
    with sr.Microphone()as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
    try:
        print("Recognizing")
        user = r.recognize_google(audio, language='en-pk')
        print(user)
        return user

    except Exception as e:
        speak("you have not said any thing......... ")
        return
    return user


def extract(text):

    ii = ee = 0

    def token(text):
        from nltk.tokenize import sent_tokenize, word_tokenize
        # nltk.download('punkt')
        words = word_tokenize(text)
        return (words)

    def remove_p(words):
        words = [word for word in words if word.isalnum()]
        return (words)

    def remove_uw(words):
        # nltk.download('stopwords')
        from nltk.corpus import stopwords
        stop_words = set(stopwords.words('english'))
        filtered_words = []
        for i in words:
            if i not in stop_words:
                filtered_words.append(i)
        return (filtered_words)

    def stemming(words):
        ws = []
        from nltk.stem import PorterStemmer
        ps = PorterStemmer()
        for i in words:
            ws.append(ps.stem(i))
        return (ws)

    words = token(text)
    words = remove_p(words)
    words = remove_uw(words)
    words = stemming(words)

    intents = ["order", "reserv", "menu", 'buy', "purchase", "take", 'get']
    enitities = ['pizza', 'burger', 'sandwich', 'drink', 'member']
    for w in words:
        for i in intents:
            if w == i:
                print("Intent: ", w)
                ii = 1
        for i in enitities:
            if w == i:
                print("Entity: ", w)
                ee = 1

    if ii == 0 and ee == 0:
        print("\nBot: Sorry I didn't understand your intent")
        return ("Sorry I didn't understand your intent")

    else:
        return (w)


if __name__ == '__main__':
    print("****** Wel come to Our Restaurant ******")

    flag = "false"
    while flag != 'True':

        mode = input(
            "Bot: PLease select the mode \n 1.Text \n 2.Voice\n User: ")
        mode = mode.lower()

        if mode == "text" or mode == "1" or mode == "one":
            print("***** Your are in Text Mode ******")
            print("Here is a Menu \n Pizza\n Burger\n Sandwich\n Colddrink")

            flag2 = "false"

            while flag2 != "true":
                msg = '\nBot: How can I help you? \nUser: '
                user = input(msg)
                user = user.lower()
                flag2 = extract(user)

            flag = "True"

        elif mode == "voice" or mode == "2" or mode == "two":
            print("***** Your are in Voice Mode *****")
            flag3 = "false"
            print("\nBot: ")
            print("\n Here is a Menu \n Pizza\n Burger\n Sandwich\n Colddrink")
            speak("We have Pizza, Burger, Sandwich, Cold drink")
            speak('How can I help You?')
            speak('speak Please!')
            print('\nUser: ')
            user = takecommand()
            print(user)
            if user != None:
                user = user.lower()
                flag3 = extract(user)

            flag = "True"
        else:
            print("Invalid Option")
            flag = "False"

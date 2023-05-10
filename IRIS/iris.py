import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5') #sapi5 is a speech api developed by microsoft
voices = engine.getProperty('voices') #getting details of current voice
print(voices[1].id) #printing the voice id
engine.setProperty('voices', voices[1].id)#for female voice

#speak the argument it is given
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wisME():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!") 
    speak("I am Iris. Please tell me how may I help you")



def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()#Recognizer class helps to recognize the audio
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        #r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')#Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.
    except Exception as e:
        #print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


if __name__ == "__main__":
    wisME()
    #while True:
    if 1:
        query = takeCommand().lower() #Converting user query into lower case
        
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")#replacing wikipedia with empty string
            results = wikipedia.summary(query, sentences=2)#searching wikipedia for the query and returns two sencences
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")#opens youtube
        elif 'open google' in query:
            webbrowser.open("google.com")#opens youtube

        #elif 'play music' in query:
            #music_dir = 'D:\\Music\\Music\\English\\English Songs\\En 
            # songs = os.listdir(music_dir)
            # print(songs)
            # os.startfile(os.path.join(music_dir, songs[0]))#play the first song in the directory

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Ma'am, the time is {strTime}") 

        





